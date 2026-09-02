# scripts/ — corpus automation

## daily-corpus-sync.py

Deterministic daily producer for source classes **1 (job postings)** and **2 (agency claims / overlap matrix)**. It exists so the corpus stops depending on WebSearch (which cannot date-stamp ATS postings or agency claims) and instead consumes the two daily data feeds NorthPoint already runs.

### What it reads (already-running daily feeds)
| Source | Path | Provides |
|---|---|---|
| A — job postings | `../northpoint/sales-funnel/prospects/open-positions.json` | Daily ATS API scan (greenhouse/ashby/lever/breezy/workable/…). URL-verified, dated, seniority-scored marketing/growth roles. Also lists `needs_chrome_fallback` (proprietary ATS not API-reachable) and `fetch_errors`. |
| B — agency intel | `../northpoint/sales-funnel/competitor-intelligence/trend-data.json` | Daily 18-agency panel. Each agency has dated entries with `recentClientsNamed`, `healthScore`, `threatLevel`. |

### What it writes (every run, into `corpus/`)
- `job-postings/<firm>.csv` — per tracked-firm marketing roles (Stratum 1–4 cohort only; dedup by `source_url`). Schema: `date_posted,title,jurisdiction,seniority,source_url,captured_date,notes`.
- `job-postings/_absence.csv` — tracked firms with **no API coverage** (proprietary ATS or fetch error) + their careers URL. Absence is data (methodology rule).
- `agency-overlap-matrix.csv` — tracked firm × claiming agencies, with `OVERLAP` flag where >1 agency claims the same firm (Theme 3).
- `agency-claims/<agency>.csv` — dated per-agency claimed-client snapshot, each client tagged tracked / not-tracked.

### Feed-health guard (added 2026-08-06 — watch bb)

"0 new postings" is ambiguous between **ABSENT** (the scan ran and found nothing) and **UNOBSERVED** (the scan did not run). On 2026-08-05 the upstream ATS scan had been frozen for ~66h and the sync reported 0 new postings anyway — the corpus was one step from publishing an absence claim it had not earned, which is the same defect it documents in other firms' promotional estates.

Every run now prints:

```
FEED HEALTH: HEALTHY|STALE|UNKNOWN (scanned_at_utc=..., age=..h, fingerprint total_jobs_fetched=..., delta=+N vs YYYY-MM-DD (N))
  reason: ...
```

The verdict is the AND of **two** predicates. Both must pass for a class-1 absence claim to be permitted.

- **Predicate 1 — age.** `scanned_at_utc` under 36h old. Over 36h ⇒ **STALE**; missing or unparseable ⇒ **UNKNOWN** (treated as stale).
- **Predicate 2 — fingerprint delta (added 2026-08-14, watches bb + ff).** `total_jobs_fetched` is compared against the last observation from a **prior calendar date**, persisted in `corpus/job-postings/_feed-fingerprint.json`. A delta of **0 degrades the verdict to STALE regardless of age.** If no prior-date observation exists, the delta is unmeasurable and reported as `n/a` (verdict falls back to the age test, and the reason line says so).

When the verdict is not HEALTHY the run prints `CLASS-1 ABSENCE CLAIM REFUSED`; the run record must say **"class 1 unobserved"**, never "class 1 produced nothing."

**Why the second predicate exists.** The rule *"if the fingerprint moves while `new_count` stays 0 the scan genuinely looked; if it is byte-identical the scan did not"* was written on 2026-08-06 but never enforced — only printed. On **2026-08-13** the two halves disagreed for the first time: age 14.0h said HEALTHY while the fingerprint was byte-identical (2,151 → 2,151) **across a two-calendar-day gap**, and the banner reported only the half that passed. That run had to be recorded as `CLASS 1 UNRESOLVED` by hand. The guard now makes that ruling itself.

Same-day re-runs stay **idempotent**: the comparison is always against a prior *date*, never against the run's own entry, so re-running does not manufacture a zero delta. Discrimination was verified both ways on 2026-08-14 (real delta `+24` ⇒ HEALTHY; prior-date fingerprint forced equal ⇒ **STALE** + absence claim refused).

### Class-1 capture-window freeze (added 2026-09-02 — closes watch (ao), fixes watch (ai))

The feed-health guard answers *did the scan look?* It answers that correctly every day — **including every day after the capture window closed**, which is when the right question changed and nothing in the script knew it.

`methodology.md` §1, `README.md` and the public `README-for-github.md` all state the class-1 window as *"rolling 12 months ending August 31, 2026"*. The script had no concept of that end date, so on **2026-09-01 (ship day)** a HEALTHY feed rolled the `as_of` column of `_absence.csv` and `_chrome-queue.csv` — **shipped Theme-1/Theme-4 exhibits** — from `2026-08-31` to `2026-09-01`. Restored by hand. On **2026-09-02** the same roll recurred **and the absence panel gained a member** (Gemini, greenhouse read timeout): a post-window class-1 observation, one write from entering a shipped exhibit. Restored by hand again. **Two hand corrections is the signal to put the rule in code.**

```
CAPTURE_WINDOW_END = "2026-08-31"     # or --window-end YYYY-MM-DD | none
```

When `today > CAPTURE_WINDOW_END` the run prints `CLASS-1 CAPTURE WINDOW CLOSED` and:

| Artifact | Post-window behaviour | Why |
|---|---|---|
| `job-postings/<firm>.csv` | **not written**; offered rows counted and printed | a corpus claim |
| `job-postings/_absence.csv` | **not written** — not even when content is unchanged | a corpus claim; the `as_of` column alone re-dates it |
| `job-postings/_chrome-queue.csv` | **not written** | same |
| `job-postings/_feed-fingerprint.json` | **still written, every run** | an **instrument log**. "A 09-02 scan ran" is a true fact about the instrument |
| class 2 (`agency-*`) | unaffected | its `as_of` comes from the feed's `lastUpdated`, not the run clock |

The feed is still read and still reported, so the daily record can state the live instrument state without the corpus absorbing it. **Absence-panel drift is printed explicitly** — a firm in today's live read but not in the shipped `_absence.csv` is a change in *instrument reach after the window*, and the banner says so in those words, because that is the exact conflation `methodology.md` §1 forbids.

**Red-proofed both ways (2026-09-02), per lessons L16:**

| Invocation | Verdict |
|---|---|
| default (`--window-end 2026-08-31`) | **FROZEN** — both exhibits byte-identical to `HEAD` (md5 verified), 0 rows admitted, Gemini drift flagged |
| `--window-end none` | **WRITES** — reproduces the exact defect: `as_of` → `2026-09-02` on both files, plus the new Gemini row |
| `--window-end 2026-12-31` | **WRITES** — window open, normal behaviour intact |

`--window-end` exists so the guard *can* be made to return the other verdict. A guard that cannot fail is not a guard.

### Coverage rules honoured
Tracked-firm cohort only (alias table mirrors `tracked-firms.md`); every row carries a primary source URL; dedup against existing rows; **no fabrication** — only what the upstream feeds contain. Idempotent: re-running the same day adds nothing.

### Run
```
python3 scripts/daily-corpus-sync.py
# override paths if the repo is relocated:
python3 scripts/daily-corpus-sync.py --repo <repo> --sales <sales-funnel>
```

---

## verify-capture.py

**Class-3 capture guard (added 2026-08-20 — closes watch (pp)).** Class 1 has a two-predicate feed-health guard that prints a verdict every run. Class 3 — the regulator registers — became load-bearing for Theme 4 and had no guard at all.

Two large-register captures have now been **silently incomplete**: `CASPS.csv` on 2026-08-17 (HTTP 200, 49% missing, cut mid-field, tool reported success) and `OTHER.csv` on 2026-08-20. **A truncated CSV parses cleanly**, so every derived statistic is internally consistent and wrong — and the claim this report most intends to make about named companies is *"absent from the register."*

### Run
```
python3 scripts/verify-capture.py <file> [--expect-rows N] [--json]
```
Exit code `0` = COMPLETE, `1` = TRUNCATED/SUSPECT, `2` = file not found.

### Verdict
`COMPLETE` / `TRUNCATED` / `SUSPECT` / `UNKNOWN`. **Only COMPLETE permits an absence claim about a named entity.** Positive hits inside a truncated capture remain usable; absences do not. When the verdict is not COMPLETE the banner prints `CLASS-3 ABSENCE CLAIM REFUSED`.

### Predicates
- **Primary — final-row termination.** Does the last data row carry the same field count as the header? **This is the check that caught both real truncations.**
- **Secondary — field-count consistency.** Ragged rows are reported. ESMA registers contain legitimately quoted multi-line fields, so ragged ⇒ `SUSPECT` (adjudicate by hand), not `TRUNCATED`.
- **Recorded every run** — byte count and md5, so the capture is auditable and a re-fetch is comparable byte-for-byte.
- **`--expect-rows`** cross-checks against a prior verified capture. Below expectation ⇒ TRUNCATED; above ⇒ a note (the source may have gained rows; re-baseline before claiming a delta).

### 🔴 The size heuristic is NOT a predicate — retired 2026-08-20
The 08-17 rule read *"any `web_fetch` result near ~82,000 characters is presumed truncated."* On 08-20 `OTHER.csv` truncated at **64,556** characters, while a 24,614-character `NCASP.csv` capture was complete. **The cut point is a property of the retrieval channel's budget on the day, not of the file**, so a byte threshold cannot discriminate. Kept as a printed note only. **Structure, not size.**

### Discrimination verified both ways (2026-08-20)
| Input | Verdict |
|---|---|
| `_esma-ncasp-snapshot-2026-08-16.csv` (167 rows) | **COMPLETE**, exit 0 |
| `_esma-casps-snapshot-2026-08-17.csv` (329 rows, md5 `69e7dc…`) | **COMPLETE**, exit 0 |
| CASPS cut at the real 08-17 cut point (82,445 chars) | **TRUNCATED**, exit 1 — final row 4 of 16 fields |
| CASPS cut at the 08-20 cut point (64,556 chars) | **TRUNCATED**, exit 1 — final row 1 of 16 fields |

The two COMPLETE runs independently reproduce the 08-17 record's own figures (329 rows, 161,380 bytes, md5 `69e7dc9…`), which re-verifies that capture as a side effect.

---

---

## date-provenance-audit.py

**Class-4 / class-5 retrospective date guard (added 2026-08-21 — closes recommendation 3 of the 08-20 run).** Class 1 has a feed-health guard and class 3 has a capture guard. Classes 4 and 5 had a date check that ran **only at intake**, and it was two days old. Nothing had ever audited the rows admitted before it existed.

On 08-20 two candidate items were refused because their real publication dates were 2020 and 2022 while the search results that surfaced them carried no date at all. **Both would have confirmed an open question** — which is exactly the class of item that gets the least scrutiny (watch (ss)).

### Run
```
python3 scripts/date-provenance-audit.py
```
Exit `0` = no date inversions and no citationless rows. Exit `1` = at least one.

### The predicate
**Does the row's own `source_url` carry a date in its path, and is that date consistent with the date the corpus recorded?** A URL-path date is publisher-asserted, ships inside the citation the report already carries, and is checkable without a re-fetch. It is the mechanism that resolved the 08-20 Coinbase refusal.

### Verdicts
`SELF-DATED` · `DATE-INVERSION` (🔴 article predates the event it reports) · `LAG-EXCEEDED` · `NO-URL-DATE` (uncorroborated, not contradicted) · `NO-URL` (🔴 no citation at all) · `NO-PUBDATE-FIELD` (class-4 only: nothing machine-readable to check).

### 🔴 The first run's two DATE-INVERSIONs were both bugs in this script
Recorded, because it is the same shape as `verify-capture.py`'s retired byte heuristic — **a predicate that looked decisive and was not.**

| Reported | Reality | Fix |
|---|---|---|
| BitMEX row: url `2026-07-01` precedes event `2026-07-23` | `/2026/07/` is **month-precision**, compared as a day | **Precision is symmetric** — ruling is made at the coarser of the two sides |
| Kalifowitz file: url `2026-05-05` precedes `2026-08-11` | `2026-08-11` is the `Captured:` line — **our clock, not the artifact's** | Class-4 audit no longer guesses from prose; needs an explicit publication-date field |

**Rule adopted: a new guard's first run is a test of the guard, not of the corpus. Adjudicate every flag by hand before believing any of it.**

### What it found on the corpus (2026-08-21)
Class 5: **12 SELF-DATED · 10 NO-URL-DATE · 2 LAG-EXCEEDED · 2 NO-URL.** Class 4: **5 NO-PUBDATE-FIELD · 2 NO-URL · 1 LAG-EXCEEDED.**

The headline catch: **`Algorand -25%` is printed as a class-5 example in `README.md`, `methodology.md` and the public `README-for-github.md`, and its tracker row had no `source_url` at all.** Repaired at source the same run; sourcing it also produced a Theme-1 signal the uncited row never carried. **MARA Holdings remains uncited and is flagged to strike if unsourced by ship.**

### Known limit — it narrows the queue, it does not empty it
**`SELF-DATED` means the citation and the corpus agree. It does not mean either is right.** Only a first-party fetch settles that. And **no class-4 file carries a machine-readable publication-date field**, so five of eight are unauditable by any script; the fix is a one-line `**Published:**` field in the class-4 template.

---

### Daily task ordering (recommended)
1. `python3 scripts/daily-corpus-sync.py` → classes 1 + 2 (deterministic, always produces output).
2. WebSearch pass → classes 3 (regulator), 4 (operator statements), 5 (layoffs) for net-new in-window items.
3. **`python3 scripts/verify-capture.py` on every register CSV captured in step 2, BEFORE deriving any statistic from it.**
4. **`python3 scripts/date-provenance-audit.py` — cheap, and it is the only thing watching what was admitted before the guards existed.**
5. Write the dated run record in `corpus/weekly-runs/`, update `findings/`, commit.

### Known residual gap (bounded)
Proprietary-ATS exchanges (Binance, Bybit, KuCoin, HTX) + Solana/ConsenSys are not API-reachable and surface only in `_absence.csv`. Closing them = pointing the existing `chrome-supplemental-scan` lane at `open-positions.json`'s `needs_chrome_fallback` list and feeding rendered postings back through the same schema.

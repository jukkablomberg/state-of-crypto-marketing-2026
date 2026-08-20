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

### Daily task ordering (recommended)
1. `python3 scripts/daily-corpus-sync.py` → classes 1 + 2 (deterministic, always produces output).
2. WebSearch pass → classes 3 (regulator), 4 (operator statements), 5 (layoffs) for net-new in-window items.
3. **`python3 scripts/verify-capture.py` on every register CSV captured in step 2, BEFORE deriving any statistic from it.**
4. Write the dated run record in `corpus/weekly-runs/`, update `findings/`, commit.

### Known residual gap (bounded)
Proprietary-ATS exchanges (Binance, Bybit, KuCoin, HTX) + Solana/ConsenSys are not API-reachable and surface only in `_absence.csv`. Closing them = pointing the existing `chrome-supplemental-scan` lane at `open-positions.json`'s `needs_chrome_fallback` list and feeding rendered postings back through the same schema.

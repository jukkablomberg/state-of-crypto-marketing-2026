# Corpus-assembly daily run — 2026-08-25 **(day 55 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-25 (**Tuesday**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, from the 08-24 recommendations:** (1) **run the symmetric sweep — audit the seventeen `N` rows** (watch zz), the highest-value sweep left; (2) **extend the grading ladder to `headcount_change` and `percentage`** (watch ab), then open rows 5 / 12 / 13; (3) **`CASPS.csv` — stop re-fetching it the same way; change the channel or ship it unread**; (4) do **not** re-fetch `OTHER.csv`, re-issue the retry queue, re-open MAS, or re-read `NCASP.csv` by the calendar; (5) six escalations to Jukka.
**Dedup baseline read before writing:** `2026-08-24-corpus-run.md` in full; `README.md`, `methodology.md`, `scripts/README.md`, `tracked-firms.md`, `corpus/README.md` in full; all 26 tracker rows via `csv.DictReader` with all 17 `N`-row notes read individually; `corpus/regulator-filings/`, `corpus/operator-statements/`, `corpus/layoff-tracker/`, `corpus/job-postings/`, `findings/` indexes; grep sweep for `binance` and for EU-cessation language across `corpus/` + `findings/`.
**✅ CADENCE: HELD. 08-24 → 08-25 is a ONE-DAY GAP. Watch (e′) improves to 9 of 10.** Corroborated from inside the data: today's class-1 fingerprint comparison is against **2026-08-24**, yesterday.

---

## Headline result

**All four mandated work items were executed. The channel change worked and closed the oldest queue entry. The symmetric sweep came back clean — the first time self-inspection has not found a defect in our own favour. And the deterministic feed, which has been the one part of this corpus that never needed adjudicating, turned out to be measuring itself.**

### 1. 🔴 **THE FEED GREW 47% OVERNIGHT AND THE GUARD CERTIFIED IT HEALTHY. IT WAS RIGHT BY ACCIDENT.**

`FEED HEALTH: HEALTHY … fingerprint total_jobs_fetched=3334, delta=+1071 vs 2026-08-24 (2263)`.

Opened against yesterday's backup of `open-positions.json`: **`companies_via_api` moved 89 → 99; `companies_via_chrome_pending` 58 → 48; `companies_scanned` never moved.** Ten firms became API-reachable (Circle, ConsenSys, FalconX, Fireblocks, Ondo, OpenAI, Parity, Ripple, Starknet, Stellar).

**The denominator changed. The job market did not.** The fingerprint predicate tests *movement* to certify liveness; it cannot distinguish *"the scan looked and the world moved"* from *"the scan looked at more of the world."* **The series is now discontinuous and no longitudinal reading may cross 08-24 → 08-25.**

**⚠ Watch (ss), inside our own instrumentation.** A +1071 delta *confirms* what the guard wants to be true, so it is the least-scrutinised possible result. Unopened, the record would have printed a true verdict resting on a false reason.

→ `../job-postings/_coverage-expansion-and-first-absence-panel-exit-2026-08-25.md` (**NEW**)

### 2. ⭐🔴 **A FIRM LEFT THE ABSENCE PANEL FOR THE FIRST TIME — AND ITS ABSENCE HAD NEVER BEEN ABOUT THE FIRM.**

**MetaMask / ConsenSys** exited `_absence.csv` (6 → 5) and `_chrome-queue.csv` (6 → 5). Upstream fixed the Greenhouse slug the blocker note has named for weeks. **The firm did nothing.**

The posting that arrived is dated **2026-08-06** — *Product Marketing Lead – Trade*, Lead/PMM. **It was public for nineteen days before this corpus could see it. It was never absent. We were.**

**The consequence is load-bearing.** Every row `_absence.csv` has ever held carries `reason = api-fetch-error` or `proprietary-ATS/needs-chrome`. **Not one has ever meant "this firm published nothing."** The file was honest — the `reason` column recorded it all along. **The reading was not.**

> 🔴 **PROHIBITED before ship:** any sentence of the form *"Binance / Bybit / HTX / KuCoin / Aave shows no public marketing-hiring signal."* The supportable sentence is *"is not reachable through the ATS APIs this corpus scans"* — a statement about our method, which belongs in the appendix.

### 3. 🟢 **CASPS.csv — CHANNEL CHANGED, FILE COMPLETE, AND THE THEME-4 ABSENCE CLAIM IS PERMITTED FOR THE FIRST TIME SINCE 08-17.**

Two `web_fetch` attempts returned **82,445 characters, byte-identical, cut mid-field.** A browser-context `fetch()` returned **163,026 characters, 335 rows, all 16 fields, final row terminating cleanly.** One URL, two channels, consecutive days.

**The 08-20 ruling is now confirmed by construction, not inference: the cut point is a property of the retrieval channel. Structure, not size.**

**Of the eleven Tier-1 tracked exchanges, nine hold an entry. Binance and HTX hold none** — zero occurrences in any field of any of 335 rows. Binance's absence has a published explanation (its own June 2026 EU-cessation notice, already in corpus). **HTX's has none.**

**🔴 And fourteen of the sixteen "absent" tracked firms are a category error, not a finding** — foundations are not service providers, non-custodial wallets are outside the CASP perimeter, Tether is an issuer. **Only Binance and HTX clear the bar.**

→ `../regulator-filings/esma-casps-register-complete-capture-alternate-channel-2026-08-25.md` (**NEW**)

### 4. 🟢 **THE SYMMETRIC SWEEP CAME BACK CLEAN — AND CAUGHT ONE THING.**

All seventeen `N` rows read individually. **Sixteen of sixteen labelled rows are correctly `N`**, each with an explicit non-AI rationale captured from its source. **The 35% → 15% collapse of 08-24 stands; the labelling is not noisy in both directions.**

**First result: the Y-side token predicate does not transfer.** Applied to the `N` rows it flags 16 of 17 — because on the `Y` side it reads the source and on the `N` side it reads *our own adjudication prose*. **A 94% false-positive rate. Same shape as the retired byte heuristic.**

**🔴 The catch: row 6 (MARA) was never labelled at all.** The cell was **blank**, and the 08-24 audit's *"9 of 26 Y, 17 N"* silently coerced it to `N`. **The adjudicable denominator is 25.** Grade-A share 15.4% → **16.0%** — a 0.6-point move, recorded at full length anyway, because an audit that quietly fills a blank cell with a category it just invented has manufactured a datapoint.

**⭐ And the binary column is destroying a better fact.** Robinhood did not merely have a non-AI rationale — **Tenev publicly declined the AI-blame framing** when it was offered. `N-absent` and `N-declined` are different findings. Proposed, **not applied** (schema change, n=1, seven days out).

### 5. 🔴 **THE FIGURE COLUMNS ARE GRADED, AND ONE HEADCOUNT NUMBER IN THE WHOLE TRACKER IS FIRM-STATED.**

New `headcount_grade` and `percentage_grade`, all 26 rows, same five-step ladder.

**Fourteen rows carry a headcount figure. Exactly one is Grade A — Gnosis, and it is scoped to two teams at a perimeter firm.** Sixteen carry a percentage; **four are Grade A, two of those are SEC filings.**

> 🔴 **PROHIBITED:** any aggregate headcount sentence across this tracker.
> 🟢 **PERMITTED:** *Only four of the 2026 crypto workforce reductions this corpus records carry a percentage the firm itself stated in a document we hold — and half of those are filings made to a securities regulator.*

→ `../layoff-tracker/_symmetric-n-sweep-and-figure-column-grading-2026-08-25.md` (**NEW**)

**Class 1: +1 net-new (first absence-panel exit in the series); guard HEALTHY but the delta is instrument growth, not signal. Class 2: byte-identical, 15th run, panel 71 days stale. Class 3: +1 NEW — CASPS captured COMPLETE via an alternate channel; Binance and HTX absent from the authorised register; fourteen other absences ruled category errors. Class 4: 0 net-new, TWELFTH consecutive recall confirmation. Class 5: 0 net-new layoffs; symmetric sweep clean; two new grade columns; one silent coercion repaired.**

---

## Six-class audit trail

### 0. Retry-queue seed — not re-issued, per mandate item 4

One line, as instructed. `OTHER.csv` not re-fetched. MAS not re-opened. `NCASP.csv` not re-read by the calendar.

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

```
date: 2026-08-25   source A (jobs) scan_date: 2026-08-25
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-24T21:49:01Z, age=14.4h,
  fingerprint total_jobs_fetched=3334, delta=+1071 vs 2026-08-24 (2263))
  reason: age 14.4h, fingerprint delta +1071
job postings ADDED: 1  firms: ['MetaMask / ConsenSys']
  of which via Chrome inbox: 0
```

**Both predicates pass and the verdict is correct, but the reason printed is not the reason it is true.** See headline 1. Fingerprint series, now with a denominator break:

```
2151 → 2151 (frozen) → 2186 → 2196 → 2259 → 2265 → 2263 ‖ 3334
                                                        ↑ break
```

**Absence panel 6 → 5:** Aave, Binance, Bybit, HTX, KuCoin. **Chrome work-queue 6 → 5:** Binance, Bybit, HTX, KuCoin, Solana. **First reduction in either list in the series.**

⚠ **The ConsenSys row is not first-party.** `web_fetch` refused `consensys.io/open-roles/8048308?gh_jid=8048308` — *"URL not in provenance set"* — and search-then-fetch did not surface it (it surfaced a different role, `/open-roles/6841507`). **The row rests on the feed's `url_verified=True`.** Watch (i), twelfth run. **The Chrome channel was deliberately NOT used here** — see §Discipline.

### 2. Agency claims / overlap matrix (deterministic)

`trend-data.json` `lastUpdated` **2026-06-15 — 71 days stale.** 18 agency-claims files written, **byte-identical for the fifteenth consecutive run.** 8 overlap-matrix rows. One overlap on a tracked firm: **Sui (Coinbound + RZLT)** — unchanged since first observation.

**Watch (d), 21st run.** `methodology.md` §6 still calls this a *"daily 18-agency panel."* **It is not daily and has not been for 71 days. Seven days to ship.**

### 3. Regulator — **+1 NEW. THE OLDEST QUEUE ENTRY IS CLOSED.**

Full record with seven explicit non-claims: `../regulator-filings/esma-casps-register-complete-capture-alternate-channel-2026-08-25.md`. See headline 3.

**Register composition:** 335 rows · 27 competent authorities · 26 member states · **+6 vs the 329-row COMPLETE baseline of 08-17.** SHA-256 of raw bytes `196090fa6fa15162fee56084dd0d0e53c158bb7347991538ce683b0b256d6b3e` (163,370 bytes) recorded as the auditable anchor.

⚠ **No snapshot file was written, and the reason is new.** Base64 transfer of the raw bytes was **blocked by the channel** (respected, not routed around). A text transfer was **ruled out on evidence**: raw 163,370 bytes vs UTF-8 re-encoded 163,367 — **the file is not valid UTF-8, so a text round-trip would have produced an artifact three bytes different from the register and indistinguishable by eye.** The 08-23 precedent extends: **a lossy re-encode is a fabrication too, even automated.**

⚠ **`verify-capture.py` NOT RUN, third consecutive run** — the fetch again never became a file. **But unlike 08-24 its predicates were applied programmatically**, against an RFC-4180 parser, not by hand. Weaker than the tool; stronger than 08-24. Labelled.

**Watch (b) — NOT restated. `NCASP.csv` was not re-read today.** The count stands at twenty by observation as of 08-23.

**Search, no net-new primary:** ESMA/BaFin/AMF/CONSOB/AFM/CySEC marketing-side actions — nothing in-window the corpus does not hold. ⚠ A third-party tracker (`casptracker.eu`) describes the warning register as carrying CONSOB + AFM + NBS entries; **this does not contradict the corpus's "one authority out of thirty," which is scoped to the five post-deadline additions, not the register's history. No contradiction was manufactured from it.**

**Not fetched, not guessed:** the five post-deadline CONSOB resolutions; `OTHER.csv` (standing instruction); the notification dates of the six new CASPS rows (**not isolated — no post-deadline authorisation rate may be printed**).

### 4. Operator statements — **0 NET-NEW. TWELFTH consecutive recall confirmation.**

Search returned agency SEO content and undated marketing-vendor blog posts. **No dated public statement by a CMO / VP Marketing / Head of Brand / Head of Growth at a tracked firm that the corpus does not already hold.**

⚠ **Watch (l), 22nd costing — a mild one, recorded for completeness.** The search surfaced a compliance podcast featuring **Crypto.com's Antonio Alvarez** speaking on MiCA. **Refused twice over:** §4 admits only marketing titles and his is compliance, and the episode carries **no date** in the surfaced result. The date failure alone is disqualifying, so this instance does **not** strengthen escalation (v) the way the Gemini SEC exhibit did. Recorded so it is not re-discovered as a near-miss.

**+0 admitted.**

### 5. Layoffs — **0 NET-NEW. Both mandated sweeps executed.**

Full record: `../layoff-tracker/_symmetric-n-sweep-and-figure-column-grading-2026-08-25.md`. See headlines 4 and 5.

| Sweep | Result |
|---|---|
| (zz) symmetric `N` audit, all 17 rows | **16/16 labelled rows correct.** Y-side token predicate does not transfer (94% FP). **Row 6 blank-coerced-to-N — repaired; denominator 26 → 25.** |
| (ab) figure grading, all 26 rows × 2 cols | `headcount_grade`: **A=1** C=6 D=1 E=5 UNCITED=1 n/a=12. `percentage_grade`: **A=4** B=2 C=9 D=1 n/a=10. |

**Rows 5 (Block), 12 (OP Labs), 13 (Kraken) NOT opened** — the fetch budget went to CASPS (mandate 3), refused twice and gating a Theme-4 claim. **All three now sit at Grade C on both figure columns, which is the sweep's own prediction of where they break.**

**Search returned:** FalconX, Crypto.com, Gemini, CryptoJobsList, layoffhedge, trueup — **all held. 0 net-new.** ⚠ **Both struck figures are still propagating in the search surface**: `layoffhedge.com` carries *"Crypto.com Layoffs 2026 – 180 Jobs Cut"* (the outlet's arithmetic, struck 08-22) and a Yahoo aggregate carries *"Gemini's roughly 30%"* (struck 08-24). **Refused again; the strikes are the reason they can be refused on sight.**

**Class-5 audit deltas** (`date-provenance-audit.py`, run post-edit, **exit 1**): `DATE-INVERSION` **0** · `NO-URL` **3 total** (1 class-5 MARA + 2 class-4) · `LAG-EXCEEDED` **2 total** · `SELF-DATED` 17 · `NO-URL-DATE` 13. **No regression** — the audit was re-run against the pre-edit tracker and returned **the identical verdict and the identical exit code**, so the two new columns and the row-6 repair changed nothing it measures.

> 🔴 **CORRECTION MADE BEFORE COMMIT — this record briefly claimed "exit 0", and it was wrong.**
> The first invocation was piped (`… | tail -25; echo $?`), so the captured status was **`tail`'s, not the script's.** `date-provenance-audit.py` exits **1** and has been exiting 1 since the NO-URL rows were first flagged on 08-21 — MARA plus two class-4 files, all pre-existing, none of them touched today. **The verdict text was read correctly; the exit code was not read at all.**
> **Recorded rather than silently fixed, because it is the run's own instance of the defect it spent the day documenting: a number that agreed with what the run wanted to be true, taken without being opened.** Watch (ss), fourth instance today, and the only one committed by this run rather than found by it. **Discipline adopted: never capture `$?` through a pipe when the exit code is the thing being reported.**

### 6. NorthPoint longitudinal panel

`findings/longitudinal-2026-06.md` — day-55 shift appended. Panel itself unchanged (71 days stale, §2).

---

## Discipline note — why the browser channel was used for one URL and refused for another

Two URLs were unreachable by `web_fetch` today, for **different reasons**, and were treated differently on purpose:

| URL | Failure | Action |
|---|---|---|
| ESMA `CASPS.csv` | **HTTP 200, content truncated** — the channel succeeded and returned unusable bytes | **Channel changed.** A truncation is a channel defect; recovering the same public document through a channel that does not truncate is the same retrieval, done correctly. |
| `consensys.io/open-roles/8048308` | **Refused — "URL not in provenance set"** | **Not routed around.** A provenance refusal is a refusal. The row is recorded as feed-verified, not first-party, and the gap is stated. |

**Recorded because the corpus's habit of "routing around it" is one search-result away from becoming a habit of ignoring refusals.** The two cases look alike from the inside and are not alike.

---

## Watch items

- **(b) First named post-deadline NCA marketing-side action** — **NOT RESTATED. The register was not re-read today.** Twenty by observation as of 08-23.
- **(d) Agency panel staleness — 71 days**, byte-identical fifteen runs running. **21st run. Seven days to ship.**
- **(e′) Cadence** — **✅ HELD. One-day gap; 9 of 10.**
- **(f) Friday nomination cadence** — **NOT TESTABLE TODAY (Tuesday).** Two consecutive Friday failures (08-14, 08-21) stand unrepaired; `inbound-nominations.md` still does not exist. **08-28 is the last Friday before ship — three days away.** Escalation (ii) at full strength.
- **(h′) Layoff rationale correlates with firm type** — **REJECTED, and now doubly so.** The `Y` labels carry five evidentiary weights (08-24) and the `N` labels conflate *absent* with *declined* (today). **Do not print.**
- **(i) `web_fetch` provenance refusals** — **🔴 TWELFTH RUN. Today it blocked verification of the first absence-panel exit in the series** — the most consequential class-1 event the corpus has recorded. Search-then-fetch did **not** rescue it this time. **Fix: paste the tracker's and feed's `source_url` values verbatim into the scheduled-task prompt.** One edit. Twelve runs unchanged.
- **(j) Senior-leader exits** — **ADVANCED, twelfth consecutive run.**
- **(l) §4 too narrow** — **22nd costing, but a WEAK instance** (undated compliance-officer podcast, refused on date as well as title). **Escalation (v) is not strengthened by it and is not inflated here.**
- **(n) Full-range re-sweep of classes 3, 4, 5** — **🟢 TENTH CONSECUTIVE VINDICATION.** The run's two biggest findings came from a *deterministic script's summary line* and a *register re-fetch* — the two least novel items on the plan.
- **(oo) The "not fetched, not guessed" list is a work queue** — **🟢 EIGHTH CONSECUTIVE PAYOUT, AND THE OLDEST ENTRY IS FINALLY CLOSED.** `CASPS.csv` came off the queue after eight days and two refusals, by changing channel rather than retrying. **New oldest live entries: the five CONSOB resolutions; AscendEX (eleventh carry); PIP Labs (fifth carry); two class-5 primaries that would upgrade grades C→A and B→A** (`theblock.co/post/391520`, Block/Dorsey; `x.com/diran_li/…`, Messari/Li) — both open since 08-06.
- **(pp) A clean parse is not a complete capture** — **🟢 FIRED AND PAID.** The guard's *logic* caught what its *executable* could not run on: 335/335 rows at full field count, final row terminating. **Third consecutive run where the tool could not open the artifact.** The plumbing gap is now the binding constraint on class 3, not the predicate.
- **(ss) A false item that confirms is not scrutinised the way a surprising one is** — **🔴 PAID FOUR TIMES, AND THE FOURTH WAS THIS RUN'S OWN.** (a) A +1071 fingerprint delta confirms liveness, which is what the guard wants, which is why nobody would have opened it. (b) A blank cell read as `N` agreed with the 08-24 denominator. (c) Fourteen "absent from the register" firms would have agreed with Theme 4. **(d) And this run reported `date-provenance-audit.py` as "exit 0" — a status captured through a pipe, belonging to `tail`, never actually read. Caught in final verification and corrected before commit.** **The watch has now fired on a search result, on a press release, on a search summary's fabricated names, on a guard's passing verdict — and on the run record's own reporting of a guard.**
- **(tt) A new guard's first run is a test of the guard, not of the corpus** — **🟢 HONOURED BY NOT SHIPPING ONE.** The `companies_via_api` comparability predicate is written down as a recommendation and deliberately **not implemented** seven days from ship.
- **(vv) A number is not safe until someone has read its citation** — **SIX-FOR-SIX, unchanged; no new citations opened.** But the ladder now says where the next breaks will be: **rows 5, 12, 13, all Grade C on both figure columns.**
- **(zz) The symmetric audit has never been run** — **🟢 CLOSED. RUN, AND IT CAME BACK CLEAN.** 16/16 correct. **The first time self-inspection has not found a defect in our own favour.** One real catch: a blank cell silently counted as `N`.
- **(ab) The figure columns need the grading ladder** — **🟢 CLOSED. SHIPPED.** Two columns, 26 rows. **One firm-stated headcount figure in the entire tracker.**
- **🆕 (ac) 🔴 THE FINGERPRINT SERIES IS NOT ONE SERIES.** The guard certifies liveness and is silent on comparability. **Persist `companies_via_api`; report UNCOMPARABLE when it moves.** Until then, no cross-08-24 reading.
- **🆕 (ad) 🔴 THE ABSENCE PANEL HAS NEVER CONTAINED AN ABSENCE.** Every row it has ever held is a statement about NorthPoint's ATS reach. **The methodology's "absence is data" rule is sound and the panel does not implement it.** Four of the five remaining rows are Tier-1 exchanges on proprietary SPAs — **the panel is a sample of firms that run their own recruiting stack, not a sample of silence.**
- **🆕 (ae) ⚠ THE COHORT IS 27 NAMED FIRMS; BOTH READMEs SAY THIRTY.** Counted: 11 + 8 + 5 + 3 named, plus 3 unresolved TBD placeholders. `tracked-firms.md` line 69's own arithmetic ("40 = 10+8+5+6+11") does not reconcile with its own tables. **Same defect class as the three layoff examples: a published number a hostile reader can count.**
- **Unchanged and not re-narrated today:** (a), (c), (e), (g), (h), (k), (m), (o), (q), (r), (s), (t′)/(dd), (u), (v), (w — CLOSED), (x), (y), (z — CLOSED), (aa), (bb)/(ff — CLOSED), (cc), (ee), (gg), (hh), (ii), (jj), (ll), (mm), (nn), (qq), (rr — downgraded), (uu), (ww), (xx — CLOSED), (yy).

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **HEALTHY, age 14.4h, fingerprint 2263 → 3334, delta +1071. +1 posting (ConsenSys).**
2. **Upstream adjudication:** `open-positions.json` compared field-by-field against `.backups/open-positions.json.20260824T214901Z.bak`. **`companies_via_api` 89 → 99; ten named firms left `needs_chrome_fallback`; `fetch_errors` set identical.** This is what settled the delta.
3. Repo dedup pass: 08-24 record in full; five repo docs in full; all 26 tracker rows via `csv.DictReader` with all 17 `N`-row notes read individually; five directory indexes; grep `binance` + EU-cessation language across `corpus/` + `findings/`.
4. **Programmatic cohort count** from `tracked-firms.md` tables → **27 named + 3 TBD.**
5. `web_fetch` `consensys.io/open-roles/8048308` → 🔴 **REFUSED, "URL not in provenance set."** Watch (i).
6. WebSearch — ConsenSys Product Marketing Lead → surfaced a **different** ConsenSys role (`/open-roles/6841507`) and job-board mirrors. **The specific URL was not brought into provenance. Row left feed-verified.**
7. WebSearch — ESMA/BaFin/AMF/CONSOB/AFM/CySEC marketing enforcement Aug 2026 → **0 net-new primary.**
8. WebSearch — crypto CMO / VP marketing Aug 2026 → **0 net-new.** Surfaced the undated Alvarez compliance podcast; refused on date and title.
9. WebSearch — crypto layoffs marketing Aug 2026 → **0 net-new.** Located both struck figures still propagating.
10. **Browser-context `fetch()` → ESMA `CASPS.csv`: 200, `text/csv`, 163,026 chars / 335 rows / 16 fields throughout / final row terminates.** 🟢 **COMPLETE.** SHA-256 `196090fa…` recorded.
11. **Browser-context analysis of the complete register:** RFC-4180 parse; tracked-firm lookup across `ae_lei_name` + `ae_commercial_name`; whole-row confirmation searches for Binance, HTX/Huobi, Securitize, Tether, Ledger, Aave; authority and member-state counts.
12. **Base64 byte transfer → BLOCKED by the channel. Respected, not routed around.** Text transfer **ruled out on evidence** (163,370 raw vs 163,367 re-encoded bytes — not valid UTF-8).
13. `python3 scripts/date-provenance-audit.py` — run post-edit, **exit 1** (3 NO-URL rows, all pre-existing). ⚠ **First reported here as "exit 0" — wrong; the status was captured through a pipe and belonged to `tail`. Corrected before commit, and the error is recorded in §5 rather than erased.** Re-run against the pre-edit tracker returned an identical verdict and identical exit code: **no regression.**
14. **`verify-capture.py`: NOT RUN — could not be.** Predicates applied programmatically by an equivalent implementation; weakening labelled.
15. **`OTHER.csv`, MAS, retry queue, `NCASP.csv`: deliberately not attempted**, per mandate item 4.
16. **No URL was fabricated. No figure was entered that its source did not state. No snapshot was hand-transcribed or lossily re-encoded. No absence claim was made from an unverified capture.**

---

## Net-new / changed this run

- `corpus/job-postings/_coverage-expansion-and-first-absence-panel-exit-2026-08-25.md` — **NEW.** The +1071 adjudication against the upstream backup; the fingerprint-discontinuity finding and the unimplemented comparability predicate; the first absence-panel exit and the prohibition it forces; the three Stratum-4 TBD slots now covered by the feed; the 27-vs-30 cohort count; six explicit non-claims.
- `corpus/regulator-filings/esma-casps-register-complete-capture-alternate-channel-2026-08-25.md` — **NEW. The run's shippable class-3 finding.** The channel comparison table; programmatic verification and the SHA-256 anchor; why no snapshot was written and why that reason is new; the nine-of-eleven Tier-1 table; **Binance and HTX absent**; the fourteen category-error absences; the Securitize/Stratum-4 inconsistency; seven explicit non-claims.
- `corpus/layoff-tracker/_symmetric-n-sweep-and-figure-column-grading-2026-08-25.md` — **NEW.** All 17 `N` rows adjudicated; the non-transferring token predicate; the blank-coerced-to-`N` repair and the 26 → 25 denominator; the `N-declined` proposal; both grade ladders with full distributions; the three things prose had hidden; five explicit non-claims.
- `corpus/layoff-tracker/2026-layoff-tracker.csv` — **UPDATED. 26 rows, now 10 fields.** New `headcount_grade` and `percentage_grade` populated for all 26; row 6 `ai_cover_narrative_y_n` corrected from blank to `(BLANK - NEVER LABELLED)` with its grade and note. **No figure changed, struck or added.**
- `findings/longitudinal-2026-06.md` — day-55 shift appended.
- `corpus/README.md` — index + reading rules updated.
- `corpus/job-postings/metamask-consensys.csv` — **NEW** (1 row, feed-verified). `_absence.csv` 7 → 6 lines, `_chrome-queue.csv` 7 → 6, `_feed-fingerprint.json` + agency files — sync writes (15th run).
- **Deliberately NOT written:** a CASPS snapshot file of any kind; any absence claim about the fourteen out-of-perimeter firms; any post-deadline authorisation rate from the +6 rows; any `verify-capture.py` exit code for today; any restatement of watch (b); the `N-declined` schema split; the `companies_via_api` guard; any edit to `tracked-firms.md`, `README.md` or `README-for-github.md`; any first-party claim for the ConsenSys posting; any Chrome-channel retrieval of a provenance-refused URL.

---

## Recommendation for next run

1. **🔴 OPEN ROWS 5, 12 AND 13 — THE LADDER HAS NAMED THEM.** All three are Grade C on both figure columns, which is the shape all six prior defects took. Watch (vv) is six-for-six and these are the last reachable rows. **Highest-value sweep left, and it is now a targeted one rather than a fishing trip.**
2. **🔴 ISOLATE THE SIX NEW CASPS ROWS' NOTIFICATION DATES.** Today's capture is complete and the +6 delta is real, but the dates were not read, so **no post-deadline authorisation rate may be printed.** One pass over a file whose retrieval route is now known to work. **This is the Theme-4 number the report actually wants** — how many CASPs were authorised *after* the transitional period ended.
3. **⚠ DECIDE THE ABSENCE-PANEL SENTENCE (new watch ad) BEFORE ANY THEME-1/THEME-4 DRAFTING.** The panel has never contained an absence. Either the methodology gains a paragraph distinguishing *firm silence* from *scanner reach*, or Themes 1 and 4 quietly inherit a claim the corpus cannot support. **Six days.**
4. **Do NOT re-fetch `OTHER.csv`. Do NOT re-issue the retry queue. Do NOT re-open MAS. Do NOT re-read `NCASP.csv` by the calendar. Do NOT re-fetch `CASPS.csv` via `web_fetch`.** One line each.
5. **Escalate to Jukka — six items, in order:**
   - **(i) 🔴 TWELFTH RUN, AND TODAY IT BLOCKED THE VERIFICATION OF THE SERIES' FIRST ABSENCE-PANEL EXIT.** `web_fetch` refused the ConsenSys posting URL; unlike 08-24, search-then-fetch did **not** rescue it. The corpus's first-ever proof that an "absent" firm was never absent rests on a feed flag rather than a first-party read. **Fix: paste the `source_url` values verbatim into the scheduled-task prompt. One edit. Twelve runs. Six days.**
   - **(ii) 🔴 THE README'S FRIDAY PROMISE — 08-28 IS THE LAST FRIDAY BEFORE SHIP, THREE DAYS AWAY.** Two consecutive Friday failures stand; no mailbox access; `inbound-nominations.md` does not exist. **Route the mailbox into a readable artifact this week, or amend the sentence. The second takes thirty seconds and is honest.** After 08-28 the choice is made by default.
   - **(iii) 🔴 THE READMEs NOW CARRY *TWO* COUNTABLE DEFECTS, NOT ONE.** The three layoff examples are 0-for-3 on inspection (Algorand, Crypto.com, Gemini) **and the cohort is 27 named firms while both READMEs advertise thirty** — with `tracked-firms.md`'s own arithmetic not reconciling with its own tables. **The corpus is public and both are countable in ninety seconds.** Correct four lines before ship.
   - **(iv) ⭐ THEME 5 NOW HAS TWO HONEST NUMBERS AND BOTH ARE SMALLER THAN THE OBVIOUS ONE.** *Nine of 25 adjudicable 2026 crypto workforce reductions are framed around AI; only four carry a verbatim statement from the firm itself.* And: *of the sixteen rows carrying a percentage, four are firm-stated — half of those in SEC filings. Of the fourteen carrying a headcount, one is.* **The aggregate-headcount sentence is now prohibited in the tracker's own documentation.**
   - **(v) ⚠ ESCALATION (v) IS UNCHANGED AND WAS NOT INFLATED TODAY.** §4's twenty-second costing was a weak instance (an undated compliance-officer podcast, refused on date as well as title). **The decision still rests on the three strong refusals of 08-23/08-24 — a CEO's dated statement, a firm's own account of its marketing function, and an SEC-filed exhibit. Decide it on those. Twenty-two runs of neither is not a position.**
   - **(vi) 🔴 `methodology.md` STILL NEEDS SIX SECTIONS REWRITTEN — §1, §3, §4, §5, §6, §7 — TWENTY-FIRST run for §1. SIX DAYS.** §1 must now also carry **watch (ad)**: the absence panel measures scanner reach, not firm silence. §3 must state the register's one-stated-reason structure, must not lean on `ae_infrigment`, and should carry the CASPS channel finding. §6's *"daily 18-agency panel"* describes a file **71 days stale**. §5 must carry `[DERIVED]` on Crypto.com, `[REPORTED]` on Luno, `[PERIMETER]` on Algorand, `[STRUCK]` on Gemini −30%, and now **three** grading ladders. **Still the one thing in the repo that could embarrass the report.**

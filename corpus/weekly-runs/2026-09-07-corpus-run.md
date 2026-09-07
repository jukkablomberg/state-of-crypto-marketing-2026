# 2026-09-07 — corpus run (day 68, sixth full post-window day)

**KPI — 11 of 11 units done. Bundle FROZEN; publish 2026-09-15.** The unit ladder is complete and no chapter is
re-drafted, per the REMAINING RUNS row in `synthesis-plan.md` (set 2026-09-03). Neither bounded exception is live
today: exception (a), the second-pass citation audit, was taken and closed by the 09-03 run; exception (b), the
**FCA v Huobi stay expiry, falls tomorrow — 09-08**. This run is STEP 0 plus this record.

**Not a FAILED run.** The prompt's failure test is a run that ends without a unit written or advanced. There is no
undone unit to advance, and manufacturing a twelfth would edit a frozen bundle the same plan forbids editing.

---

## STEP -1 — system map

`python3 _meta/verify_system_map.py` → **exit 0, clean** (15 active loops · 10 retired · 32 edge artifacts · 25
prompt checks). **No findings at all today** — yesterday's `[DEPLOY] _meta ahead=5` line is gone from the output.
Cause is on the record and is not this loop's: the os-plumber staged a push-only stanza for
`distribution-engineer.sh` this morning and Jukka **APPLIED** it in the ~11:00 EEST decision window
(`situation.md` RECENT DECISIONS, 2026-09-07). Recorded, not re-escalated.

**E22 unchanged.** This loop is still the producer; the report is still the consumer; Jukka still publishes. No work
was assigned to any other loop, so no other loop's prompt needed editing. This repo was **level with `origin/main`**
before this run's commit (`git log origin/main..HEAD` empty); the DE shipped 09-06 as designed.

---

## STEP 0 — post-window corpus check

`python3 repo/scripts/daily-corpus-sync.py`. **Class-1 capture window CLOSED 2026-08-31 and honoured in code**
(`CAPTURE_WINDOW_END` untouched). `_absence.csv` and `_chrome-queue.csv` were **not** rewritten; their `as_of` stays
2026-08-31. Only `_feed-fingerprint.json` was written — an instrument log, not a corpus claim.

| class | net-new |
|---|---|
| 1 — job postings | **0 admitted** (window closed; nothing offered, nothing admissible) |
| 2 — agency claims | **0** new relationships; 18 snapshot files written, 8 matrix rows, 1 tracked-firm overlap (Sui — Coinbound + RZLT); panel as-of **2026-06-15**, unchanged and not stale by Jukka's 07-10 Path-2 decision |
| 3 — regulator filings | **0** |
| 4 — operator statements | **0 net-new** (one candidate surfaced, rejected on cohort grounds — below) |
| 5 — layoff tracker | **0** |
| 6 — campaigns | **0** |

### 🟢 FEED HEALTH: RECOVERED after two stale days

`scanned_at_utc` 2026-09-06T21:46:06Z, **age 14.4 h** (limit 36 h; was 62.3 h yesterday, 38.3 h on 09-05),
fingerprint `total_jobs_fetched` **3458, delta +6** vs 09-06's 3452 — the first non-zero delta in four days. The
upstream NorthPoint ATS scan is moving again. The standing `scan_metadata` cross-check guard, which **refused the
class-1 absence claim on 09-05 and 09-06**, would pass today.

**No report consequence, and deliberately no back-fill.** The class-1 window closed 2026-08-31 and the absence
exhibit is frozen at that date, so neither the stale days nor today's recovery can reach the report body. The five
tracked firms still without coverage (Aave, Binance, Bybit, HTX, KuCoin) remain a **live read only**, unchanged and
unwritten. Recorded here so the two-day stall in the record closes with its own resolution rather than trailing off.
One dated line appended to `cos-feedback.md` closing the evidence count. **Not** escalated to `needs-jukka.md`.

**Drop-everything sweep — three explicit zeroes.**

1. **First named NCA marketing-side enforcement case: NO.** Searched again; the public picture is unchanged from
   09-03 → 09-06. What is published is *supervisory practice*: NCAs (CySEC named explicitly) sampling marketing
   communications across channels against the Art. 7 / Art. 66 fair-clear-not-misleading standard, checking
   risk-warning prominence and probing finfluencer-supervision programmes, with information requests, inspections
   and authorisation suspension available as remedies. All of it is **compliance-vendor secondary guidance
   describing the regime, not a named case against a named CASP.** No addendum box is owed. This is not a corpus
   gap — it is Chapter 1's thesis holding for a 68th day.
2. **Class-4 statement by a senior operator at a tracked firm about the marketing function: NO — one candidate
   surfaced and rejected on cohort grounds.** The sweep returned a crypto.news interview with **Bitget's CMO
   (Aguirre Franco)** arguing exchanges must evolve beyond trading. It is a marketing-seat statement about the
   function, but **Bitget is not in the tracked cohort** — it appears in this corpus only as a perimeter row in
   `corpus/layoff-tracker/2026-layoff-tracker.csv`. Class 4 is defined on the tracked cohort, so it is
   **non-admissible regardless of date**, and the window is closed besides. Not fetched, not entered. Logged so a
   later run does not re-surface it as new. The only other CMO material returned was the Conlan→Chen and
   Kalifowitz items, both long held and cited.
3. **2026 marketing-team layoff with a stated rationale: NO.** The cuts on the record are whole-company under
   AI-efficiency (Coinbase ~700 / ~14%, Crypto.com ~180 / 12%), automation-and-B2B-pivot (Luno ~20%) or
   market-conditions rationales, plus one operator ceasing trading operations. **Not one names marketing as the
   function.** Theme 5's headline thesis is unmoved.

**Watch items (POST-WINDOW — recorded here, not admitted to the report body).**

- The **">7,254 disclosed job cuts across 47 companies"** aggregator figure resurfaced a **fifth** time, again
  alongside a ">7,000" headline variant. Non-admission stands and is now well-tested: aggregator arithmetic against
  an unstated base is not a primary figure. Entered nowhere.
- **FCA v Huobi — the 09-08 check is live and falls tomorrow, and today's early read is NO CHANGE.** Jukka and the
  CoS probed the FCA proceedings page in the ~11:00 EEST decision window: **no settlement, no judgment and no
  extension published** as of this morning (`situation.md` RECENT DECISIONS, 2026-09-07). That is a day-before
  reading, not the check — the stay expires Tuesday. The 09-08 run re-opens the FCA
  proceedings page and, **only if an outcome is published**, updates the one sentence in Chapters 5 and 7 and
  rebuilds report → HTML → PDF with a dated `PUBLISH.md` changelog line. If nothing is published, the bundle stays
  frozen and the run says so. It is the last scheduled change before publication.

**Inbound nominations:** the Friday duty; today is Monday. Not due, not checked.

**Re-date side duty:** closed. The `PUBLIC-REDATE-2026-09-02.md` README lines were applied 09-02 and live-verified;
nothing owed.

---

## Bundle state — unchanged, and deliberately so

| artefact | state |
|---|---|
| `report/state-of-crypto-marketing-2026.md` | 23,070 words ≈ **21.0pp** of a 25pp budget |
| provenance gate | **250 URLs / 0 untraced** |
| `publish-bundle/report.html` | 176 live citation links |
| `publish-bundle/report.pdf` | 44pp A4 (WeasyPrint) |
| `publish-bundle/PUBLISH.md` | written; the PUBLISH needs-jukka row is **OPEN** since 09-02 |

No file in `findings/`, `report/` or `publish-bundle/` was touched by this run.

---

## What Jukka has to do

Nothing new. The single open ask is the existing row — **PUBLISH on 15 September, bundle ready at
`publish-bundle/`, steps in `PUBLISH.md`** (now the three morning-of checks plus `SOCM_PUBLISHED=1` in Vercel
Production and a redeploy, per the 09-04 publish-rail rewrite). No second row was filed and none will be.

**Next run (09-08): the FCA v Huobi check** — the one scheduled opportunity for the bundle to change before
publication.

**Sources opened this run:** search-level only; no new primary source was fetched, because no candidate cleared the
admissibility bar to justify a fetch.

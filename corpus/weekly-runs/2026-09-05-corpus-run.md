# 2026-09-05 — corpus run (day 66, fourth full post-window day)

**KPI — 11 of 11 units done. Bundle FROZEN; publish 2026-09-15.** Per the re-based cadence's REMAINING RUNS row
(`synthesis-plan.md`, set 2026-09-03), the unit ladder is complete and no chapter is re-drafted. Neither bounded
exception is live today: exception (a), the second-pass citation audit, was taken and closed by the 09-03 run
(its 09-03→09-05 window is spent, not merely open); exception (b), the FCA v Huobi stay expiry, falls on **09-08**.
This run is therefore STEP 0 plus this record.

**Not a FAILED run.** The prompt's failure test is a run that ends without a unit written or advanced. There is no
undone unit to advance. Manufacturing a twelfth unit would edit a frozen bundle, which the same plan forbids.

---

## STEP -1 — system map

`python3 _meta/verify_system_map.py` → **exit 0, clean.** 15 active loops · 10 retired · 31 edge artifacts ·
25 prompt checks. The `[MIRROR]` finding that the 09-04 run recorded (prompts-mirror `.auto` 2.3 h stale) has
cleared on its own — the launchd job is syncing again. Nothing to escalate and nothing to un-escalate.

**E22 unchanged.** This loop is still the producer; the report is still the consumer; Jukka still publishes. No work
was assigned to any other loop, so no other loop's prompt needed editing.

---

## STEP 0 — post-window corpus check

`python3 repo/scripts/daily-corpus-sync.py`. **Class-1 capture window CLOSED 2026-08-31 and honoured in code**
(`CAPTURE_WINDOW_END` untouched). `_absence.csv` and `_chrome-queue.csv` were **not** rewritten; their `as_of` stays
2026-08-31. Only `_feed-fingerprint.json` was written — an instrument log, not a corpus claim.

| class | net-new |
|---|---|
| 1 — job postings | **0 admitted** — and today, per the guard below, **0 is UNOBSERVED, not ABSENT** |
| 2 — agency claims | **0** new relationships; 18 snapshot files written, 8 matrix rows, 1 tracked-firm overlap (Sui — Coinbound + RZLT); panel as-of **2026-06-15**, unchanged and not stale by Jukka's 07-10 Path-2 decision |
| 3 — regulator filings | **0** |
| 4 — operator statements | **0** |
| 5 — layoff tracker | **0** |
| 6 — campaigns | **0** |

### 🟠 FEED HEALTH: STALE — and the cross-check guard did exactly what it exists to do

`scanned_at_utc` 2026-09-03T21:47:05Z, **age 38.3 h** (limit 36 h), fingerprint `total_jobs_fetched` 3452,
**delta +0** vs 09-04 (3452). The upstream NorthPoint ATS scan has not moved in two days: 09-04 read the same
timestamp at 14.6 h and passed; today the same timestamp is 38.3 h old and fails. **The standing `scan_metadata`
cross-check guard therefore REFUSED the class-1 absence claim**, and this run did not write one. A read of
"0 new postings" against a frozen scan means *unobserved*, not *absent* — the distinction the methodology's
absence-as-data rule stands or falls on.

**Consequence for the report: none.** The class-1 window closed 2026-08-31 and the absence exhibit is frozen at
that date, so a stale feed after the window cannot reach the report body. The five tracked firms still without
coverage (Aave, Binance, Bybit, HTX, KuCoin) remain a **live read only**, unchanged and unwritten.

**Ownership.** This is the same silent-producer-death instance the strategist filed 2026-08-30 (ATS scan frozen
since 08-27, caught then too by this loop's own feed-health guard) — a known fault with a named owner, not a new
blocker for this loop. Recorded here and as one dated line in `cos-feedback.md` for the evidence count; **not**
re-escalated to `needs-jukka.md`.

**Drop-everything sweep — three explicit zeroes.**

1. **First named NCA marketing-side enforcement case: NO.** Searched again. The public picture is unchanged from
   09-03/09-04: NCAs are described as running thematic reviews, supervisory sampling of marketing communications
   against the Art. 7 / Art. 66 fair-clear-not-misleading standard, and spot checks. No named marketing-side case
   against a CASP has been published. This is not a corpus gap — it is Chapter 1's thesis holding for a 66th day.
2. **Class-4 statement by a senior operator at a tracked firm about the marketing function: NO.** The CMO record
   surfaced nothing new. The Binance transition remains exactly as the report states it in the narrower CITED
   reading (CoinDesk 2026-05-12 announcement; effective date a separate field). Nothing about a search process was
   found, and nothing was added.
3. **2026 marketing-team layoff with a stated rationale: NO.** Cuts continue to be announced at the whole-company
   level under AI-efficiency, market-conditions or narrowing-focus rationales; **not one names marketing as the
   function.** Theme 5's headline thesis is unmoved.

**Watch items (POST-WINDOW — recorded here, not admitted to the report body).**

- The ">7,254 disclosed job cuts across 47 companies" aggregator figure resurfaced a **third** time. Non-admission
  stands for the third time: aggregator arithmetic against an unstated base is not a primary figure. Entered
  nowhere. Logged only so a later run does not mistake it for new.
- **FCA v Huobi — the 09-08 check is live and unchanged.** The stay expires Tuesday. That run re-opens the FCA
  proceedings page and, **only if an outcome is published**, updates the one sentence in Chapters 5 and 7 and
  rebuilds report → HTML → PDF with a dated `PUBLISH.md` changelog line. If nothing is published, the bundle stays
  frozen and the run says so.

**Friday duty — inbound nominations: checked, none.**

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
`publish-bundle/`, steps in `PUBLISH.md`.** No second row was filed and none will be.

**Next runs (09-06 → 09-07):** STEP 0 and one line. **09-08:** the FCA v Huobi check.

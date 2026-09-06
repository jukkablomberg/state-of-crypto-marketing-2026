# 2026-09-06 — corpus run (day 67, fifth full post-window day)

**KPI — 11 of 11 units done. Bundle FROZEN; publish 2026-09-15.** The unit ladder is complete and no chapter is
re-drafted, per the REMAINING RUNS row in `synthesis-plan.md` (set 2026-09-03). Neither bounded exception is live
today: exception (a), the second-pass citation audit, was taken and closed by the 09-03 run; exception (b), the
FCA v Huobi stay expiry, falls on **09-08**. This run is STEP 0 plus this record.

**Not a FAILED run.** The prompt's failure test is a run that ends without a unit written or advanced. There is no
undone unit to advance, and manufacturing a twelfth would edit a frozen bundle that the same plan forbids editing.

---

## STEP -1 — system map

`python3 _meta/verify_system_map.py` → **exit 0**. 15 active loops · 10 retired · 32 edge artifacts · 25 prompt
checks. One finding, and it is **not this loop's**:

> `[DEPLOY] DEPLOY-STRANDED _meta ahead=5 since 2026-08-17 05:23 UTC (486.7 h)` — committed, never pushed.

**Already owned and already filed.** The `product-builder` logged it as `[NP-DEPLOY-BLOCK-VISIBLE]` for `os-plumber`
in `cos-feedback.md` on 2026-09-06: `_meta` has an `origin` remote but `distribution-engineer.sh` enumerates repos
under `projects/` only, so it has a producer and no shipper. Recorded here so a reader of this run record does not
read an exit-0-with-findings as new breakage. **Not re-escalated** — it has a named owner and a filed row.

**E22 unchanged.** This loop is still the producer; the report is still the consumer; Jukka still publishes. No work
was assigned to any other loop, so no other loop's prompt needed editing. This repo is **level with `origin/main`**
(`git log origin/main..HEAD` empty before this run's commit) — the DE shipped 09-05 as designed.

---

## STEP 0 — post-window corpus check

`python3 repo/scripts/daily-corpus-sync.py`. **Class-1 capture window CLOSED 2026-08-31 and honoured in code**
(`CAPTURE_WINDOW_END` untouched). `_absence.csv` and `_chrome-queue.csv` were **not** rewritten; their `as_of` stays
2026-08-31. Only `_feed-fingerprint.json` was written — an instrument log, not a corpus claim.

| class | net-new |
|---|---|
| 1 — job postings | **0 admitted** — and again, per the guard below, **0 is UNOBSERVED, not ABSENT** |
| 2 — agency claims | **0** new relationships; 18 snapshot files written, 8 matrix rows, 1 tracked-firm overlap (Sui — Coinbound + RZLT); panel as-of **2026-06-15**, unchanged and not stale by Jukka's 07-10 Path-2 decision |
| 3 — regulator filings | **0** |
| 4 — operator statements | **0 net-new** (one candidate examined and found already in the corpus — see below) |
| 5 — layoff tracker | **0** |
| 6 — campaigns | **0** |

### 🟠 FEED HEALTH: STALE for a second consecutive day — and worsening

`scanned_at_utc` 2026-09-03T21:47:05Z, **age 62.3 h** (limit 36 h; was 38.3 h yesterday), fingerprint
`total_jobs_fetched` 3452, **delta +0** vs both 09-05 and 09-04. The upstream NorthPoint ATS scan has not moved in
**three days**. The standing `scan_metadata` cross-check guard therefore **REFUSED the class-1 absence claim for the
second day running**, and this run did not write one.

**Consequence for the report: none.** The class-1 window closed 2026-08-31 and the absence exhibit is frozen at that
date, so a stale feed after the window cannot reach the report body. The five tracked firms still without coverage
(Aave, Binance, Bybit, HTX, KuCoin) remain a **live read only**, unchanged and unwritten.

**Ownership unchanged.** Same silent-producer-death instance the strategist filed 2026-08-30. A known fault with a
named owner, not a new blocker for this loop. One dated line appended to `cos-feedback.md` for the evidence count —
the escalation is that it is now **three days frozen and lengthening**, not that it is new. **Not** re-escalated to
`needs-jukka.md`.

**Drop-everything sweep — three explicit zeroes.**

1. **First named NCA marketing-side enforcement case: NO.** Searched again. The public picture is unchanged from
   09-03 → 09-05: NCAs are described running thematic reviews and supervisory sampling of marketing communications
   against the Art. 7 / Art. 66 fair-clear-not-misleading standard, plus spot checks. Secondary compliance-vendor
   guides describe the *supervisory practice*; **no named marketing-side case against a CASP has been published.**
   This is not a corpus gap — it is Chapter 1's thesis holding for a 67th day.
2. **Class-4 statement by a senior operator at a tracked firm about the marketing function: NO NET-NEW —
   one candidate examined and rejected as already-held.** The sweep surfaced the CoinGape *Block of Fame* interview
   with **Eowyn Chen, Binance interim CMO** — a tracked firm, a senior marketing seat, and squarely about the
   marketing function. It was fetched and read in full rather than judged from a headline. **It is dated 18 July
   2026 (`article:modified_time` 2026-07-20), it is in-window, and it is already in the corpus and in the report:**
   `corpus/operator-statements/binance-chen-marketing-not-hype-2026-07.md`, cited in Chapter 2 (the "comprehension
   as the product" contrast against Coinbase and Kraken), in Chapter 3's AI matrix and narrative, and twice in the
   citation index — in every place with the near-primary caveat intact (branded-content vertical that sells
   cover-story placement, not labelled sponsored; usable for what Chen said, not as evidence of editorial
   selection). **Nothing added, nothing changed.**
   > 🟢 **Incidental re-verification, recorded because it costs nothing and the claim is live.** Chapter 5 states
   > that this interview mentioned MiCA, the EU and the exit *zero* times and never used the words "regulation" or
   > "regulatory" at all. Today's full fetch confirms it: no occurrence of *MiCA*, *EU*, *regulation* or
   > *regulatory* anywhere in the piece. The nearest word in it is "compliance", inside an AI-infrastructure
   > sentence — which is precisely the point the chapter makes. The claim stands as written.
3. **2026 marketing-team layoff with a stated rationale: NO.** Cuts continue to be announced at the whole-company
   level under AI-efficiency, market-conditions or narrowing-focus rationales. **Not one names marketing as the
   function.** Theme 5's headline thesis is unmoved.

**Watch items (POST-WINDOW — recorded here, not admitted to the report body).**

- The **">7,254 disclosed job cuts across 47 companies"** aggregator figure resurfaced a **fourth** time (now also
  as a ">7,000" variant, and a separate "over 5,700" figure from a different aggregator — the two disagree, which
  is itself the reason for the bar). Non-admission stands: aggregator arithmetic against an unstated base is not a
  primary figure, and two aggregators publishing different totals for the same year does not make either primary.
  Entered nowhere. Logged only so a later run does not mistake it for new.
- Secondary commentary that "teams that previously prioritized aggressive marketing are being reduced" appeared in
  a market-roundup piece with **no named firm and no primary attribution**. **Non-admissible** and deliberately not
  entered: it reads as support for Theme 5's thesis while being exactly the kind of unsourced generality the thesis
  is built to be falsifiable against. Recorded so a later run does not admit it on a second sighting.
- **FCA v Huobi — the 09-08 check is live and unchanged.** The stay expires Tuesday. That run re-opens the FCA
  proceedings page and, **only if an outcome is published**, updates the one sentence in Chapters 5 and 7 and
  rebuilds report → HTML → PDF with a dated `PUBLISH.md` changelog line. If nothing is published, the bundle stays
  frozen and the run says so.

**Inbound nominations:** the Friday duty; today is Sunday. Not due, not checked.

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

**Next run (09-07):** STEP 0 and one line. **09-08:** the FCA v Huobi check.

**Sources opened this run:** [CoinGape — Chen interview](https://coingape.com/block-of-fame/opinion/crypto-marketings-next-job-isnt-hype-binance-interim-cmo-eowyn-chen/) (re-verification only; already in corpus).

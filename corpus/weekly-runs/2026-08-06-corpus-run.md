# Corpus-assembly daily run — 2026-08-06 **(day 36 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-06 (Thursday).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, verbatim from the 08-05 recommendations:** (1) fix the feed-health guard (watch bb) **before anything else**; (2) paginate the ESMA index to cover post-deadline days 1–8; (3) 08-09 time-to-teardown measurement (scheduled, not today); (4) sweep MAS at source; (5) test watch (z) across the panel; (6) implement the four-field date schema (watch aa); (7) escalate five items.
**Dedup baseline read before writing:** `2026-08-05-corpus-run.md` in full; `layoff-tracker/2026-layoff-tracker.csv` all 18 rows; `regulator-filings/` (14 files, index); `operator-statements/` (5); `marketing-campaigns/` (10); `findings/longitudinal-2026-06.md` tail; `findings/00-opening-register-first-cases-later.md` head + tail; `_absence.csv`; `open-positions.json` `scan_metadata` + all 28 filtered roles; repo-wide greps for `messari`, `pip labs`, `esma.europa.eu` URLs, `common-supervisory-action-casps`.
**CADENCE: RECOVERED.** 08-05 ran, 08-06 ran. Last gap 08-04. Guard (e′) improving.

---

## Headline result

**Four things, in descending order of consequence.**

**1. The thirty-six-day null now has a stated reason, and the reason is deliberate forbearance.** The FT reported today, and The Block relayed verbatim, that the **AMF has avoided setting an aggressive deadline for unlicensed exchanges to halt operations — in order to limit scams** targeting users pushed off those venues. It is attributed to a **named official with a title and a directorate**: Stéphane Pontoizeau, executive director, market intermediaries and market infrastructure supervision. **This is the first explanation for the enforcement absence that comes from a supervisor rather than from the corpus's own inference.** → `../regulator-filings/eu-nca-post-deadline-scam-warnings-and-amf-forbearance-2026-08-06.md` (NEW FILE).

**2. Yesterday's discharged instrument failed its first falsification test, and it failed silently.** The 08-05 run swept ESMA's news index, found a clean null across days 9–33, **discharged watch (w) for ESMA**, and recommended paginating to close days 1–8. Pagination ran today. **Page 1 ends 10/07/2026; page 2 begins 02/06/2026 — a 37-day hole — and this corpus holds two ESMA items inside it**, one of which (the 8 July Common Supervisory Action) lives at a `/press-news/esma-news/` URL, i.e. in the index that omits it. **Watch (w) is UN-DISCHARGED for ESMA. No absence claim may rest on that index.**

**3. Two layoff-rationale hypotheses are dead, and the second one died the same day it became tempting.** The Messari backfill (2026-03-16, firm-stated **"AI-first"** pivot) makes the natural successor to watch (h′) — *AI framing early, market framing late* — look compelling for about a minute, until Messari (AI, March) is placed beside OP Labs (non-AI, 12 March) and Luno (AI, 28 July) beside six non-AI July rows. **Both hypotheses tested and rejected; both recorded as rejected so a later run does not re-derive them.**

**4. The corpus's own guard now works, and it caught nothing — which is the point.** Watch (bb) implemented in `scripts/daily-corpus-sync.py`: the sync now prints an explicit **FEED HEALTH** verdict with `scanned_at_utc`, age in hours, and a `total_jobs_fetched` fingerprint, and **refuses to permit a class-1 absence claim when the upstream scan is stale or undatable**. Today: **HEALTHY, 14.4h, fingerprint moved 2,087 → 2,090.** Today's zero is therefore a genuine *absent*, not an *unobserved* — and for the first time that distinction is machine-asserted rather than eyeballed.

**Day-36 named marketing-side enforcement silence HOLDS** — and is now, for the first time, partially *explained by a regulator* rather than merely measured.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0 — and this time that is a real absence.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-08-06
source A (jobs)   scan_date: 2026-08-06
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-05T21:45:20Z, age=14.4h,
             fingerprint total_jobs_fetched=2090)
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

**WATCH (bb) IMPLEMENTED — mandate item 1, done first as instructed.** The guard compares `scanned_at_utc` to now, flags **HEALTHY** (≤36h) / **STALE** (>36h) / **UNKNOWN** (unparseable), carries `total_jobs_fetched` as an idempotency fingerprint so *"ran and found nothing"* is distinguishable from *"did not run"*, and prints an explicit refusal line — `CLASS-1 ABSENCE CLAIM REFUSED` — in the non-healthy case. `scripts/README.md` updated.

**The upstream feed recovered on its own.** 08-05 read a scan frozen at `2026-08-02T21:46:03Z` (~66h). Today: `2026-08-05T21:45:20Z`, 14.4h, and the fetch total moved **2,087 → 2,090** with `total_jobs_after_filter` **27 → 28**. The scan ran, looked, and found no net-new *tracked-cohort* marketing role. **That is an absence claim the corpus is now entitled to make.** The 08-04/08-05 class-1 entries remain **"unobserved"** and must not be retro-converted.

**Where the +1 went, checked rather than assumed:** all 28 filtered roles carry `first_seen 2026-08-05`; the cohort-matching layer admitted none of them. The 28 are dominated by **non-cohort AI labs** — Anthropic ×9, Perplexity ×3, Cohere ×2 — plus tracked-adjacent Coinbase (Creative Director), Gemini (Predictions Partnerships Marketing Lead), Phantom (Head of Brand Creative) and Kraken (Director, Paid Marketing ×2), all of which are **already-held rows, correctly deduped by `source_url`**. Kraken's twin reqs are now **15 days open**; Gemini's Predictions role **8 days**. Time-to-fill is accruing on both and nothing has been written about it yet.

**Watch (y) unchanged:** class 1's only pre-2026 rows remain arithmetic inferences from relative Getro board labels.

#### Absence panel — four upstream gaps unfixed for a **sixth** run
`_absence.csv`: Aave (Lever 404) + Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys (proprietary, chrome-pending). **OKX (Tier-1), Securitize, Rabby, Relai remain missing from the upstream company list.** No config write attempted — that is the sales funnel's repo. **Sixth run. It needs an owner outside the corpus run.**

### 2. Agency claims / overlap matrix (deterministic)

18 agency-claims files rewritten; 8 matrix rows; **1 OVERLAP: Sui (coinbound, rzlt)** — unchanged. **`trend-data.json` `lastUpdated` still 2026-06-15 — the panel is now 52 days stale.** Watch (d) stable-by-decision; `methodology.md` §6's phrase *"daily 18-agency panel"* remains inaccurate as written. Escalation stands, **sixth run**.

### 3. Regulator — **2 NET-NEW FILES. Watch (w) UN-DISCHARGED for ESMA. MAS swept at source for the first time.**

#### (a) The AMF forbearance statement — the run's principal result
→ `../regulator-filings/eu-nca-post-deadline-scam-warnings-and-amf-forbearance-2026-08-06.md` (NEW).

Three EU authorities on the record about post-deadline conduct, dated **today**:

- **AMF** — **Stéphane Pontoizeau**, named with directorate: the moment is *"an opportunity for scammers more than usual."* The AMF has identified suspects **posing as AMF staff** to redirect client assets. And, decisively: **it has avoided setting an aggressive shutdown deadline for unlicensed exchanges precisely to limit those scams.**
- **AFM** — bad actors may target investors **searching for an alternative licensed provider**.
- **ESMA** — aware of fraudulent activity **exploiting ESMA's own logo** to promote scams.

**Why this is the strongest class-3 item since the deadline.** The corpus could previously offer only structural readings of the null. It now holds a *supervisory rationale*: at least one NCA is consciously declining to force the issue, for a stated consumer-protection reason. **The three-part Phase-2 wording is: perimeter-shaped toolkit (structural) + first coordinated action aimed elsewhere (prioritisation) + deliberate forbearance, named and sourced (conduct). Print all three. Never print "silence."**

**Marketing-side reading:** the first regulator-brand abuse in this corpus is a *marketing* abuse — ESMA's mark deployed as a trust signal inside someone else's acquisition funnel. And the AFM's warning identifies the target population as consumers *shopping for a licence*. Read with the Google Ads France change of 2026-07-01, the shape is clean: **authorisation has become the highest-converting claim in EU crypto marketing — platform-enforced, fraudster-counterfeited, and regulator-unadjudicated.**

**Provenance, stated plainly.** Captured source: The Block, 2026-08-06 05:08 EDT, bylined Timmy Shen, fetched HTTP 200. Underlying primary: **FT, paywalled, NOT fetched** — URL recorded only because The Block links it verbatim. **NEAR-PRIMARY. `[VERIFY]` at the FT before Phase 2 prints the quote.**

**Theme-4 register arithmetic, logged not resolved:** The Block reports **"roughly 320"** MiCA-authorised entities per an ESMA list *updated Aug 5*, against an FT/VASPnet estimate of **>1,700 needing to cease operations**. NorthPoint's own primary-register read the same day returned **324** distinct pairs — *including two firms whose authorisation has already ended*. Compatible, not identical. **`[VERIFY]`; state the snapshot date and the de-dup rule or do not print the number.**

**NOT AN ENFORCEMENT ACTION.** No firm named as subject, no measure imposed, no marketing communication found deficient. **The day-36 null holds.** This item explains it; it does not end it.

#### (b) MAS PS-G02 — standing gap closed for the instrument
→ `../regulator-filings/mas-ps-g02-dpt-public-promotion-guidelines.md` (NEW). **Mandate item 4, done.**

PDF fetched and read verbatim. Admitted despite its 2022 date under the same standing exception as MiCA itself: it is the operative instrument, not news.

**The finding is the contrast, and it reframes the headline null.** MiCA governs *what marketing may say*. **PS-G02 governs whether marketing may exist**: DPT providers *"should not promote their DPT services to the general public in Singapore"* — public areas, transport, broadcast, periodicals, third-party sites, social platforms, public events, **and social-media influencers by name (§2.3)** — with a carve-out only for a firm's **own website, apps and official accounts (§2.2)**. Physical ATMs are treated as promotion (§3.1).

> **MiCA adjudicates content. MAS forecloses reach.** The EU's thirty-six-day enforcement null is a fact about a regime that must adjudicate in order to act at all. That is a far better frame for the null than duration, and both halves are now anchored to primaries.

**Cross-reference to the campaign corpus, with the verdict REFUSED.** The 08-05 run captured `okx.com/en-sg/…` live under an "OKX Singapore" masthead. The corpus now holds that capture *and* the instrument governing promotion in that jurisdiction. **It draws no inference**, for three reasons written into the file: §2.2 expressly permits own-website promotion; entity scope under the PS Act is not established here; and the *"trivialises the high risks"* test is an adjudication this corpus does not perform. **Exposure-surface datum, not a finding of breach.**

**Honest limit, stated so it is not misread:** this closes MAS for the **instrument only**. **The MAS enforcement register remains unswept**, so no MAS absence claim may be made in the way the six EU NCAs support one. The landing page returned an empty body; the PDF is the capture of record.

#### (c) ESMA pagination — the recommendation executed, the premise falsified
`?page=1` fetched. **Page 1: 03/08 → 10/07. Page 2: 02/06 → 07/05.** A **37-day discontinuity**, and the corpus holds **two ESMA items inside it**:

1. **23 June 2026** — Public Statement ESMA75-113276571-1710 on the transitional-period end (`esma-mica-transitional-period-end-2026-06.md`).
2. **8 July 2026** — Common Supervisory Action on CASPs' digital operational resilience, at `https://www.esma.europa.eu/press-news/esma-news/esma-launches-common-supervisory-action-casps-digital-operational-resilience` — **an item in the news index that the news index does not return.**

**Cause NOT established, and the file says so:** `?page=1` may be rendering a filtered view rather than a pure offset (the response carried a "Reset filters" control absent from page 1), i.e. this may be a fetch artefact rather than an ESMA defect. **The operational conclusion is cause-independent: the index drops items it holds, so it cannot carry an absence claim.** Yesterday's bounded claim narrows from *"across the 24 days page 1 covers, ESMA published no crypto-marketing item"* to *"no crypto-marketing item appears among the ten items page 1 returned."* **Watch (w) reopened for ESMA. Days 1–8 remain uncovered and are now known to be uncoverable by this route.**

**Second consecutive run in which the corpus caught its own instrument reporting an unverified state.** Yesterday's was luck; today's came from executing a recommendation. That is the argument for keeping the recommendation list.

**NOT REACHED, NOT GUESSED:** FT original (paywalled) · ESMA index pages 3+ and the `sort_by=chronological` view (**the obvious next attempt at days 1–8**) · MAS enforcement register · **PSN08 Notice on Disclosures and Communications** (the disclosure rule PS-G02 §2.2 is measured against — the natural next MAS primary) · MAS Guidelines on Licensing for DTSPs · **VARA, still never swept at source** · CONSOB comunicato PDFs · BaFin/CySEC/CNMV re-sweeps. **No URL was fabricated.**

### 4. Operator statements — **0 NET-NEW. Class 4 stays at 5 files. Third consecutive run in which the best quote found was refused on the role gate.**

The August CMO / Head-of-Marketing sweep surfaced no in-window verbatim statement by a qualifying marketing operator at a tracked firm.

**The refusals, logged because the gate only means something when applying it costs something.** Two quotable, dated, first-party sentences were found and both fail §4: **Pontoizeau (AMF)** is a supervisor, not a marketing operator — correctly routed to class 3; **Diran Li (Messari)** is a CTO-turned-CEO, not a marketing seat, and Messari is perimeter besides — routed to class 5.

**Class 4 is static for a 5th day and has produced 1 item in 11 days.** Watch (l), **7th costing**. The empirical case for widening §4 now runs to four consecutive runs: Mulvenny (08-03), the Coinbase spokesperson (08-05), Pontoizeau and Li (08-06) — **the four most useful sentences found in four days were all structurally ineligible.** §4 is not selecting for quality; it is selecting for job title.

### 5. Layoffs — **1 NET-NEW ROW + 1 ROW CORRECTED. Tracker 18 → 19.**

**Messari [PERIMETER]**, **2026-03-16**, crypto market-data and research firm. CEO **Eric Turner** stepped down (remains an advisor); CTO **Diran Li** assumed the role after board discussions; layoffs conducted alongside. **Headcount and percentage NOT disclosed by the firm — no figure is entered and none may be printed.** Firm-stated rationale is **AI-framed**: repositioning as an *"AI-first"* company serving institutions through research and AI-driven products. Verbatim from Li: *"This transition also includes a difficult decision: we've parted ways with many teammates who helped build Messari into what it is today."*

Captured source: The Block 2026-03-16 (fetched, HTTP 200, bylined Danny Park), which **discloses that Messari is a competitor of The Block** — noted, not treated as disqualifying. **Primaries cited and linked but NOT fetched** (same limit as the Gnosis row): the Li and Turner X posts. `[VERIFY]` before Phase 2 quotes Li directly.

**ROW CORRECTED — Block, Inc.** was carried as `2026-Q2, 4000` with `ai_cover = N` and no source URL. **Both captured articles date the round to "last month" relative to mid-March 2026 → February 2026, i.e. Q1**, and both describe it as **~4,000 jobs / roughly 40%**, framed by Dorsey as a smaller, flatter, AI-driven organisation — **and explicitly cited by Messari's incoming CEO as the template for its own pivot.** Row re-dated **2026-02**, `ai_cover` flipped **N → Y**, percentage `~-40% [VERIFY]`, source attached. The underlying primary (`theblock.co/post/391520/…`) is **linked by both captures but not itself fetched**; day-of-month and the 4,000/40% reconciliation stay open.

**TWO HYPOTHESES TESTED AND REJECTED THIS RUN — recorded as rejected so a later run does not re-derive them.**

| Hypothesis | Falsifier |
|---|---|
| **(h′)** AI framing at consumer exchanges, repositioning framing at infrastructure/protocol firms | **Uphold** (07-27) — consumer-facing, explicitly non-AI |
| **NEW, tempting, false** — AI framing is early-2026, market framing late-2026 | **Messari** (AI, 03-16) sits beside **OP Labs** (non-AI, 03-12); **Luno** (AI, 07-28) sits among six non-AI July rows |

**What survives is only the weak, honest statement:** AI framing runs the length of the 2026 window and has been the **minority** framing since mid-July (Jul: 1 of 7; Aug: 0 of 1). **Do not print a correlation.**

**watch (n) → FOUR-FOR-FOUR.** OP Labs (Mar→Jul), Kraken (May→Jul), Coinbase→OpenAI (Apr→Aug), **Messari (Mar→Aug)**. All in-window, all at well-covered firms, all in top-tier outlets, all found late and incidentally — **Messari was found while reading a competitor's newsletter for something else.** This is a measured instrument defect, not luck.

**Standing finding unchanged, cohort-scoped: no TRACKED firm's 2026 contraction has named marketing as an affected function.** The tracker-scoped version remains broken by the perimeter Gnosis row, whose marketing claim is still single-sourced to an X post and whose two primaries remain uncaptured. **Still the corpus's highest-value verification item; not advanced this run — fifth run carried.**

### 6. NorthPoint longitudinal panel

`trend-data.json` **52 days stale**. No trend claim made.

---

## Cross-class methodological finding — the secondary layer is going machine-written

Recorded because it is a provenance variable, not a curiosity. **Two of this run's capture sources disclose model assistance, and the disclosure varies article-by-article inside a single outlet:**

- The Block, *The Daily*, 2026-03-17: *"produced with the assistance of OpenAI's ChatGPT/xAI's Grok and reviewed and edited by our editorial team."*
- The Block, news items 2026-03-16 and 2026-08-06: **no such disclosure.**
- The Cryptonomist (FalconX row, 08-05): AI-assistance disclosure.

For a report whose entire claim is verifiability, **"was this secondary machine-written?" is a schema field, not a footnote.** Proposed: `capture_ai_disclosure` on every non-primary capture, added alongside the four date fields of watch (aa).

---

## What this run did to the mandate

| # | 08-05 recommendation | status |
|---|---|---|
| 1 | Fix the feed-health guard (watch bb) **first** | **DONE, and done first.** HEALTHY/STALE/UNKNOWN verdict + fingerprint + explicit absence-claim refusal; `scripts/README.md` updated. Passed cleanly today (14.4h). |
| 2 | Paginate ESMA to cover days 1–8 | **DONE — and it falsified its own premise.** 37-day hole, two counterexamples from the corpus's own holdings. **Watch (w) un-discharged for ESMA.** |
| 3 | 08-09 time-to-teardown measurement | **on schedule.** Three days out. Not touched today. |
| 4 | Sweep MAS at source | **DONE for the instrument.** PS-G02 fetched verbatim; the reach-vs-content contrast is the run's best Phase-2 frame. **Enforcement register still unswept — said so.** |
| 5 | Test watch (z) across the panel | **NOT DONE. Carried a FOURTH run.** |
| 6 | Implement the four-field date schema (watch aa) | **NOT IMPLEMENTED, fourth run — and its scope grew again** (see the AI-disclosure field above). |
| 7 | Escalate five items | **DONE — below; four carried, one closed, one new.** |

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged. Named today as the notable MiCA failure case; no new fact.
- **(b) First named post-deadline NCA marketing-side action** — **day-36 silence HOLDS, and today it acquired a supervisory rationale.** Phase-2 wording is now **three-part**: structural (perimeter-shaped toolkit) + prioritisation (first CSA aimed at custody) + **forbearance (AMF, named, on the record)**. **Never print "silence."**
- **(c) Capture panel** — untouched today. **(ii) 08-09 time-to-teardown remains the highest-value scheduled item in the repo**; (iii) Gate/Coinbase/Bybit/Crypto.com/Gemini/Sui own-channel sweeps unrun; (iv) OKX denominator floor stands at ≥34 surfaces.
- **(d) Agency panel staleness — 52 days.** Stable-by-decision; §6 wording must change. **6th run.**
- **(e′) Cadence — RECOVERING.** 08-05 and 08-06 both ran. Last gap 08-04.
- **(f) Friday nomination cadence** — next check **08-07, tomorrow**. No `inbound-nominations.md` exists; none have ever arrived.
- **(g) Coinbase n=1** — void as filed; re-file only after backfill.
- **(h′) Layoff rationale correlates with firm type** — **REJECTED, and its successor hypothesis rejected with it.** See the table in class 5. **Do not print either.**
- **(i) Kraken paid-media build-out** — the two Director, Paid Marketing reqs are now **15 days open**. Time-to-fill is accruing and unwritten.
- **(j) Senior-leader exits** — superseded by (aa).
- **(k) Chrome-lane instrumentation gap** — unchanged.
- **(l) §4 inventory too narrow AND provenance-blind** — **7th costing, and the argument is now four-for-four:** Mulvenny (08-03), Coinbase spokesperson (08-05), Pontoizeau and Li (08-06) — the four most useful sentences found in four days, all structurally ineligible. Class 4: 1 item in 11 days.
- **(m) Ad-platform gating** — **strengthened without new capture.** The Google Ads France change (07-01) and today's counterfeit-licence scam pattern are the same phenomenon seen from two sides: authorisation as marketing credential.
- **(n) Full-range re-sweep of classes 3, 4 and 5** — **FOUR-FOR-FOUR.** Measured defect, not suspicion. **The single highest-value unbuilt instrument in the repo, with Phase 2 days away.**
- **(o) Date the document, never an event held about it** — held.
- **(p) Absence claims tested against firms' OWN channels** — not advanced today. **Still unswept: Coinbase, Gate, Bybit, Crypto.com, Gemini, Sui, all of Strata 2 and 4.**
- **(q) Agency matrix measures the crypto-native segment** — unchanged.
- **(r) Absence panel needs a two-directional "structural withdrawal" category** — unchanged.
- **(s) Robinhood row misclassified** — unchanged, **7th run**.
- **(t′) Class 1 is a FLOW register presented as a STOCK register** — unchanged.
- **(u) Brand absorption defeats name-keyed sweeps** — unchanged; alias table still unbuilt.
- **(v) NCA sweep** — 6 of 6, COMPLETE. **Today adds a seventh datum of a different kind**: not another sweep, but a supervisor explaining the result of the previous six.
- **(w) Class-3 sweep vocabulary AND method** — **REOPENED FOR ESMA.** Direct-index fetch was 3-for-3 and has now failed once, silently, with two counterexamples. **CONSOB and AFM index reads are unaffected and stand.** Remaining: ESMA via a non-index route, MAS enforcement, VARA.
- **(x) `fetch_errors` null** — closed.
- **(y) Pre-2026 class-1 rows are arithmetic inferences** — unchanged.
- **(z) Promotional surfaces decoupled from operational state** — **panel-wide test unrun, 4th run.** The generalised version of the corpus's best finding, and it keeps not getting run.
- **(aa) Announcement vs effective dates** — **NOT IMPLEMENTED, 4th run, scope grew again.** Now four date fields **plus** `capture_ai_disclosure`.
- **(bb) Class-1 feed-health guard** — **CLOSED. Implemented and passing.** The one watch item this run retires.
- **(cc) NEW — the corpus's secondary layer is going machine-written, unevenly and without consistent disclosure.** Two capture sources disclosed model assistance this run; a third outlet disclosed it on one article and not on two others. **Needs a schema field before Phase 2, not a footnote after it.**

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2; **guard implemented, re-run, FEED HEALTH HEALTHY 14.4h**; 0 new postings, 18 agency files, 8 matrix rows.
2. Direct read of `prospects/open-positions.json` `scan_metadata` **and all 28 filtered roles** → feed recovered (2,087→2,090 fetched, 27→28 after filter); the +1 is non-cohort; Kraken ×2 at 15 days open, Gemini Predictions at 8.
3. Repo dedup baseline reads — 08-05 run record, tracker (18 rows), regulator/operator/campaign indexes, findings head+tail, greps for `messari`, `pip labs`, `esma.europa.eu`, `common-supervisory-action-casps`.
4. WebSearch — MAS DPT service provider advertising/marketing restrictions 2026 → surfaced PS-G02 landing page + PDF.
5. `web_fetch https://www.mas.gov.sg/regulation/guidelines/ps-g02-…` → HTTP 200 but **empty body**; recorded, not claimed.
6. **`web_fetch` MAS PS-G02 PDF** → **read verbatim. First MAS primary in the corpus.** §1.3, §2.1, §2.2, §2.3, §3.1, §4.2 + fn.4 extracted.
7. WebSearch — ESMA news index July 2026 crypto/MiCA marketing → surfaced the index URL into provenance.
8. **`web_fetch https://www.esma.europa.eu/press-news/esma-news`** → HTTP 200. Ten items **03/08 → 10/07**, zero crypto. **Index unmoved in 3 days.** Exposed the `?page=1` Load-More URL.
9. **`web_fetch https://www.esma.europa.eu/press-news/esma-news?page=1`** → HTTP 200. Ten items **02/06 → 07/05**. **37-day hole; two known ESMA items inside it. Watch (w) reopened.**
10. WebSearch — crypto exchange CMO / VP Marketing August 2026 → **0 qualifying class-4 items.**
11. WebSearch — crypto layoffs August 2026 marketing → FalconX only (already row 18); surfaced Messari.
12. WebSearch — Messari layoffs 2026 → surfaced The Block primary + the AI-assisted secondary.
13. **`web_fetch https://www.theblock.co/post/393979/…the-daily-messari…`** → HTTP 200. Block Inc. "last month" dating; **carries an AI-assistance disclosure**; **surfaced the 08-06 EU-watchdogs item in its live sidebar.**
14. **`web_fetch https://www.theblock.co/post/410966/eu-watchdogs-warn-crypto-scams-mica`** → HTTP 200. **The run's principal result.** Pontoizeau named + quoted; AMF forbearance; AFM warning; ESMA logo abuse; ~320 vs >1,700.
15. **`web_fetch https://www.theblock.co/post/393840/messari-ceo-steps-down-layoffs`** → HTTP 200. **Tracker row 19** + the Block Inc. correction.
16. **Not reached / not guessed:** FT originals (both, paywalled) · `theblock.co/post/391520` (Block Inc. primary) · Li + Turner X posts · ESMA pages 3+ and `sort_by=chronological` · MAS enforcement register · **PSN08 Notice** · MAS DTSP licensing guidelines · **VARA** · CONSOB comunicato PDFs · Gnosis X post + forum primaries · the ~27 unfetched OKX locale surfaces. **All recorded as open. No URL was fabricated.**

---

## Net-new / changed this run

- `corpus/regulator-filings/eu-nca-post-deadline-scam-warnings-and-amf-forbearance-2026-08-06.md` — **NEW.** AMF/AFM/ESMA on the record, day 36; **Pontoizeau named + quoted; the AMF's deliberate non-deadline and its stated reason**; ESMA logo abuse; the licence-as-counterfeited-marketing-claim reading; ~320-vs-324-vs-1,700 register arithmetic `[VERIFY]`; near-primary provenance stated.
- `corpus/regulator-filings/mas-ps-g02-dpt-public-promotion-guidelines.md` — **NEW.** First MAS primary; §§1.3/2.1/2.2/2.3/3.1/4.2 verbatim; **"MiCA adjudicates content, MAS forecloses reach"**; OKX `/en-sg/` cross-reference with the verdict explicitly refused and three reasons why; enforcement register declared unswept.
- `corpus/layoff-tracker/2026-layoff-tracker.csv` — **18 → 19 rows.** Messari [PERIMETER] 2026-03-16 added (AI-framed, figures undisclosed, watch (n) 4th strike); **Block, Inc. row corrected** — date Q2 → 2026-02, `ai_cover` N → Y, percentage + source added.
- `scripts/daily-corpus-sync.py` — **watch (bb) CLOSED.** FEED HEALTH verdict, age, fingerprint, and an explicit class-1 absence-claim refusal in the stale case.
- `scripts/README.md` — guard documented.
- `findings/longitudinal-2026-06.md` — seven-point day-36 shift appended.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` — date re-stamps (sync).
- `corpus/agency-claims/*.csv` (18), `corpus/agency-overlap-matrix.csv` — dated snapshots (sync).
- **Operator statements: unchanged at 5 files. Job postings: 0 net-new (genuine absence, guard-asserted).**

---

## Recommendation for next run

1. **Reach ESMA by a route that is not the news index.** Today proved the index drops items it holds. Try `?sort_by=chronological`, the MiCA activities page, and the ESMA library with a date filter — **and validate any new route against the two known items (23 Jun, 8 Jul) before trusting a null from it.** That validation step is the actual lesson of this run and should become standing practice: **an instrument may not produce an absence claim until it has been shown to detect a known presence.**
2. **08-09 time-to-teardown measurement.** Pre-committed, three days out. Design it to measure teardown *rate* against the ≥34-surface denominator, not teardown *fact*.
3. **Fetch PSN08.** PS-G02 §2.2's carve-out is measured against it, and without it the MAS record is an instrument with no yardstick. Cheapest high-value class-3 item on the board.
4. **Test watch (z) across the panel** — carried a **fourth** run. It is the generalised form of the corpus's best finding and it keeps not getting run. **Either run it next or kill it explicitly.**
5. **Implement the schema (watch aa + cc):** four date fields on personnel records, plus `capture_ai_disclosure` on every non-primary capture. Scope has grown three runs running; it is cheap now and a retraction after synthesis.
6. **Escalate to Jukka — five items, in order:**
   - **(i) Commission the full-range re-sweep (watch n) — NOW. Four-for-four.** OP Labs, Kraken, Coinbase→OpenAI, Messari: four in-window events at well-covered firms, all found late and by accident, the latest while reading a competitor's newsletter for something else. **The corpus does not know what else is sitting in the public record from Dec 2024 onward, and Phase 2 starts within days.** This was recommendation (v) on 08-05 and it is now first.
   - **(ii) `methodology.md` §1 must be re-scoped. SIXTH run, unaddressed.** Class 1 cannot evidence *"rolling 12 months"*: it is a flow register of a handful of rows in a 28-day window whose deepest entries are arithmetic inferences. **The guard now at least makes its silences honest — but an honest silence is not twelve months of data.** Still the one thing in this repo that could embarrass the report.
   - **(iii) `methodology.md` §4 needs two changes** — widen the inventory *and* add an earned-vs-placed provenance field. **The empirical case is now four-for-four across four consecutive runs.** §4 is selecting for job title, not for evidentiary value. Class 4: 1 item in 11 days.
   - **(iv) The four upstream company-list gaps — OKX (Tier-1), Securitize, Rabby, Relai — unfixed, SIXTH run.** OKX remains invisible to the class-1 instrument while supplying the corpus's best campaign primaries. **Needs an owner outside the corpus run.**
   - **(v) §6's "daily 18-agency panel" is inaccurate at 52 days stale.** Re-word or re-feed. Sixth run.

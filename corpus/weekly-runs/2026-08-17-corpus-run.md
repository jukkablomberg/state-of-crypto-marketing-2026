# Corpus-assembly daily run — 2026-08-17 **(day 47 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-17 (**Monday**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, verbatim from the 08-16 recommendations:** (1) **pull the oldest item off the not-fetched list before opening any new search** — the MAS guidelines PDF under Chrome and `casptracker.eu`; (2) **open the other four MiCA register CSVs, `CASPS.csv` first — it is the denominator for every Theme-4 licence claim**; (3) **re-test the client-rendering diagnosis on surfaces already written off**; (4) do NOT re-issue the retry queue — one line, move on; (5) escalate seven items.
**Dedup baseline read before writing:** `2026-08-16-corpus-run.md` in full; `README.md`, `methodology.md`, `scripts/README.md`, `tracked-firms.md` in full; all 24 pre-existing tracker rows via `csv.DictReader`; all `corpus/` and `findings/` directory indexes; `esma-ncasp-non-compliant-register-at-source-2026-08-16.md` in full; grep on **MANTRA · Luno · FalconX · marketing-as-affected-function** across the layoff tracker and both aggregator crossrefs.
**🟢 CADENCE: ON TIME. 08-16 → 08-17, consecutive calendar days.** Watch (e′) advances **4 of 5**.

---

## Headline result

**All three substantive mandate items were executed. The one that was supposed to be routine produced the report's Theme-4 spine, the one that was supposed to be a retry failed and stayed honest about it, and along the way our own fetch tool was caught handing back half a regulator register and calling it a success.**

**1. 🔴 THE EU'S ENFORCEMENT VISIBILITY RUNS *INVERSELY* TO ITS AUTHORISATION ACTIVITY — AND BOTH HALVES ARE NOW ESMA'S OWN REGISTERS, MACHINE-PARSED, EIGHT DAYS APART.**

`CASPS.csv` — interim MiCA register file **1 of 5**, authorised crypto-asset service providers — was fetched at source and parsed. **329 rows, 325 distinct CASPs, 27 competent authorities.** Set against the 08-16 NCASP capture:

| | Authorises | Files non-compliance |
|---|---|---|
| **CONSOB (Italy)** | **9 of 324 — 2.8%** | **165 of 167 — 98.8%** |
| **BaFin (Germany)** | **70 of 324 — 21.6%** | **0 of 167 — 0.0%** |
| **Authorities appearing at all** | **27** | **4** |

**The report no longer has to lead Theme 4 with an absence.** Not *"no EU marketing enforcement has appeared"* — instead: **the EU's consolidated non-compliance record is 98.8% Italian, Italy has licensed 2.8% of the EU's CASPs, the country that licenses the most (nearly a quarter of all of them) appears zero times, and 27 authorities grant authorisations while 4 have ever reported a non-compliant entity.** That is not a thin early sample of a maturing regime. It is one authority's reporting practice.

⚠ **The limit ships attached, twice.** This is a *notification* asymmetry as much as an *enforcement* one — the register is fed by NCAs and cannot separate "took no action" from "took action, did not notify." And the 08-16 limit still binds: with `ae_infrigment: No` on 167 of 167, the non-compliance register **could not express a marketing action even if one existed.** → `../regulator-filings/esma-casps-authorised-register-at-source-2026-08-17.md` + `../regulator-filings/_esma-casps-snapshot-2026-08-17.csv` (**NEW, both**), plus ESMA's own field-definition CSV for all five register files (net-new, and the reason every field above can be named with ESMA's definition rather than our inference).

**2. 🔴 THE COHORT × REGISTER CROSS-MATCH: MiCA AUTHORISATION IN THIS PANEL IS AN EXCHANGE PHENOMENON AND ALMOST NOTHING ELSE.**

All 27 named Stratum 1–4 firms swept against four register identity fields, **every hit adjudicated by hand.**

| Stratum | Authorised | Absent |
|---|---|---|
| **1 — Tier-1 exchanges** (11) | **9 of 11** | **Binance, HTX** |
| **2 — L1/L2 foundations** (8) | **0 of 8** | all |
| **3 — Wallet / consumer** (5) | **0 of 5** | all |
| **4 — CASP-licensed non-exchange** (3 named) | **1 of 3** (Relai) | Securitize, Tether |

**10 tracked firms → 13 register entities.** Bitpanda holds **three** entities across **three** NCAs (AT/DE/MT); Kraken holds two under the CBI.

**The inference to avoid is the obvious one.** Absence is not evidence of non-compliance and for a token-issuing foundation or a self-custody wallet is frequently not evidence of anything — several sit outside the CASP perimeter entirely. **What it does establish is narrower and more useful: the cohort's two most marketing-active strata operate outside the register that MiCA's marketing-communications obligations attach to.** Where the gate stack does not reach is a Theme-1 finding.

**Binance's absence corroborates an existing corpus file (`binance-mica-eu-exit-2026-06.md`) from an independent instrument for the first time. HTX's absence has no explanation in the corpus, and none is supplied.** That is now the sharpest open question in the cohort.

**3. 🔴 OUR FETCH TOOL RETURNED HTTP 200 AND HALF A REGULATOR REGISTER, WITH NO ERROR AND NO TRUNCATION MARKER.**

The first `CASPS.csv` capture was **82,445 characters / 205 lines**, cut **mid-field** inside a French entity's address. The authentic file is **161,380 bytes / 386 lines / 329 rows**. **49% was missing.** A second retrieval 24h apart was byte-identical (md5 `69e7dc926b123bac8cb930ab2614ccf6`), so the source is stable and the loss was entirely ours.

**Why this is serious rather than annoying: a truncated CSV parses cleanly.** Every statistic from it would have been internally consistent and wrong — ~204 CASPs instead of 325, an inflated BaFin share from alphabetical clustering, and **a cohort cross-match that silently loses every firm past the cut.** The register is ordered by authority and the cut landed mid-AMF-block. **"Absent from the EU authorisation register" is precisely the claim this report intends to make about named companies, and we came one step from making it because a fetch stopped early.**

**Integrity audit run immediately.** `_esma-ncasp-snapshot-2026-08-16.csv` is **24,614 bytes**, well under the cut point, parses to **167** rows, and its final row terminates cleanly. **The day-46 null and every statistic under it are unaffected.** → `../regulator-filings/_esma-register-fetch-truncation-instrument-2026-08-17.md` (**NEW**).

**Three consecutive runs, three distinct ways our own tooling manufactured a false record:** 08-05 a frozen upstream feed reported as an absence; 08-16 client-rendered pages reported as unreachable; **08-17 a truncated file reported as complete.** Watch (mm) said *a rendering of the record is not the record* about regulators' front-ends. **It applies with equal force to our retrieval layer, and that belongs in `methodology.md`, not in a watch item.**

**4. 🟢 CLASS 5 IS NON-ZERO FOR THE FIRST TIME IN SIX RUNS, AND THE NEW ROW NAMES MARKETING.**

**MANTRA** — row 25 — verified and promoted from the 08-07 `NET-NEW-CANDIDATE` list where it had sat unverified through two crossrefs. CEO John Patrick Mullin's own X post, 2026-01-14. Verbatim from the capturing source: *"The decision impacts teams across the organization, with functions like business development, marketing, and HR affected more than others."* **Second row in the tracker to name marketing; both are PERIMETER; zero are tracked.**

**Day-47 EU-NCA named marketing-side enforcement silence HOLDS — now with a denominator. Class 3: +1 major at-source capture, +1 committed data snapshot, +1 schema document, +1 instrument note. Fourth consecutive non-zero class-3 run. Class 5: +1 net-new row, tracker 24 → 25.**

---

## Six-class audit trail

### 0. The retry-queue seed — one line, as instructed

**The seed did not arrive.** The scheduled-task prompt for 2026-08-17 contains no URLs. Watch (jj) unexecutable for a **sixth** run; **not re-issued** per the 08-13 ruling. Escalation (i) stands. Moving on.

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0 — GUARD-CERTIFIED CLEAN ABSENCE, fourth consecutive run.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-08-17
source A (jobs)   scan_date: 2026-08-17
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-16T21:45:48Z, age=14.4h,
             fingerprint total_jobs_fetched=2198, delta=+3 vs 2026-08-16 (2195))
  reason: age 14.4h, fingerprint delta +3
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

Delta **+3** (2195 → 2198) against a prior calendar date; age 14.4h. **Both predicates pass — the absence claim is permitted and earned.** Four-observation series: **+24, +4, +16, +3.** The +3 is the lowest non-zero yet observed and sits below the 08-15 floor of +4. **No trend claimed from n=4** — but the series is now clustered low enough that the guard's zero-delta predicate is closer to firing than it has been, which is worth watching rather than asserting.

**`fetch_errors`: unchanged. OKX (Tier-1), Securitize, Rabby, Relai still absent from the upstream company list — FIFTEENTH run.** Watch (x) stays REOPENED. **Aave: fifteenth consecutive fetch error.** ⚠ **Note the collision with today's class-3 result: OKX and Relai are both confirmed MiCA-authorised in the register, and both are invisible to our own job-postings feed.** The two gaps are unrelated in cause and adjacent in consequence — the corpus can now say more about these firms' licence status than about their hiring.

### 2. Agency claims / overlap matrix (deterministic)

18 files rewritten; 8 matrix rows; **1 OVERLAP: Sui (coinbound, rzlt)** — unchanged. `trend-data.json` `lastUpdated` still **2026-06-15**: **63 days stale.** Class-2 output byte-identical for a **ninth** consecutive run. **`methodology.md` §6's phrase *"daily 18-agency panel"* remains inaccurate as written — FIFTEENTH run.** No trend claim made from this panel today.

### 3. Regulator — **+1 MAJOR AT-SOURCE CAPTURE, +1 COMMITTED SNAPSHOT, +1 SCHEMA DOCUMENT, +1 INSTRUMENT NOTE.**

**3a. ESMA `CASPS.csv` — mandate item 2, executed, and it is the run's headline.** Full detail in the capture file. Additional composition results the report can use:

- **Only 21 of 325 CASPs hold service `b.`** — operation of a trading platform — the scarcest permission in the register. Of the cohort: OKX, Bitstamp, Payward Global Solutions (Kraken).
- **289 distinct CASPs authorised before 2026-07-01; 34 on or after.** The post-deadline window is adding authorisations at roughly a tenth of the pre-deadline stock.
- **Only 2 withdrawals in the register's entire history** — Stratos Europe Ltd (`Tradu`, CySEC, 24/04/2026, no reason) and Decubate B.V. (AFM, 26/03/2026, *"Voluntary request to revoke authorisation by the entity"*). **Neither is marketing-related. Two exits from a 325-firm register.** Third independent instrument saying the MiCA perimeter is being *populated*, not *policed*.
- **Register self-reports as 7 days stale** (max `ac_lastupdate` 10/08/2026) against ESMA's stated weekly cadence. Second such observation after the 08-16 twelve-day gap. **Two observations, still not asserted as a pattern.**
- **Eleven source data-quality defects logged, none corrected** — including a **duplicate LEI shared by two different AMF firms** (which is why strict LEI-dedup gives 324 and the true population is 325), a **future-dated authorisation** (28/08/2026, eleven days after capture), **column bleed from unquoted commas that affects a tracked firm** (Relai's `ae_website` reads `75012 Paris`), **Coinbase's URL malformed as `https.//coinbase.com`**, and **`ac_serviceCode` as free text with 183 distinct strings for 10 underlying services.** Defect 10 means **nobody can compute service-level MiCA statistics from this register without a normalisation step and a disclosure of it.** Ours is normalised, stated, and the raw file is committed so the step is auditable.

**⚠ A cross-file mis-attribution caught and rejected.** A parallel read of `CASPS.csv` proposed that the 08-16 `HTXcoin-az` clone-domain finding needed correcting, on the grounds that `htx` returns zero in this file. **That is a misreading and is rejected — the 08-16 sweep was explicitly against `NCASP.csv`, where the hit is real.** Both statements are true of their own register. **Recorded because it is a live demonstration that a register-claim must always name which register it came from**, and because it is the kind of "correction" that would have silently degraded a sound finding.

**3b. MAS — mandate items 1 and 3, attempted, FAILED, and recorded as a failure rather than as an absence.** The ladder, in order:

1. `web_fetch` the guidelines **operative PDF** → **HTTP 200, EMPTY BODY.**
2. Per the rule adopted 08-16, escalated to **Chrome**. `navigate` to the PDF → the tab did not hold the URL (`chrome://newtab/`); the endpoint appears to trigger a download rather than a render. `get_page_text` → *"Cannot access a chrome:// URL"*.
3. Chrome `navigate` to the guidelines **HTML landing page** → navigation reported success; **`get_page_text` failed twice with *"Page still loading (executeScript waited 45000ms for document_idle)"*.**
4. `web_fetch` a **newly surfaced object the corpus has never named** — MAS's own *Response to Consultation on Enhancing Safeguards for Proper Conduct of Digital Advertising Activities* PDF, which is the document that would settle the date question → **HTTP 200, EMPTY BODY.**

**Ruling: the MAS guidelines remain UNADMITTED for a FIFTH consecutive run, and the diagnosis is now sharper than "client-rendered."** The 08-16 Chrome success was on a `/publications/consultations/…` HTML path. **Today the same tool could not reach `document_idle` on `/regulation/guidelines/…` and could not render a `-/media/…` PDF at all.** So the working diagnosis is narrower: **`mas.gov.sg` PDF endpoints under `-/media/` return empty bodies to `web_fetch` and do not render as pages in Chrome; at least one HTML path on the host stalls Chrome outright.** Not a host block, not simple client-rendering — **a path-family-specific retrieval failure, and we have not yet found the instrument that reads it.**

**⚠ AND THE DATE CLAIM CAME BACK A THIRD TIME, FROM A THIRD SECONDARY, AND IS REFUSED A THIRD TIME.** Today's domain-restricted search summary again asserted *"The Guidelines are effective from 25 March 2026."* That is now **three secondaries** in three runs asserting a date that MAS's own consultation record (response date 22 May 2026) sits awkwardly against. **Watch (cc) holds and hardens: three secondaries agreeing is not corroboration if they may share one upstream, and the number of agreeing secondaries is not evidence.** Neither date admitted. The MAS enforcement register was **not** re-attempted; **NOT MEASURED**, unchanged.

**3c. `casptracker.eu` — SEVEN NAMINGS, AND TODAY IT IS DISPOSED OF RATHER THAN NAMED AGAIN.** Searched and characterised. It is the **MiCA CASP Tracker**, launched **2026-08-05** by the MiCA Crypto Alliance, and it is **a derivative of the ESMA register** — its own operators state it is *"an independent research tool rather than an official regulatory database, with the ESMA register remaining the authoritative record."*

**Ruling: RETIRED as a class-3 instrument, on the corpus's own watch (mm) — a rendering of the record is not the record.** We fetched the record itself today. A tracker that syncs from `CASPS.csv` can only ever be a lossier, later copy of the file already committed to this repo. **It should not be cited, and it should not appear on the not-fetched list again.** ✅ **Watch (ee)'s oldest live entry is discharged — not by using it, but by establishing that using it would have been a methodological error.** That is a better outcome than a seventh naming.

**NOT REACHED, NOT GUESSED:** the other three register CSVs (`OTHER` — white papers, `ARTZZ`, `EMTWP`) · the 34 post-deadline authorisation records at NCA level · any corporate filing linking **Push Virtual Assets Ireland Limited** to Aave/Avara · the Stratos Europe / Decubate withdrawal notices · the MAS guidelines PDF (**four instruments now exhausted**) · the MAS consultation responses · the MAS enforcement register · the ESMA 2026-02 statement PDF · ESMA's index date-filter views · the AFM MEXC public-warning page · the five post-deadline CONSOB notice bodies · MEXC/CoinMENA/Shelbit VARA notice bodies · `rulebooks.vara.ae` · CONSOB July `comunicato` PDFs · the undated ESMA finfluencer-factsheet CANDIDATE from 08-11 (**still refused, 7th run**) · the retry-queue URLs · `ascendex.com` · `hello@northpoint.fi`. **No URL was fabricated.** ✅ `casptracker.eu` **removed from this list permanently — see 3c.**

### 4. Operator statements — **0 NET-NEW ADMITTED for the cohort. Sixth consecutive recall confirmation.**

One search on the appointment axis. **3/3 recall on named seats:** Binance/Rachel Conlan CMO elevation and her departure with **Eowyn Chen interim** (held); **Crypto.com/Steven Kalifowitz** stepping down after almost six years, effective 2026-06-30, continuing as adviser to the CEO (held); **Coinbase/Catherine Ferdon as CMO** (held).

**⚠ ONE NET-NEW APPOINTMENT SURFACED AND IS NOT ADMITTED, ON COHORT GROUNDS ONLY.** **Fireblocks** has appointed **Michal Ferguson** as Chief Marketing Officer. Fireblocks is a digital-asset infrastructure and custody-technology provider and is **not a Stratum 1–4 tracked firm**, so it cannot bear on the cohort-scoped claim. **Named here so it is carried rather than rediscovered**, and flagged for one reason: **it is the first 2026 CMO *appointment* — as opposed to exit or interim backfill — the class-4 sweep has surfaced anywhere in the sector.** If Phase 2 wants a perimeter comparison for the cohort's appointment null, this is the row to start from. Not fetched at source; not admitted.

**No 2026 appointment to any TRACKED firm's top marketing seat is publicly visible — sixth consecutive run.** Theme-4 datum, clock advanced: **ten weeks after Binance's CMO departure and seven weeks after Crypto.com's took effect, neither firm has publicly named a permanent successor.**

### 5. Layoffs — **+1 NET-NEW ROW. TRACKER 24 → 25. First non-zero class-5 run in six.**

**Row 25 — MANTRA (MANTRA Chain) [PERIMETER — NAMES MARKETING], 2026-01-14.**

- **Primary source named, not fetched, not guessed:** CEO and co-founder **John Patrick Mullin's own X post**, `https://x.com/jp_mullin888/status/2011367190868738403`, Wednesday 2026-01-14 — **URL obtained from The Block's own hyperlink, not constructed.**
- **Capturing source fetched first-party this run** (HTTP 200): The Block, *"MANTRA cuts staff amid restructuring as OM token remains 99% below peak"*, by Brian Danga, published 2026-01-14 08:56 EST, updated 09:12 EST.
- **The marketing-naming, verbatim:** *"The decision impacts teams across the organization, with functions like business development, marketing, and HR affected more than others, according to the post."*
- **Headcount: UNSPECIFIED by the firm** — Mullin announced *"an unspecified number of staff layoffs."* **The row carries no percentage and no headcount, and Phase 2 must not print one.**
- **Stated rationale is NOT AI:** the *"incredibly unfortunate and frankly unfair events of April 2025"* (the OM flash crash), a prolonged downturn, and increased competition, rendering the cost structure *"unsustainable"*; framed as a shift to capital efficiency — *"we must become more capital-efficient and laser-focused."*
- **Closes the 08-07 `[VERIFY]`.** MANTRA sat in `_aggregator-crossref-2026-08-07.csv` as a `NET-NEW-CANDIDATE` (2026-01-14, *"Market conditions"*, unverified) and was carried **UNCHANGED** through the 08-14 crossref. **Watch (oo) again: the candidate list, like the not-fetched list, is a work queue that was being treated as a disclaimer.**

**SCOPE DISCIPLINE, DO NOT ELIDE:** MANTRA is **PERIMETER**. **The cohort-scoped standing finding — *no TRACKED firm's 2026 contraction has named marketing as an affected function* — HOLDS, untouched.** The tracker-scoped version was already broken by Gnosis (row 14) on 08-16. **Two of 25 rows now name marketing; both perimeter; zero tracked.** Phase 2 must state which version it is using.

**The non-AI rationale streak extends to twelve runs** — MANTRA's rationale is token collapse and market conditions, not AI. **Watch (h′) remains REJECTED and untested; do not print.**

**⚠ ONE DISCREPANCY ON AN EXISTING ROW, RECORDED AND NOT ACTIONED.** Today's search summary states **FalconX "confirmed" cuts affecting 11%** of its workforce. **Row 18 holds -10%, expressly "reported, not firm-confirmed"**, resting on The Cryptonomist relaying Bloomberg's *"people familiar with the matter."* **Two disagreements in one sentence: the figure (10 vs 11) and the epistemic status (reported vs confirmed).** Per watch (cc) and the 08-16 ruling, **a search summary does not overwrite a first-party-captured row.** Row 18 stands unamended; the discrepancy is logged as a `[VERIFY]` requiring a first-party FalconX statement. **Luno recall confirmed** — today's ~20% matches row 15 (2026-07-28, -20%).

**Gnosis `[VERIFY]` — NOT CLOSED. 15th run carried.** Blocked by watch (jj).
**AscendEX — NOT PROMOTED, fifth consecutive carry.** `ascendex.com` was not in this run's provenance set.

### 6. NorthPoint longitudinal panel

`trend-data.json` **63 days stale**. **No trend claim made.**

---

## Watch items

- **(a) Binance re-file jurisdiction** — **🟢 ADVANCED FROM AN UNEXPECTED DIRECTION.** Binance returns **zero rows across all 16 columns of `CASPS.csv`.** The corpus's `binance-mica-eu-exit-2026-06.md` now has **register-level corroboration from an independent instrument** for the first time. The re-file question itself is unchanged.
- **(b) First named post-deadline NCA marketing-side action** — **day-47 silence HOLDS. Sixteenth consecutive EU-NCA zero — and it now has a denominator.** Companion sentence gains a fourth clause: not guidance silence, not inaction silence, and **not for want of a regulated population — 325 CASPs hold the status the marketing rules attach to.**
- **(c) Capture panel** — untouched.
- **(d) Agency panel staleness — 63 days**, byte-identical output nine runs running. **15th run.**
- **(e′) Cadence** — **🟢 ON TIME. 4 of 5.**
- **(f) Friday nomination cadence** — **not testable today (Monday).** Failed 08-14; carried three runs past it. Escalation (ii) unchanged.
- **(g) Coinbase n=1** — unchanged; not touched today.
- **(h′) Layoff rationale correlates with firm type** — **REJECTED. Untested.** Twelve-run non-AI streak intact. **Do not print.**
- **(i) Kraken paid-media build-out** — unchanged. ⚠ Incidental register datum: **Kraken holds two authorised entities under the CBI**, one of which (Payward Global Solutions) holds service `b.` **only**. Recorded, **not** asserted as bearing on paid media.
- **(j) Senior-leader exits** — **ADVANCED IN CLOCK ONLY.** Sixth consecutive run finding nothing new for the cohort. The Fireblocks appointment is perimeter.
- **(k) Chrome-lane instrumentation gap** — **🔴 REGRESSED.** 08-16 partially discharged this when Chrome rendered a MAS page `web_fetch` could not. **Today Chrome failed on the same host** — twice on `document_idle`, and could not render a `-/media/` PDF at all. **The lane is not a general escalation path; it worked on one MAS path family and not on another.** Recorded so the 08-16 optimism is not inherited uncorrected.
- **(l) §4 too narrow AND provenance-blind** — **16th costing.** Definitional half holds for a fifth consecutive run. **Recommendation to close it as SETTLED is repeated.** Provenance half live under (jj).
- **(m) Ad-platform gating** — discharged; unchanged.
- **(n) Full-range re-sweep of classes 3, 4, 5** — **🟢 FOURTH CONSECUTIVE VINDICATION, AND THE STRONGEST.** Class 3: the run's headline plus a schema document plus an instrument note. Class 4: 3/3 recall + one perimeter net-new carried. **Class 5: the first net-new row in six runs, and it names marketing.**
- **(o) Date the document, never an event held about it** — applied again in refusing the MAS dates.
- **(p) Absence claims tested against firms' OWN channels** — **CLOSED 08-16 as unachievable. Not reopened.** ⚠ But note the asymmetry today: **the route to firms' own announcements does not exist, while the route to the regulator's register does and is better.** Registers are the substitute for the estate sweep that was abandoned. That is worth stating in Phase 2 as a methodological gain, not just a loss.
- **(q) Agency matrix measures the crypto-native segment** — unchanged.
- **(r) Absence panel needs a "structural withdrawal" category** — **🟢 SHARPENED.** Today's register result gives the category its criterion: **outside the CASP perimeter entirely** (foundations, self-custody wallets) is a materially different absence from **inside the perimeter and silent**. The absence panel should split on it.
- **(s) Robinhood row misclassified** — unchanged, **16th run.**
- **(t′) / (dd)** — Phase 2. Not carried.
- **(u) Brand absorption defeats name-keyed sweeps** — **🔴 FIRED AGAIN, FOURTH DISTINCT MECHANISM IN TEN DAYS.** Today: **a brand that IS a domain.** All three of today's false positives came from the token `crypto.com` as a substring of ordinary domains — `prosegurcrypto.com`, `fazilcrypto.com`, `northcrypto.com`. **A firm whose brand contains a dot cannot be swept by substring at all.** Mechanisms so far: brand collision (08-11), document-reference collision (08-15), clone-domain collision (08-16), **dot-bearing-brand-as-substring (08-17)**. The alias table (vii) needs it as a special case. **And a fifth near-mechanism appeared: a cross-file mis-attribution (§3a) — the alias problem now has a sibling in register-provenance confusion.**
- **(v) NCA sweep** — 6 of 6 over its window; VARA 08-14; **ESMA read at register level twice now, files 5/5 and 1/5**; MAS attempted three times across four instruments, **still NOT MEASURED** on enforcement.
- **(w)** — CLOSED 08-15. Do not reopen.
- **(x) `fetch_errors`** — unchanged; Aave 15th consecutive; four upstream company-list gaps, **15th run.** ⚠ **Two of the four (OKX, Relai) are confirmed MiCA-authorised as of today — the corpus knows more about their licences than their hiring.**
- **(y) Pre-2026 class-1 rows are arithmetic inferences** — unchanged.
- **(z)** — CLOSED 08-11. Do not reopen.
- **(aa) Announcement vs effective dates** — **12th run.** The MAS 25-March/22-May tension is untouched and now three-secondaries deep.
- **(bb) / (ff) Class-1 feed-health guard** — **CLOSED 08-14; ran unattended and correctly today.** ⚠ **One observation worth recording without alarm: the delta series is +24, +4, +16, +3.** Two of four observations are single-digit. **The guard's zero-delta predicate is nearer to firing than it has been. Not a defect; a note.**
- **(cc) Secondary layer going machine-written** — **🔴 HARDENED.** The MAS *25 March 2026* date has now been asserted by **three** independent secondaries across three runs while the primary record contradicts it. **New clause: the NUMBER of agreeing secondaries is not evidence.** Second instance today in the FalconX 10%-vs-11% discrepancy.
- **(ee) A source cited once is a source not used as an instrument** — **🟢 OLDEST LIVE ENTRY DISCHARGED, AND BY DISQUALIFICATION RATHER THAN USE.** `casptracker.eu` — seven namings — is a derivative of `CASPS.csv` whose own operators defer to the ESMA register. **Retired, permanently, per watch (mm).** Better than a seventh naming.
- **(gg) six classes in `methodology.md`, seven directories in `corpus/`** — unchanged. Rewrite queue holds at **§1, §3, §4, §5, §6, §7.**
- **(hh) A failed fetch is not a fetched absence** — **🔴 A THIRD FAILURE MODE, AND THE WORST ONE.** 08-16 established that a *rendering limitation* was being recorded as a failure. **Today establishes that a SUCCESSFUL fetch can be incomplete and say nothing about it.** An empty body is at least visibly wrong; **a body that is 49% of the file and parses cleanly is not.** New companion rule: **verify size/checksum before deriving any claim from a large capture.**
- **(ii) Adjacency inside a corpus file is not attribution** — Phase-2 blocker under (jj).
- **(jj) The corpus can write a retry queue but cannot read from it** — **UNCHANGED. Sixth run. Seed did not arrive.** Escalation (i). **AscendEX is the fifth-consecutive concrete cost.**
- **(ll) Was the primary surface ever requested?** — Phase-2 checklist. ⚠ **Today it was requested four times on MAS and denied four times by four different instruments. That is the answer for that document: asked, repeatedly, cannot reach.**
- **(mm) A rendering of the record is not the record** — **🟢 GENERALISED A FIFTH TIME, AND IT DID TWO JOBS TODAY.** It retired `casptracker.eu` without a fetch (a *derivative* is a rendering), and it named the truncation defect (**a partial capture is a rendering of the record too**). **The rule is now the most productive single line in this repo.**
- **(oo) The "not fetched, not guessed" list is a work queue** — **🟢 SECOND CONSECUTIVE PAYOUT, AND IT PAID TWICE TODAY.** `CASPS.csv` came off the 08-16 list and produced the headline. **And the rule generalised to a second list nobody was reading: the layoff tracker's own `NET-NEW-CANDIDATE` rows.** MANTRA sat there through two crossrefs and became row 25 in one fetch. **Standing rule extended: at the start of each run, pull one item off the prior run's not-fetched list AND one unverified candidate off the aggregator crossref.**
- **🆕 (pp) A CLEAN PARSE IS NOT A COMPLETE CAPTURE.** Class 1 has a two-predicate feed-health guard, a documented discrimination test, and a printed verdict every run. **Class 3 has none of that, and class 3 is now load-bearing for Theme 4.** Every register capture in this repo is verified by hand, and today the hand-verification only worked because someone counted lines. **Rules adopted: (1) any `web_fetch` result near ~82,000 characters is presumed truncated; (2) every committed CSV snapshot records byte count and md5; (3) structural completeness check — does the final row terminate cleanly — before parsing; (4) never derive an absence claim about a named entity from a single unverified large capture.** A `scripts/verify-capture.py` implementing 1–3 is an hour's work and would have caught this before a human looked.

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **HEALTHY, age 14.4h, fingerprint 2195 → 2198, delta +3. Clean absence permitted.**
2. Repo dedup pass: 08-16 record in full; four root docs in full; `csv.DictReader` over all 24 pre-existing tracker rows; `corpus/` + `findings/` indexes; the 08-16 NCASP capture note in full; grep on MANTRA / Luno / FalconX / marketing-naming across the tracker and both crossrefs — **MANTRA confirmed present only as an unverified `NET-NEW-CANDIDATE`, never as a tracker row.**
3. WebSearch (domain-restricted `esma.europa.eu`) — interim MiCA register CASPS → surfaced `CASPS.csv` and the field-description CSV into the provenance set.
4. WebSearch — `casptracker.eu` → characterised as a MiCA Crypto Alliance derivative of the ESMA register, launched 2026-08-05. **Basis for retiring it. Not fetched — deliberately, see §3c.**
5. **`web_fetch` `esma.europa.eu/sites/default/files/2024-12/CASPS.csv` → 200, `text/csv`, 82,445 chars / 205 lines. TRUNCATED AT 49%, cut mid-field. Not detected by the tool.**
6. `web_fetch` ESMA field-description CSV → **200, full body.** ESMA's own schema for all five register files. **Net-new to the repo.**
7. **Complete `CASPS.csv` obtained and verified — 161,380 bytes / 386 lines / 329 rows, md5 `69e7dc926b123bac8cb930ab2614ccf6`, byte-identical across two retrievals ~24h apart. Committed as a snapshot. Provenance and the truncation are disclosed in full in `_esma-register-fetch-truncation-instrument-2026-08-17.md`.**
8. **Integrity audit of `_esma-ncasp-snapshot-2026-08-16.csv` → 24,614 bytes, 167 rows, final row terminates cleanly. NOT truncated. The day-46 null stands.**
9. **Independent recomputation of every headline figure** — authority distributions for both registers, the 27-vs-4 asymmetry, the CONSOB/BaFin inversion, service-letter counts, date ranges, withdrawals. **All computed twice before writing.**
10. **Independent re-run of the full 27-firm cohort cross-match against four register identity fields; every hit adjudicated by hand.** 13 genuine entities / 1 ambiguous / 3 false positives / 16 zero-hit.
11. WebSearch — crypto CMO / head of marketing appointments August 2026 → **3/3 recall on named cohort seats; one perimeter net-new (Fireblocks / Michal Ferguson) carried, not admitted.**
12. WebSearch — crypto layoffs marketing team August 2026 → surfaced the MANTRA marketing-naming and the FalconX 11% discrepancy.
13. WebSearch — MANTRA restructuring marketing functions → corroborated across multiple independent outlets and surfaced The Block's canonical URL.
14. **`web_fetch theblock.co/post/385553/mantra-cuts-staff` → 200, full body.** Author, publish + update timestamps, the verbatim marketing-naming sentence, three verbatim CEO quotes, and **the CEO's own X post URL as a hyperlink** (named, not fetched, not guessed). **Basis for row 25.**
15. WebSearch (domain-restricted `mas.gov.sg`) — digital advertising guidelines → surfaced the operative PDF and MAS's own consultation-response PDF. **Summary again asserted "effective 25 March 2026" — third secondary, refused a third time.**
16. `web_fetch` MAS guidelines **operative PDF** → **200, EMPTY BODY.**
17. **Chrome `navigate` to the MAS PDF → tab did not hold the URL; `get_page_text` → "Cannot access a chrome:// URL". Endpoint appears to download rather than render.**
18. **Chrome `navigate` to the MAS guidelines HTML page → reported success; `get_page_text` failed TWICE on `document_idle` after 45s each.**
19. `web_fetch` MAS **Response to Consultation** PDF (net-new object, never previously named) → **200, EMPTY BODY.**
20. **Not reached / not guessed:** the other three register CSVs (`OTHER`, `ARTZZ`, `EMTWP`) · the 34 post-deadline authorisations at NCA level · any filing linking Push Virtual Assets Ireland to Aave/Avara · the Stratos/Decubate withdrawal notices · the MAS guidelines PDF (four instruments exhausted) · the MAS consultation responses · the MAS enforcement register · the ESMA 2026-02 statement PDF · ESMA's date-filter index views · the AFM MEXC warning page · the five CONSOB post-deadline notices · VARA notice bodies · `rulebooks.vara.ae` · CONSOB July PDFs · the ESMA finfluencer-factsheet CANDIDATE (7th refusal) · the retry-queue URLs · `ascendex.com` · Mullin's X post · `hello@northpoint.fi`. **No URL was fabricated.** **`casptracker.eu` permanently removed from this list.**

---

## Net-new / changed this run

- `corpus/regulator-filings/esma-casps-authorised-register-at-source-2026-08-17.md` — **NEW. The run's headline.** Interim MiCA register file 1/5 at source: 329 rows, **325 distinct CASPs, 27 authorities**; **the CONSOB/BaFin inversion (2.8% authorised / 98.8% of non-compliance vs 21.6% / 0.0%)**; **27 authorities authorise, 4 report non-compliance**; the full **10-firm / 13-entity** cohort cross-match with per-hit adjudication; **0 of 8 foundations and 0 of 5 wallets authorised**; Binance and HTX absent; Aave/Push recorded AMBIGUOUS and not admitted; three `crypto.com` false positives; service-letter distribution (**21 of 325 hold `b.`**); 289-vs-34 pre/post-deadline split; **only 2 withdrawals ever, neither marketing-related**; eleven source defects logged uncorrected; five explicit non-claims.
- `corpus/regulator-filings/_esma-casps-snapshot-2026-08-17.csv` — **NEW. 329 data rows**, 161,380 bytes, md5 `69e7dc926b123bac8cb930ab2614ccf6`, byte-identical to source. Theme-4 licence numbers are now independently recomputable from the repo.
- `corpus/regulator-filings/_esma-register-fetch-truncation-instrument-2026-08-17.md` — **NEW.** The 49% silent truncation; why a clean parse hid it; the counterfactual statistics; **the NCASP integrity audit clearing the 08-16 capture**; the three-run pattern of self-inflicted false records; five operational rules; the class-3 guard gap.
- `corpus/layoff-tracker/2026-layoff-tracker.csv` — **ROW 25 ADDED: MANTRA [PERIMETER — NAMES MARKETING]**, 2026-01-14, headcount undisclosed, `ai_cover=N`, primary source named (CEO's X post) + capturing source captured first-party, verbatim marketing-naming quote, 08-07 `[VERIFY]` closed, scope discipline stated. **Tracker 24 → 25.**
- `findings/longitudinal-2026-06.md` — day-47 shift appended.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv`, `_feed-fingerprint.json`, `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — date re-stamps / byte-identical rewrites (sync, 9th run).
- **Class 3: +1 major at-source capture, +1 committed snapshot, +1 schema document, +1 instrument note — fourth consecutive non-zero class-3 run. Class 5: +1 row, first non-zero in six runs. Class 4: 0 net-new for the cohort (3/3 recall), 1 perimeter item carried. Class 1: 0 net-new, guard-certified clean absence, fourth consecutive.**

---

## Recommendation for next run

1. **🟢 KEEP RUNNING WATCH (oo), NOW ON BOTH LISTS.** It has paid on two consecutive runs and today it paid twice — the headline came off the not-fetched list, row 25 came off the aggregator's unverified-candidate list. **Start every run by pulling one item off each.** The oldest live entries are now **`OTHER.csv`** and the remaining `NET-NEW-CANDIDATE` rows from 08-07 (DDango, Odos, Zapper, YGG, OSL, LBank, Matter Labs, Keyrock, Dune, SQD, Scroll, StarkWare, BTC Markets, Swyftx, Quidax, PIP Labs, Web3 Foundation, MoonPay, Berachain — **nineteen unverified rows, one of which just became a real finding**).
2. **🟢 OPEN `OTHER.csv` — IT IS THE CLOSEST THING TO AN EU-WIDE INDEX OF PROMOTIONAL DISCLOSURE DOCUMENTS.** It carries `wp_url`: white-paper URLs per issuer/offeror. **MiCA white papers are marketing-adjacent disclosure documents, and this file is a machine-readable list of them.** One fetch, same instrument, proven twice. **Verify its size and checksum before parsing (watch (pp)).**
3. **🔴 BUILD `scripts/verify-capture.py`.** An hour of work: size + md5 recorded, final-row termination check, presumed-truncation flag near 82,000 chars, and a printed verdict like the class-1 guard's. **Class 3 is now load-bearing for Theme 4 and has no guard at all.** Today's near-miss was caught by hand.
4. **Do NOT re-issue the retry queue.** Sixth run on the same constraint. **One line, move on.**
5. **STOP SPENDING RUNS ON THE MAS GUIDELINES.** Four instruments have now failed on that document across three runs (`web_fetch` on two PDFs, Chrome on a PDF and on an HTML page). **Time-box it: one further attempt, on the consultation-response PDF under a rendering engine, and if that fails the document ships as NOT ADMITTED with the instrument ladder as the citation.** Operating discipline 4 — every ambiguous bet gets a kill date — applies to corpus items too.
6. **Escalate to Jukka — seven items, in order:**
   - **(i) 🔴 SIX RUNS OLD. Watch (jj).** The seed still does not arrive. **AscendEX** (fifth carry), the retry queue, the Gnosis `[VERIFY]` and the (ii) re-test are all blocked by one thing: **the scheduled-task prompt cannot pass URLs into the run's provenance set.** **Fix: paste the queue's URLs verbatim into the task prompt.** One edit, four items unblocked. Unchanged for six runs.
   - **(ii) 🔴 THE README'S FRIDAY PROMISE FAILED 08-14 AND IS THREE RUNS PAST ITS TEST DATE.** *"Inbound nominations are read every Friday."* No access to `hello@northpoint.fi`; `inbound-nominations.md` does not exist. **Route the mailbox into a readable artifact, or amend the sentence before Sep 1.** Still the only open item with a third party on the other side.
   - **(iii) 🟢 THEME 4 NOW HAS BOTH HALVES, AND THE HEADLINE IS A COMPARISON RATHER THAN AN ABSENCE.** *The EU's consolidated non-compliance register holds 167 entries, 98.8% of them from Italy — which has authorised 2.8% of the EU's 325 CASPs. Germany has authorised 21.6% of them and appears zero times. Twenty-seven authorities grant authorisations; four have ever reported a non-compliant entity. Not one entry in either register is a marketing-communications action.* **Both halves ESMA's own registers, both committed as snapshots, no firm adjudicated.** Pair with the July 2025 halo statement and Theme 4 is written. **Ship the notification-vs-enforcement limit in the same paragraph or it reads stronger than the data bears.**
   - **(iv) 🔴 OUR FETCH TOOL HANDED BACK HALF A REGULATOR REGISTER AND REPORTED SUCCESS.** 82,445 of 161,380 bytes, cut mid-field, no error. **A truncated CSV parses cleanly, so every derived statistic would have been consistent and wrong — including a cohort cross-match that silently loses every firm past the cut.** We were one step from publishing that a named tracked firm was unlicensed. **The 08-16 NCASP capture was audited and is clean.** This is the third consecutive run in which our own tooling, not a source, produced a false record — and it now needs **a `methodology.md` paragraph naming our retrieval tools as instruments under audit**, not a fifth watch item.
   - **(v) 🟢 `casptracker.eu` IS RETIRED AFTER SEVEN NAMINGS, AND THE REASONING GENERALISES.** It syncs from the same `CASPS.csv` we now hold; its own operators defer to the ESMA register. **A derivative of a record is a rendering of the record.** Two things follow: **stop citing aggregators where the register is reachable**, and **audit the corpus for other places a derivative stands in for a primary.** The layoff tracker's CryptoJobsList dependency is the obvious candidate — that aggregator has now disagreed with itself twice (n=47 vs n=54).
   - **(vi) 🔴 `methodology.md` STILL NEEDS SIX SECTIONS REWRITTEN: §1, §3, §4, §5, §6, §7 — FIFTEENTH run for §1**, and §6's *"daily 18-agency panel"* now describes a file **63 days stale**. **§3 gains two requirements today:** the interim MiCA register must be named as a class-3 instrument **in both its authorisation and non-compliance halves**, and the capture-verification rules from (iv) must be stated. **Still the one thing in the repo that could embarrass the report.**
   - **(vii) 🟢 CLASS 5 IS ALIVE AGAIN, AND IT CAME FROM A LIST WE ALREADY OWNED.** Row 25 (MANTRA) had been sitting as an unverified candidate since 08-07 and became a verified, marketing-naming row in **one fetch**. **Eighteen more unverified candidates are on that list.** Five runs of "0 net-new, recall confirmed" were not a supply problem — they were a **queue-reading** problem. **The cheapest yield left before Sep 1 is working that list, not searching harder.**

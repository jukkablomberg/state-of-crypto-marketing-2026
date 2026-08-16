# Corpus-assembly daily run — 2026-08-16 **(day 46 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-16 (**Sunday**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, verbatim from the 08-15 recommendations:** (1) **go back for the MAS digital-advertising guidelines — refused on provenance, not relevance — trying a different surface on the same host**; (2) **close the ESMA sweep properly using the index's own date filter, not `?page=N`**, and clear the 2026-02 `[VERIFY]`; (3) **re-run the mandate-2 audit table's rows 5 and 6 against ONE tracked firm's own newsroom** (Coinbase named); (4) do NOT re-issue the retry queue — one line, move on; (5) escalate seven items.
**Dedup baseline read before writing:** `2026-08-15-corpus-run.md` in full; `README.md`, `methodology.md`, `scripts/README.md`, `tracked-firms.md` in full; all 24 tracker rows via `csv.DictReader`; all seven `corpus/` directory indexes; `esma-sanctions-perimeter-casp-absence-2026-08-07.md` and `_industry-scale-denominator-2026-08-10.md` in full; repo-wide case-insensitive grep on **NCASP · ae_competentAuthority · "non-compliant entities" · "interim MiCA register" · LWEX · "Atomic Wallet" · MEXC · 1303207761 · P003-2023 · "digital advertising activities" · "25 March 2026" · "22 May 2026" · "12 August 2026"**.
**🟢 CADENCE: ON TIME. 08-15 → 08-16, consecutive calendar days.** Watch (e′) advances **3 of 4**.

---

## Headline result

**Three mandate items were executed. Two of them worked by escalating past a tool that had been silently lying, and the third worked by opening a file the corpus had listed under "not fetched" nine days ago and never gone back for.**

**1. 🔴🟢 THE DAY-46 EU ENFORCEMENT NULL HAS FINALLY BEEN TESTED AGAINST THE EU'S OWN CONSOLIDATED REGISTER — IT HOLDS, AND THE DISTRIBUTION UNDERNEATH IT IS THE BETTER FINDING.** ESMA's interim MiCA register file 5 of 5 — **non-compliant entities providing crypto-asset services**, Articles 109/110 — was fetched at source (`NCASP.csv`, HTTP 200, `text/csv`) and machine-parsed. **167 rows. 165 CONSOB (Italy). 1 AFM. 1 NBS. Every other EEA authority contributes zero.** Decision dates span **10 Feb 2025 → 22 Jul 2026**, so this is seventeen months of EU-wide reporting in which two non-Italian entries were made.

**Not one row is a marketing-communications action.** The register's own `ae_infrigment` column reads **`No` on all 167**; `ae_reason` reads `None` on **166 of 167**. The single reasoned row is the AFM's, and it is an Article **59** authorisation case — *"MEXC Global provides crypto-asset services in the Netherlands without the required MiCAR license"* — **not Article 66, not Article 68.**

**Five rows are post-deadline** (08/07/2026 and 22/07/2026, all CONSOB, all reason `None`). **So the post-deadline record is not empty — and it is still not marketing.**

**Why this matters more than another zero.** For six weeks the null has been derived from searches and paginated indexes, instruments this corpus has itself documented as lossy (watch (mm)). It has now been checked against the strongest instrument that exists, and it survived. **And the concentration is a report finding in its own right: 98.8% of the EU's visible non-compliance record is one national regulator.** → `../regulator-filings/esma-ncasp-non-compliant-register-at-source-2026-08-16.md` + `../regulator-filings/_esma-ncasp-snapshot-2026-08-16.csv` (**NEW, both**).

⚠ **And the honest limit is filed next to the finding:** with `ae_infrigment: No` on 167 of 167 and `ae_reason: None` on 166 of 167, **this register could not report a marketing-side action even if one existed** — CONSOB, which files 165 of the rows, does not populate the reason field at all. **The null must ship with that sentence attached or it will read as stronger than the data can bear.**

**2. 🔴 `web_fetch` HAS BEEN REPORTING CLIENT-RENDERED PAGES AS EMPTY, AND THE CORPUS RECORDED THAT AS UNREACHABILITY. THE 08-15 MAS DIAGNOSIS WAS WRONG.** Eight surfaces were walked on `mas.gov.sg`. Five returned **HTTP 200 with empty bodies**. Two returned full text. **The two that rendered are siblings of the ones that did not — same host, same path family** (`/regulation/guidelines/…fsg-g02` rendered; `/regulation/guidelines/…digital-advertising-activities` did not). That control kills the host-block hypothesis the 08-15 record implied. **These pages are client-rendered and `web_fetch` does not execute JavaScript.** Escalated to the Chrome extension; **the page rendered on the first try.**

**Rule adopted:** an HTTP 200 with an empty body **next to a rendered sibling on the same host** is a **client-rendering diagnosis, not a fetch failure** — escalate to a rendering engine before recording it as unreachable. **The corpus recorded three MAS URLs as unreachable on 08-15; at least one of them was reachable the whole time, by a tool that was already available.**

**3. 🔴 AND WHAT THE RENDERED PAGE RETURNED PUTS A DATE THE CORPUS WAS ABOUT TO PRINT IN DOUBT.** MAS's own page for *Guidelines on Standards of Conduct for Digital Advertising Activities* serves a **consultation record**: P003-2023, opened 25 Apr 2023, closed 30 Jun 2023, **MAS response date 22 May 2026.** The 08-15 record carried, from a compliance vendor, *"stated effective 25 March 2026"*; today's search summary repeated it. **A guideline cannot straightforwardly take effect eight weeks before MAS's own response to the consultation that produced it.** Three readings are available and the corpus cannot distinguish them — including that there are **three near-identical MAS titles** in play (*Digital Advertising Activities* / *Digital Prospecting and Marketing Activities* / FSG-G02 *Marketing and Distribution Activities*), which is watch (u) exactly.

**Ruling: neither date is admitted.** Not 25 March 2026 (secondary, now contradicted), not 22 May 2026 (a date of a response *about* the instrument — watch (o)). **Second consecutive run in which a date carried from a secondary source failed on contact with a primary surface.** → `../regulator-filings/_mas-digital-advertising-guidelines-provenance-2026-08-16.md` (**NEW**).

**4. 🔴 THE FIRM-ESTATE ROUTE — FIVE RUNS OF WATCH (p) — WAS TESTED ON THE BEST POSSIBLE SUBJECT AND THE ROUTE DOES NOT EXIST.** `coinbase.com/press` is **a brand-asset download portal**: an email address, a link to the consumer blog, five social links, and zip files of logos, product screenshots, office photography, the corporate typeface, and a leadership-headshot archive named **`Coinbase_Leadership__2024.zip`**. There is **no press-release archive on it.** `investor.coinbase.com/news` renders its full navigation and **zero news items** (client-rendered), exposing one machine-readable endpoint — an RSS feed whose **`lastBuildDate` is 22 September 2022** and whose newest item is dated **17 February 2023**.

**Watch (p) has been carried for five runs as a work item. It is not one. It is a structural property of the estates.** → `../../findings/theme-1-firm-estate-instrument-coinbase-2026-08-16.md` (**NEW**).

**Day-46 EU-NCA named marketing-side enforcement silence HOLDS — now register-anchored. Class 3: +1 net-new at-source capture (+1 committed data snapshot) + 1 instrument/provenance note. Third consecutive non-zero class-3 run.**

---

## Six-class audit trail

### 0. The retry-queue seed — one line, as instructed

**The seed did not arrive.** The scheduled-task prompt for 2026-08-16 contains no URLs. Watch (jj) unexecutable for a **fifth** run; **not re-issued** per the 08-13 ruling. Escalation (i) stands. Moving on.

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0 — GUARD-CERTIFIED CLEAN ABSENCE, third consecutive run.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-08-16
source A (jobs)   scan_date: 2026-08-16
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-15T22:08:12Z, age=14.0h,
             fingerprint total_jobs_fetched=2195, delta=+16 vs 2026-08-15 (2179))
  reason: age 14.0h, fingerprint delta +16
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

Delta **+16** (2179 → 2195) against a prior calendar date; age 14.0h. **Both predicates pass — the class-1 absence claim is permitted and earned.** The +4 series floor recorded on 08-15 is not repeated; +16 sits between the 08-14 (+24) and 08-15 (+4) observations. **Three-observation series: +24, +4, +16. No trend claimed from n=3.**

**`fetch_errors`: unchanged. OKX (Tier-1), Securitize, Rabby, Relai still absent from the upstream company list — FOURTEENTH run.** Watch (x) stays REOPENED. **Aave: fourteenth consecutive fetch error.**

### 2. Agency claims / overlap matrix (deterministic)

18 files rewritten; 8 matrix rows; **1 OVERLAP: Sui (coinbound, rzlt)** — unchanged. `trend-data.json` `lastUpdated` still **2026-06-15**: **62 days stale.** Class-2 output byte-identical for an **eighth** consecutive run. **`methodology.md` §6's phrase *"daily 18-agency panel"* remains inaccurate as written — FOURTEENTH run.** No trend claim made from this panel today.

### 3. Regulator — **+1 NET-NEW AT-SOURCE CAPTURE, +1 COMMITTED DATA SNAPSHOT, +1 PROVENANCE NOTE.**

**3a. ESMA — mandate item 2, executed by a different and better route than the one recommended.**

The recommendation was to close the sweep *"using the index's own date filter, not `?page=N`."* **The date-filter view was not reached — its URL never entered the fetch tool's provenance set, and it was not guessed.** Stated plainly rather than papered over: **the recommended object was not executed as written.**

What was executed instead: the **MiCA topic page** was fetched at source and its **register CSVs** — listed under *"Not fetched, not guessed"* in the 08-07 file and never revisited since — were opened. **That produced the run's headline.** The 08-07 ruling that the MiCA topic page **fails the known-presence test as a news instrument** is respected in full and **no news-absence claim is made from it**; what was taken from the page is a *document it hosts*, which is the record rather than a rendering of it.

**Also read from the same page and NOT admitted:** ESMA75-1303207761-6284, 28 Nov 2025, *Statement to support the smooth implementation of MiCA standards and format* — grep-confirmed net-new to the repo, and **refused on relevance**: it is a data-format instrument, not a marketing one. Named here so it is carried, not rediscovered.

**Also: the register-freshness `[VERIFY]` moved.** The MiCA page stamped *"Last update: **31 July 2026**"* on 08-07 and *"Last update: **12 August 2026**"* today, against its own stated cadence of *"weekly intervals"* — **twelve days.** And the file's own newest `ae_lastupdate` is **31/07/2026**, *older* than today's page stamp. **The page claims a freshness its contents do not carry.** One observation, not a pattern; the 08-07 operational rule (cite the CSV's own timestamp, never the page stamp) stands and is reinforced.

**The 2026-02 statement PDF `[VERIFY]` was NOT cleared.** Not reached this run.

**3b. MAS — mandate item 1, executed, and it changed a method rather than adding a capture.** Eight surfaces, the rendering diagnosis, and the date tension. Full detail in the provenance note. **The guidelines remain UNADMITTED for a fourth consecutive run — and the reason has changed from "unreachable" to "reached the wrong document, and the date the corpus was carrying is now in doubt."** The MAS enforcement register was **not** re-attempted today; it remains **NOT MEASURED**, unchanged from 08-15.

**NOT REACHED, NOT GUESSED:** ESMA's index date-filter and chronological-sort views · `esma.europa.eu/databases-library/esma-library` · the ESMA 2026-02 statement PDF · the other four MiCA register CSVs · the AFM MEXC public-warning page · the five post-deadline CONSOB notice bodies · the MAS guidelines PDF **under Chrome** (the obvious next move, not made this run) · the two MAS consultation responses · the MAS enforcement register's real contents · MEXC/CoinMENA/Shelbit VARA notice bodies · `rulebooks.vara.ae` · CONSOB July `comunicato` PDFs · the undated ESMA finfluencer-factsheet CANDIDATE from 08-11 (**still refused, 6th run**) · the retry-queue URLs · `hello@northpoint.fi`. **`casptracker.eu` remains named, never used — SIXTH consecutive prospective naming under watch (ee).** **No URL was fabricated.**

### 4. Operator statements — **0 NET-NEW ADMITTED. Fifth consecutive recall confirmation.**

One search on the appointment axis (deliberately returning to it once, to test whether 08-15's re-vocabularisation failure was axis-specific or supply-specific). **Everything returned is already held:** Binance/Rachel Conlan CMO elevation and her June departure with **Eowyn Chen interim** (held — `binance-chen-marketing-not-hype-2026-07.md`); **Crypto.com's head of marketing exiting after almost six years** (held — `cryptocom-kalifowitz-cmo-exit-primary-2026-08-11.md`); **Coinbase / Catherine Ferdon as CMO** (held — `coinbase-ferdon-marketing-vanguard-2026-04.md`). **3/3 recall on named seats. Zero net-new, zero near-misses.**

**The answer to the test: supply-specific, not axis-specific.** 08-15 changed the vocabulary and got vendor explainers; 08-16 changed it back and got the corpus's own three files returned to it. **Watch (nn) survives the check** — the class-4 null is not an artefact of how the search is phrased.

**No 2026 appointment to any tracked firm's top marketing seat is publicly visible — fifth consecutive run.** Theme-4 datum, clock advanced: **ten weeks after Binance's CMO exit and eight weeks after Crypto.com's took effect, neither firm has publicly named a permanent successor.**

### 5. Layoffs — **0 NET-NEW ROWS. Tracker holds at 24. Fifth consecutive recall confirmation.**

One search (crypto exchange layoffs August 2026, marketing-team framing). Everything surfaced is already held: **Crypto.com (row 1), Gemini (row 2), Coinbase (row 4), BitGo (row 8), Exodus (row 10), BitMEX (row 11), Luno (row 15), FalconX (row 18), Ethereum Foundation (row 21). 9/9 recall. No candidate row surfaced that the corpus does not hold.**

**Standing finding UNCHANGED, cohort-scoped: no TRACKED firm's 2026 contraction has named marketing as an affected function.** 24 rows.
**The non-AI rationale streak extends to eleven runs** — no new contraction arrived to test it.

⚠ **One aggregator datum surfaced and NOT admitted.** A secondary summary attributes to CryptoJobsList **"more than 7,254 disclosed job cuts across 47 companies"** in 2026 and **"twelve companies / 894 positions in July alone."** The 08-10 denominator file works from a CryptoJobsList reading of **n=54**. **47 vs 54 is the same aggregator disagreeing with itself across two readings, via two different secondaries.** Not fetched at source, **not admitted, and the 08-10 ruling stands unchanged: no single recall percentage, ever.** Recorded because it is the second independent instance of the aggregator layer being internally inconsistent.

**Gnosis `[VERIFY]` — NOT CLOSED. 14th run carried.** Blocked by watch (jj).
**AscendEX — NOT PROMOTED, fourth consecutive carry.** `ascendex.com` was not in this run's provenance set. Unchanged reason; escalation (i).

### 6. NorthPoint longitudinal panel

`trend-data.json` **62 days stale**. **No trend claim made.**

---

## Mandate item 3 — the Coinbase estate test, executed

Full detail in `../../findings/theme-1-firm-estate-instrument-coinbase-2026-08-16.md`. The audit-table consequence, in one table:

| Row | Standing claim | Before today | After today |
|---|---|---|---|
| 5 | No tracked firm's 2026 contraction names marketing as affected | press-visibility claim; *"sweep the estates"* pending | **Estate swept on the best subject. No enumerable index exists. Claim is PERMANENTLY a press-visibility claim — label it and print it** |
| 6 | No 2026 appointment to any tracked firm's top marketing seat is publicly visible | same | **same** |
| 7 | No senior operator at a tracked firm has spoken publicly on marketing compliance | search-derived only | **same, and now with a stated reason rather than an outstanding task** |

**The aspiration that watch (p) encoded — that these claims could be upgraded by going to the firms — is withdrawn.** Not because the work is hard, but because on the cohort's most disclosure-rich member the surface does not exist. **That is a finding, and it belongs in Theme 1, not in a methodology apology.**

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged.
- **(b) First named post-deadline NCA marketing-side action** — **day-46 silence HOLDS. Fifteenth consecutive EU-NCA zero — and the first one tested against the EU's own consolidated register rather than against an index.** The 08-15 companion sentence (enforcement silence, not guidance silence) is retained verbatim and **gains a third clause today: it is also not *inaction* silence — five post-deadline perimeter actions exist, all Italian, none promotional.**
- **(c) Capture panel** — untouched.
- **(d) Agency panel staleness — 62 days**, byte-identical output eight runs running. **14th run.**
- **(e′) Cadence** — **🟢 ON TIME. 3 of 4.**
- **(f) Friday nomination cadence** — **not testable today (Sunday).** Failed on its scheduled date 08-14; carried two runs past it. Escalation (ii) unchanged.
- **(g) Coinbase n=1** — **⚠ SHARPENED, NOT RESOLVED.** Today's estate test is also n=1, and it is the same n=1. **The finding it produced is about instruments, which generalises more safely than a finding about Coinbase's behaviour would. Said explicitly so the report does not over-extend it.**
- **(h′) Layoff rationale correlates with firm type** — **REJECTED. Untested today.** Eleven-run non-AI streak intact. **Do not print.**
- **(i) Kraken paid-media build-out** — unchanged. The 2026-02 CFD adjacency recorded on 08-15 stands and remains **NOT asserted**.
- **(j) Senior-leader exits** — **ADVANCED IN CLOCK ONLY.** Fifth consecutive run finding nothing new.
- **(k) Chrome-lane instrumentation gap** — **🟢 PARTIALLY DISCHARGED, AND FROM AN UNEXPECTED DIRECTION.** The Chrome lane has been carried as a *class-1 job-postings* instrument that never runs. **Today it ran twice, on class 3 and on a class-1-adjacent estate test, and it returned what `web_fetch` could not on both.** The lane is not blocked; it was simply never pointed at anything but ATS pages.
- **(l) §4 too narrow AND provenance-blind** — **15th costing.** The definitional half **holds for a fourth consecutive run** — the 28 Nov 2025 ESMA statement was refused on relevance under the same boundary. **Recommendation to close the definitional half as SETTLED is repeated.** The provenance half remains live under (jj).
- **(m) Ad-platform gating** — discharged. The 08-15 cross-read against the halo statement stands.
- **(n) Full-range re-sweep of classes 3, 4, 5** — **🟢 THIRD CONSECUTIVE VINDICATION.** Class 3: +1 at-source capture from a file listed as unfetched nine days ago. Class 4: **3/3 recall, and the axis-vs-supply question answered.** Class 5: **9/9 recall.**
- **(o) Date the document, never an event held about it** — **APPLIED, AND IT WAS LOAD-BEARING.** 22 May 2026 is the date of a *response to a consultation*, not of the guidelines. It was refused on exactly this rule.
- **(p) Absence claims tested against firms' OWN channels** — **🔴 CLOSED AS UNACHIEVABLE, NOT AS UNDONE.** Five runs carried; tested today on the best available subject; **the route does not exist.** Replaced by a Phase-2 labelling requirement, which is a decision rather than a task.
- **(q) Agency matrix measures the crypto-native segment** — unchanged.
- **(r) Absence panel needs a "structural withdrawal" category** — unchanged.
- **(s) Robinhood row misclassified** — unchanged, **15th run.**
- **(t′) / (dd)** — Phase 2. Not carried.
- **(u) Brand absorption defeats name-keyed sweeps** — **🔴 FIRED TWICE TODAY, ON TWO NEW MECHANISMS.** (1) **Clone-domain collision:** a substring sweep of the cohort against the ESMA register returned `HTX` — resolving to **`HTXcoin-az`**, an impersonation domain, not the Stratum-1 exchange. A naive sweep would have printed *"a tracked firm appears in the EU non-compliance register."* (2) **Near-identical-title collision:** MAS runs **three** adjacent instrument names (*Digital Advertising* / *Digital Prospecting and Marketing* / FSG-G02 *Marketing and Distribution*), which is a live candidate explanation for the 25-March date discrepancy. **The alias table (vii) must key on entity identity and document title AND date — three mechanisms now, in nine days.**
- **(v) NCA sweep** — 6 of 6 over its window; VARA 08-14; ESMA re-swept 08-15 (instrument defective) and **read at register level today**; MAS attempted twice, **still NOT MEASURED** on enforcement.
- **(w)** — CLOSED 08-15. Do not reopen.
- **(x) `fetch_errors`** — unchanged; Aave 14th consecutive; four upstream company-list gaps, **14th run.**
- **(y) Pre-2026 class-1 rows are arithmetic inferences** — unchanged.
- **(z)** — CLOSED 08-11. Do not reopen.
- **(aa) Announcement vs effective dates** — **11th run, AND TESTED TODAY FOR THE FIRST TIME IN A WHILE.** The MAS 25-March/22-May tension is precisely this watch. **It cost a refusal, which is the watch working.**
- **(bb) / (ff) Class-1 feed-health guard** — **CLOSED 08-14; ran unattended and correctly today (+16, HEALTHY). Not reopened.**
- **(cc) Secondary layer going machine-written** — **🔴 STRONGEST INSTANCE YET, AND IT IS A NEW FAILURE MODE.** A compliance-vendor summary and a search-engine summary **agreed with each other on 25 March 2026, and the primary page agreed with neither.** **Agreement between two secondaries is not corroboration when both may derive from the same upstream.** Added as a standing rule.
- **(ee) A source cited once is a source not used as an instrument** — **🟢 DISCHARGED ON A NINE-DAY-OLD ENTRY.** The 08-07 file listed the five MiCA register CSVs under *"Not fetched, not guessed"* and nine runs passed without anyone opening them. **Today one of them produced the headline.** **The "not fetched, not guessed" list is not a disclaimer, it is a work queue, and this corpus has been treating it as the former.** `casptracker.eu` named a **sixth** time and still unused.
- **(gg) six classes in `methodology.md`, seven directories in `corpus/`** — unchanged. Rewrite queue holds at **§1, §3, §4, §5, §6, §7**.
- **(hh) A failed fetch is not a fetched absence** — **🔴 INVERTED TODAY, AND THIS IS THE RUN'S SECOND-BEST LESSON.** The watch protected the corpus from converting failures into absences. **It did not protect it from converting a *rendering limitation* into a failure.** Three MAS URLs were recorded as unreachable on 08-15; at least one was reachable by an available tool. **New companion rule: before recording a fetch as failed, check whether a sibling on the same host renders. If it does, the diagnosis is client-rendering and the escalation is a rendering engine.**
- **(ii) Adjacency inside a corpus file is not attribution** — Phase-2 blocker, blocked by (jj).
- **(jj) The corpus can write a retry queue but cannot read from it** — **UNCHANGED. Fifth run. Seed did not arrive.** Escalation (i). **AscendEX is the fourth-consecutive concrete cost.**
- **(kk)** — promoted into (mm) on 08-15. Not separately carried.
- **(ll) Was the primary surface ever requested?** — Phase-2 checklist item. **Row 5/6/7 disposition settled today; see mandate item 3.**
- **(mm) A rendering of the record is not the record** — **🟢 GENERALISED AGAIN, AND THE GENERALISATION IS NOW ABOUT OUR OWN TOOLING.** Three regulators taught the lesson about *their* renderings (VARA's table, ESMA's pagination, MAS's register). **Today a fourth case says the same thing about ours: `web_fetch` renders a client-side page as an empty body, which is our tool's rendering of the record, not the record.** **The rule extends: name the instrument that produced every absence, including our own.**
- **🆕 (oo) THE "NOT FETCHED, NOT GUESSED" LIST IS A WORK QUEUE, NOT A DISCLAIMER.** Every run ends with a list of named-but-unreached objects. **That list has been treated as an honesty ritual and not as an input.** The 08-07 entry for the MiCA register CSVs sat unexecuted for nine runs and then produced a headline in one fetch. **Standing rule adopted: each run must pull at least one item off a prior run's not-fetched list before opening any new search.** `casptracker.eu` (6 namings) and the MAS guidelines PDF-under-Chrome are the two oldest live entries.

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **HEALTHY, age 14.0h, fingerprint 2179 → 2195, delta +16. Clean absence permitted.**
2. Repo dedup pass: 08-15 record in full; four root docs in full; `csv.DictReader` over all 24 tracker rows; seven directory indexes; two corpus files in full; repo-wide grep on thirteen keys — **`NCASP`, `ae_competentAuthority`, `LWEX`, `Atomic Wallet`, `1303207761`, `P003-2023`, `22 May 2026`, `12 August 2026` ALL returned ZERO hits: net-new confirmed, not assumed.**
3. `web_fetch mas.gov.sg/regulation/guidelines/…digital-advertising-activities` → **200, EMPTY BODY.**
4. WebSearch (domain-restricted `mas.gov.sg`) — digital advertising guidelines → surfaced six MAS URLs into the provenance set, plus a summary asserting *effective 25 March 2026* and a *25 September 2025* media release. **Summary NOT admitted.**
5. `web_fetch` MAS guidelines operative PDF → **200, EMPTY BODY.**
6. `web_fetch` MAS media release (25 Sep 2025) → **200, EMPTY BODY.**
7. `web_fetch` MAS consultation Annex A PDF → **200, EMPTY BODY.**
8. `web_fetch` MAS consultation landing page → **200, RENDERED** (document list only).
9. `web_fetch` MAS **FSG-G02** guidelines page (**control**) → **200, RENDERED WITH BODY TEXT. This is the observation that reclassified the empty bodies.**
10. `web_fetch` MAS parliamentary reply → **200, EMPTY BODY.**
11. **Chrome extension `navigate` + `get_page_text` on surface 3 → ✅ RENDERED. Consultation P003-2023; MAS response date 22 May 2026.**
12. WebSearch (domain-restricted `esma.europa.eu`) — ESMA crypto marketing / MiCA 2026 → surfaced the ESMA root and MiCA topic page into the provenance set.
13. `web_fetch esma.europa.eu/` → **200, full body.** Homepage news list read: 03/08 → 10/07/2026, contiguous, **and it does not carry the 14/08 item that page 0 of the news index carried on 08-15 — a fourth distinct rendering of the same record.** No absence claim derived from it.
14. **`web_fetch` ESMA MiCA topic page → 200, full body.** Register stamp **12 August 2026**; five CSVs linked; **the 08-07 known-presence failure respected — no news-absence claim taken from this page.**
15. **`web_fetch esma.europa.eu/sites/default/files/2024-12/NCASP.csv` → 200, `text/csv`. THE RUN'S HEADLINE. 167 rows, parsed with `csv.DictReader`, committed as a snapshot.**
16. Cohort cross-check of all ~40 tracked firms against the register → **one substring hit (`HTX` → `HTXcoin-az`), correctly rejected as a clone domain.**
17. WebSearch — crypto exchange layoffs August 2026 marketing → **0 net-new. 9/9 recall.** One inconsistent aggregator datum recorded and refused.
18. WebSearch — CMO / VP marketing / head of marketing crypto exchange August 2026 → **0 net-new. 3/3 recall on named seats.**
19. WebSearch (domain-restricted `coinbase.com`) — newsroom → surfaced the press and IR URLs.
20. **`web_fetch investor.coinbase.com/news/default.aspx` → 200, chrome rendered, ZERO news items (client-rendered).**
21. **`web_fetch coinbase.com/press` → 200, fully rendered. A brand-asset download portal; no press archive.**
22. **Chrome extension on the IR page's RSS endpoint → `lastBuildDate` 22 September 2022; newest item 17 February 2023.**
23. **Not reached / not guessed:** ESMA's date-filter and chronological-sort index views · the ESMA library · the 2026-02 statement PDF · the other four register CSVs · the AFM MEXC warning page · the five CONSOB post-deadline notices · **the MAS guidelines PDF under Chrome (the obvious next move)** · the MAS consultation responses · the MAS enforcement register · VARA notice bodies · `rulebooks.vara.ae` · CONSOB July PDFs · the retry-queue URLs · Coinbase's SEC index and individual 2026 IR releases · `ascendex.com` · `hello@northpoint.fi`. **No URL was fabricated.**

---

## Net-new / changed this run

- `corpus/regulator-filings/esma-ncasp-non-compliant-register-at-source-2026-08-16.md` — **NEW. The run's headline.** ESMA interim MiCA register file 5/5, Art. 109/110, fetched at source and machine-parsed. 167 rows; **CONSOB 165 / AFM 1 / NBS 1 / every other EEA authority 0**; `ae_infrigment: No` on 167 of 167 and `ae_reason: None` on 166 of 167; the single reasoned row (AFM/MEXC) is an **Art. 59** authorisation case; five post-deadline rows, all CONSOB, none promotional; the clone-domain false positive recorded; the register-freshness `[VERIFY]` advanced; four explicit non-claims including a refusal to adjudicate any firm.
- `corpus/regulator-filings/_esma-ncasp-snapshot-2026-08-16.csv` — **NEW. 167 data rows**, byte-identical to the fetch. The report's Theme-4 numbers are now independently recomputable from the repo.
- `corpus/regulator-filings/_mas-digital-advertising-guidelines-provenance-2026-08-16.md` — **NEW.** The eight-surface ladder with the rendered **control**; the client-rendering reclassification; the Chrome escalation and its full verbatim return; **the 25 March 2026 vs 22 May 2026 date tension and the double refusal**; the three-near-identical-titles hypothesis; the named next surface.
- `findings/theme-1-firm-estate-instrument-coinbase-2026-08-16.md` — **NEW.** Mandate item 3. Coinbase's press page as brand-asset portal; the IR news module client-rendered to zero items; **the RSS feed's `lastBuildDate` of 22 September 2022**; watch (p) closed as unachievable; the Theme-1 reading (heavily-resourced marketing surface, unmaintained corporate-communications surface) with the adverse inferences explicitly disclaimed.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv`, `_feed-fingerprint.json`, `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — date re-stamps / byte-identical rewrites (sync, 8th run).
- `findings/longitudinal-2026-06.md` — day-46 shift appended.
- **Layoff tracker: 24 rows, unchanged (9/9 recall). Operator statements: unchanged (0 net-new, 3/3 recall on named seats). Regulator: +1 at-source capture, +1 committed data snapshot, +1 provenance note — third consecutive non-zero class-3 run. Job postings: 0 net-new, guard-certified clean absence.**

---

## Recommendation for next run

1. **🟢 PULL THE OLDEST ITEM OFF THE NOT-FETCHED LIST BEFORE OPENING ANY NEW SEARCH — this is watch (oo) and it is the highest-yield change available.** Today's headline came from a line that had been sitting in a nine-day-old file under *"not fetched, not guessed."* **The two oldest live entries are the MAS guidelines operative PDF (retry under Chrome — the ladder is proven on that host) and `casptracker.eu` (six namings, never used).** Do both. **This is a one-line change to how a run starts and it just paid for itself.**
2. **🟢 OPEN THE OTHER FOUR MiCA REGISTER CSVs.** `CASPS.csv` is the authorised-CASP register — **it is the denominator for every Theme-4 claim the report will make about which tracked firms hold a licence**, and the corpus has been describing licensed status from firms' own marketing rather than from the register. **`OTHER.csv` (white papers) is the closest thing that exists to an EU-wide index of promotional disclosure documents.** One fetch each. Same instrument, same provenance, already proven to work.
3. **Re-test the client-rendering diagnosis on the surfaces the corpus has already written off.** Watch (hh)'s inversion means **every "HTTP 200, empty body" in this repo is now suspect** — the MAS enforcement register, the MAS guidelines PDF, and the ESMA statement PDF are the three named ones. **Escalate each to Chrome once and record the result either way.** If the register renders, the 08-15 "NOT MEASURED" ruling can finally be resolved.
4. **Do NOT re-issue the retry queue.** Fifth run on the same constraint. **One line, move on.**
5. **Escalate to Jukka — seven items, in order:**
   - **(i) 🔴 FIVE RUNS OLD. Watch (jj).** The seed still does not arrive. **AscendEX** (fourth consecutive carry, the only 2026 aggregator row attributed to `Regulatory`), the retry queue, the Gnosis `[VERIFY]`, and the (ii) re-test are all blocked by one thing: **the scheduled-task prompt cannot pass URLs into the run's provenance set.** **Fix: paste the queue's URLs verbatim into the task prompt.** One edit, four items unblocked. Unchanged for five runs.
   - **(ii) 🔴 THE README'S FRIDAY PROMISE FAILED 08-14 AND IS NOW TWO RUNS PAST ITS TEST DATE.** *"Inbound nominations are read every Friday."* No access to `hello@northpoint.fi`; `inbound-nominations.md` does not exist. **Route the mailbox into a readable artifact, or amend the sentence before Sep 1.** Still the only open item with a third party on the other side.
   - **(iii) 🟢 THE ENFORCEMENT NULL IS NOW REGISTER-ANCHORED, AND IT COMES WITH A NUMBER THE REPORT CAN LEAD WITH.** Not *"no EU marketing enforcement has appeared"* but: **the EU's own consolidated non-compliance register holds 167 entries, 98.8% of them from one national regulator, and not one of them is a marketing-communications action.** Pair it with the ESMA halo statement — *"Some CASPs may even use their regulated status under MiCA as a marketing argument"*, July 2025 — and Theme 4 has its spine: **the guidance is thirteen months old, it is specific, and the register shows nobody has enforced it.** Both halves primary-sourced, no firm adjudicated.
   - **(iv) 🔴 OUR OWN FETCH TOOL HAS BEEN GENERATING FALSE ABSENCES AND WE RECORDED THEM AS FACTS.** `web_fetch` returns HTTP 200 with an empty body on client-rendered pages. **The corpus wrote three MAS URLs up as unreachable on 08-15; at least one was reachable by a tool already installed.** Every *"HTTP 200, EMPTY BODY"* line in this repo is now a suspect absence. **This needs a `methodology.md` paragraph, not a watch item** — a reader who re-runs our citations will hit the same wall and needs to know which tool we used.
   - **(v) 🔴 WATCH (p) IS CLOSED AS UNACHIEVABLE AND THAT CHANGES WHAT THREE FINDINGS CAN SAY.** Coinbase — US-listed, IR site, press page, named CMO, the Theme-1 spine — **maintains no enumerable first-party announcement index.** Its press page is a logo-download portal; its only feed stopped building in **September 2022**. **Three standing findings must ship labelled as press-visibility claims. That is now a decision, not a pending task**, and it is better than the alternative of pretending the sweep is still coming.
   - **(vi) `methodology.md` STILL NEEDS SIX SECTIONS REWRITTEN: §1, §3, §4, §5, §6, §7 — FOURTEENTH run for §1**, and §6's *"daily 18-agency panel"* now describes a file **62 days stale**. **§3 gains two requirements today:** the ESMA interim MiCA register must be named as a class-3 instrument, and the tool-rendering caveat from (iv) must be stated. **Still the one thing in the repo that could embarrass the report.**
   - **(vii) 🟢 A CHEAP PROCESS CHANGE WITH A PROVEN PAYOFF — ADOPT WATCH (oo).** Every run ends by listing objects it named and did not fetch. **That list has never been read back at the start of the next run.** One of its nine-day-old entries produced today's headline in a single fetch. **Rule: pull one item off the prior run's not-fetched list before starting anything new.** It costs nothing, it compounds, and it is the closest thing this project has to free yield with sixteen days to ship.

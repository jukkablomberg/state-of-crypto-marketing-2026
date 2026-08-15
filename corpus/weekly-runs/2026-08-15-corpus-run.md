# Corpus-assembly daily run — 2026-08-15 **(day 45 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-15 (**Saturday**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, verbatim from the 08-14 recommendations:** (1) **finish the job the method change started — sweep the remaining two objects at source: ESMA's pre-deadline 2026 index window, and the MAS enforcement register**; (2) re-read every standing absence claim against watch (ll) and mark it `primary surface requested: yes/no`; (3) promote AscendEX from the aggregator queue or state why not; (4) do NOT re-issue the retry queue — one line, move on; (5) escalate seven items.
**Dedup baseline read before writing:** `2026-08-14-corpus-run.md` in full; `README.md`, `methodology.md`, `scripts/README.md`, `tracked-firms.md` in full; all 24 tracker rows via `csv.DictReader`; directory indexes for all seven `corpus/` subdirectories; `mas-ps-g02-dpt-public-promotion-guidelines.md`, `esma-consob-post-deadline-index-sweep-2026-08-05.md`, `esma-binary-options-event-contracts-prediction-markets-2026-07.md`, `esma-mica-transitional-period-end-2026-06.md`, `okx-europe-ghoos-licence-as-marketing-asset-2026-08.md`, `mica-competitive-capture-2026-06.md` heads; repo-wide case-insensitive grep on **halo · 1872330276 · "unregulated activities" · 11/07/2025 · 2025-07-11 · ESMA35 · 8024 · "digital advertising activities" · "perpetual futures" · "product intervention" · ascendex**.
**🟢 CADENCE: ON TIME. 08-14 → 08-15, consecutive calendar days.** Watch (e′) advances **2 of 4**.

---

## Headline result

**The 08-14 recommendation was executed literally for the second run running, and for the second run running it corrected a claim the report was going to print — this time by finding that the EU had already published the marketing rulebook the corpus was about to describe as missing.**

**1. 🔴🟢 ESMA PUBLISHED A MARKETING DOS-AND-DON'TS TABLE FOR CASPs THIRTEEN MONTHS AGO, AND THIS CORPUS DID NOT HOLD IT.** The 11 July 2025 Statement *"Avoiding Misperceptions: Guidance for Crypto-Asset Service Providers Offering Unregulated Services"* (**ESMA35-1872330276-2329**) was fetched at source, full body, and is **net-new — grep-confirmed zero prior hits on `halo`, `1872330276`, `unregulated activities`, `2025-07-11`.**

It contains, in ESMA's own words, the sentence the report's Theme 4 has needed and never had:

> "**Some CASPs may even use their regulated status under MiCA as a marketing argument** and encourage the confusion between regulated and unregulated products and services."

And in the **DON'T** column of a four-row table:

> "**The CASP's regulatory status is used as a promotional tool.** When engaging in unregulated activities, information provided to the client or potential client, **including marketing materials** and other documentation, includes a reference to the CASP being authorised/regulated by an NCA."

**The corpus has spent the post-deadline window documenting exactly this pattern without knowing the regulator had already named it.** `../marketing-campaigns/okx-europe-ghoos-licence-as-marketing-asset-2026-08.md` (OKX Europe's three-authorisation column), `../marketing-campaigns/mica-competitive-capture-2026-06.md` (OKX 8% / Coinbase 5% / Kraken €1M, all keyed to licensed status), `../marketing-campaigns/kraken-institutional-mica-counterparty-2026-06.md`.

**What this changes, precisely.** The standing finding — *no EU NCA has published a named marketing-side enforcement action against a CASP since the transitional deadline* — **is untouched and still holds at day 45.** What is retired is the implication that was riding alongside it: that **the EU has said nothing operational about crypto marketing conduct.** It has. **The gap is not guidance. The gap is enforcement.** That is a sharper, more defensible, and more regulator-readable framing than the one the corpus was carrying, and it arrived before Phase 2 rather than after publication. → `../regulator-filings/esma-halo-effect-regulatory-status-as-marketing-argument-2025-07.md` (**NEW**).

**2. 🟢 A SECOND NET-NEW ESMA CAPTURE FROM THE SAME SWEEP — AND IT ADDS A THIRD REGULATORY PHILOSOPHY THE REPORT'S TWO-ROW TABLE DID NOT HAVE.** **24 February 2026, ESMA35-243228190-8024**: CFD product-intervention measures apply to derivatives *"often marketed as perpetual futures"*, **crypto-assets such as Bitcoin named explicitly.** The in-scope requirements include **a mandatory risk warning**, **a narrow target market with an aligned distribution strategy**, and **the prohibition of monetary and non-monetary benefits** — a flat ban on the acquisition-incentive mechanic.

**That is the same mechanic the corpus captured running at EEA scale six weeks before the deadline** (OKX 8% transfer bonus / Coinbase 5% / Kraken €1M draw). The jurisdictional table now reads: **MAS regulates marketing *reach*; MiCA Art. 66 regulates marketing *content*; CFD product intervention regulates marketing *mechanics*.** The third row is new to this corpus. → `../regulator-filings/esma-cfd-product-intervention-perpetual-futures-2026-02.md` (**NEW**).

⚠ **Near-miss worth recording:** this document's reference stem (`ESMA35-243228190`) is **identical** to the binary-options statement the corpus captured on 08-01 (`-8148`, 2026-07-03). **A stem match is not a document match — the dedup pass nearly discarded a net-new capture against its own near-neighbour.**

**3. 🔴 THE INSTRUMENT DEFECT IS AS IMPORTANT AS EITHER CAPTURE, AND THE CORPUS FALSIFIED IT FROM ITS OWN SHELF.** ESMA's news index, walked `?page=0,1,2`, returns **10 items per page while the offset advances by ~20**. Measured boundaries: page 0 = **14/08/2026 → 10/07/2026**; page 1 = **02/06/2026 → 07/05/2026**; page 2 = **11/03/2026 → 23/02/2026**. **A 37-day gap and a 56-day gap, on a surface with no visible discontinuity.**

**The gap is proven to contain real items without leaving the repo:** the corpus already holds **ESMA75-113276571-1710, dated 23 June 2026** — the MiCA transitional-period wind-down statement, one of the most consequential documents in the whole corpus — **and 23 June sits inside the first gap.**

**This is the exact sibling of watch (kk) one run later.** On 08-14 the falsifier was one click away on the same host; today it was **one page boundary away on the same URL**. Two consecutive runs, two different regulators, one defect class: **the corpus was reading a rendering of the record and calling it the record.** → `../regulator-filings/_esma-news-index-pagination-instrument-2026-08-15.md` (**NEW**).

**Day-45 EU-NCA named marketing-side enforcement silence HOLDS. Class 3: +2 net-new captures + 1 instrument note — the second consecutive non-zero, and the largest single-run class-3 yield in the project's history.**

---

## Six-class audit trail

### 0. The retry-queue seed — one line, as instructed

**The seed did not arrive.** The scheduled-task prompt for 2026-08-15 contains no URLs. Watch (jj) unexecutable for a fourth run; **not re-issued** per the 08-13 ruling. Escalation (i) stands. Moving on.

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0 — GUARD-CERTIFIED CLEAN ABSENCE, second consecutive run.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-08-15
source A (jobs)   scan_date: 2026-08-15
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-14T21:46:39Z, age=14.3h,
             fingerprint total_jobs_fetched=2179, delta=+4 vs 2026-08-14 (2175))
  reason: age 14.3h, fingerprint delta +4
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

**The two-predicate guard shipped on 08-14 is now running unattended and doing its job.** Delta **+4** (2175 → 2179) vs a prior calendar date; age 14.3h. Both predicates pass, so the class-1 absence claim is **permitted and earned**. ⚠ **Honest note on the magnitude:** +4 is the smallest non-zero delta observed since the fingerprint series began (+24 on 08-14). The guard tests **direction, above zero** — it does **not** test whether +4 represents a full scan or a partially completed one. **That is not a defect the guard was built to catch, and it is not being claimed as one; it is recorded so the series has a floor observation on it.**

**`fetch_errors`: unchanged.** **OKX (Tier-1), Securitize, Rabby, Relai still absent from the upstream company list — THIRTEENTH run.** Watch (x) stays REOPENED. **Aave: thirteenth consecutive fetch error.**

### 2. Agency claims / overlap matrix (deterministic)

18 files rewritten; 8 matrix rows; **1 OVERLAP: Sui (coinbound, rzlt)** — unchanged. `trend-data.json` `lastUpdated` still **2026-06-15**: **61 days stale.** Class-2 output byte-identical for a **seventh** consecutive run. **`methodology.md` §6's phrase *"daily 18-agency panel"* remains inaccurate as written — THIRTEENTH run.** No trend claim made from this panel today.

### 3. Regulator — **+2 NET-NEW CAPTURES, +1 INSTRUMENT NOTE. Largest single-run class-3 yield in the project's history.**

Full detail in the three new files. **Mandate item 1 was executed on both named objects. One returned two captures; the other returned a refusal.**

**3a. ESMA — swept at source. Mandate item 1, first object: ✅ DONE, and it over-delivered.**

The 08-14 record named *"ESMA's pre-deadline 2026 index window"* as never swept. It was swept today. **It did not produce a 2026 marketing item from the pre-deadline window the recommendation had in mind — it produced a 2025 one and a February 2026 one, both of which thirteen runs of secondary-source searching had never surfaced,** plus the pagination defect that explains why. **The recommendation was right about the method and wrong about what the method would find, which is the correct way for a recommendation to be wrong.**

**Post-deadline window re-measured:** page 0 of ESMA's index now carries **one item newer than the 08-05 sweep** — *"ESMA confirms go-live for weekly commodity derivatives position reporting", 14/08/2026, tag: Trading.* **Not crypto, not marketing. The post-deadline ESMA silence on crypto marketing HOLDS at day 45** — with the pagination caveat now attached to it in writing.

**3b. MAS — swept at source. Mandate item 1, second object: ⚠ ATTEMPTED, AND THE HONEST ANSWER IS "NOT MEASURED".**

- **`mas.gov.sg/regulation/enforcement/enforcement-actions` → HTTP 200, full body.** The register renders its own scope rule — *"The information will remain on this page for five years from the date of publication"* — and then returns **ten rows, all dated 22 October 2020 → 03 March 2021.** A five-year retention window read on 2026-08-15 should surface 2021–2026. **It surfaced only the oldest edge of that window.**
- **Ruling: this is a partial or non-current rendering, NOT a measured absence.** Filed under watch **(hh)** — a failed fetch is not a fetched absence — and under **today's new (mm)**: it is the same page-rendering defect class as the ESMA index, on a second regulator, in the same run. **The corpus will NOT claim MAS has published no 2021–2026 enforcement actions.** No MAS file was written from this fetch, and none should be until the surface is read correctly.
- **Also surfaced and NOT admitted:** MAS **Guidelines on Standards of Conduct for Digital Advertising Activities**, stated effective **25 March 2026**, applying to all MAS-regulated FIs and their appointed third parties advertising via digital media. **This is a high-value class-3 candidate and it is being refused today on provenance grounds, not on relevance grounds.** Both MAS primary URLs — the guidelines landing page and the operative PDF — **returned HTTP 200 with EMPTY BODIES.** The only substantive account available was secondary (a compliance-vendor summary). **Per the coverage rules, a regulator instrument is not admitted to this corpus on a vendor's paraphrase.** Named here explicitly so it is carried, not rediscovered: **this is the single highest-value unadmitted class-3 object in the queue.**

**NOT REACHED, NOT GUESSED:** the ESMA 2026-02 statement PDF (URL published by ESMA, cited but unfetched — `[VERIFY]`) · ESMA's chronological-sort and date-filter index views · `esma.europa.eu/databases-library/esma-library` · the section-filtered ESMA views · MAS digital-advertising guidelines PDF and landing page (both empty-bodied) · the MAS enforcement register's real current contents · MEXC / CoinMENA / Shelbit VARA notice bodies · `rulebooks.vara.ae` · CONSOB July `comunicato` PDFs · the still-undated ESMA finfluencer-factsheet CANDIDATE from 08-11 (**still refused, 5th run**) · the nine retry-queue URLs · `hello@northpoint.fi`. **`casptracker.eu` remains named, never used — FIFTH consecutive prospective naming under watch (ee).** **No URL was fabricated.**

### 4. Operator statements — **0 NET-NEW ADMITTED. Held at 6. Fourth consecutive recall confirmation.**

One search, deliberately re-vocabularised toward MiCA marketing compliance rather than toward CMO appointments (the rut the 08-14 record identified). **Everything returned was a law-firm, vendor, or exchange-owned explainer of MiCA — zero operator statements, zero near-misses worth naming.** Refused as a class: `hacken.io`, `adamsmith.lt`, `unit21.ai`, `innreg.com`, `bingx.com/learn`, `cyfrin.io`, `paybis.com`, `narvi.com`.

**🔴 THE VOCABULARY CHANGE FAILED, AND THE FAILURE IS INFORMATIVE.** Switching the search axis from *who holds the seat* to *what the seat says about MiCA* returned **only the compliance-explainer content industry** — no operator at any tracked firm has a publicly indexed statement on the marketing-compliance surface. **That is a cleaner statement of the class-4 null than four runs of appointment searches produced:** the absence is not that senior marketers are not being written about; it is that **senior crypto marketing operators do not speak publicly about marketing compliance at all.** Recorded as **new watch (nn)**.

**No 2026 appointment to any tracked firm's top marketing seat is publicly visible — fourth consecutive run.** Theme-4 datum, clock advanced: **nine weeks after Binance's CMO exit and seven weeks after Crypto.com's took effect, neither firm has publicly named a permanent successor.**

**One scope note.** The ESMA halo statement contains highly quotable marketing language. **Not admitted to class 4** — the speaker is a regulator, not a marketing operator at a tracked firm, and it is unattributed to a natural person. It lives in class 3 where it belongs. **Same ruling as the VARA statement on 08-14; the boundary is holding under pressure.**

### 5. Layoffs — **0 NET-NEW ROWS. Tracker holds at 24. Fourth consecutive recall confirmation.**

One search (crypto layoffs August 2026, marketing-team framing). Everything surfaced is already held: **Luno −20% (row 15), Gemini −30% (row 2), Bitwise −14% (row 24), Exodus −25% (row 10), BitMEX wind-down (row 11), Coinbase (row 4), BitGo (row 8), Polygon Labs (rows 9, 20), FalconX (row 18).** **9/9 recall. No candidate row surfaced that the corpus does not hold.**

**Standing finding UNCHANGED, cohort-scoped: no TRACKED firm's 2026 contraction has named marketing as an affected function.** 24 rows.
**The non-AI rationale streak extends to ten runs** — no new contraction arrived to test it.
**Gnosis `[VERIFY]` — NOT CLOSED. 13th run carried.** Blocked by watch (jj), not by effort.

**Mandate item 3 — AscendEX: 🔴 NOT PROMOTED, and the reason is stated rather than deferred.** The row (2026-07-10, −100%, stated reason `Regulatory`, aggregator-sourced to CoinPedia/Ascendex.com) is the **only 2026 aggregator row whose stated reason is regulatory**, and it is an exchange shutdown nine days post-deadline. **Promotion requires the first-party `ascendex.com` notice, and `ascendex.com` was not in this run's provenance set** — the class-5 search returned nine URLs, none of them AscendEX's own. **The corpus will not enter a `Regulatory`-attributed shutdown of a whole exchange on an aggregator's single-word reason field.** Third consecutive carry. **This is now the clearest instance of escalation (i): the row is one fetch from resolution and the fetch is unreachable because no search has put the domain in front of the run.**

### 6. NorthPoint longitudinal panel

`trend-data.json` **61 days stale**. **No trend claim made.**

---

## Mandate item 2 — the watch-(ll) absence audit, executed

Every standing absence claim in the repo, marked `primary surface requested: yes/no`. **This is the audit the 08-14 record asked for, and it is the single most useful page in this run record for Phase 2.**

| # | standing absence claim | primary surface requested? | status after today |
|---|---|---|---|
| 1 | No **EU NCA** named marketing-side enforcement action post-deadline | **PARTIAL** — AFM, CNMV, CONSOB, ESMA, AMF, BaFin indexes fetched at source (08-03/08-05/08-06/08-07); **ESMA's now known to be page-lossy** | **HOLDS at day 45**, but the ESMA leg must carry the (mm) caveat |
| 2 | ESMA published nothing on crypto marketing in the post-deadline window | **YES, but on a defective surface** | **RE-SCOPED, not withdrawn.** Print the measured coverage, not the nominal window |
| 3 | **EU has issued no operational marketing guidance to CASPs** | **NO — never requested** | **🔴 FALSIFIED TODAY.** ESMA 2025-07-11 halo statement + 2026-02-24 CFD statement. **This claim must not appear in the report** |
| 4 | MAS enforcement register contains no marketing-side crypto action | **ATTEMPTED, RETURNED A NON-CURRENT RENDERING** | **NOT MEASURED.** Do not print in either direction |
| 5 | No tracked firm's 2026 contraction names marketing as affected | **NO** — derived from press reporting, not from firms' own estates | **HOLDS, but it is a press-visibility claim, not a firm-disclosure claim.** Label it as such (watch (p)) |
| 6 | No 2026 appointment to any tracked firm's top marketing seat is publicly visible | **NO** — no tracked firm's own newsroom swept | **HOLDS, same caveat.** Blocked by (jj)/(p) |
| 7 | No senior operator at a tracked firm has spoken publicly on marketing compliance | **NO** — search-derived only | **HOLDS; promoted to watch (nn)** |
| 8 | Class-2 agency panel shows no movement | **N/A** — the file is 61 days stale; this is UNOBSERVED, not absent | **Correctly labelled already** |

**The audit's verdict: of eight standing absence claims, ONE has been falsified, TWO must be re-scoped, THREE are press-visibility claims wearing firm-disclosure clothing, and only ONE (class 2) was already labelled correctly.** Watch (ll) was the right diagnosis and this table is its payload.

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged.
- **(b) First named post-deadline NCA marketing-side action** — **day-45 silence HOLDS. Fourteenth consecutive EU-NCA zero.** Scope wording as fixed on 08-14 is retained verbatim. ⚠ **Today adds a necessary companion sentence: the silence is enforcement silence, NOT guidance silence.** Printing the former without the latter would misdescribe the regime.
- **(c) Capture panel** — untouched.
- **(d) Agency panel staleness — 61 days**, byte-identical output seven runs running. **13th run.**
- **(e′) Cadence** — **🟢 ON TIME. 2 of 4.**
- **(f) Friday nomination cadence** — **FAILED on its scheduled date 08-14; not re-testable today (Saturday).** Escalation (ii) unchanged and now carried past its test date by one run.
- **(g) Coinbase n=1** — unchanged, open.
- **(h′) Layoff rationale correlates with firm type** — **REJECTED. Untested today** (no new contraction). Ten-run non-AI streak intact. **Do not print.**
- **(i) Kraken paid-media build-out** — unchanged. ⚠ **Gains a live regulatory adjacency today:** the €1M prize draw is an acquisition inducement, and the 2026-02 CFD statement prohibits monetary and non-monetary benefits **within the CFD perimeter**. **Whether Kraken's draw touches that perimeter is unestablished and is NOT asserted.**
- **(j) Senior-leader exits** — **ADVANCED IN CLOCK ONLY.** Fourth consecutive run finding nothing new.
- **(k) Chrome-lane instrumentation gap** — unchanged.
- **(l) §4 too narrow AND provenance-blind** — **14th costing. The definitional half loses ground for a THIRD consecutive run** — the ESMA statement was correctly refused on the same test that refused VARA's. **A boundary that has now held against three consecutive temptations is a good boundary; recommend closing the definitional half of (l) as SETTLED.** The provenance half remains live under (jj).
- **(m) Ad-platform gating** — discharged. ⚠ Cross-reads against the 2025-07 halo statement: **Google's CASP gate enforces the licence as an access condition; ESMA warns against the licence being used as a promotional claim. The two private/public treatments of the same credential now point in opposite directions, and the corpus holds both.**
- **(n) Full-range re-sweep of classes 3, 4, 5** — **🟢 SECOND CONSECUTIVE VINDICATION, AND THE STRONGEST YET.** Class 3 re-swept by the at-source method: **two net-new captures and a falsified standing claim.** Class 4: fourth clean recall; the vocabulary change failed informatively → (nn). Class 5: **9/9 recall.**
- **(o) Date the document, never an event held about it** — **APPLIED.** Both new ESMA files carry the regulator's own publication date; the 2026-02 PDF is `[VERIFY]` because it was cited by the source but not fetched.
- **(p) Absence claims tested against firms' OWN channels** — **🔴 BLOCKED, 4th run.** ⚠ **Broadened again by the mandate-2 audit: three standing absence claims are now formally identified as press-visibility claims mislabelled as firm-disclosure claims.** That is a Phase-2 labelling requirement, not an aspiration.
- **(q) Agency matrix measures the crypto-native segment** — unchanged.
- **(r) Absence panel needs a "structural withdrawal" category** — unchanged.
- **(s) Robinhood row misclassified** — unchanged, **14th run.**
- **(t′) / (dd)** — Phase 2. Not carried.
- **(u) Brand absorption defeats name-keyed sweeps** — **STRENGTHENED IN A NEW DIRECTION.** Today's near-miss was not a brand collision but a **document-reference collision**: `ESMA35-243228190-8148` vs `-8024`, four months apart, different subjects. **The alias table (vii) must key documents by reference AND date, not by stem.**
- **(v) NCA sweep** — 6 of 6 over its window; VARA added 08-14; **ESMA re-swept today and its instrument found defective. MAS attempted and NOT measured.**
- **(w) Class-3 sweep vocabulary AND method** — **🟢 FULLY DISCHARGED ON THE METHOD HALF.** All three objects the 08-13 record named have now been attempted at source: VARA (08-14, produced the headline), **ESMA (today, produced two captures + an instrument defect)**, **MAS (today, produced a refusal that is itself correctly recorded)**. **The list is empty. The method is proven three for three.** Closing (w) and replacing it with **(mm)**, which is what the method actually taught.
- **(x) `fetch_errors`** — unchanged; Aave 13th consecutive; four upstream company-list gaps, **13th run**.
- **(y) Pre-2026 class-1 rows are arithmetic inferences** — unchanged.
- **(z)** — CLOSED 08-11. Do not reopen.
- **(aa) Announcement vs effective dates** — 11th run; **not tested today** (no new dated event).
- **(bb) / (ff) Class-1 feed-health guard** — **🟢 CLOSED 08-14; ran unattended and correctly today (+4, HEALTHY).** One observation logged: **+4 is the series floor to date**, and the guard tests direction above zero, not scan completeness. **Not reopened.**
- **(cc) Secondary layer going machine-written** — **STRONGLY EVIDENCED TODAY.** The entire class-4 return was compliance-explainer content from vendors and law firms. **The structural answer remains the same: fetch the regulator's own domain.**
- **(ee) A source cited once is a source not used as an instrument** — **DISCHARGED TWICE.** VARA on 08-14, **ESMA's own index today**. `casptracker.eu` named a **fifth** time and still unused. **MAS's digital-advertising guidelines join the named-but-unused list today.**
- **(gg) six classes in `methodology.md`, seven directories in `corpus/`** — unchanged. Rewrite queue holds at **§1, §3, §4, §5, §6, §7**.
- **(hh) A failed fetch is not a fetched absence** — **STANDS, and was load-bearing twice today**: the MAS register's non-current rendering and the MAS guidelines' empty bodies were both refused rather than converted into absences.
- **(ii) Adjacency inside a corpus file is not attribution** — Phase-2 blocker, blocked by (jj).
- **(jj) The corpus can write a retry queue but cannot read from it** — **UNCHANGED. Fourth run. Seed did not arrive.** Escalation (i). **AscendEX is today's concrete cost.**
- **(kk) A regulator's summary table is not the regulator's record** — **🟢 GENERALISED AND CONFIRMED ON A SECOND REGULATOR IN ONE RUN.** VARA's table vs its notices index (08-14); **ESMA's page 0 vs its own page boundaries (today).** Promoted into (mm).
- **(ll) Was the primary surface ever requested?** — **🟢 EXECUTED IN FULL** as mandate item 2. Eight claims audited; **one falsified, two re-scoped, three relabelled.** The watch has delivered its payload and **should now be treated as a Phase-2 checklist item rather than a daily watch.**
- **🆕 (mm) A RENDERING OF THE RECORD IS NOT THE RECORD — AND THIS IS NOW A THREE-REGULATOR PATTERN, NOT AN ANECDOTE.** VARA's fines table stopped 6 months short of its own notices index. **ESMA's news index drops ~half its items between `?page=N` boundaries — proven from inside this repo, because a document the corpus already holds (ESMA75-113276571-1710, 23 June 2026) falls in the gap.** **MAS's enforcement register returns 2020–21 rows under a stated five-year retention window.** **Standing rule adopted: before any absence claim is derived from a paginated or summarised index, record the first and last item date of every page fetched and confirm the boundaries meet. If they do not, name the measured coverage, never the nominal window.**
- **🆕 (nn) THE CLASS-4 NULL IS NOT "NO ONE IS HIRED", IT IS "NO ONE SPEAKS".** Re-vocabularising the class-4 search from appointments to marketing-compliance substance returned **only vendor and law-firm explainers — zero operator voices.** **Senior crypto marketing operators at tracked firms have no publicly indexed statements on the marketing-compliance surface at all.** That is a much stronger and more report-ready statement of the class-4 absence than four runs of appointment searches produced, and it is directly on Theme 1 and Theme 4.

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **HEALTHY, age 14.3h, fingerprint 2175 → 2179, delta +4. Clean absence permitted.**
2. Repo dedup pass: 08-14 record in full; four root docs in full; `csv.DictReader` over all 24 tracker rows; seven directory indexes; six corpus-file heads; repo-wide grep on eleven keys — **`halo`, `1872330276`, `unregulated activities`, `2025-07-11`, `11/07/2025`, `8024`, `digital advertising activities` ALL returned ZERO hits: net-new confirmed, not assumed.**
3. WebSearch — MAS enforcement register / DPT advertising 2026 → surfaced `mas.gov.sg` enforcement + guidelines URLs into the provenance set.
4. **`web_fetch mas.gov.sg/regulation/enforcement/enforcement-actions` → HTTP 200, full body. TEN ROWS, ALL 2020–2021, under a stated five-year retention rule. NOT MEASURED — recorded as a rendering defect, not an absence.**
5. WebSearch (domain-restricted to `mas.gov.sg`) — digital advertising guidelines → surfaced the guidelines landing page + operative PDF.
6. **`web_fetch` MAS guidelines PDF → HTTP 200, EMPTY BODY. NOT USABLE.**
7. **`web_fetch` MAS guidelines landing page → HTTP 200, EMPTY BODY. NOT USABLE.**
8. **`web_fetch` MAS consultation-response PDF → HTTP 200, EMPTY BODY. NOT USABLE.** All three added to the retry queue that cannot be read.
9. WebSearch (domain-restricted to `esma.europa.eu`) — ESMA news index / crypto marketing communications → **surfaced the halo-effect item into the provenance set. The run's headline begins here.**
10. **`web_fetch esma.europa.eu/press-news/esma-news/investors-should-consider-risks-unregulated-products-offered-regulated-crypto` → HTTP 200, full body.** 11/07/2025, tags *Digital Finance and Innovation · Investor protection*.
11. **`web_fetch esma.europa.eu/sites/.../ESMA35-1872330276-2329_-_MiCA_Statement_Access_to_Unregulated_Activities.pdf` → HTTP 200, full body. The Dos/Don'ts table transcribed verbatim.**
12. **`web_fetch esma.europa.eu/press-news/esma-news` → HTTP 200, full body.** Page 0: 14/08/2026 → 10/07/2026. One item newer than the 08-05 sweep; not crypto, not marketing.
13. **`web_fetch esma.europa.eu/press-news/esma-news?page=1` → HTTP 200, full body.** 02/06/2026 → 07/05/2026. **The 37-day gap becomes visible.**
14. **`web_fetch esma.europa.eu/press-news/esma-news?page=2` → HTTP 200, full body.** 11/03/2026 → 23/02/2026. **The 56-day gap confirms the defect is systematic, not a one-off.** Surfaced the CFD/perpetual-futures item.
15. **`web_fetch esma.europa.eu/press-news/esma-news/esma-reminds-firms-their-obligations-under-cfd-product-intervention-measures` → HTTP 200, full body.** 24/02/2026. Second net-new capture.
16. WebSearch — crypto layoffs August 2026 marketing team cuts → **0 net-new. 9/9 recall against the held tracker.**
17. WebSearch — head of marketing / VP marketing / crypto exchange / MiCA marketing compliance → **0 net-new, 0 near-misses. Eight vendor/law-firm explainers refused as a class → watch (nn).**
18. **Not reached / not guessed:** the ESMA 2026-02 statement PDF · ESMA chronological-sort, date-filter, library and section-filtered views · MAS register's current contents · MAS digital-advertising guidelines operative text · `ascendex.com` · MEXC/CoinMENA/Shelbit VARA notice bodies · `rulebooks.vara.ae` · CONSOB July PDFs · the retry-queue URLs (now twelve) · the Gnosis `[VERIFY]` URL · the ten Stratum-1 estate URLs · `hello@northpoint.fi`. **No URL was fabricated.**

---

## Net-new / changed this run

- `corpus/regulator-filings/esma-halo-effect-regulatory-status-as-marketing-argument-2025-07.md` — **NEW. The run's headline.** ESMA35-1872330276-2329, 11 July 2025, fetched at source. The four-row marketing Dos/Don'ts table transcribed as published; the *"regulated status as a marketing argument"* sentence; Art. 66(1)/(2) anchors; the cross-read against three held `marketing-campaigns/` files; four explicit non-claims including a refusal to adjudicate any tracked firm.
- `corpus/regulator-filings/esma-cfd-product-intervention-perpetual-futures-2026-02.md` — **NEW.** ESMA35-243228190-8024, 24 February 2026. Crypto perpetual futures in CFD scope; mandatory risk warning, narrow target market + aligned distribution strategy, **prohibition of monetary and non-monetary benefits**; the three-row reach/content/mechanics jurisdictional table; the reference-stem near-miss recorded; operative PDF marked `[VERIFY]` because cited-but-unfetched.
- `corpus/regulator-filings/_esma-news-index-pagination-instrument-2026-08-15.md` — **NEW.** Measured page boundaries for pages 0–2; the 37-day and 56-day gaps; **the repo-internal falsifier (ESMA75-113276571-1710, 23 June 2026, sits in the gap)**; the retroactive re-scoping of the 08-05 sweep; the standing page-contiguity rule; five alternative ESMA surfaces named and explicitly NOT used.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv`, `_feed-fingerprint.json`, `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — date re-stamps / byte-identical rewrites (sync, 7th run).
- `findings/longitudinal-2026-06.md` — day-45 shift appended.
- **Layoff tracker: 24 rows, unchanged (9/9 recall). Operator statements: 6, unchanged (0 net-new, 0 near-misses). Regulator: +2 captures +1 instrument note — largest single-run class-3 yield in the project's history. Job postings: 0 net-new, guard-certified clean absence.**

---

## Recommendation for next run

1. **🟢 GO BACK FOR THE MAS DIGITAL-ADVERTISING GUIDELINES — IT IS THE HIGHEST-VALUE UNADMITTED OBJECT IN THE QUEUE AND IT WAS REFUSED ON PROVENANCE, NOT RELEVANCE.** Effective 25 March 2026, applies to all MAS-regulated FIs **and their appointed third parties** advertising via digital media — i.e. **agencies and influencers, by name, inside the report's own comparison panel.** Both MAS primary URLs returned empty bodies today. **Try the MAS media-release surface and the consultation-response PDF instead of the guidelines page** — a different surface on the same host, which is exactly the move that worked on VARA (08-14) and ESMA (today). **Three regulators, one method, three for three.**
2. **🟢 CLOSE THE ESMA SWEEP PROPERLY USING THE INDEX'S OWN DATE FILTER, NOT `?page=N`.** The defect is documented; the fix is on the page. **A bounded From/To sweep over Dec-2024 → today would give the corpus its first genuinely complete class-3 ESMA coverage** — and today proved the yield is not zero: **two captures came out of three pages of a lossy surface.** Also fetch the **2026-02 statement PDF** to clear its `[VERIFY]`.
3. **Re-run the mandate-2 audit table's row 5 and row 6 against ONE tracked firm's own newsroom.** Three standing absence claims are now known to be press-visibility claims wearing firm-disclosure clothing. **One firm, one estate, one run** converts a labelling caveat into a measurement. Coinbase is the obvious candidate — it is already the Theme-1 spine and its estate is API-reachable.
4. **Do NOT re-issue the retry queue.** Fourth run on the same constraint. **Check in one line, move on.**
5. **Escalate to Jukka — seven items, in order:**
   - **(i) 🔴 FOUR RUNS OLD AND TODAY IT COST A NAMED, IDENTIFIED ROW.** Watch (jj). **AscendEX** — the only 2026 aggregator row attributed to `Regulatory`, an exchange shutdown nine days post-deadline, third consecutive carry — **is one fetch of `ascendex.com` from resolution, and the run cannot reach it because no search put the domain in the provenance set.** Also blocked: the twelve-entry retry queue (three MAS URLs joined today), the (p) estate sweep, the (ii) re-test, the Gnosis `[VERIFY]`. **Fix: paste the queue's URLs verbatim into the scheduled-task prompt.** One edit, five items unblocked.
   - **(ii) 🔴 THE README'S FRIDAY PROMISE FAILED ITS TEST DATE ON 08-14 AND IS NOW CARRIED PAST IT.** *"Inbound nominations are read every Friday."* No access to `hello@northpoint.fi`; `inbound-nominations.md` does not exist. **Route the mailbox into a readable artifact, or amend the sentence.** Only open item with a third party on the other side.
   - **(iii) 🔴 A CLAIM THE REPORT WAS GOING TO PRINT HAS BEEN FALSIFIED FOR THE SECOND RUN RUNNING.** 08-14 corrected *"named marketing-side enforcement silence"*. **Today falsifies the companion claim: that the EU has issued no operational marketing guidance to CASPs.** ESMA published a marketing Dos/Don'ts table on **11 July 2025** and a promotional-inducement prohibition on **24 February 2026**. **The correct Theme-4 spine is now: the guidance exists, is specific, and is a year old — what is absent is enforcement.** That is a stronger report, and it is stronger because the corpus went and looked.
   - **(iv) 🟢 THEME 4 NOW HAS A REGULATOR SENTENCE THAT LANDS DIRECTLY ON WHAT TRACKED FIRMS ARE ACTUALLY DOING.** ESMA: *"Some CASPs may even use their regulated status under MiCA as a marketing argument."* The corpus independently captured OKX, Coinbase and Kraken doing licence-keyed marketing in 2026. **The report can put the regulator's sentence and the firms' campaigns on the same page, both primary-sourced, without alleging a breach.** That is the most quotable pairing in the corpus.
   - **(v) 🔴 THE INSTRUMENT DEFECT IS NOW A THREE-REGULATOR PATTERN AND IT NEEDS A METHODOLOGY PARAGRAPH, NOT A WATCH ITEM.** VARA's table, ESMA's pagination, MAS's register — **three regulators, three renderings that are not the record, two consecutive runs.** `methodology.md` should state the page-contiguity rule explicitly. **A reader who checks the report's citations will hit these same surfaces; the report is stronger for having documented the defect than for having avoided it.**
   - **(vi) `methodology.md` STILL NEEDS SIX SECTIONS REWRITTEN: §1, §3, §4, §5, §6, §7 — THIRTEENTH run for §1**, and §6's *"daily 18-agency panel"* now describes a file **61 days stale**. **§3 needs two additions today**: MAS is named as a source class and its enforcement register has never been successfully read, and the class-3 method must carry the (mm) rule. **Still the one thing in the repo that could embarrass the report.**
   - **(vii) 🟢 THE CLASS-4 NULL FINALLY HAS ITS RIGHT WORDING, AND IT IS BETTER THAN THE OLD ONE.** Not *"no CMO appointments are visible"* — **"no senior marketing operator at any tracked firm has a publicly indexed statement on marketing compliance at all."** Four runs of appointment searches never produced that; one deliberately re-vocabularised search did. **Watch (nn).** It is a Theme-1 and Theme-4 finding in one sentence, and it is exactly the kind of visibility-as-analysis claim the methodology was built to support.

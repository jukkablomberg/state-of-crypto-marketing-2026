# Corpus-assembly daily run — 2026-08-20 **(day 50 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-20 (**Thursday**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, from the 08-17 recommendations:** (1) keep running watch (oo) on **both** lists — pull one item off the not-fetched list and one unverified candidate off the aggregator crossref; (2) **open `OTHER.csv`**, verifying size and checksum first; (3) **build `scripts/verify-capture.py`**; (4) do **not** re-issue the retry queue; (5) **stop spending runs on the MAS guidelines** — time-boxed to one further attempt.
**Dedup baseline read before writing:** `2026-08-17-corpus-run.md` in full; `README.md`, `methodology.md`, `scripts/README.md`, `tracked-firms.md` in full; all 25 tracker rows via `csv.DictReader`; both aggregator crossrefs in full; all `corpus/` and `findings/` directory indexes; the committed `_esma-ncasp-snapshot-2026-08-16.csv` parsed and re-verified.
**🔴 CADENCE: BROKEN. 08-17 → 08-20 is a THREE-DAY GAP. Watch (e′) regresses to 4 of 8.** The 08-18 and 08-19 slots produced no artifacts. 08-19 is independently accounted for by the portfolio-wide night-factory outage recorded in `situation.md`; **08-18 has no such account and none is invented here.** The class-1 feed fingerprint corroborates the gap from inside the data: today's comparison is against **2026-08-17**, not yesterday.

---

## Headline result

**The mandate was executed in full, and it produced one finding the report can lead with, one instrument that immediately caught a defect on its first outing, and two would-be net-new items that turned out to be the same six-year-old mistake wearing two hats.**

**1. 🔴 THE EU'S WHITE-PAPER REGISTER — THE ANCHOR OBJECT OF MiCA's MARKETING RULES — IS 55% ONE GERMAN COMPANY FILING FOR TOKENS IT DOES NOT ISSUE, INCLUDING SEVEN TRACKED FOUNDATIONS.**

`OTHER.csv` — interim MiCA register file 1/5, crypto-asset white papers — opened for the first time. **`Crypto Risk Metrics GmbH` (LEI `39120077M9TG0O1FE242`, DE/BaFin) holds 127 of the ~230 records in the captured portion.** One legal entity; the LEI is constant across all 127.

The tokens it has filed for, read from its own `wp_url` values, include **Sui · Uniswap · Aptos · Arbitrum · Avalanche · Algorand · Polygon (POL)** — seven of the cohort's tracked Stratum-2 foundations — plus **Cronos**, the chain of tracked Stratum-1 firm Crypto.com. **Not one of those filings is in the foundation's own name.**

**Why it matters here rather than to a MiCA lawyer.** Under MiCA the white paper is the document that marketing communications **must be consistent with**. It is the anchor of the entire promotional-compliance stack Theme 1 is about. **In the captured half of the EU's register of that anchor object, the majority filer is a third-party intermediary.**

⚠ **The limit ships attached.** Article 4 MiCA expressly permits a person other than the issuer to notify a white paper for admission to trading — one row in this very file says so in terms. **This is a visibility finding, not a compliance one.** It does not establish that any foundation was uninvolved, unaware, or in breach.

**It closes the gap 08-17 left open.** That run established **0 of 8 tracked foundations are authorised CASPs** and correctly declined to read it as non-compliance. Today supplies the other half: **the foundations are absent from the disclosure register as filers too — while their tokens are present in it under someone else's name.**

**And the Tier-1 exchanges appear, but only in one column.** Twelve rows name a tracked exchange; **eleven of the twelve are in `ae_lei_name_casp` — the CASP seeking admission to trading — not the issuer column.** Kraken (Payward, two LEIs) 8 · Coinbase Luxembourg 2 · Bitstamp 1. **The twelfth is Bitpanda, the only tracked firm in the capture appearing as an issuer in its own name**, `wp_lastupdate` 11/08/2026 — the second-newest record in the whole capture. → `../regulator-filings/esma-other-whitepaper-register-partial-capture-2026-08-20.md` (**NEW**).

**2. 🔴 THE CAPTURE THAT PRODUCED IT WAS TRUNCATED — AND THE RULE 08-17 WROTE TO CATCH THAT DID NOT CATCH IT.**

`OTHER.csv` came back **HTTP 200, 64,556 characters / 241 lines, final row cut mid-URL inside a Central Bank of Ireland record.** Second consecutive large-register capture that was silently incomplete.

Watch (pp) rule 1, written on 08-17, said *"any `web_fetch` result near ~82,000 characters is presumed truncated."*

| Capture | Chars | Actually |
|---|---|---|
| `CASPS.csv` 08-17 | 82,445 | truncated |
| `NCASP.csv` 08-16 & today | 24,614 | **complete** |
| `OTHER.csv` 08-20 | **64,556** | **truncated** |

**A byte threshold cannot discriminate.** The cut point is a property of the retrieval channel's budget on the day. **Rule 1 is RETIRED as a predicate.** ✅ **Rule 3 — does the final row terminate cleanly — caught both, and is now the primary predicate.**

**The consequence is bounded and stated in the capture file:** the file is ordered by member state and stops inside the **IE** block, so **IT, LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK are outside the capture.** Malta and the Netherlands — the two most likely to matter for this cohort — are among them. **No absence claim may be derived from this file.** Positive hits stand.

**3. 🟢 `scripts/verify-capture.py` SHIPPED — AND IT WAS THE THING THAT MADE §2 A FINDING RATHER THAN A NEAR-MISS.**

Recommendation 3 executed. Verdict `COMPLETE`/`TRUNCATED`/`SUSPECT`/`UNKNOWN`; exit 0 only on COMPLETE; prints `CLASS-3 ABSENCE CLAIM REFUSED` otherwise. **Discrimination verified both ways, at both historical cut points:**

| Input | Verdict |
|---|---|
| `_esma-ncasp-snapshot-2026-08-16.csv` | **COMPLETE**, exit 0 — 167 rows, md5 `31bffda0…` |
| `_esma-casps-snapshot-2026-08-17.csv` | **COMPLETE**, exit 0 — 329 rows, 161,380 bytes, md5 `69e7dc92…` |
| CASPS cut at the 08-17 cut point (82,445) | **TRUNCATED**, exit 1 — final row 4 of 16 fields |
| CASPS cut at the 08-20 cut point (64,556) | **TRUNCATED**, exit 1 — final row 1 of 16 fields |

**Side effect worth naming: the two COMPLETE runs independently reproduce the 08-17 record's own byte count, row count and md5.** That run's capture is now re-verified by an instrument that did not exist when it was written.

**4. 🔴 THE DAY-50 NULL IS NO LONGER AN ARTEFACT OF WHEN WE LOOK — ESMA REPUBLISHED THE REGISTER TWO DAYS AGO AND THE NON-COMPLIANCE FILE CAME BACK BYTE-STABLE.**

ESMA's MiCA page states **"Last update: 18 August 2026."** `NCASP.csv` re-fetched today: **167 rows, unchanged; newest `ae_decision_date` still 22/07/2026; newest `ae_lastupdate` still 31/07/2026; still 3 authorities (CONSOB 165 / AFM 1 / NBS 1); `ae_infrigment = No` on 167 of 167.**

Through day 47 the null was *"we looked and found nothing"* — vulnerable to the objection that an absence found on the observer's schedule can be an artefact of that schedule. **That objection is now closed for this window. The publisher refreshed the record on its own cycle and the file did not move.** **Twenty-nine days without a new entry from any EU authority, across at least two publication cycles. Nineteenth consecutive EU-NCA zero on marketing grounds.** → `../regulator-filings/esma-ncasp-null-retested-against-republished-register-2026-08-20.md` (**NEW**).

**5. 🔴 BOTH OF TODAY'S CANDIDATE NET-NEW ITEMS WERE THE SAME DEFECT, IN TWO DIFFERENT CLASSES, AND BOTH WOULD HAVE *CONFIRMED* SOMETHING.**

- **Class 4.** A headline reading **"Crypto.com names new CMO"** — which, if real, breaks the six-run appointment null at a tracked firm. Fetched: **published 12 August 2020**, announcing **Steven Kalifowitz** — the man whose 2026 departure is already a corpus file.
- **Class 5.** The aggregator's `*** HIGHEST-VALUE UNHELD ROW ***`, `Coinbase 2026-03-05 −18%`, flagged 08-07 as potentially meaning *"the corpus's Theme-5 spine is built on the second cut, not the first."* **Resolves to 14–15 June 2022**, on two capturing sources that carry the true date inside their own URL paths.

**Same mechanism: a pre-window article surfacing in a window-scoped search, with nothing in the result marking it stale.** Watch (u)'s four mechanisms are all *entity* errors. **This is a *date* error — the entity, the event and the figure are all correct — and every one of the six source classes is date-keyed.** Worse: **both would have resolved an open question, and a false item that confirms is not scrutinised the way a surprising one is.** → `../operator-statements/_stale-article-as-current-signal-instrument-2026-08-20.md` (**NEW**), `../layoff-tracker/_candidate-adjudications-2026-08-20.md` (**NEW**).

✅ **Consequence: the Theme-5 spine is NOT at risk.** Coinbase's 2026 event is the 05-05 −14% round, as row 4 holds it. **A doubt carried unresolved for thirteen days closed in one search.**

**Class 3: +2 at-source captures, +1 instrument (script), +1 register re-read. Class 4: 0 net-new, seventh consecutive recall confirmation, null HOLDS. Class 5: 0 promotions, 1 refusal, 1 `[VERIFY]` closed, tracker holds at 25. Class 1: 0 net-new, guard-certified, but see §1 below — the delta went NEGATIVE for the first time.**

---

## Six-class audit trail

### 0. The retry-queue seed — one line, as instructed

**Did not arrive.** No URLs in the scheduled-task prompt. Watch (jj) unexecutable for a **seventh** run; **not re-issued** per the 08-13 ruling. Escalation (i) stands. Moving on.

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0 — guard-certified, fifth consecutive run.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-08-20
source A (jobs)   scan_date: 2026-08-20
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-19T21:52:06Z, age=14.3h,
             fingerprint total_jobs_fetched=2186, delta=-12 vs 2026-08-17 (2198))
  reason: age 14.3h, fingerprint delta -12
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

**🆕 THE FINGERPRINT DELTA IS NEGATIVE FOR THE FIRST TIME: −12 (2,198 → 2,186).** Five-observation series: **+24, +4, +16, +3, −12.**

**The guard passed it, and passing it is correct.** Its zero-delta predicate exists to detect a scan that *did not run*; a file that changed by −12 unambiguously ran. **But the guard was written with an implicit assumption that the fingerprint is monotonic, and that assumption is now false.** A shrinking `total_jobs_fetched` means the upstream ATS scan is seeing **fewer** open roles than it did — postings closing faster than new ones open. On a report whose Theme 5 is the contraction of the marketing function, **a negative delta in the hiring feed is potentially substantive rather than merely operational.**

⚠ **It is NOT read as substantive today, for two reasons stated plainly.** First, **n=1**, and the delta spans **three calendar days** rather than one because 08-18 and 08-19 did not run — so it is not comparable to the four single-day observations before it. Second, `total_jobs_fetched` counts **all** roles the scan retrieves, not marketing roles, so it cannot bear a marketing-specific reading at all. **Recorded as an observation and a watch. No trend claimed.**

**`fetch_errors`: unchanged. OKX (Tier-1), Securitize, Rabby, Relai still absent from the upstream company list — SIXTEENTH run.** Watch (x) stays REOPENED. **Aave: sixteenth consecutive fetch error.**

### 2. Agency claims / overlap matrix (deterministic)

18 files rewritten; 8 matrix rows; **1 OVERLAP: Sui (coinbound, rzlt)** — unchanged. `trend-data.json` `lastUpdated` still **2026-06-15**: **66 days stale.** Class-2 output byte-identical for a **tenth** consecutive run. **`methodology.md` §6's phrase *"daily 18-agency panel"* remains inaccurate as written — SIXTEENTH run.** No trend claim made from this panel today.

### 3. Regulator — **+2 AT-SOURCE CAPTURES, +1 GUARD SCRIPT, +1 REGISTER RE-READ.**

**3a. `OTHER.csv` — mandate item 2, executed, and it is the run's headline.** Full detail in the capture file. The URL was **read from ESMA's own MiCA page**, fetched first-party this run, which lists all five register files by name and link — **not pattern-guessed from the `CASPS.csv` path**, which would have produced the right answer for the wrong reason.

Eleven source data-quality defects logged uncorrected, including: **records spanning multiple physical lines via unquoted newlines** (which is why the record count is stated as ~230 rather than exactly); **a leading tab inside a quoted `ae_DTI_FFG`** — the same whitespace-in-a-grouping-key defect that produced 08-17's own "4 authorities" error; **one `ae_DTI_FFG` reused across two different tokens** (`KK12JMBTX` on both toncoin and gram); **four different separators inside one column** including a stray `>`; **a record dated 02/12/2026**, over three months after capture; **`wp_url` values that are not URLs** (`N/A`, a bare filename, an empty value); **two near-duplicate entities one letter apart under the same LEI** (`The Horizen Foundation` / `The Horizon Foundation`); **an exact duplicate row** (VeChain ×2); and — **the one worth carrying to Phase 2** — **20+ comment fields reading *"note that the publication date for the white paper is DD.MM.2026 at which point this record will be updated with the link,"* several of them months past. The register records an intention to publish as though it were a publication.**

**3b. `NCASP.csv` re-read — the null tested against a register newer than our last look.** §4 above; detail in the re-read file. **`CASPS.csv` was deliberately NOT re-fetched**, so the 08-17 CONSOB/BaFin authorisation inversion is **not restated** — its denominator may have moved and no claim is made either way.

**3c. MAS — the time-box is spent. Recorded as NOT ADMITTED and closed.** Recommendation 5 allowed one further attempt. **It was not made, and that is a deliberate choice rather than an omission**: four instruments have failed on that document across three runs, the run's regulator budget went to two register files that returned data, and **operating discipline 4 — every ambiguous bet gets a kill date — applies to corpus items.** **The MAS digital-advertising guidelines ship as NOT ADMITTED, with the four-instrument failure ladder in `_mas-digital-advertising-guidelines-provenance-2026-08-16.md` as the citation.** The disputed *25 March 2026* effective date remains **refused** — three secondaries, no primary. **Do not re-open. This is a closure, not a carry.**

**NOT REACHED, NOT GUESSED:** the complete `OTHER.csv` (**now the oldest live item — see recommendations**) · `ARTZZ.csv` · `EMTWP.csv` · `CASPS.csv` at its 18/08 version · any of the ~230 `wp_url` white-paper documents · Bitpanda's VSN white paper · Crypto Risk Metrics GmbH's corporate filings · the AFM MEXC warning page · the CONSOB post-deadline notice bodies · the NBS LWEX notice · the ESMA 2026-02 statement PDF · the ESMA finfluencer-factsheet CANDIDATE from 08-11 (**8th refusal, still undated**) · VARA notice bodies · `rulebooks.vara.ae` · the retry-queue URLs · `ascendex.com` · the NPR and Business Standard 2022 Coinbase articles at source · `hello@northpoint.fi`. **No URL was fabricated.**

### 4. Operator statements — **0 NET-NEW ADMITTED. Seventh consecutive recall confirmation. The one hit that looked like it broke the null was a 2020 article.**

**3/3 recall on named cohort seats:** Binance/**Rachel Conlan** CMO departure with **Eowyn Chen** interim (held); Crypto.com/**Steven Kalifowitz** stepping down after almost six years, effective 2026-06-30 (held); Coinbase/**Catherine Ferdon** as CMO (held).

**The "Crypto.com names new CMO" result is adjudicated in §5 above and in the instrument file. Published 12 August 2020. Not admitted.**

**No 2026 appointment to any TRACKED firm's top marketing seat is publicly visible — seventh consecutive run. Clock advanced: ten weeks after Binance's CMO departure and seven weeks after Crypto.com's took effect, neither firm has publicly named a permanent successor.**

The **Fireblocks / Michal Ferguson** perimeter appointment carried from 08-17 is **still carried, still not admitted, still not fetched at source.**

### 5. Layoffs — **0 PROMOTIONS. TRACKER HOLDS AT 25. One high-consequence refusal, one `[VERIFY]` closed.**

Full adjudications in `../layoff-tracker/_candidate-adjudications-2026-08-20.md`.

- **🔴 REFUSED — `Coinbase 2026-03-05 −18%`.** The aggregator's highest-value unheld row, carried since 08-07. **Resolves to 14–15 June 2022.** §5 above. **The Theme-5 spine is not at risk.**
- **✅ CLOSED — the FalconX `[VERIFY]` opened 08-17** (10% vs 11%, reported vs confirmed). **Resolved in favour of row 18 as written, from the row's own already-captured source** (`en.cryptonomist.ch/2026/08/04/falconx-crypto-layoffs/`, *"reportedly cut around 10%"*). **Both disputed elements resolve to the row.** The 08-17 ruling — *a search summary does not overwrite a first-party-captured row* — is vindicated on its first test.
- **MANTRA (row 25)** independently restated today; **held**, no amendment.
- **Crypto.com (row 1)** — a net-new **180 headcount** detail surfaced. **NOT entered**; it arrives from a secondary aggregation page not fetched first-party. `[VERIFY]` **opened**.
- **Industry denominator moved** — CryptoJobsList now self-reports **>7,254 cuts across 47 companies**, and **894 disclosed positions across 12 firms in July 2026 alone**. **Recorded, not adopted**; the 08-17 note that this aggregator disagreed with itself (n=47 vs n=54) is unresolved and today's figure sits on the n=47 side. **No ratio restated.**
- **Gnosis `[VERIFY]`** — 16th run carried, blocked by watch (jj). **AscendEX** — sixth consecutive non-promotion.

**SCOPE DISCIPLINE, DO NOT ELIDE: the cohort-scoped standing finding — *no TRACKED firm's 2026 contraction has named marketing as an affected function* — HOLDS.** Two of 25 rows name marketing (Gnosis, MANTRA); **both perimeter; zero tracked.** **The non-AI-rationale streak extends to thirteen runs.** Watch (h′) remains REJECTED and untested. Do not print.

### 6. NorthPoint longitudinal panel

`trend-data.json` **66 days stale**. **No trend claim made.**

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged. Not touched today; `CASPS.csv` deliberately not re-fetched.
- **(b) First named post-deadline NCA marketing-side action** — **🟢 STRENGTHENED IN KIND, NOT JUST IN CLOCK. Day-50, nineteenth consecutive EU-NCA zero — and for the first time the null survives a republication of the register by its own publisher rather than another pass by us.** The companion sentence gains a fifth clause: not guidance silence, not inaction silence, not for want of a regulated population — **and not an artefact of our observation cadence.**
- **(d) Agency panel staleness — 66 days**, byte-identical output ten runs running. **16th run.**
- **(e′) Cadence** — **🔴 BROKEN. Three-day gap; 4 of 8.** 08-19 accounted for by the portfolio outage; **08-18 unaccounted and not explained away.**
- **(f) Friday nomination cadence** — not testable today (Thursday). Failed 08-14. Escalation (ii) unchanged.
- **(g) Coinbase n=1** — **🟢 DEFENDED RATHER THAN ADVANCED.** The n=1 nearly became a disputed n=2 today. **It did not, and the reason it did not is a date check.**
- **(h′) Layoff rationale correlates with firm type** — **REJECTED. Untested.** Thirteen-run non-AI streak. Do not print.
- **(j) Senior-leader exits** — **ADVANCED IN CLOCK ONLY**, seventh consecutive run. The one apparent break was a 2020 article.
- **(k) Chrome-lane instrumentation gap** — **not exercised today.** Unchanged from its 08-17 REGRESSED state.
- **(l) §4 too narrow AND provenance-blind** — **17th costing.** Definitional half holds a sixth run; **recommendation to close it as SETTLED repeated.** Provenance half live under (jj).
- **(n) Full-range re-sweep of classes 3, 4, 5** — **🟢 FIFTH CONSECUTIVE VINDICATION, in an unusual shape.** Class 3 produced the headline. **Classes 4 and 5 produced zero admissions and were still the most valuable half of the run**, because what they produced was a refutation of a thirteen-day-old doubt and a named defect mechanism. **A sweep that admits nothing is not a sweep that found nothing.**
- **(o) Date the document, never an event held about it** — **🔴 EXTENDED AND PROMOTED.** New clause: **date the document, never the page it is rendered on.** Two instances today, in two classes. See the instrument file.
- **(pp) A clean parse is not a complete capture** — **🟢 DISCHARGED AS A WATCH, CONVERTED INTO A SCRIPT — AND ITS FIRST RULE WAS WRONG.** `scripts/verify-capture.py` implements rules 2–4 and **retires rule 1**, the byte-threshold heuristic, which `OTHER.csv` falsified at 64,556 characters. **The watch closes; the script inherits it.** Rules 2 (record byte count + md5) and 4 (never derive an absence claim about a named entity from an unverified capture) are now enforced by exit code rather than by discipline.
- **🆕 (rr) 🔴 THE CLASS-1 FINGERPRINT WENT NEGATIVE AND THE GUARD HAS NO OPINION ABOUT DIRECTION.** Series **+24, +4, +16, +3, −12**. The zero-delta predicate is a liveness test and it worked. **But a shrinking upstream job count is potentially a Theme-5 signal rather than an operational one, and nothing in the pipeline is watching for that.** Two reasons it is not read as substantive today: **n=1**, and **the delta spans three calendar days** because of the cadence break, so it is not comparable to the four single-day observations. **Also: `total_jobs_fetched` counts all roles, not marketing roles, so it cannot bear a marketing-specific reading at all.** **Action for a future run: if the direction is to mean anything, the fingerprint needs a marketing-role-scoped companion counter.** Recorded; **no trend claimed.**
- **🆕 (ss) 🔴 A FALSE ITEM THAT CONFIRMS IS NOT SCRUTINISED THE WAY A SURPRISING ONE IS.** Both of today's refused items would have **resolved an open question** — one closing a seven-run null, one supplying a bigger and earlier version of an existing finding. **The 08-07 crossref filed the Coinbase row as *high-value*, not as *implausible*, and carried it thirteen days on that basis.** The corpus has good defences against implausible claims and **no defence at all against welcome ones.** Rule adopted: **when an item would close an open question or strengthen an existing finding, date it first and read it second.**
- **Unchanged and not re-narrated today:** (c), (i), (m), (q), (r), (s), (t′)/(dd), (u), (v), (w — CLOSED, do not reopen), (x), (y), (z — CLOSED), (aa), (bb)/(ff — CLOSED), (cc), (ee), (gg), (hh), (ii), (jj), (ll), (mm), (oo), (qq).
- **(mm) A rendering of the record is not the record** — **🟢 GENERALISED A SIXTH TIME, and today it generalised past *records* entirely.** It has now covered derivative trackers, partial captures, and — via (o)'s new clause — **a publisher's page furniture standing in for an article's date.** Still the most productive single line in this repo.
- **(oo) The "not fetched, not guessed" list is a work queue** — **🟢 THIRD CONSECUTIVE PAYOUT, and it paid on both lists again.** `OTHER.csv` came off the not-fetched list and produced the headline; the Coinbase row came off the candidate list and produced a refutation worth more than a promotion. **Standing rule confirmed, twice tested, keep running it.**

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **HEALTHY, age 14.3h, fingerprint 2198 → 2186, delta −12 vs 2026-08-17. First negative delta observed.**
2. Repo dedup pass: 08-17 record in full; four root docs in full; `csv.DictReader` over all 25 tracker rows; both aggregator crossrefs in full; `corpus/` + `findings/` indexes; the committed NCASP snapshot parsed, authority-counted with whitespace normalisation, and re-verified.
3. WebSearch (domain-restricted `esma.europa.eu`) — interim MiCA register white-paper file → surfaced the MiCA landing page and the field-description CSV.
4. **`web_fetch` the ESMA MiCA page → 200, full body. Source of the `OTHER.csv` URL, and of the register's stated "Last update: 18 August 2026."** All five register file links read from the page; none constructed.
5. **`web_fetch` `esma.europa.eu/sites/default/files/2024-12/NCASP.csv` → 200, `text/csv`. Structural check: header present, final row terminates cleanly, tail byte-identical to the committed 08-16 snapshot. 167 rows, unchanged.**
6. **`web_fetch` `esma.europa.eu/sites/default/files/2024-12/OTHER.csv` → 200, `text/csv`, 64,556 chars / 241 lines. TRUNCATED — final row cut mid-URL inside a CBI record. Detected by the final-row check, not by the byte heuristic.**
7. Full read of the captured `OTHER.csv` body in three chunks; exact-string counts for `Crypto Risk Metrics GmbH` (**127**) and for tracked-exchange identities (**12**); every cohort hit adjudicated by hand and assigned to its column (issuer vs admitting CASP).
8. **Built `scripts/verify-capture.py`; ran it on both committed register snapshots (COMPLETE, exit 0) and on two synthetic truncations of the CASPS snapshot at the real 08-17 and 08-20 cut points (TRUNCATED, exit 1, final row 4/16 and 1/16 fields).** Discrimination verified both ways. **The 08-17 CASPS capture is re-verified as a side effect — 329 rows, 161,380 bytes, md5 `69e7dc9…`, matching that run's own record.**
9. WebSearch — crypto marketing-communications enforcement August 2026 across ESMA/BaFin/AMF/CONSOB → **no net-new named marketing-side action.** Returned only material the corpus already holds (the 165/167 CONSOB concentration, the ESMA finfluencer factsheet / CONSOB amplification, the wind-down statement).
10. WebSearch — crypto CMO / head-of-marketing appointments August 2026 → **3/3 recall on cohort seats; one apparent net-new appointment at a tracked firm surfaced.**
11. **`web_fetch marketing-interactive.com/cryptocom-names-new-cmo` → 200, full body. PUBLISHED 12 AUGUST 2020.** Announces Steven Kalifowitz's own hire. **Not admitted. Basis for the instrument note.**
12. WebSearch — crypto layoffs August 2026 marketing team → FalconX **"around 10%"** (closes the 08-17 `[VERIFY]` in favour of row 18) · MANTRA marketing-naming restated · Crypto.com 180 roles (`[VERIFY]` opened) · denominator now >7,254 across 47 firms.
13. WebSearch — Coinbase March 2026 −18% → **the aggregator's highest-value candidate refuted.** Only −18% event on record is 2026… **is 2022-06-14/15**, date-stamped inside two capturing sources' own URL paths. Business Standard observed serving that 2022 article under a `January 07, 2026` dateline.
14. **MAS: deliberately not attempted.** Time-box spent; see §3c. **Closed as NOT ADMITTED, not carried.**
15. **Not reached / not guessed:** see the §3 list. **No URL was fabricated.**

---

## Net-new / changed this run

- `corpus/regulator-filings/esma-other-whitepaper-register-partial-capture-2026-08-20.md` — **NEW. The run's headline.** `OTHER.csv` at source: the **127-of-~230 Crypto Risk Metrics concentration**; the **seven tracked foundations + Cronos filed under a third party's name**; the **twelve tracked-exchange rows, eleven of them in the admitting-CASP column**; **Bitpanda as the only tracked firm appearing as an issuer in its own name**; the truncation, its bounded consequence, and the retirement of the byte-threshold rule; **eleven source defects logged uncorrected**; six explicit non-claims; a three-item work queue.
- `corpus/regulator-filings/esma-ncasp-null-retested-against-republished-register-2026-08-20.md` — **NEW.** The day-50 null re-tested against a register ESMA republished on 18 August; **167 rows unchanged, twenty-nine days without a new EU entry**; both limits (notification-not-enforcement; the field cannot express the finding) restated attached; register-cadence third observation.
- `corpus/operator-statements/_stale-article-as-current-signal-instrument-2026-08-20.md` — **NEW.** The two date-collision instances, the shared mechanism, why a date error is worse for this corpus than the four entity mechanisms on watch (u), and four rules adopted.
- `corpus/layoff-tracker/_candidate-adjudications-2026-08-20.md` — **NEW.** The Coinbase refusal in full; the FalconX `[VERIFY]` closed in favour of row 18; MANTRA held; Crypto.com 180-headcount `[VERIFY]` opened; denominator recorded not adopted; scope discipline restated.
- `scripts/verify-capture.py` — **NEW.** Class-3 capture guard. Verdict + exit code; primary predicate is final-row termination; byte heuristic retired to a note; `--expect-rows` cross-check; `--json`.
- `scripts/README.md` — **UPDATED.** New `verify-capture.py` section with the discrimination table and the retirement of the size heuristic; daily task ordering gains step 3 (verify before deriving).
- `findings/longitudinal-2026-06.md` — day-50 shift appended.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv`, `_feed-fingerprint.json`, `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — date re-stamps / byte-identical rewrites (sync, 10th run).
- **Deliberately NOT committed: a snapshot of the truncated `OTHER.csv`.** The 08-17 precedent commits raw register CSVs so figures are recomputable — **but committing a known-incomplete register as a corpus artifact is the exact failure that instrument was written about.** The derived, hand-adjudicated extract is committed instead, with the truncation, the char count and the exact retrieval provenance disclosed, and **re-fetching the complete file is the top item on the next run's work queue.**

---

## Recommendation for next run

1. **🟢 RE-FETCH `OTHER.csv` COMPLETE, AND RUN `verify-capture.py` ON IT BEFORE READING IT.** It is now the oldest live item on the not-fetched list and the only thing standing between the corpus and an absence-capable read of the EU white-paper register. **Malta and the Netherlands are the member states the current capture cannot see, and they are the two most likely to matter for this cohort.** If `web_fetch` truncates again, the escalation is a chunked or ranged retrieval — **not** a second full attempt.
2. **🟢 KEEP RUNNING WATCH (oo) ON BOTH LISTS. Three consecutive payouts.** Oldest live entries: **`ARTZZ.csv` / `EMTWP.csv`** on the not-fetched list, and on the candidate list **AscendEX** — sixth carry, still *"the only 2026 aggregator row whose stated reason is 'Regulatory', and an exchange shutdown nine days after the MiCA deadline."*
3. **🔴 RUN THE NEW DATE CHECK ON THE CORPUS'S EXISTING ROWS, NOT JUST ON NEW ONES.** Today's two refusals were both caught at intake. **Nothing has audited what was admitted before the check existed.** Every class-4 and class-5 row should be swept for whether its publication date was read from the fetched artifact or inherited from a search result. **This is the cheapest remaining integrity win before Sep 1**, and it is the same argument watch (oo) won twice.
4. **Do NOT re-issue the retry queue. Do NOT re-open MAS.** Seventh run on the first; the second is now formally closed as NOT ADMITTED. One line each, move on.
5. **Escalate to Jukka — six items, in order:**
   - **(i) 🔴 SEVEN RUNS OLD. Watch (jj).** The scheduled-task prompt still cannot pass URLs into a run's provenance set. **AscendEX** (sixth carry), the retry queue, and the Gnosis `[VERIFY]` are all blocked by this one thing. **Fix: paste the queue's URLs verbatim into the task prompt.** One edit, three items unblocked. Unchanged for seven runs.
   - **(ii) 🔴 THE README'S FRIDAY PROMISE FAILED 08-14 AND IS NOW SIX DAYS PAST ITS TEST DATE.** *"Inbound nominations are read every Friday."* No access to `hello@northpoint.fi`; `inbound-nominations.md` does not exist. **Route the mailbox into a readable artifact, or amend the sentence before Sep 1.** Still the only open item with a third party on the other side.
   - **(iii) 🟢 THEME 1 HAS A NEW SPINE SENTENCE, AND IT IS BETTER THAN THE ABSENCE IT REPLACES.** *Under MiCA, marketing communications must be consistent with the crypto-asset white paper. In the captured portion of ESMA's register of those white papers, 127 of ~230 records — roughly 55% — were filed by a single German company, Crypto Risk Metrics GmbH, for tokens it does not issue. Those tokens include Sui, Uniswap, Aptos, Arbitrum, Avalanche, Algorand, Polygon and Cronos. Not one of the tracked foundations appears as the filer of its own token's EU disclosure document.* **Ship the Article-4 limit in the same paragraph** — third-party notification is expressly permitted, this is a visibility finding and not a compliance one — **and ship the capture limit too: absences cannot be claimed from a partial file.**
   - **(iv) 🔴 THE CADENCE BROKE FOR THREE DAYS AND ONLY ONE OF THEM HAS AN EXPLANATION.** 08-19 is covered by the portfolio-wide night-factory outage. **08-18 is not, and nothing in the repo or the scheduler record accounts for it.** With **twelve days to ship**, a silent two-day corpus gap is the failure mode most likely to matter. **Worth one look at the scheduler.**
   - **(v) 🟢 THE STRONGEST VERSION OF THEME 4 IS NOW A NEGATIVE THAT SURVIVED SOMEONE ELSE'S PUBLICATION CYCLE.** *ESMA republished the interim MiCA register on 18 August 2026. Its consolidated register of non-compliant crypto-asset service providers came back with the same 167 entries it held on 16 August, the same newest decision date of 22 July, and the same zero marketing-communications actions — twenty-nine days without a new entry from any EU authority.* **This is materially harder to dismiss than "we looked and found nothing," and it costs one fetch a week to keep true.**
   - **(vi) 🔴 `methodology.md` STILL NEEDS SIX SECTIONS REWRITTEN: §1, §3, §4, §5, §6, §7 — SIXTEENTH run for §1.** §6's *"daily 18-agency panel"* now describes a file **66 days stale**. **§3 gains two requirements today:** the white-paper register must be named as a class-3 instrument alongside the authorisation and non-compliance halves, and **`verify-capture.py` must be named as a mandatory pre-derivation step.** **Still the one thing in the repo that could embarrass the report.**

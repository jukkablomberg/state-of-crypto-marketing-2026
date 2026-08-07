# Corpus-assembly daily run — 2026-08-07 **(day 37 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-07 (**Friday**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, verbatim from the 08-06 recommendations:** (1) reach ESMA by a route that is not the news index, **and validate any new route against the two known items before trusting a null from it**; (2) 08-09 time-to-teardown measurement (scheduled, not today); (3) fetch PSN08; (4) test watch (z) across the panel **or kill it explicitly**; (5) implement the schema (watch aa + cc); (6) escalate five items.
**Dedup baseline read before writing:** `2026-08-06-corpus-run.md` in full; `layoff-tracker/2026-layoff-tracker.csv` all 19 rows in full; `regulator-filings/` (16 files, index); `operator-statements/` (5); `marketing-campaigns/` (10); `job-postings/` all 13 firm CSVs in full + `_absence.csv`; `open-positions.json` `scan_metadata` + all 29 filtered roles + `fetch_errors` + `top_picks`; `findings/` index.
**CADENCE: HEALTHY.** 08-05, 08-06, 08-07 — three consecutive on-time runs. Last gap 08-04. **Watch (e′) is discharged.**

---

## Headline result

**Three things, in descending order of consequence.**

**1. The structural leg of the thirty-seven-day null is no longer an inference. ESMA's own sanctions page enumerates what ESMA may sanction, and CASPs are not on the list.** Six entity classes named — CRAs, Securitisation Repositories, Trade Repositories, Tier-2 TC-CCPs, Benchmark Administrators, DRSPs. **No crypto. No CASPs. No MiCA.** For eleven runs the corpus has read the enforcement absence as *perimeter-shaped* and sourced that reading to the *shape of the absence itself*. It is now sourced to the regulator's own statement of its powers. → `../regulator-filings/esma-sanctions-perimeter-casp-absence-2026-08-07.md` (NEW FILE).

**2. Watch (n) stopped being a suspicion and became a number: the corpus holds 19 of 54 rows — 35% recall — against a single public layoff aggregator that has been continuously available all year.** Not a new instrument, not a new theory: the tracker the corpus *already cites as a source on one row* lists 54 crypto contractions for 2026 across 50 companies. **Six of the 35 unheld rows name TRACKED Stratum 1–2 firms**, including a **Coinbase −18% on 2026-03-05** two months before and larger than the 05-05 round the report's Theme-5 spine is built on. Nothing promoted; every candidate written down with its own `[VERIFY]`. → `../layoff-tracker/_aggregator-crossref-2026-08-07.csv` (NEW FILE).

**3. Class 1 cannot measure time-to-fill, and today it can be proved rather than suspected.** `first_seen` is **re-stamped to the scan date on every scan** — all 29 filtered roles read `first_seen: 2026-08-07`, *including the 27 the feed itself labels `STILL_OPEN` / "still open from prior scans."* `days_open` is `None` on every row. And the fallback field drifts: for **fixed requisition IDs**, `posted_at` moved **Coinbase gh_jid=8054862 07-17 → 07-20** and **Gemini gh_jid=8091954 07-29 → 07-30** between the corpus's own capture and today. Both moved *forward*. **Time-to-fill — one of the five fields `methodology.md` §1 promises to extract — is not derivable from this feed, and any age computed from `posted_at` is biased downward on every refreshed requisition.**

**Day-37 named marketing-side enforcement silence HOLDS** — and its explanation is now three-legged and fully primary-anchored.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0 — a genuine absence, guard-asserted.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-08-07
source A (jobs)   scan_date: 2026-08-07
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-06T22:40:57Z, age=13.4h,
             fingerprint total_jobs_fetched=2139)
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

**Watch (bb) passes a second time and earns its keep.** Age **13.4h** (HEALTHY, threshold 36h) and the fingerprint moved **2,090 → 2,139 (+49)** with `total_jobs_after_filter` **28 → 29**. The scan ran, looked at 49 more postings than yesterday, and admitted no net-new tracked-cohort marketing role. **That is an absence the corpus is entitled to claim.**

#### 🔴 THE RUN'S CLASS-1 FINDING: the feed's two date fields cannot support time-to-fill, and both failure modes are measured

**(a) `first_seen` is a re-stamp, not a first-seen.**

```
distinct first_seen values across all 29 filtered rows: ['2026-08-07']
```

Every row carries today's date. **27 of those rows sit under the key `still_open_from_prior_scans` with `status: "STILL_OPEN"`.** A row cannot be *first seen today* and *still open from prior scans*. `days_open` is `None` on all 29. Yesterday's run read `first_seen 2026-08-05` on all 28 rows and treated it as a real observation date; it was the 08-05 scan date. **The field has never meant what it says.**

**(b) `posted_at` drifts forward for a fixed requisition ID.** Checked against the corpus's own captured rows, by `gh_jid` / Ashby UUID:

| Requisition | Corpus `date_posted` (captured) | Feed `posted_at` today | Δ |
|---|---|---|---|
| Coinbase Creative Director `gh_jid=8054862` | 2026-07-17 (captured 07-18) | **2026-07-20** | **+3d, forward** |
| Gemini Predictions Partnerships Marketing Lead `gh_jid=8091954` | 2026-07-29 (captured 07-30) | **2026-07-30** | **+1d, forward** |
| Phantom Head of Brand Creative `815cacde…` | 2026-07-01 | 2026-07-01 | stable |
| Kraken Director, Paid Marketing (US) `5e07a439…` | 2026-07-23 | 2026-07-23 | stable |
| Kraken Director, Paid Marketing (UK) `f0b3a00e…` | 2026-07-23 | 2026-07-23 | stable |

**2 of 5, both forward.** This is ordinary ATS behaviour — a refreshed or edited requisition re-stamps — but the consequence for the report is not ordinary.

**Concretely, and this is the part that would have shipped:** the 08-06 run printed *"Gemini's Predictions role 8 days [open]"*. Today the role is one day older and the derived age is **still 8 days**, because `posted_at` advanced with the calendar. **A requisition that is refreshed weekly registers as permanently young.** Time-to-fill computed this way understates duration on exactly the roles that are hardest to fill — the ones being refreshed.

**Consequences, stated as rules rather than notes:**
- **No time-to-fill figure may be printed from class 1.** Not from `first_seen` (meaningless), not from `posted_at` alone (biased downward, unquantifiably).
- The corpus's `captured_date` column **is** a real first-observation date and is the only honest floor available: "open on or before *captured_date*, still open on *today*." That is a **minimum** duration and must be labelled one.
- **This strengthens escalation (ii), the §1 re-scope, for the seventh run.** §1 promises "time-to-fill" among five extracted fields. Four of the five are supportable. This one is not, and now it is measured rather than doubted.

**Feed-health note, adjacent:** `fetch_errors` is non-null again with **7 entries** — Wormhole Foundation, **Aave (tracked; Lever 404)**, Injective Labs, Bitwise, Chainlink Labs, Elliptic, B2C2. **Watch (x) was closed on 08-06 as "fetch_errors null"; that closure was a snapshot, not a property. REOPENED.** Six of the seven are non-cohort; Aave's is the same 404 the absence panel has carried for seven runs.

**Where the +49 went, checked rather than assumed:** the 29 filtered roles are dominated by **non-cohort AI labs** (Anthropic ×7, Perplexity ×3, Cohere ×3) plus tracked-adjacent already-held rows (Coinbase, Gemini, Phantom, Kraken ×2) and non-cohort crypto (Paxos Head of Communications, Chainalysis VP Marketing, Monad, Blockstream, Immutable ×2, CoinTracker, Tempo). **All correctly deduped by `source_url`. Zero cohort admissions.**

#### Absence panel — four upstream gaps unfixed for a **seventh** run
`_absence.csv`: Aave (Lever 404) + Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys (proprietary, chrome-pending). **OKX (Tier-1), Securitize, Rabby, Relai remain missing from the upstream company list.** No config write attempted — the sales funnel is a different repo. **Seventh run. It needs an owner outside the corpus run** — and today's class-5 work sharpens why: **OKX appears in the layoff aggregator with a January 2026 contraction while being invisible to the class-1 instrument entirely.**

### 2. Agency claims / overlap matrix (deterministic)

18 agency-claims files rewritten; 8 matrix rows; **1 OVERLAP: Sui (coinbound, rzlt)** — unchanged.

**Measured this run and worth recording: the 18 rewritten files and the matrix are BYTE-IDENTICAL to yesterday's.** `git status` after the sync shows only `_absence.csv` and `_chrome-queue.csv` modified — i.e. the two files whose only change is a date re-stamp. The class-2 corpus has not moved in **53 days**. `trend-data.json` `lastUpdated` still **2026-06-15**. Watch (d) stable-by-decision; `methodology.md` §6's phrase *"daily 18-agency panel"* remains inaccurate as written. Escalation stands, **seventh run**.

### 3. Regulator — **1 NET-NEW FILE. The mandate's ESMA route hunt ran and mostly FAILED, which is the honest result. MAS PSN08 attempted and unreachable.**

#### (a) ESMA's sanctioning perimeter — the run's principal result
→ `../regulator-filings/esma-sanctions-perimeter-casp-absence-2026-08-07.md` (NEW).

Three ESMA pages fetched first-party, HTTP 200 each, no relay. The **Sanctions and Enforcement** page enumerates ESMA's direct sanctioning perimeter verbatim:

> "As the single supervisor for Credit Rating Agencies (CRAs), Securitisation Repositories (SRs), Trade Repositories registered under EMIR and/or SFTR (TRs), Tier 2 Third-Country Central Counterparties (Tier 2 TC-CCPs), EU Critical Benchmark Administrators and Recognised Third-Country Administrators (Benchmark Administrators) as well as Data Reporting Service Providers (DRSPs) in the EU, ESMA has responsibilities and powers to deal with possible infringements."

**Six classes. CASPs absent.** Corroborated by the **Investigations and Inspections** page, whose "Perimeter monitoring" is scoped to credit ratings only — verbatim, *"ESMA seeks to identify companies that are providing credit ratings without having registered with ESMA … via Internet searches"*. **ESMA runs exactly the instrument a marketing-side crypto sweep would need, and points it at CRAs.**

**Phase-2 effect:** leg 1 of the three-part wording (structural / prioritisation / forbearance) upgrades from *inference* to *citation*. **Never print "silence." Print the mechanism.**

#### (b) The mandate's instrument-validation practice, applied — and it disqualified the route it found
The 08-06 standing rule: *an instrument may not produce an absence claim until it has been shown to detect a known presence.* Known presences: **23 June 2026** Public Statement (ESMA75-113276571-1710) and the **8 July 2026** Common Supervisory Action.

- **MiCA activities page** (`/esmas-activities/digital-finance-and-innovation/…-mica`), HTTP 200: **detects NEITHER.** Its document table's newest MiCA statement is Nov-2025; its "Statement on MiCA Transitional Measures" is the **2024-12** one. **FAILS validation. Carries no absence claim.**
- **`?sort_by=chronological`** — the obvious next attempt, explicitly named in yesterday's recommendation — **BLOCKED by the fetch tool's provenance rule. Not fetched. Not guessed. Still untried.**

**Watch (w) remains UN-DISCHARGED for ESMA.** Three routes, two runs, none passing. **Post-deadline days 1–8 remain uncovered.** The validation rule is doing its job: it cost this run a route it would otherwise have trusted.

#### (c) Register arithmetic — the 08-06 `[VERIFY]` gets a third, disagreeing date
The MiCA page stamps the interim register **"Last update: 31 July 2026"** with a stated *weekly* cadence. Against The Block's *"updated Aug 5"* (08-06) and NorthPoint's own primary CSV read showing `ac_lastupdate` to **04 Aug**. **Three sources, three dates, one register — the page-level stamp lags the files it links.** Operational rule written into the file: **cite the CSV and its `ac_lastupdate`, never the page stamp; never a figure without its snapshot date and de-dup rule.**

#### (d) MAS PSN08 — mandate item 3, ATTEMPTED, UNREACHABLE, NOT CLAIMED
`https://www.mas.gov.sg/regulation/notices/psn08-notice-on-disclosures-and-communications` fetched: **HTTP 200 with an empty body** — the identical failure mode as the PS-G02 landing page on 08-06 (that one was rescued by fetching the PDF directly; no PDF URL for PSN08 surfaced in search). **PS-G02 §2.2's carve-out therefore still has no yardstick.** Secondary descriptions of PSN08 were surfaced by search and **deliberately not used** — a notice's operative text is not quotable from a law-firm summary. Standing gap, unclosed, said plainly.

**NOT REACHED, NOT GUESSED:** ESMA `?sort_by=chronological` and index pages 3+ (provenance-blocked) · PSN08 operative text · MAS enforcement register · MAS DTSP licensing guidelines · **VARA, still never swept at source** · CONSOB comunicato PDFs · BaFin/CySEC/CNMV re-sweeps · FT originals (paywalled). **No URL was fabricated.**

### 4. Operator statements — **0 NET-NEW. Class 4 stays at 5 files. FOURTH consecutive run with a refusal on the role/format gate.**

The August sweep surfaced no in-window verbatim statement by a qualifying marketing operator at a tracked firm.

**The refusal, logged because the gate only means something when applying it costs something.** The Fintech Marketing Hub **Top 30 Most Influential Fintech Marketers 2026** list (fetched, HTTP 200) names marketing leaders at **two tracked firms**: **Mary-Kate Collins, Head of International Communications, Coinbase** and **Imo Bábics, Chief Growth Officer & CMO, Relai** (plus Paul Afshar, CMO, Paybis — non-cohort). **Refused for class 4** on three counts, none of them role: the entries are **third-party editorial bio prose, not first-party statements**; they carry **no date**; and there is **no verbatim quote from the operator**. §4 requires "verbatim quote + URL + speaker + date + role at time of statement" and this satisfies one of four.

**But it is not worthless and should not be discarded — it is a Theme-1 named-leadership datum**, and it independently corroborates `tracked-firms.md`'s Relai entry (Imo Bábics, ex-Bitpanda). Recorded here rather than filed, because the corpus has no home for "a tracked firm has a publicly named senior marketing leader" that is not class 4. **That gap is itself watch (l)'s point.**

**Class 4 has produced 1 item in 12 days. Watch (l), 8th costing.** The empirical case for widening §4 now runs to five consecutive runs: Mulvenny (08-03), the Coinbase spokesperson (08-05), Pontoizeau and Li (08-06), the Top-30 entries (08-07). **§4 is selecting for format and job title, not for evidentiary value.**

### 5. Layoffs — **0 rows promoted. 1 NEW CROSS-REFERENCE FILE. Watch (n) MEASURED for the first time: recall = 19/54 = 35%.**

→ `../layoff-tracker/_aggregator-crossref-2026-08-07.csv` (NEW). **`2026-layoff-tracker.csv` is UNCHANGED at 19 rows and that is deliberate.**

**What was done.** CryptoJobsList's 2026 layoff tracker was fetched first-party (HTTP 200, footer *"Updated August 2026"*) and cross-referenced row-by-row against the corpus's 19. It reports **54 rows / 50 companies / 7,294+ jobs** for 2026.

**Why this source and not a new one.** The corpus **already cites it** — the BitGo row's `source_url` *is* `cryptojobslist.com/crypto-layoffs`. It has been sitting in the repo as a citation on one row while never being read as a *census*. **Watch (n) has been carried for four runs as "the corpus does not know what it is missing." It could have known at any point by reading a page it already cites.**

**The number.** **19 of 54. 35% recall against one public source that requires no special access.** Watch (n) was four-for-four on *late, accidental* discoveries; it is now a measured recall rate, and it is the single most important honest figure this corpus has produced about itself, with Phase 2 days away.

**Six unheld rows name TRACKED Stratum 1–2 firms:**

| Firm | Agg. date | Agg. figure | Why it matters |
|---|---|---|---|
| **Coinbase** | 2026-03-05 | −18% | **Two months before, and LARGER than, the 05-05 −14% round the report's Theme-5 spine is built on.** Blockworks-sourced. |
| **Gemini** | 2026-03-10 | −30% | Bears directly on the corpus's open `-30% YTD [VERIFY]` — may resolve the 25%-vs-30% reconciliation or may be a re-report. |
| **Gemini** | 2026-04-07 | −40 / −5% | A *third* Gemini row; weakly sourced. |
| **Polygon** | 2026-01-15 | −60 / −30% | The corpus's Polygon Labs row already cites this as context and never made it a row. Cheapest promotion available. |
| **OKX** | 2026-01-09 | −10 / −33% | The Tier-1 firm class 1 cannot see at all. |
| **Bybit** | 2026-06-23 | −15 / −20% | **INTERNALLY INCONSISTENT — −15 at −20% implies a 75-person firm, and the source column is EMPTY. Recorded as a demonstration that the aggregator carries unvetted rows.** |

**Two rows corroborate existing corpus `[VERIFY]`s from outside:** **Ethereum Foundation** (the FalconX row flagged an undated, unsourced −20% claim on 08-05 and said "[VERIFY] before it is ever entered" — this supplies 2026-06-23, −54, first-party attribution) and **Block, Inc.** (day-of-month **2026-02-26** for a row whose exact day is explicitly open).

**One row creates a new conflict that makes an existing weak row weaker:** **FalconX** — the aggregator dates it **2026-07-15**, the corpus **2026-08-03**, both citing Bloomberg, both at −10%. **A 19-day gap between two readings of the same outlet.** The corpus row is already its weakest-provenance row (AI-assisted secondary relaying an anonymously-sourced paywalled primary). **The `[VERIFY]` there is now urgent.**

**One probable double-count, and it is instructive:** the aggregator carries **both "OP Labs" and "Optimism" on 2026-03-12**. Almost certainly one event listed twice — a live instance of **watch (u)** (name-keyed sweeps defeated by entity naming), observed in someone else's instrument.

**Discipline held, stated explicitly so a later run does not soften it.** Nothing was promoted. The standing no-import rule from the Exodus row (aggregator 54 vs SEC-reported ~77) is honoured throughout; **every figure in the new file is labelled aggregator-reported and every candidate carries its own `[VERIFY]`.** A candidate may enter the tracker only after its own primary is fetched and read, exactly as all 19 existing rows were. **Six candidate rows have an EMPTY source column in the aggregator itself** (Bybit, OSL, Keyrock, SQD, CoinLens, Web3 Foundation) and are marked "[VERIFY] or discard."

**Standing finding unchanged, cohort-scoped: no TRACKED firm's 2026 contraction has named marketing as an affected function.** The tracker-scoped version remains broken by the perimeter Gnosis row, whose marketing claim is still single-sourced to an X post and whose two primaries remain uncaptured — **sixth run carried.** **Also unchanged and now explicitly at risk:** the July AI-framing ratio ("Jul: 1 of 7") **must not be restated** until the unheld July rows (YGG, AscendEX, Pump.fun, DDango, Odos, Zapper) are resolved — the denominator is provably wrong.

### 6. NorthPoint longitudinal panel

`trend-data.json` **53 days stale**. No trend claim made.

---

## Watch (z) — mandate item 4: "either run it next or kill it explicitly." NEITHER. Named, not buried.

**Watch (z)** — *promotional surfaces are decoupled from the operational state of the business* — was carried a **fifth** run. It was not run and it was not killed. **The reason is a scheduling collision, not a judgement:** the 08-09 time-to-teardown measurement (two days out) is the pre-committed instrument for exactly this question at the ≥34-surface OKX denominator, and running a hand-rolled panel sweep 48h beforehand would spend the same budget on a weaker version of the same measurement.

**That is an explanation, not an excuse, and the mandate said "either/or".** → **Converted to a hard commitment: watch (z) is folded INTO the 08-09 teardown run as its panel arm, or it is killed in that run's record.** No sixth carry.

---

## What this run did to the mandate

| # | 08-06 recommendation | status |
|---|---|---|
| 1 | Reach ESMA by a non-index route; **validate against the two known items** | **DONE — and the validation disqualified the route.** MiCA activities page fetched, detects neither known item, **carries no absence claim.** `?sort_by=chronological` provenance-blocked, not guessed. **Watch (w) stays open.** The run's principal *result* came from a different ESMA page entirely. |
| 2 | 08-09 time-to-teardown measurement | **on schedule.** Two days out. Not touched today — and now carries watch (z) as its panel arm. |
| 3 | Fetch PSN08 | **ATTEMPTED, UNREACHABLE.** HTTP 200 / empty body, same failure as PS-G02's landing page; no PDF URL surfaced. Secondary summaries deliberately not used. **Gap unclosed, said plainly.** |
| 4 | Test watch (z) or **kill it** | **NEITHER — 5th carry, explained above and converted into an 08-09 hard commitment.** The one mandate item this run did not honour on its own terms. |
| 5 | Implement schema (watch aa + cc) | **PARTIAL, 5th run.** `capture_ai_disclosure` is populated on the new class-3 file (`none — first-party regulator pages`); the four date fields on personnel records remain unimplemented. |
| 6 | Escalate five items | **DONE — below. Two carried, one closed, two new.** |

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged.
- **(b) First named post-deadline NCA marketing-side action** — **day-37 silence HOLDS. Leg 1 of the three-part wording is now PRIMARY-ANCHORED** (ESMA's sanctions perimeter excludes CASPs). Legs 2 and 3 unchanged. **Never print "silence."**
- **(c) Capture panel** — untouched. **(ii) 08-09 time-to-teardown is now the highest-value scheduled item in the repo AND carries watch (z).**
- **(d) Agency panel staleness — 53 days**, and measured today as **byte-identical output**. §6 wording must change. **7th run.**
- **(e′) Cadence — DISCHARGED.** Three consecutive on-time runs (08-05, 08-06, 08-07).
- **(f) Friday nomination cadence** — **DUE TODAY and NOT RUN.** `hello@northpoint.fi` was not read; `inbound-nominations.md` still does not exist; none have ever arrived. **The mailbox is outside this run's public-source scope and no credentialed read was attempted.** Either give the intake an owner or drop the promise from `README.md`, which currently tells the public nominations are "read every Friday."
- **(g) Coinbase n=1** — void as filed. **And now doubly so:** the aggregator names a **2026-03-05 Coinbase −18%** the corpus does not hold. Any Coinbase-shaped claim is unsafe until that is resolved.
- **(h′) Layoff rationale correlates with firm type** — **REJECTED**, with its date-successor. **Do not print either.** New caveat: **the July AI-framing ratio may not be restated** until the six unheld July rows are resolved.
- **(i) Kraken paid-media build-out** — the two Director, Paid Marketing reqs are **open on or before 2026-07-24 and still open today** (minimum 14 days, `captured_date`-floored). **The "15 days open" phrasing used on 08-06 is withdrawn** — see the class-1 finding.
- **(j) Senior-leader exits** — superseded by (aa).
- **(k) Chrome-lane instrumentation gap** — unchanged.
- **(l) §4 inventory too narrow AND provenance-blind** — **8th costing. Five-for-five.** Today's refusal also exposes a *second* gap: the corpus has **no home for a named-marketing-leadership datum that is not a quote**, which is a Theme-1 input it keeps throwing away.
- **(m) Ad-platform gating** — unchanged.
- **(n) Full-range re-sweep of classes 3, 4 and 5** — **NO LONGER A SUSPICION. MEASURED: 19/54 = 35% recall on class 5 against one already-cited public source.** Partially executed today (cross-reference written, nothing promoted). **Classes 3 and 4 remain unmeasured and are now the open half.** Still the highest-value unbuilt instrument in the repo.
- **(o) Date the document, never an event held about it** — held.
- **(p) Absence claims tested against firms' OWN channels** — not advanced.
- **(q) Agency matrix measures the crypto-native segment** — unchanged.
- **(r) Absence panel needs a two-directional "structural withdrawal" category** — unchanged.
- **(s) Robinhood row misclassified** — unchanged, **8th run.**
- **(t′) Class 1 is a FLOW register presented as a STOCK register** — **reinforced and sharpened by today's date-field finding.**
- **(u) Brand absorption defeats name-keyed sweeps** — **observed live in a third-party instrument today** (OP Labs / Optimism double-listed on one date). Alias table still unbuilt.
- **(v) NCA sweep** — 6 of 6, COMPLETE.
- **(w) Class-3 sweep vocabulary AND method** — **STILL OPEN FOR ESMA.** Three routes tried across two runs; none passes the known-presence test. Days 1–8 uncovered. `?sort_by=chronological` provenance-blocked.
- **(x) `fetch_errors` null** — **REOPENED.** Non-null today with 7 entries incl. tracked-firm Aave. The 08-06 closure was a snapshot mistaken for a property.
- **(y) Pre-2026 class-1 rows are arithmetic inferences** — unchanged.
- **(z) Promotional surfaces decoupled from operational state** — **5th carry, NOT killed, converted into an 08-09 hard commitment.**
- **(aa) Announcement vs effective dates** — **NOT IMPLEMENTED, 5th run.**
- **(bb) Class-1 feed-health guard** — CLOSED, passing (13.4h, fingerprint +49).
- **(cc) Secondary layer going machine-written** — **FIRST USE.** `capture_ai_disclosure: none` populated on the new class-3 file. Schema still not applied retroactively.
- **(dd) NEW — class 1 cannot measure time-to-fill, and both of the feed's date fields fail differently.** `first_seen` is a scan-date re-stamp (29/29 rows, including 27 marked STILL_OPEN, `days_open: None`); `posted_at` drifts forward on refreshed requisitions (2 of 5 tracked reqs checked). **Only `captured_date` supports a claim, and only a MINIMUM one.** Directly falsifies one of `methodology.md` §1's five promised extraction fields.
- **(ee) NEW — the corpus cited a census as a single row for six weeks.** CryptoJobsList has been the BitGo row's `source_url` since 06-28 while its 54-row 2026 table went unread. **Standing rule: when a source is cited once, check whether it is an index. An aggregator used as a citation is an aggregator not used as an instrument.**

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **FEED HEALTH HEALTHY, 13.4h, fingerprint 2,090→2,139.** 0 new postings, 18 agency files, 8 matrix rows.
2. Direct read of `prospects/open-positions.json` — `scan_metadata`, all 29 filtered roles, `top_picks`, `fetch_errors`, `drops_summary`. **Yielded the class-1 date-field finding.**
3. Programmatic diff of feed `posted_at` vs corpus `date_posted` on 5 tracked requisition IDs → **2 forward drifts.**
4. `git status` post-sync → **class-2 output byte-identical; only 2 date-stamp files modified.**
5. Repo dedup baseline reads — 08-06 run record in full, tracker (19 rows) in full, all 13 job-posting CSVs, regulator/operator/campaign indexes, `_absence.csv`.
6. WebSearch — ESMA MiCA marketing-communications enforcement August 2026 → surfaced the MiCA activities page.
7. **`web_fetch` ESMA MiCA activities page** → HTTP 200. **FAILS known-presence validation.** Register stamp *"Last update: 31 July 2026"* captured.
8. **`web_fetch` ESMA Investigations and Inspections** → HTTP 200. "Perimeter monitoring" scoped to credit ratings, verbatim.
9. **`web_fetch` ESMA Sanctions and Enforcement** → HTTP 200. **THE RUN'S PRINCIPAL RESULT.** Six-class sanctioning perimeter, CASPs absent.
10. `web_fetch` ESMA `?sort_by=chronological` → **BLOCKED by provenance rule. Not fetched, not guessed.**
11. WebSearch — BaFin/AMF/CONSOB/AFM/CySEC crypto advertising enforcement August 2026 → **0 net-new primary enforcement items.** Only undated secondary aggregations; none admitted.
12. WebSearch — MAS PSN08 → surfaced the notice landing page.
13. `web_fetch` MAS PSN08 → **HTTP 200, empty body. Not claimed.**
14. WebSearch ×2 — crypto layoffs Aug 2026 / marketing roles → surfaced the CryptoJobsList census and trendingtopics.eu.
15. `web_fetch` trendingtopics.eu → **empty body. Not claimed** (its "marketing and sales teams felt the brunt" line was surfaced only in search-result summary and is **deliberately not entered** — an unfetched claim is not a source).
16. **`web_fetch` cryptojobslist.com/crypto-layoffs** → HTTP 200, full 2026 table. **The class-5 result.**
17. WebSearch + **`web_fetch` fintechmarketinghub.com Top 30 2026** → HTTP 200. **Class-4 refusal**, recorded with reasons.
18. **Not reached / not guessed:** ESMA `?sort_by=chronological` and pages 3+ · PSN08 operative text · MAS enforcement register · VARA · CONSOB PDFs · FT originals · Bloomberg originals · every `[VERIFY]` primary behind the 35 aggregator candidates. **No URL was fabricated.**

---

## Net-new / changed this run

- `corpus/regulator-filings/esma-sanctions-perimeter-casp-absence-2026-08-07.md` — **NEW.** ESMA's six-class sanctioning perimeter with CASPs absent, verbatim; credit-ratings-only perimeter monitoring, verbatim; the three-route validation table with two failures named; the register's three-date freshness conflict; `capture_ai_disclosure` populated.
- `corpus/layoff-tracker/_aggregator-crossref-2026-08-07.csv` — **NEW.** 54 aggregator rows × 19 corpus rows, every row classified HELD / HELD-CONFLICT / NET-NEW-CANDIDATE / PROBABLE-DOUBLE-COUNT; **recall 35% stated at the top of the file**; no-import rule restated; six empty-source rows flagged.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` — date re-stamps (sync).
- `findings/longitudinal-2026-06.md` — day-37 shift appended.
- **`corpus/layoff-tracker/2026-layoff-tracker.csv` — UNCHANGED at 19 rows, deliberately.**
- **Operator statements: unchanged at 5 files. Job postings: 0 net-new (genuine absence, guard-asserted). Agency claims: byte-identical.**

---

## Recommendation for next run

1. **Promote the two cheapest, best-corroborated layoff candidates and no others: Polygon (2026-01-15) and Ethereum Foundation (2026-06-23).** Both have a date, a headcount, and an independent reason to be believed (Polygon is already cited as context inside a corpus row; EF is the second independent appearance of a claim the corpus itself flagged on 08-05). **Fetch each primary first.** Resist the temptation to bulk-import — 35% recall is fixed by 35 verifications, not by one paste.
2. **Then resolve the two that change the report, in this order: Coinbase 2026-03-05 (−18%) and FalconX's 19-day date conflict.** The first may mean the Theme-5 spine is built on the wrong Coinbase event. The second sits on the tracker's weakest provenance chain.
3. **08-09 teardown, with watch (z) folded in as its panel arm.** Pre-committed, two days out, and now carrying a fifth-carry watch item. Measure teardown *rate* against the ≥34-surface denominator.
4. **Apply the (dd) rule to the corpus retroactively:** re-label every class-1 duration statement in `findings/` and in prior run records as a **minimum** derived from `captured_date`. Small, mechanical, and it stops a wrong number reaching Phase 2.
5. **Escalate to Jukka — five items, in order:**
   - **(i) `methodology.md` §1 must be re-scoped. SEVENTH run, unaddressed — and today it stopped being an argument and became a measurement.** §1 promises five extracted fields; **time-to-fill is not one class 1 can supply**, proven this run (`first_seen` is a scan-date re-stamp on 29/29 rows; `posted_at` drifts forward on refreshed reqs). §1 also cannot evidence "rolling 12 months." **Still the one thing in this repo that could embarrass the report, and the evidence is now in-repo and reproducible.**
   - **(ii) Commission the class-3 and class-4 halves of the (n) re-sweep — NOW.** Class 5's recall is measured at **35%** against a source the corpus already cited. **There is no reason to believe classes 3 and 4 are better and no measurement saying they are.** Phase 2 starts within days.
   - **(iii) `methodology.md` §4 needs two changes** — widen the inventory *and* add an earned-vs-placed provenance field. **Five-for-five across five runs.** Today adds a second, distinct gap: **no home for named-marketing-leadership data that is not a quote** (two tracked firms' leaders identified and discarded today).
   - **(iv) The four upstream company-list gaps — OKX (Tier-1), Securitize, Rabby, Relai — unfixed, SEVENTH run.** Sharpened today: **OKX has a January 2026 contraction in the public record and is invisible to class 1 entirely**, while **Relai's CMO was identified by name in a public 2026 list this run.** Needs an owner outside the corpus run.
   - **(v) The Friday nomination promise in `README.md` is unkept and unowned.** The public text says inbound nominations are "read every Friday." **Today is Friday; nothing was read; no intake file has ever existed.** Either assign the mailbox read or amend the README. It is a published commitment, which makes it a different class of debt from the rest of this list.

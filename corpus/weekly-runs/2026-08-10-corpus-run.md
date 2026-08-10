# Corpus-assembly daily run — 2026-08-10 **(day 40 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-10 (**Monday**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, verbatim from the 08-08 recommendations:** (1) run the 08-09 teardown with watch (z) as its panel arm, or kill (z); (2) **fetch the OKX / Rafique CoinDesk item**; (3) apply the (dd) rule retroactively (2nd carry); (4) audit the watch list the way the aggregator was audited; (5) escalate seven items.
**Dedup baseline read before writing:** `2026-08-08-corpus-run.md` in full; `2026-layoff-tracker.csv` all 21 rows in full; `open-positions.json` `scan_metadata` + `fetch_errors`; directory indexes for `operator-statements/`, `regulator-filings/`, `marketing-campaigns/`, `ad-platform-gates/`, `layoff-tracker/`, `job-postings/`; `findings/longitudinal-2026-06.md` tail.
**🔴 CADENCE: BROKEN. 08-09 DID NOT RUN.** Four consecutive on-time runs (08-05 → 08-08) ended Sunday. **Watch (e′) REOPENS.** The item the 08-08 record called *"the highest-value scheduled item in the repo, and it is due"* was pre-committed for 08-09 and did not fire. **See "What this run did to the mandate" — it did not fire today either, and that is named rather than buried.**

---

## Headline result

**Three things, in descending order of consequence.**

**1. The corpus cannot establish, from any public source, who runs marketing at OKX in 2026 — and the fetch that proved it was the one the last run pre-registered to end the class-4 drought.** OKX's own estate says **Chief Marketing Officer** (post published 2022-12-06, **last updated April 2024**). CoinDesk's in-window exclusive describes the same named person as the exchange's **"global managing partner for Corporate Affairs and Investor Relations."** Both fetched first-party, HTTP 200. **No dated transition document exists anywhere the corpus has captured.** This is not claimed as a demotion or a departure — a combined-scope reading fits the evidence equally well and the corpus holds no primary either way. **The claim is the absence:** a MiCA-CASP-authorised Tier-1 exchange with an EU entity publishes nothing dated about its own marketing leadership, and a regulator doing this read hits the same wall. Theme 1 and Theme 4 in one artefact. → `../operator-statements/okx-rafique-role-reclassification-2026-08-10.md` (NEW).

**2. The null has a second counterparty, and it is the licensee itself.** On **2026-08-04**, forty days after the deadline and with no named marketing-side NCA action anywhere in this corpus, **Erald Ghoos, CEO of OKX Europe, published the second instalment of a weekly bylined column on OKX's own estate titled *"Europe's Crypto Reset Is Working."*** It converts the firm's authorisation count into the differentiator: *"three separate authorisations… answerable to European regulators across all 30 EEA states"*, *"MiCA created the first real single market for crypto anywhere in the world."* **Where Google (08-08) turned the licence into an access gate, OKX turns it into promotional inventory.** The shape to print: *in the post-deadline window, MiCA's observable marketing consequence is not enforcement against non-compliant promotion — it is the licence becoming promotional inventory for the compliant.* Both counterparties are private actors. Neither is a regulator. Neither tests whether any communication is fair, clear and not misleading. → `../marketing-campaigns/okx-europe-ghoos-licence-as-marketing-asset-2026-08.md` (NEW).

**3. The class-5 recall figure did not just weaken again — it was measuring the wrong universe.** CoinDesk 2026-08-09 (fetched): **over 100 crypto projects shut down, filed for bankruptcy or went permanently dark in 2026, per RootData.** That counts **project deaths**; CryptoJobsList's 54 counts **layoff events**. Different objects; they must never be divided by one another. **Three consecutive runs have degraded this corpus's headline self-measurement — 35% → floor → wrong universe — and that is the system working.** → `../layoff-tracker/_industry-scale-denominator-2026-08-10.md` (NEW).

**Day-40 named marketing-side enforcement silence HOLDS.**

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0 — a genuine absence, guard-asserted.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-08-10
source A (jobs)   scan_date: 2026-08-10
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-09T21:45:44Z, age=17.6h,
             fingerprint total_jobs_fetched=2144)
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

Age 17.6h (HEALTHY). Fingerprint **2,140 → 2,144 (+4 across two calendar days**, 147 companies, 89 via API). The guard passes on direction. **Watch (ff) — magnitude floor — is unaddressed and the observed distribution is now +49 / +1 / +4 across three observations.**

#### 🔴 A NEW CLASS-1 DEFECT, AND IT IS SHARPER THAN (dd)

`total_jobs_after_filter` moved **29 → 28**. **A tracked marketing requisition left the filtered set while `new_count` stayed 0.**

The sync is **append-only, dedup-by-`source_url`**. It has no delete path. Therefore:

> **The corpus can observe a posting appearing. It cannot observe a posting disappearing.**

This is worse than (dd) and it subsumes part of it. (dd) established that `first_seen` is a scan artefact and only `captured_date` supports a **minimum** duration claim. **Today establishes that even the minimum is one-sided:** a requisition filled or withdrawn on 08-09 is still in `job-postings/*.csv` today, indistinguishable from one still open, and **the run cannot say which of the 29 became 28.** Every "still open" statement in this corpus is therefore *"last observed open on `captured_date`, and not since re-verified."*

**Immediate consequence, applied now rather than carried:** the two Kraken **Director, Paid Marketing** requisitions — watch (i) — must be restated. Prior wording: *"open on or before 2026-07-24 and still open today: minimum 15 days."* **Corrected wording: last observed in the filtered set on a `captured_date` of 2026-07-24; the corpus cannot assert they are open today.** This is the (dd) retroactive pass finally beginning, on the one row where it was load-bearing. **watch (t′) — flow register presented as a stock register — is CONFIRMED with a mechanism and should be promoted out of the watch list into `methodology.md`.**

**`fetch_errors`: 6, unchanged** (Wormhole Foundation, **Aave — tracked, 9th run**, Injective Labs, Bitwise, Chainlink Labs, Elliptic). Watch (x) stays REOPENED.

#### Absence panel — four upstream gaps unfixed for a **ninth** run
`_absence.csv`: Aave + Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys. **OKX (Tier-1), Securitize, Rabby, Relai remain missing from the upstream company list.** Ninth run. Needs an owner outside the corpus run. **Note the irony this run earned: OKX produced the run's two best findings and is not in the class-1 company list at all.**

### 2. Agency claims / overlap matrix (deterministic)

18 files rewritten; 8 matrix rows; **1 OVERLAP: Sui (coinbound, rzlt)** — unchanged. `trend-data.json` `lastUpdated` still **2026-06-15**: **56 days stale.** Class-2 output byte-identical for a third consecutive run. `methodology.md` §6's phrase *"daily 18-agency panel"* remains inaccurate as written. **Ninth run.**

### 3. Regulator — **0 NET-NEW PRIMARY ITEMS. Day-40 silence holds.**

WebSearch on MiCA marketing-communications enforcement, August 2026, CASP scope returned **only secondary material**: law-firm and compliance-vendor explainers (Lexology ×2, Trusty, InnReg, Sigma360, Sumsub, Global Relay, Global Law Experts) and one AI marketing-review vendor tool. **Every one is an undated-or-explanatory secondary restating Articles 66–68 and the 1 July cut-off. None is a primary. None admitted.**

**One thing worth recording from the secondary layer, as a market fact and not as a regulator fact:** a vendor is now selling *"MiCAR Marketing Communications Review — AI Compliance Check for CASPs."* That is a commercial product occupying the exact gap this corpus has spent forty days documenting as unenforced. **Directly competitive-relevant to NorthPoint and named here for that reason; not entered as a corpus source.**

**NOT REACHED, NOT GUESSED, unchanged from 08-08:** ESMA `?sort_by=chronological` (provenance-blocked, **watch (w) still open, days 1–10 uncovered**) · MAS PSN08 operative text · MAS enforcement register · **VARA, still never swept at source** · CONSOB comunicato PDFs · Google `answer/14009787` · six other distribution platforms. **No URL was fabricated.**

### 4. Operator statements — **0 NET-NEW ADMITTED. 6th consecutive refusal — and the FIRST refused on SUBSTANCE.**

The mandate's single fetch was made. **The pre-registered test resolved to its second branch, exactly as written.**

The CoinDesk item satisfies **every formal §4 requirement**: in-window, dated, named speaker, verbatim quotes, URL, Tier-1 tracked firm, first-party exclusive interview. It is the cleanest-shaped candidate class 4 has surfaced since 07-28. **And it contains zero marketing-function content** — the three quotes are on Democratic vote-counting, offshore entrepreneurship, and bitcoin price efficiency; the reporting covers an ICE joint venture. Nothing on brand, growth, channel, agency, budget, team shape, or the post-MiCA marketing surface.

**Therefore, per the 08-08 pre-registration: this is the first evidence that §4's problem is SUPPLY, not definition.** When a qualifying operator at a qualifying firm gives a first-tier outlet an exclusive, what he talks about is policy and price. **Watch (l), 10th costing — and its character changes: widening §4 would not have caught this item's substance, only its format.**

**Plus the role datum (headline 1) and two instrument defects, both in first-tier sources' own artefacts:**

- **🔴 Date defect in a URL slug.** The URL path reads `/2026/08/04/`; `publish_date`, `parsely-pub-date`, `display_date` and `create_date` all read **2026-08-07 15:22 UTC**, and the on-page relative stamp read "3 days ago" today. **The 08-08 record already carried "dated 2026-08-04" — taken from a nav rail and a URL.** Had it been promoted on 08-08 as recommended, it would have entered dated wrong. **Watch (o) extends: a date in a publisher's own URL slug is not a publication date. Two of the last three date defects were in first-tier sources, not aggregators.**
- **🔴 Watch (cc) confirmed at the corpus's most-used secondary.** The item carries `meta-author_2: ai-boost`, a byline reading **"By Will Canny, AI Boost"**, and an AI disclaimer. **CoinDesk is the principal capture for Crypto.com, OP Labs, Uphold, Polygon Labs (both rounds), the Ethereum Foundation and today's scale datum.** Machine-assistance is not a marker of publisher tier. Nothing is withdrawn — the disclosure states editorial review and both CoinDesk captures today were internally consistent — but **`capture_ai_disclosure` must become a populated field on every capture, retroactively**, or Phase 2 will draw a provenance distinction its own records cannot support.

**Class 4 stays at 5 files. One item in 15 days.**

### 5. Layoffs — **2 ROWS ADDED (21 → 23). 1 NEW ANALYSIS FILE. The recall measure reframed.**

**(a) Pump.fun / Baton Corporation Ltd. [PERIMETER] — added, and it opens a category the tracker did not have.** Crowdfund Insider 2026-08-05 captured HTTP 200, relaying a **Sandmark** investigation (internal documents, emails, recordings). **The Sandmark original was REFUSED by the fetch provenance rule — `[VERIFY]`.** Wave 1: head of talent convened affected staff **late March**, agreements ended **early April**, severance one week per month served. Wave 2: alleged **mid-July**, ~40 people — **sourced to an anonymous X account, and Sandmark itself stated it could not confirm the numbers or the July timing. 40 is NOT printable as confirmed.** Firm did not comment.

Rationale, verbatim from co-founder **Noah Tweedale**: the firm *"grew too quickly"*, hindering its ability to operate in a *"fast and rough"* manner. **8th consecutive non-AI rationale; h′ stays rejected.**

**THE NEW CATEGORY: token-denominated compensation as the mechanism of loss.** Grants entered ~mid-June 2025 with 25% unlocking after one year; wave-1 departures fell **~2 months short of the cliff** and unvested portions were cancelled; one former worker reported to have forfeited a seven-figure allocation. **Every other row in this tracker concerns salary headcount. This is the first where the loss is denominated in the firm's own token.** Phase 2 must not fold it into the generic bucket.

**And the juxtaposition, stated without motive:** the same CoinDesk feature captured today quotes Ark Invest's Lorenzo Valente saying **Hyperliquid and Pump.fun together account for 67% of total app revenue.** A firm cutting staff while being one of the sector's two top-revenue apps is the inverse of the market-conditions rationale dominating the 2026 window.

**(b) MVMT Labs (Movement Labs) [PERIMETER — Chapter 11] — added with the date flagged.** The **captured** fact is CoinDesk 2026-08-09's own sentence: *"Four major firms announced closures or filings within a single week in late July alone: BitMEX, BitMart, Movement Labs and Storj Labs."* The **2026-07-15 filing date, Delaware venue, creditor bands and the 09-14/10-13 deadlines come from a WebSearch summary of an unfetched CoinDesk 07-21 article** — `[VERIFY]`. Note the internal tension the row records: 07-15 vs the captured source's "late July" — **plausible as an announcement-vs-filing gap, which is precisely what watch (aa) exists to catch, and it is now a live instance rather than a hypothetical.** Third contraction-by-closure after BitMEX and BitMart.

**(c) STORJ LABS — fourth name in that sentence, entirely new to this corpus, unresearched.** Named so it is not lost.

**(d) Moonbeam — stopped producing blocks 2026-07-31**, stranding assets in Moonwell and other on-chain protocols. Dated, in-window, named. **Not added — no primary captured.** Queued.

**Standing finding UNCHANGED, cohort-scoped: no TRACKED firm's 2026 contraction has named marketing as an affected function.** Neither new row names a function. Both are perimeter. The Gnosis `[VERIFY]` remains the corpus's highest-value open verification, **ninth run carried.**

### 6. NorthPoint longitudinal panel

`trend-data.json` **56 days stale**. No trend claim made.

---

## What this run did to the mandate

| # | 08-08 recommendation | status |
|---|---|---|
| 1 | Run the 08-09 teardown with (z) as its panel arm, or kill (z) | **🔴 NOT DONE — SECOND CONSECUTIVE MISS, AND THIS ONE IS THIS RUN'S OWN.** 08-09 did not fire at all. Today's run chose the mandate's fetch and the net-new classes over the teardown and **ran out of budget before reaching it**. That is a choice, not an accident, and it is recorded as one. **Watch (z) is now on its sixth carry after the 08-08 record said "No sixth carry."** The commitment was broken by this run. |
| 2 | Fetch the OKX / Rafique item | **DONE — and it returned three results instead of one.** Class-4 refusal on substance (the pre-registered branch); the role/absence datum (headline 1); and two instrument defects in first-tier artefacts (URL-slug date; CoinDesk AI byline). |
| 3 | Apply (dd) retroactively (2nd carry) | **PARTIALLY DONE — and the rule got worse before it got applied.** The Kraken watch-(i) duration claim is restated in §1 above. The full mechanical sweep is **still not done**, and today's `29 → 28` finding means the sweep must now correct *two* defects per statement, not one. **3rd carry.** |
| 4 | Audit the watch list the way the aggregator was audited | **NOT DONE as a systematic pass — but (ee) fired anyway, twice.** Once productively: the RootData list is named as the highest-value unfetched class-5 instrument **before** it costs anything. Once retroactively: the "dated 2026-08-04" note was itself an unverified carried fact and was wrong. **The audit is now overdue with evidence attached.** |
| 5 | Escalate seven items | **DONE — below.** |

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged.
- **(b) First named post-deadline NCA marketing-side action** — **day-40 silence HOLDS. Second counterparty acquired, and it is the licensee's own brand estate.** The null now has two private counterparties (Google, 08-08; OKX/Ghoos, today) and no public one. Never print "silence."
- **(c) Capture panel** — untouched. **See (z).**
- **(d) Agency panel staleness — 56 days**, byte-identical output three runs running. §6 wording must change. **9th run.**
- **(e′) Cadence** — **🔴 REOPENED. 08-09 did not run.** Discharged on 08-08 after four on-time runs; broken the next day.
- **(f) Friday nomination cadence** — **unkept for a second consecutive Friday (08-07).** `inbound-nominations.md` still does not exist. `README.md` still tells the public nominations are read every Friday. Unowned, unkept, **published.**
- **(g) Coinbase n=1** — unchanged, open.
- **(h′) Layoff rationale correlates with firm type** — **REJECTED, 8th consecutive non-AI rationale (Pump.fun).** Do not resurrect.
- **(i) Kraken paid-media build-out** — **CLAIM RESTATED AND WEAKENED THIS RUN.** No longer "still open today"; now *last observed in the filtered set on `captured_date` 2026-07-24, not since re-verified.* See §1.
- **(j) Senior-leader exits** — superseded by (aa); **and the OKX role datum is the first instance where the corpus cannot tell whether an exit even occurred.**
- **(k) Chrome-lane instrumentation gap** — unchanged.
- **(l) §4 too narrow AND provenance-blind** — **10th costing, and its character CHANGED. The first refusal on substance.** Widening §4 would not have admitted today's item; nothing in it is about marketing. **The supply hypothesis now has its first evidence.**
- **(m) Ad-platform gating** — discharged 08-08; **its logic generalised today by the OKX/Ghoos capture.**
- **(n) Full-range re-sweep of classes 3, 4, 5** — class 5 advanced (2 rows, 1 analysis file, denominator reframed). **Classes 3 and 4 remain unmeasured.**
- **(o) Date the document, never an event held about it** — **EXTENDED, and it was load-bearing today. A date in a publisher's own URL slug is not a publication date.** Two of the last three date defects were in first-tier sources.
- **(p) Absence claims tested against firms' OWN channels** — **ADVANCED, for the first time, and it produced the run's headline.** OKX's own estate was read for its own marketing leadership and the answer was a 28-month-stale page. **This is the method (p) was asking for. Apply it to the other nine Stratum-1 firms.**
- **(q) Agency matrix measures the crypto-native segment** — unchanged.
- **(r) Absence panel needs a "structural withdrawal" category** — unchanged.
- **(s) Robinhood row misclassified** — unchanged, **10th run.**
- **(t′) Class 1 is a FLOW register presented as a STOCK register** — **🔴 CONFIRMED WITH A MECHANISM, AND PROMOTED.** `total_jobs_after_filter` 29 → 28 with `new_count` 0. The sync is append-only with no delete path: **the corpus can observe appearance and cannot observe disappearance.** Belongs in `methodology.md`, not the watch list.
- **(u) Brand absorption defeats name-keyed sweeps** — unchanged; alias table still unbuilt.
- **(v) NCA sweep** — 6 of 6, COMPLETE.
- **(w) Class-3 sweep vocabulary AND method** — **STILL OPEN FOR ESMA.** Days 1–10 uncovered.
- **(x) `fetch_errors`** — **6 entries, unchanged**, incl. tracked-firm Aave (9th run).
- **(y) Pre-2026 class-1 rows are arithmetic inferences** — unchanged.
- **(z) Promotional surfaces decoupled from operational state** — **🔴 SIXTH CARRY, against an explicit "no sixth carry" written on 08-08.** Broken by this run. **It must be executed or killed in the next record; a third statement of intent is worth less than a kill.**
- **(aa) Announcement vs effective dates** — **NO LONGER HYPOTHETICAL.** The Movement Labs 07-15-vs-"late July" tension is a live instance in the tracker. **7th run.**
- **(bb) Class-1 feed-health guard** — passing; see (ff).
- **(cc) Secondary layer going machine-written** — **🔴 CONFIRMED AT COINDESK, the corpus's most-used secondary.** Not a tier marker. `capture_ai_disclosure` must be populated retroactively.
- **(dd) Class 1 cannot measure time-to-fill** — **SUBSUMED AND WORSENED by (t′).** Not only is `first_seen` a scan artefact; disappearance is unlogged, so even minimum-duration claims are one-sided. Retroactive sweep **3rd carry**, and now doubled in scope.
- **(ee) A source cited once is a source not used as an instrument** — **THIRD AND FOURTH FIRINGS.** Retroactively: the carried "dated 2026-08-04" note was wrong. Prospectively: **the RootData 2026 dead-projects list is named as the highest-value unfetched class-5 instrument before it costs anything** — the first time this watch item has been applied ahead of a failure rather than after one.
- **(ff) Feed-health guard tests direction, not magnitude** — unchanged. Distribution now +49 / +1 / +4. **And today adds that the guard is blind in the other direction too: it cannot see the filtered set shrink.**
- **(gg) `methodology.md` has six classes and the corpus has seven directories** — unchanged, unwritten. **Joined today by §5's completeness framing (see the denominator file) and by (t′).** The methodology rewrite queue is now **§1, §4, §5, §6, §7** — five of the document's sections.

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **FEED HEALTH HEALTHY, 17.6h, fingerprint 2,140→2,144 (+4).**
2. Direct read of `open-positions.json` `scan_metadata` + `fetch_errors` → **the 29→28 finding**, the run's sharpest instrument result.
3. Repo dedup pass: 08-08 run record in full; all 21 tracker rows; six directory indexes; longitudinal tail.
4. WebSearch — Haider Rafique OKX CMO August 2026.
5. **`web_fetch` CoinDesk `/policy/2026/08/04/okx-s-rafique-…`** → HTTP 200. **Class-4 refusal on substance; the Corporate-Affairs/IR descriptor; URL-slug date defect; AI co-byline.**
6. **`web_fetch` `okx.com/en-us/learn/okx-new-cmo-haider-rafique`** → HTTP 200. First-party CMO baseline, **last updated April 2024**. Surfaced the Ghoos series in its related-articles rail.
7. **`web_fetch` `okx.com/en-us/learn/europes-crypto-reset-is-working`** → HTTP 200. **The run's second headline.**
8. WebSearch — MiCA marketing-communications enforcement August 2026 CASP → **0 net-new primary items**; 9 secondary/vendor results, none admitted.
9. WebSearch — crypto layoffs August 2026 marketing team → surfaced Pump.fun and Movement Labs.
10. **`web_fetch` trendingtopics.eu 2026-07-30 layoff round-up** → HTTP 200. Secondary aggregation of the CryptoJobsList table; **no rows promoted from it** (LBank, Keyrock, Zap Africa, Swyftx all remain unfetched aggregator entries and are NOT entered). Its own Coinbase row lists **500 / 14%** against the corpus's primary-anchored **~700 / 14%** — logged, not reconciled.
11. WebSearch — Pump.fun layoffs 40 employees 2026.
12. **`web_fetch` Crowdfund Insider 2026-08-05 Pump.fun** → HTTP 200. Tweedale verbatim; vesting-cliff mechanism.
13. `web_fetch` `sandmark.com/news/top-news/pumpfun-laid-employees-two-months-token-vesting` → **REFUSED by provenance rule. Not fetched, not guessed.** `[VERIFY]`.
14. WebSearch — Movement Labs shutting down closure 2026.
15. **`web_fetch` CoinDesk 2026-08-09 dot-com-shakeout feature** → HTTP 200. **RootData 100+; the four late-July names; Moonbeam; Blockaid $1.1bn; TRM 66%; Tally/Step/Everclear; Hyperliquid/Aave/Ether.fi.**
16. **Not reached / not guessed:** ESMA chronological index · MAS PSN08 + register · VARA · CONSOB PDFs · the RootData list itself · CoinDesk 2026-07-21 Movement Labs · the four unfetched in-window OKX `/learn/` posts · Rafique's LinkedIn and the Entrepreneur/Campaign profiles. **No URL was fabricated.**

---

## Net-new / changed this run

- `corpus/operator-statements/okx-rafique-role-reclassification-2026-08-10.md` — **NEW.** Two first-party captures; the role/absence datum with an explicit not-claimed list; the class-4 substance refusal; the URL-slug date defect; the CoinDesk AI byline.
- `corpus/marketing-campaigns/okx-europe-ghoos-licence-as-marketing-asset-2026-08.md` — **NEW.** Ghoos 2026-08-04 verbatim; the licence-as-promotional-inventory shape; four `[VERIFY]`s; four unfetched in-window OKX posts named as the cheapest capture queue.
- `corpus/layoff-tracker/_industry-scale-denominator-2026-08-10.md` — **NEW.** RootData 100+; deaths-vs-events distinction; **the three sentences Phase 2 may write about class-5 completeness, and nothing stronger.**
- `corpus/layoff-tracker/2026-layoff-tracker.csv` — **21 → 23 rows.** Pump.fun + MVMT Labs.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` — date re-stamps (sync).
- `findings/longitudinal-2026-06.md` — day-40 shift appended.
- **Operator statements: unchanged at 5 admitted files (+1 refusal record). Job postings: 0 net-new (genuine absence, guard-asserted). Agency claims: byte-identical, third run.**

---

## Recommendation for next run

1. **🔴 RUN THE TEARDOWN OR KILL WATCH (z) IN THE RECORD. No seventh carry, and this time the sentence has to hold.** It has been pre-committed twice and missed twice. **If it is not the first thing the next run does, kill it explicitly and say the corpus decided not to do it** — that is a defensible position; a third deferral is not.
2. **Fetch the RootData 2026 dead-projects list.** Named today as the highest-value unfetched class-5 instrument. One fetch. It is the only object that can tell the corpus the size of the universe it has been sampling.
3. **Apply (p) to the other nine Stratum-1 firms — read each firm's OWN estate for its OWN marketing leadership.** Today's headline came from doing this once, at one firm, and finding a 28-month-stale page. **If OKX is typical, Theme 4 has a much stronger spine than the corpus currently knows. If OKX is atypical, that is also the finding.** Cheapest high-value sweep available.
4. **Do the (dd)+(t′) retroactive sweep. 3rd carry, now doubled in scope.** Every duration statement needs both corrections: `captured_date`-floored *and* "not since re-verified."
5. **Escalate to Jukka — seven items, in order:**
   - **(i) `methodology.md` now needs FIVE sections rewritten: §1, §4, §5, §6, §7. NINTH run for §1.** §1 promises fields class 1 cannot supply and today added that class 1 cannot see a posting close. **Still the one thing in this repo that could embarrass the report.**
   - **(ii) The class-4 supply result is a Phase-2 structural input, not a data gap.** Six refusals, the last on substance. **If senior crypto marketing operators do not talk publicly about marketing, then "operator statements" cannot be a load-bearing source class and Theme 1 must rest on job postings, org artefacts and absence.** Decide this before drafting, not during.
   - **(iii) `capture_ai_disclosure` must be populated retroactively across the corpus.** Confirmed today at CoinDesk. The corpus is about to publish provenance distinctions its own records cannot support.
   - **(iv) The 08-09 miss plus the twice-broken (z) commitment is a scheduling-reliability problem, not a research one.** Two of the last three days' pre-commitments were not kept by the runs that made them.
   - **(v) Four upstream company-list gaps — OKX (Tier-1), Securitize, Rabby, Relai — NINTH run.** Today OKX supplied both headline findings and is absent from the class-1 company list. Plus the standing Ethereum Foundation cohort gap.
   - **(vi) The Friday nomination promise in `README.md` is unkept for a second consecutive Friday.** Assign the mailbox read or amend the README.
   - **(vii) The DE sync loop must still be excluded from this repo or made lock-aware.** Raised 08-07 and 08-08; it swallowed corpus output on two consecutive days. Status unknown today until this run's commit lands.

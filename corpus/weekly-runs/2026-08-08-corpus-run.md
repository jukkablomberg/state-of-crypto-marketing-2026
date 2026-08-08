# Corpus-assembly daily run — 2026-08-08 **(day 38 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-08 (**Saturday**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, verbatim from the 08-07 recommendations:** (1) promote Polygon (01-15) and Ethereum Foundation (06-23) **and no others**, fetching each primary first; (2) then resolve **Coinbase 2026-03-05 (−18%)** and the **FalconX 19-day date conflict**; (3) 08-09 teardown with watch (z) folded in *(scheduled tomorrow, not today)*; (4) apply the (dd) minimum-duration rule retroactively; (5) escalate six items.
**Dedup baseline read before writing:** `2026-08-07-corpus-run.md` in full; `2026-layoff-tracker.csv` all 19 rows in full; `_aggregator-crossref-2026-08-07.csv` in full; `open-positions.json` `scan_metadata` + all 29 filtered roles + `fetch_errors`; `job-postings/` index + `_absence.csv`; `regulator-filings/`, `operator-statements/`, `marketing-campaigns/` indexes; repo-wide grep for `google|adspolicy|ad-platform` and for `ethereum foundation` before writing either new file.
**CADENCE: HEALTHY.** 08-05, 08-06, 08-07, 08-08 — four consecutive on-time runs.

---

## Headline result

**Three things, in descending order of consequence.**

**1. The thirty-eight-day null finally has a counterparty, and it is not a regulator. On 2026-07-01 — the day after France's MiCA transitional period expired — Google withdrew AMF DASP registration as an advertising credential and required MiCA CASP authorisation instead. It had done the same in Finland on 2025-06-30 and Germany on 2025-12-30, and it extended the rule to Iceland, Liechtenstein and Norway this month.** Three Member-State deadlines, three on-time executions, keyed explicitly to **Article 143(3) of Regulation (EU) 2023/1114**, with a stated remedy (account suspension) and a stated procedural protection (≥7 days' warning). Read against the corpus's own 08-06 finding that **the AMF deliberately set no shutdown deadline** and its 08-07 finding that **ESMA has no CASP sanctioning power at all**: the marketing-side consequence of MiCA authorisation status in the EEA is presently administered on schedule by a private platform and not at all by the authorities that own the perimeter. → `../ad-platform-gates/google-ads-mica-casp-gate-eu-eea-2026-08-08.md` (NEW FILE, NEW SOURCE CLASS).

**2. The 08-07 run's "HIGHEST-VALUE UNHELD ROW" — Coinbase, 2026-03-05, −18% — is the JUNE 2022 layoff, mis-dated by three years and nine months.** Fetched at the aggregator's own linked source: Blockworks, **June 14, 2022**, 1,100 employees, SEC accession `coin-20220614.htm`, Coinbase market cap "just over $11 billion." **The corpus's Theme-5 Coinbase spine is safe.** And the aggregator's date column is now measured: **three of four dates verified this run were wrong.** → `../layoff-tracker/_aggregator-date-integrity-2026-08-08.md` (NEW FILE).

**3. Two rows promoted, one of them against the aggregator's own numbers. Tracker 19 → 21.** Polygon Labs' **January** round (2026-01-16, 60 roles, **percentage refused — the firm disputed −30% on the record in the very article the aggregator cites**) and the Ethereum Foundation (2026-06-23, 54 roles, ~20%), which resolves the `[VERIFY]` the FalconX row opened on 08-05.

**Day-38 named marketing-side enforcement silence HOLDS** — and it is no longer describable as an absence of consequence.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0 — a genuine absence, guard-asserted.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-08-08
source A (jobs)   scan_date: 2026-08-08
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-07T21:45:40Z, age=14.3h,
             fingerprint total_jobs_fetched=2140)
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

**Watch (bb) passes on the letter and should not be trusted on the spirit — a caveat this run is recording before it costs anything.** Age 14.3h (HEALTHY). But the fingerprint moved **2,139 → 2,140: plus one.** Yesterday it moved +49. `total_jobs_after_filter` held at 29. Across **147 companies scanned** and ~23.5 hours, the entire market moved by a single posting. The guard is binary — *moved* or *did not move* — so **+1 passes exactly as easily as +49**, and a scan that had partially failed while writing one new row would pass it too. The zero is still claimed as a genuine absence today, because +1 ≠ 0 and the guard's rule is the guard's rule. **But the guard needs a magnitude floor, not just a change test.** → new watch (ff).

#### Class-1 date fields: the (dd) finding CONFIRMED and refined

All 29 rows again carry an identical `first_seen`, and `days_open` is `None` on all 29 — as on 08-06 (all `2026-08-05`) and 08-07 (all `2026-08-07`). **Today the value is `2026-08-07` while the feed's own `scan_date` is `2026-08-08`.**

That is a sharper result than yesterday's. The 08-07 rule was *"`first_seen` is re-stamped to the scan date."* **Today falsifies that specific wording:** it tracks `scanned_at_utc`'s calendar date, which is not the same field the feed labels `scan_date`. So `first_seen` is not merely wrong — **it is not even consistently derived from one clock between runs.** The underlying conclusion is unchanged and now doubly evidenced: **`first_seen` is a scan artefact, not an observation date. Only `captured_date` supports a claim, and only a MINIMUM one.**

**`posted_at` drift, re-checked on the same five tracked requisitions as 08-07: zero movement today.** Coinbase `gh_jid=8054862` holds at 2026-07-20; Gemini `gh_jid=8091954` holds at 2026-07-30; Phantom, and both Kraken reqs, stable. **Drift is episodic, not daily** — which makes it worse, not better, for measurement: an intermittent forward re-stamp cannot be corrected for by a constant offset. **(dd) stands and hardens.**

**Mandate item 4 — apply (dd) retroactively — NOT DONE, and named rather than buried.** No prior run record or `findings/` duration statement was re-labelled this run. The two Kraken Director, Paid Marketing reqs remain **open on or before 2026-07-24 and still open today: minimum 15 days, `captured_date`-floored.** The mechanical sweep across prior records is carried. **Second carry when it recurs.**

**`fetch_errors`: 6 entries** (Wormhole Foundation, **Aave — tracked, Lever 404**, Injective Labs, Bitwise, Chainlink Labs, Elliptic). Down from 7 — B2C2 cleared. **Watch (x) stays REOPENED**; Aave's 404 is the same one the absence panel has carried for eight runs.

#### Absence panel — four upstream gaps unfixed for an **eighth** run
`_absence.csv`: Aave + Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys. **OKX (Tier-1), Securitize, Rabby, Relai remain missing from the upstream company list.** Eighth run. Needs an owner outside the corpus run.

### 2. Agency claims / overlap matrix (deterministic)

18 files rewritten; 8 matrix rows; **1 OVERLAP: Sui (coinbound, rzlt)** — unchanged. `trend-data.json` `lastUpdated` still **2026-06-15**: **54 days stale.** Post-sync `git status` again shows only `_absence.csv` and `_chrome-queue.csv` modified — the class-2 output is byte-identical for a second consecutive run. `methodology.md` §6's phrase *"daily 18-agency panel"* remains inaccurate as written. **Eighth run.**

### 3. Regulator / gate-stack — **1 NET-NEW FILE, IN A NEW DIRECTORY, AND IT IS EXPLICITLY NOT A REGULATOR ACTION**

→ `../ad-platform-gates/google-ads-mica-casp-gate-eu-eea-2026-08-08.md` + `../ad-platform-gates/README.md` (both NEW).

**Three Google Advertising Policies pages fetched first-party, HTTP 200 each, no relay:**

| Page | Posted | Substance |
|---|---|---|
| *Updates to Cryptocurrency Advertising Policy in the EU (April 2025)* | 2025-03-24, eff. 2025-04-23 | CASP authorisation required across **27 named EU states**; transitional periods keyed to **MiCA Art. 143(3)** — **Finland 2025-06-30, France 2026-06-30, Germany 2025-12-30**; remedy = suspension after ≥7 days' warning |
| *Updates to Cryptocurrency Advertising Policy in France (July 2026)* | 2026-07-01, eff. 2026-07-01 | AMF **DASP registration no longer accepted**; MiCA CASP authorisation required |
| *Update to Cryptocurrencies and related products policy (August 2026)* | 2026-07-22, eff. **August 2026 (month only — no day asserted)** | Extends to **Iceland, Liechtenstein, Norway** — EEA complete |

**What is genuinely net-new, stated precisely, because the corpus already knew part of this.** Watch (m) has read *"Ad-platform gating — unchanged (Google France, 2026-07-01)"* since **2026-07-27**, and `findings/longitudinal-2026-06.md` line 333 logged the France change when it created the watch item. So the *France fact* is twelve days old in this corpus. **What was never held:**

1. **No primary URL had ever been fetched.** The France fact entered via search-result summary and sat as a parenthetical.
2. **The Article 143(3) keying** — the platform names the MiCA transitional article explicitly.
3. **Finland (2025-06-30) and Germany (2025-12-30).** The corpus believed this was one country and one date. **It is three countries and three dates, and two of them executed before the France one.** The gate has been running MiCA deadlines since **June 2025**.
4. **The August 2026 EEA extension.** Entirely new. In force this month.
5. **The enforcement mechanism** — account suspension, ≥7 days' warning. **The corpus holds no marketing-side remedy with a stated timeline from any regulator source in the post-deadline window. It now holds one from a platform.**
6. **The 27-country scope enumeration.**

**Directory choice, made autonomously and flagged for review.** `methodology.md` defines six classes and this fits none. Filing it under `regulator-filings/` risked a Phase-2 reader treating a platform's contractual rule as an enforcement action — the exact conflation the report must not make. A seventh directory with a README that opens *"THIS DIRECTORY DOES NOT CONTAIN REGULATOR ACTIONS"* is cheaper than that risk. **`methodology.md` needs a §7 or an explicit rejection of one. Escalated.**

**The distinction the file is built to preserve: the gate gates the ADVERTISER, not the AD.** Nothing in any of the three pages tests whether a communication is fair, clear and not misleading under Articles 7/66. **An authorised CASP running a materially misleading advertisement passes this gate without friction.** A fully-enforced credential gate sitting on top of an entirely unenforced conduct standard *is* the report's Theme-1 gate-stack argument.

**Also not claimed, and stated in the file:** no firm-level effect has been observed — a gate is not a casualty list; and whether Google enforces its own rule is **unmeasured**. The corpus has documented published promotional rules diverging from live promotional surfaces at Kraken, OKX, Bitpanda and BitMart. Google's estate deserves the identical suspicion.

**Conventional class-3 sweep: 0 net-new primary items.** BaFin / AMF / CONSOB / AFM / CySEC / ESMA August queries returned only secondary aggregations, undated compliance-vendor explainers, and out-of-window recurrences already held (the June-2025 nine-regulator finfluencer week of action; BaFin's 2025 influencer fines; ESMA's 2025 reverse-solicitation guidance). **None admitted. Day-38 named marketing-side silence holds.**

**NOT REACHED, NOT GUESSED:** ESMA `?sort_by=chronological` (provenance-blocked, **watch (w) still open for ESMA, days 1–8 uncovered**) · MAS PSN08 operative text · MAS enforcement register · **VARA, still never swept at source** · CONSOB comunicato PDFs · Google's standing crypto policy `answer/14009787` (linked by all three captures, **not fetched**) · six other distribution platforms. **No URL was fabricated.**

### 4. Operator statements — **0 NET-NEW. Class 4 stays at 5 files. FIFTH consecutive run with a refusal on the role/format gate.**

Two sweeps run; nothing meets §4's "verbatim quote + URL + speaker + date + role at time of statement."

**Refusals logged, because the gate only means something when applying it costs something:**
- **Haider Rafique, Global CMO, OKX** — qualifying role at a Tier-1 tracked firm; the only substantive interview surfaced is The Drum, **March 2025, out of window**. Refused on date. *(Separately noted: CoinDesk ran an "OKX's Rafique" policy item dated 2026-08-04 in its latest-news rail. **Not fetched, not claimed** — the rail gives a headline only, and a headline is not a statement. Named as a live class-4 candidate for the next run: it is an in-window, dated, first-party-quoted item from a qualifying operator at a tracked firm, which is exactly what class 4 has been failing to find for twelve days.)*
- **Michelle O'Connor, VP Marketing & Community, Uphold** — LinkedIn profile, undated, non-cohort. Refused on all three.

**Class 4 has produced 1 item in 13 days. Watch (l), 9th costing.** Six consecutive runs of empirical case for widening §4.

### 5. Layoffs — **2 ROWS PROMOTED (19 → 21). 1 NEW VERIFICATION FILE. Both of the mandate's verification targets turned out to be aggregator errors.**

→ `../layoff-tracker/_aggregator-date-integrity-2026-08-08.md` (NEW).

**Verification scorecard — four aggregator rows, each checked against its own linked source:**

| Row | Aggregator date | Verified | Aggregator figure | Verified |
|---|---|---|---|---|
| Coinbase −18% | 2026-03-05 | **2022-06-14** | −18% | of a **2022** workforce |
| FalconX −10% | 2026-07-15 | **2026-08-03** (corpus was right) | −10% | −10% |
| Polygon −60 | 2026-01-15 | **2026-01-16** | −30% | **firm-disputed** |
| Ethereum Foundation −54 | 2026-06-23 ✓ | 2026-06-23 | −54 / −20% | 54 / ~20% ✓ |

**Three of four dates wrong. Two of four figures unusable as listed. One row clean.**

**(a) Coinbase — the false positive.** Blockworks, **June 14, 2022**; 1,100 employees; headcount then "over 4,900"; SEC `coin-20220614.htm`; image path `/2022/06/`; market cap "just over $11 billion"; Armstrong on "over-hiring since 2021." Corroborated by NPR and AOL 2022 items in the same search. **The 05-05 −14% round remains Coinbase's only 2026 contraction in evidence and the Theme-5 spine holds.**

**→ And this forces a correction to yesterday's own headline.** The 08-07 recall measure (19 of 54 = 35%) used the aggregator's row count as its denominator. **At least one of those 54 is not a 2026 event.** **35% is a FLOOR, not an estimate**, and Phase 2 may write no stronger sentence than: *the corpus holds at least 19 of 54 rows listed by one public aggregator whose 2026 table is demonstrably contaminated with at least one pre-window event.* Yesterday's "single most important honest figure this corpus has produced about itself" needed a caveat within twenty-four hours. **Recorded, not softened.**

**(b) Polygon Labs January round — PROMOTED, dated 2026-01-16, percentage REFUSED.** CoinDesk 2026-01-16 (Acuna; "exclusive"). 60 roles, attributed to "a source familiar with the matter"; the firm declined to give a number. **The −30% the aggregator imported is the figure the CoinDesk piece was written to rebut** — spokesperson, verbatim: *"we've made adjustments to keep our overall headcount consistent"* and *"These changes are intended to balance additions from recent acquisitions, not to reduce the size of the company."*

**New Theme-5 category, and it should not be folded into the generic bucket:** this is a **contraction reframed as headcount-neutral rebalancing** — 60 out, acquired teams in, net flat, framed as not a reduction at all. **No other row in the tracker denies a contraction occurred while confirming departures.** Non-AI. Boiron's X post linked by CoinDesk, **not fetched** (provenance rule), `[VERIFY]` before quoting him.

**Sequence:** Polygon Labs now holds **both** 2026 rounds — January and July — six months apart, both non-AI, both M&A/repositioning-framed, same CEO announcing both on X.

**(c) Ethereum Foundation — PROMOTED as PERIMETER, and it closes an open `[VERIFY]`.** CoinDesk 2026-06-23: 54 positions, ~20%, in CoinDesk's own text rather than attributed to an anonymous source. This resolves the claim the FalconX row flagged on 08-05 as *"single-sourced inside an AI-assisted aggregator piece, no date, no primary — [VERIFY] before it is ever entered."* **Now dated, numbered and anchored.** The EF's own blog post (`blog.ethereum.org/2026/06/23/ef-structure`) is **linked by CoinDesk and was REFUSED by the fetch tool's provenance rule** — `[VERIFY]`, and it should replace CoinDesk as `source_url` when captured. **7th consecutive non-AI rationale.**

**Theme-1 structural datum, third instance:** the restructure groups EF's work into five clusters **including a dedicated institutional layer** for "enterprise engagement, financial infrastructure, and policy coordination" — contraction accompanied by an explicitly named new operating unit, as with Coinbase's AI-native pods (05-05) and Kraken's "natively AI growth engine" (05-19). **State the shape; do not assert a trend from three.**

**→ COHORT ESCALATION, NEW: the Ethereum Foundation is not in `tracked-firms.md`.** Stratum 2 lists Sui, Aptos, Solana, Aave, Polygon, Optimism, Arbitrum, Avalanche. **The largest and oldest L1 foundation is absent from the report's L1/L2 foundation panel**, so a 54-role contraction at the reference L1 foundation enters this corpus as perimeter. That is a cohort-definition gap, not a data gap.

**Standing finding UNCHANGED, cohort-scoped: no TRACKED firm's 2026 contraction has named marketing as an affected function.** Neither new row names a function. The tracker-scoped version remains broken by the perimeter Gnosis row, whose marketing claim is still single-sourced to an X post and whose two primaries remain uncaptured — **seventh run carried.** The July AI-framing ratio remains **un-restatable**.

### 6. NorthPoint longitudinal panel

`trend-data.json` **54 days stale**. No trend claim made.

---

## What this run did to the mandate

| # | 08-07 recommendation | status |
|---|---|---|
| 1 | Promote Polygon + Ethereum Foundation, **and no others**, primaries first | **DONE.** Both primaries fetched, both promoted, nothing else imported. Polygon's percentage refused on the primary's own evidence. |
| 2 | Resolve Coinbase 2026-03-05 and the FalconX date conflict | **DONE — and both were aggregator errors.** Coinbase is a 2022 event; FalconX confirms the corpus's date. Yesterday's recall headline downgraded to a floor as a consequence. |
| 3 | 08-09 teardown with watch (z) folded in | **on schedule. Tomorrow.** Not touched today. |
| 4 | Apply the (dd) minimum-duration rule retroactively | **NOT DONE — carried, and named here rather than buried.** Mechanical; still the cheapest quality win in the repo. |
| 5 | Escalate six items | **DONE — below. Two closed, three carried, two new.** |

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged.
- **(b) First named post-deadline NCA marketing-side action** — **day-38 silence HOLDS, and today it stops being an absence of consequence.** Legs 1–3 (structural / prioritisation / forbearance) unchanged; **a fourth element is now available and it is not a leg of the null but its counterpart: the credential gate executed on schedule, privately.** Never print "silence."
- **(c) Capture panel** — untouched. **08-09 teardown is tomorrow and carries watch (z).**
- **(d) Agency panel staleness — 54 days**, byte-identical output twice running. §6 wording must change. **8th run.**
- **(e′) Cadence** — DISCHARGED, four consecutive on-time runs.
- **(f) Friday nomination cadence** — **yesterday was Friday and it was not run.** `inbound-nominations.md` still does not exist. `README.md` still tells the public nominations are "read every Friday." Unowned, unkept, **published**.
- **(g) Coinbase n=1** — **the specific threat raised on 08-07 is DISCHARGED**: the −18% row is a 2022 event and the Theme-5 spine is safe. The general item — n=1 as a basis for generalisation — is untouched and **stays open**.
- **(h′) Layoff rationale correlates with firm type** — **REJECTED.** Both new rows are non-AI; 7th consecutive. Do not resurrect. July ratio still un-restatable.
- **(i) Kraken paid-media build-out** — two Director, Paid Marketing reqs **open on or before 2026-07-24, still open: minimum 15 days**, `captured_date`-floored.
- **(j) Senior-leader exits** — superseded by (aa).
- **(k) Chrome-lane instrumentation gap** — unchanged.
- **(l) §4 too narrow AND provenance-blind** — **9th costing. Six-for-six.** Rafique refused on date; a live in-window CoinDesk item named for next run.
- **(m) Ad-platform gating** — **DISCHARGED AS A WATCH ITEM AND PROMOTED TO A SOURCE CLASS.** Carried as an unsourced parenthetical from 07-27 to 08-07; primaries fetched today; four facts recovered that the corpus did not hold. **Superseded by the `ad-platform-gates/` directory and by (gg).**
- **(n) Full-range re-sweep of classes 3, 4, 5** — class 5 partially executed again today (4 rows verified, 2 promoted). **Classes 3 and 4 remain unmeasured.** Its class-5 measurement is now known to rest on a contaminated denominator.
- **(o) Date the document, never an event held about it** — **held, and load-bearing today.** Polygon dated 2026-01-16 (report date) not 01-15 (aggregator).
- **(p) Absence claims tested against firms' OWN channels** — not advanced.
- **(q) Agency matrix measures the crypto-native segment** — unchanged.
- **(r) Absence panel needs a "structural withdrawal" category** — unchanged.
- **(s) Robinhood row misclassified** — unchanged, **9th run.**
- **(t′) Class 1 is a FLOW register presented as a STOCK register** — unchanged.
- **(u) Brand absorption defeats name-keyed sweeps** — unchanged; alias table still unbuilt.
- **(v) NCA sweep** — 6 of 6, COMPLETE.
- **(w) Class-3 sweep vocabulary AND method** — **STILL OPEN FOR ESMA.** `?sort_by=chronological` provenance-blocked. Days 1–8 uncovered.
- **(x) `fetch_errors`** — **REOPENED, 6 entries**, incl. tracked-firm Aave (8th run).
- **(y) Pre-2026 class-1 rows are arithmetic inferences** — unchanged.
- **(z) Promotional surfaces decoupled from operational state** — folded into tomorrow's 08-09 teardown as its panel arm, or killed there. **No sixth carry.**
- **(aa) Announcement vs effective dates** — **NOT IMPLEMENTED, 6th run.**
- **(bb) Class-1 feed-health guard** — passing, **but see (ff)**.
- **(cc) Secondary layer going machine-written** — `capture_ai_disclosure` populated on the new class-7 file. Not retroactive.
- **(dd) Class 1 cannot measure time-to-fill** — **CONFIRMED AND REFINED.** `first_seen` tracks `scanned_at_utc`'s date, not the feed's own `scan_date` — so it is not consistently derived between runs, let alone a first-seen. `posted_at` drift is **episodic, not daily** (zero movement today on the same five reqs that produced two drifts yesterday), which makes it uncorrectable by a constant offset. Retroactive re-labelling still not done.
- **(ee) A source cited once is a source not used as an instrument** — **second confirmation in two days, and this time it was the corpus's own watch list.** The Google France fact sat as a parenthetical for twelve days with no URL ever fetched; fetching it recovered four unheld facts. **Generalise: a fact carried as a watch note is a fact not being used as evidence. Audit the watch list for others.**
- **(ff) NEW — the feed-health guard tests direction, not magnitude.** Fingerprint moved **+1** today (2,139 → 2,140) across 147 companies and ~23.5 hours, versus +49 yesterday. A +1 passes the guard exactly as a +49 does. **A partially-failed scan that wrote one row would also pass.** The guard needs a magnitude floor calibrated on the observed distribution, or an explicit statement that it detects only total freeze.
- **(gg) NEW — `methodology.md` has six classes and the corpus now has seven directories.** The ad-platform gate is real, dated, primary-sourced, and material to Themes 1 and 4, and it fits no defined class. It was created this run in `corpus/ad-platform-gates/` with a self-documenting README. **§7 must be written or the directory must be rejected on the record — a corpus whose published methodology does not describe its own contents is exactly the defect this report documents in other firms' estates.**

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **FEED HEALTH HEALTHY, 14.3h, fingerprint 2,139→2,140 (+1).**
2. Direct read of `open-positions.json` — `scan_metadata`, all 29 filtered rows, `fetch_errors`. → (dd) confirmation, (ff).
3. `git status` post-sync (via `GIT_INDEX_FILE` workaround) → class-2 output byte-identical.
4. Repo dedup: 08-07 run record in full; tracker 19 rows; crossref in full; repo-wide grep `google|adspolicy|ad-platform` and `ethereum foundation` **before** writing either new file. **This is what established that the France fact was already held as a watch note, and bounded today's net-new claim honestly.**
5. WebSearch — Polygon Labs January 2026 layoffs → CoinDesk primary.
6. **`web_fetch` CoinDesk 2026-01-16 Polygon** → HTTP 200. Spokesperson rebuttal of −30% captured verbatim.
7. WebSearch — Ethereum Foundation June 2026 layoffs → CoinDesk primary.
8. **`web_fetch` CoinDesk 2026-06-23 Ethereum Foundation** → HTTP 200. 54 positions / ~20%; five clusters; leadership exodus.
9. `web_fetch` `blog.ethereum.org/2026/06/23/ef-structure` → **BLOCKED by provenance rule. Not fetched, not guessed.** `[VERIFY]` carried.
10. WebSearch — Coinbase March 2026 18% Blockworks → surfaced the Blockworks item **plus 2022-vintage NPR/AOL headlines**, which is what raised the suspicion.
11. **`web_fetch` Blockworks Coinbase 18%** → HTTP 200. **June 14, 2022. THE RUN'S SECOND RESULT.**
12. WebSearch — FalconX Bloomberg 10% → Bloomberg URL carries `2026-08-03` in its path. **Corpus date confirmed; aggregator wrong by 19 days.** Bloomberg itself paywalled, **not fetched**.
13. WebSearch — MiCA marketing-communications enforcement August 2026 → **0 net-new primary regulator items**; surfaced the Google policy page.
14. **`web_fetch` Google Ads — August 2026 EEA update** → HTTP 200.
15. **`web_fetch` Google Ads — France July 2026 update** → HTTP 200.
16. **`web_fetch` Google Ads — EU April 2025 baseline** → HTTP 200. **Article 143(3) keying + three Member-State deadlines. THE RUN'S PRINCIPAL RESULT.**
17. WebSearch — BaFin/CONSOB/CySEC/AFM crypto advertising August 2026 → **0 net-new primary items.** Secondary/undated/out-of-window only. None admitted.
18. WebSearch ×2 — crypto CMO / VP Marketing statements → **class-4 refusals** (Rafique out-of-window; O'Connor undated non-cohort).
19. **Not reached / not guessed:** ESMA `?sort_by=chronological` · PSN08 · MAS register · VARA · CONSOB PDFs · Google `answer/14009787` and six 2025–26 adjacent change-log entries · Meta/X/TikTok/Apple/Google Play/Reddit/LinkedIn ad policies · Bloomberg and Boiron originals. **No URL was fabricated.**

---

## Net-new / changed this run

- `corpus/ad-platform-gates/README.md` — **NEW DIRECTORY, NEW SOURCE CLASS.** Why it exists, what qualifies, the never-print-a-gate-as-enforcement rule, six unswept platforms named as gaps.
- `corpus/ad-platform-gates/google-ads-mica-casp-gate-eu-eea-2026-08-08.md` — **NEW.** Three first-party captures verbatim; Art. 143(3) keying; FI/DE/FR deadline chronology; EEA extension; ≥7-day suspension remedy; explicit claimed/not-claimed split; the gates-the-advertiser-not-the-ad distinction.
- `corpus/layoff-tracker/_aggregator-date-integrity-2026-08-08.md` — **NEW.** Coinbase-2022 false positive with six independent date markers; FalconX resolved in the corpus's favour; the 4-row verification scorecard; **35% recall downgraded to a floor**; Bybit/OKX re-hypothesised as date errors rather than arithmetic errors, with a named test.
- `corpus/layoff-tracker/2026-layoff-tracker.csv` — **19 → 21 rows.** Polygon Labs (Jan) + Ethereum Foundation.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` — date re-stamps (sync).
- `findings/longitudinal-2026-06.md` — day-38 shift appended.
- **Operator statements: unchanged at 5 files. Job postings: 0 net-new (genuine absence, guard-asserted). Agency claims: byte-identical.**

---

## Recommendation for next run

1. **Run the 08-09 teardown as pre-committed, with watch (z) as its panel arm — or kill (z) in that record.** Highest-value scheduled item in the repo, and it is due.
2. **Fetch the OKX / Rafique CoinDesk item dated 2026-08-04.** It is in-window, dated, first-party-quoted, and from a qualifying operator (Global CMO) at a Tier-1 tracked firm — the exact shape class 4 has failed to find for thirteen days. It was surfaced in a navigation rail today and correctly not claimed. **One fetch. If its quotes are marketing-substantive it ends the class-4 drought; if they are policy-only it is a documented refusal on substance rather than format, which is itself the first evidence that §4's problem is supply rather than definition.**
3. **Apply the (dd) rule retroactively. Second carry. It is mechanical, it takes one pass, and it stops a wrong duration reaching Phase 2.**
4. **Audit the watch list the way the aggregator was audited.** (ee) has now fired twice in two days, and the second time the unread source was **the corpus's own watch note**. Every watch item that asserts a fact without a fetched URL is a candidate for the same treatment the Google France note got today — which recovered four unheld facts from twelve days of parenthetical.
5. **Escalate to Jukka — six items, in order:**
   - **(i) `methodology.md` §1 must be re-scoped. EIGHTH run.** Time-to-fill is not derivable from class 1; today added that `first_seen` is not even consistently derived between runs. §1 promises five extracted fields and cannot supply one of them. **Still the one thing in this repo that could embarrass the report.**
   - **(ii) `methodology.md` needs a §7 for ad-platform gates, or an explicit rejection.** NEW. The corpus now has seven directories and a published methodology describing six. The seventh holds the strongest Theme-1/Theme-4 mechanism found in a fortnight.
   - **(iii) Commission the class-3 and class-4 halves of the (n) re-sweep.** Class 5's recall is now known to be **at least** 35% against a **contaminated** denominator — the measurement got weaker, not stronger, on inspection. Classes 3 and 4 have no measurement at all. Phase 2 starts within days.
   - **(iv) `methodology.md` §4 needs widening plus an earned-vs-placed provenance field.** Six-for-six.
   - **(v) Four upstream company-list gaps — OKX (Tier-1), Securitize, Rabby, Relai — EIGHTH run**, plus a new one: **the Ethereum Foundation is absent from the Stratum-2 panel**, so the reference L1 foundation's 54-role contraction enters as perimeter. Needs an owner outside the corpus run.
   - **(vi) The Friday nomination promise in `README.md` is unkept and unowned.** Yesterday was Friday. Nothing was read. No intake file has ever existed. It is a **published** commitment; either assign the mailbox read or amend the README.

---

## Postscript — the DE race fired again, worse than yesterday, and this section originally said it hadn't

**This paragraph was written before the commit step and was wrong. It is corrected here rather than deleted, because a corpus that documents other people's stale published surfaces cannot quietly repair its own.** As drafted, it read: *"No new DE sync collided with this run's write window… that is luck, not a fix."*

**What actually happened.** At **15:59:15 +0300**, while this run was still writing, the distribution-engineer's 15-minute loop ran `git add -A` and committed **six** of this run's files as `0a58476 distribution-engineer: sync 5 change(s) [2026-08-08 15:59]` — and pushed them:

```
corpus/ad-platform-gates/README.md                                  (NEW, 39 lines)
corpus/ad-platform-gates/google-ads-mica-casp-gate-eu-eea-2026-08-08.md (NEW, 159 lines)
corpus/layoff-tracker/_aggregator-date-integrity-2026-08-08.md      (NEW, 87 lines)
corpus/layoff-tracker/2026-layoff-tracker.csv                       (19 -> 21 rows)
corpus/job-postings/_absence.csv, _chrome-queue.csv                 (sync re-stamps)
```

**Second consecutive day. Yesterday it took five files; today it took six, including both files of an entirely new source class and the two-row promotion — the substantive output of the run.** By the time this run reached its own commit step, `git add -A` found only the run record and `findings/`. This corpus's day-38 commit therefore carries its narrative and none of its evidence; the evidence is on `origin/main` under a message that names none of it. Note also the message says **"5 change(s)"** while committing **six files** — the DE's own count is wrong, so the log is not merely uninformative, it is inaccurate.

**Content integrity: verified intact.** All six files were fully written before 15:59 and every one is byte-correct in `HEAD`; the tracker reads 21 rows; the working tree is clean against `HEAD`. **No partial write was committed this time.** That is the second piece of luck in two days, and it is the only thing standing between this arrangement and a half-written corpus file on `origin/main` with nothing marking it as such.

**No history rewrite attempted.** `0a58476` is pushed. Rewriting a pushed corpus commit to improve its message is a worse trade than an imperfect log.

**→ Escalation (vii), promoted from yesterday's (vi) and now the highest-priority infrastructure item in this repo.** It was raised once, nothing changed, and the failure recurred within twenty-four hours at greater scope. The DE sync loop must **exclude this repo**, or **skip any repo modified inside the last N minutes**, or **the corpus run must take a lock the DE respects**. Until then, `git log --oneline` is no longer a reliable chronology of what the corpus learned and when — **two of the last four commits on this branch are DE syncs that swallowed a corpus run's output.** This is precisely the defect the corpus documents in other firms' promotional estates: two writers, one surface, no coordination.

**Working-tree state at run end:** clean against `HEAD`. The run record and `findings/` are committed with a dated message (`958cb26`) and left **ahead of `origin/main`** for the DE to push, alongside this correction. `git push` not attempted (no auth in autonomous runs).

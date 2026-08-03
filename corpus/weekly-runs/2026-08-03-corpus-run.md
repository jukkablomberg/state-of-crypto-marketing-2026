# Corpus-assembly daily run — 2026-08-03 **(day 33 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-03 (Monday).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, taken verbatim from the 08-02 recommendations:** (1) EEA-egress re-read of the four lapsed surfaces; (2) **sweep AFM**, then CNMV; (3) **execute watch (w) properly** — against ESMA's and each NCA's own news index, not through a search engine; (4) re-check the lapsed surfaces on 08-09 to date the teardown; (5) test watch (z) across the panel; (6) capture the CONSOB July primary; (7) `[VERIFY]` the Conlan departure; (8) escalate five items.
**Dedup baseline read before writing:** `2026-08-02-corpus-run.md` in full (head + tail incl. all watch items and the audit trail); `promotional-teardown-checkpoint-2026-08-02.md`; `layoff-tracker/2026-layoff-tracker.csv` all 17 rows; `regulator-filings/` (12 files, index + AFM 04 file in full); `operator-statements/` (5); `marketing-campaigns/` (7); `findings/longitudinal-2026-06.md` tail; `_absence.csv`; `open-positions.json` `scan_metadata`. Cadence check: **08-03 run fired; the 07-31 gap remains the only miss.**

---

## Headline result

**Three things, in descending order of consequence.**

**1. Watch (v) went to its designated falsifier and did not break — and the sweep was finally run the way (w) always asked for.** AFM's **own professional news index** was fetched directly, not queried through a search engine. It carries twelve dated items back to 16 April 2026 — the entire post-deadline window in one page — and **the last crypto item on it is the 16 April advertising review. 109 days of nothing.** AFM published exactly **two enforcement instruments** in that window, both tagged "Measure" on its own index: **Euronext Amsterdam (13 May)** and **Arrowstreet Capital (22 April)**. Neither is a CASP; neither is marketing-side. **The instrument that would have broken the null exists, is in use, and was not pointed at crypto marketing.** → `../regulator-filings/afm-cnmv-post-deadline-index-sweep-2026-08-03.md` (NEW FILE).

**2. The teardown finding replicated at day 3 — and every re-read keeps finding more inventory.** Kraken `/europe-switch` is byte-comparable for a **third** day. And two surfaces neither prior checkpoint knew about are now in the corpus: **`blog.kraken.com/news/industry-news/europe-mica-switch`** (published 19 Jun 16:41 UTC, **modified 16:58 UTC the same day and never again**, Kraken's own tags: *"Promotions"*, present-tense *"we're rewarding traders who make the move"*, three enrolment CTAs) and **`okx.com/en-eu/…`** — the **EEA-locale** twin of the `/en-us/` page captured on 08-02, published 12 Jun, **updated 30 Jun**, untouched since close. **Running count: 7 surfaces identified, 6 fetched, 5 confirmed lapsed.** → `../marketing-campaigns/promotional-teardown-checkpoint-2026-08-03.md` (NEW FILE).

**3. The geofence caveat got its first hard evidence, and it cuts against the firms.** The OKX `/en-eu/` page **detected the fetch's US origin and said so in a banner** — *"Looks like you're in the United States. Switch to the United States site for products available in your region."* — **and then served the full EEA-only campaign, present tense, live CTAs, anyway.** The geo-layer fired and changed nothing about the promotional payload. This does **not** discharge the EEA-egress caveat. It moves the bar: the question is no longer *"is there a geofence"* but *"does the geofence do anything to the offer"*.

**Day-33 named marketing-side enforcement silence HOLDS**, now five-jurisdiction-tested and tested at the two NCAs most likely to break it.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-08-03
source A (jobs)   scan_date: 2026-08-03
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

**Feed-health guard: HEALTHY.** `scan_metadata` — `scanned_at_utc 2026-08-02T21:46:03Z`, `scan_date 2026-08-03`, **147 companies** (87 API / 60 chrome-pending), **2,087 jobs fetched** (2,088 → 2,087, −1), **27 after filter**, **`new_count` 0**, **`url_verification_dropped` 0**, `still_open_count` **27** (flat for a third day; no tracked role closed). ATS breakdown unchanged in shape: greenhouse 22, ashby 35, proprietary 59, lever 19, workable 5, breezy 2, teamtailor 2, personio 1, recruitee 1, comeet 1.

**Third consecutive 0-new day.** This is genuine idempotency, not a broken feed — the fetch total moved by one job and the filter/verification counters are clean. Repo diff from the sync is `_absence.csv` / `_chrome-queue.csv` date re-stamps and the dated agency snapshots.

**Watch (y) unchanged and unaddressed:** class 1's only pre-2026 rows remain arithmetic inferences from relative Getro board labels. No backfill was attempted this run (it belongs in the upstream scanner lane, not here).

#### Absence panel — four upstream gaps unfixed for a **fourth** run
`_absence.csv`: Aave (Lever 404) + Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys (proprietary, chrome-pending). **OKX (Tier-1), Securitize, Rabby, Relai remain missing from the upstream company list.** No config write attempted — that is the sales funnel's repo, and an autonomous corpus run should not silently edit it.

**The irony recorded on 08-02 got worse today, not better.** OKX is absent from the class-1 instrument entirely — and OKX supplied **two** of this run's strongest primaries (the EEA-locale lapsed surface and the geo-notice finding), plus its full three-licence MFSA stack, first-party. **Fourth consecutive run carrying this. It needs an owner.**

### 2. Agency claims / overlap matrix (deterministic)

18 agency-claims files rewritten; 8 matrix rows; **1 OVERLAP: Sui (coinbound, rzlt)** — unchanged for the Nth run. **`trend-data.json` `lastUpdated` is still 2026-06-15 — the panel is now 49 days stale.** Watch (d) stable-by-decision; `methodology.md` §6's phrase *"daily 18-agency panel"* remains inaccurate as written and must be re-worded before Phase 2. Escalation stands, **fourth run**.

### 3. Regulator — **1 NET-NEW FILE. Watch (v) 5/6. Watch (w) EXECUTED AS SPECIFIED for the first time.**

→ `../regulator-filings/afm-cnmv-post-deadline-index-sweep-2026-08-03.md` (NEW).

**AFM (NL) — the priority item, swept at the source.** `https://www.afm.nl/en/sector/actueel`, page 1, fetched direct. Twelve dated items, 16 Apr → 10 Jul 2026.

- **No crypto item since 16 April 2026 — 109 days.** The last one is the thematic advertising/cost review already in the corpus.
- **Two enforcement "Measure" items in the window** (AFM's own label, `mr-` URL prefix, mechanically identifiable): **Euronext Amsterdam 13 May** (open-access rules), **Arrowstreet Capital 22 April** (short-position notifications). **Neither crypto, neither marketing-side.**
- The one NCA that put an executive board member on the record with *"The period of leniency has ended"* (16 Apr) has published nothing since.
- **Consumer warnings surface:** four most recent — Capitvo Inc., Blue Fire Consulting, **Bitkelttrade.com**, Avaleap — **all under AFM's `/boilerroom/` path.** Crypto-named entities appear, and they appear as unauthorised-entity warnings. Perimeter, not conduct. **Dates not captured; individual warning pages not fetched; no date asserted.**

**CNMV (ES) — the second-likeliest breaker, and the reason the null means something.** Captured near-primary (Cuatrecasas, 11 Dec 2023): CNMV opened its **first-ever sanction file under Circular 1/2022** against **MIOLO DESARROLLOS, S.L.** over two mass campaigns (Sep + Nov 2022) — Norma 5 (missing risk warning) and Norma 7 (mass campaigns >100,000 audience must be pre-notified 10 days ahead), pleaded as **four serious infractions**. CNMV publicised the *opening* deliberately, and had by then run **210+ supervisory actions across 1,300+ advertising pieces**.

> **WINDOW FLAG, stated in the file and repeated here: 11 Dec 2023 is OUT OF WINDOW** under the December-2024 rule. It is entered as **interpretive context for a live null**, never as a 2026 event.

**Why the null is now a stronger claim than "silence".** The two NCAs with demonstrated willingness to act on *advertising* rather than *authorisation* — AFM (thematic review, quantified defect rates, leniency-ended) and CNMV (bespoke Circular, sanction-file precedent, deliberate publicity) — are exactly the two that would have broken it. Both tested. Neither did.

**And the honest counterweight, which must ship with the finding.** AFM's April release states supervisory letters were going to Dutch firms and ten international firms were being referred to home NCAs. **Neither instrument is public.** So the defensible Phase-2 wording is not *"regulators are doing nothing"*, it is:

> **The post-deadline supervisory response to crypto marketing is running through non-public channels — supervisory letters, cross-border referrals, perimeter warnings — and not through named, published conduct cases against authorised firms.**

**Watch (w) — EXECUTED for AFM, still open elsewhere.** This run fetched an NCA's own index directly for the first time, which is what (w) has asked for since it was opened, and it produced the cleanest class-3 result the corpus has: a 109-day null read off the regulator's own publication list rather than inferred from search coverage. **ESMA's own index was still not swept.** (w) stays open, now **partially discharged with a proven method.**

**NOT REACHED, NOT GUESSED:** ESMA news index; CNMV `Advertencias` register (the 07 register read stands); the CNMV `webservices/verdocumento` comunicado seen inside the Cuatrecasas text; CONSOB's July `comunicazione` (08-02's `[VERIFY]` on 24 sites / 1,793 / 233 crypto **remains open, second run**); AFM individual warning pages. **No URL was fabricated.**

### 4. Operator statements — **0 NET-NEW. Class 4 stays at 5 files. One qualifying-looking item REFUSED on the role gate.**

The CMO / Head-of-Marketing sweep for August surfaced no in-window verbatim statement by a CMO / VP Marketing / Head of Brand / Head of Growth at a tracked firm.

**One refusal worth logging, because the gate only matters when applying it costs something.** The new Kraken blog surface carries an on-the-record named quote — **Andrew Mulvenny, "Kraken Head of Crypto-Asset Service Provider Trading Platform"**, on MiCA authorisation and *"our enduring commitment to trust, compliance"*. It is dated, verbatim, first-party, at a Stratum-1 firm, and sits inside a promotional artefact. **It does not qualify under §4 — the role is a trading-platform head, not a marketing seat.** Recorded in the campaign file; **not counted in class 4.**

**Watch (j) — the Conlan `[VERIFY]` is now a DATE CONFLICT, not an open verification.** The 08-02 run took CoinGape's statement that *"long-time CMO Rachel Conlan stepped down in June 2026 — the MiCA deadline month"* and filed it `[VERIFY]`. **The corpus already holds the answer and it disagrees:**

- `operator-statements/sport-sponsorship-reset-2026-05.md` §5 — *"Binance CMO Rachel Conlan exit + Eowyn Chen interim (**12 May 2026**)"*.
- `regulator-filings/binance-mica-eu-exit-2026-06.md` — *"Rachel Conlan departed **~2026-06-15**, Eowyn Chen interim (captured May; longitudinal note)"*.

So the corpus holds an **announcement dated 12 May** and a **departure dated ~15 June**, and the publisher compressed both into *"stepped down in June 2026."* These are reconcilable (announce in May, effective in June) and that is the most likely reading — **but the corpus must not print "stepped down in June" as if it were the whole event, and must not print "the MiCA deadline month" as a rhetorical flourish when its own record dates the announcement to May.** Same defect class as the Crypto.com row: **Steven Kalifowitz's exit was announced 5 May 2026, effective 30 June 2026** (already held). **Announce-date and effective-date are different objects and the corpus has been sloppy about which one it means.** New watch **(aa)**.

**Class 4 is static for the 2nd day and has produced 1 item in 8 days.** Watch (l) unchanged: §4 needs both a wider inventory and an earned-vs-placed provenance field.

### 5. Layoffs — **0 NET-NEW. Tracker stays at 17 rows.**

August sweep produced no new 2026 marketing-team contraction. Everything returned was already tracked: BitMEX (07-23), Luno (07-28), Crypto.com (03-19), Kraken (05-14), Coinbase (05-05), Gemini (02-05). Aggregate round-ups ("7,000+ jobs gone", CryptoJobsList totals) were **not entered** — the Exodus row already documents why aggregator per-firm figures are refused (77 SEC-sourced vs 54 aggregator).

**Standing finding unchanged, cohort-scoped: no TRACKED firm's 2026 contraction has named marketing as an affected function.** The tracker-scoped version remains broken by the perimeter Gnosis row, whose marketing claim is still single-sourced to an X post and whose two primaries remain uncaptured under the fetch provenance rule. **Highest-value verification item in the corpus, unchanged, and not advanced this run.**

### 6. NorthPoint longitudinal panel

`trend-data.json` **49 days stale**. No trend claim made — that is what falsified watch (e).

---

## What this run did to the mandate

| # | 08-02 recommendation | status |
|---|---|---|
| 1 | EEA-egress re-read of the four lapsed surfaces | **PARTIAL — and better than expected.** No EEA egress available to an autonomous run. But the OKX geo-notice supplies the first direct evidence about what the geo-layer *does*: it detects, it announces, and it does not gate the offer. Caveat stays; the bar moved. |
| 2 | Sweep AFM, then CNMV | **AFM DISCHARGED** at its own index. **CNMV partial** — pre-window conduct precedent captured; 2026 register not re-read. |
| 3 | Execute watch (w) properly | **DONE for AFM** — first direct NCA-index fetch in the corpus, and it produced the cleanest class-3 result to date. **ESMA index still unswept.** |
| 4 | Re-check lapsed surfaces on 08-09 | **pre-dated:** day-3 read done today; 08-09 still the scheduled time-to-teardown measurement. |
| 5 | Test watch (z) across the panel | **NOT DONE.** Carried. |
| 6 | Capture the CONSOB July primary | **NOT DONE.** `[VERIFY]` carried, second run. |
| 7 | `[VERIFY]` the Conlan departure | **RESOLVED INTO A DIFFERENT PROBLEM** — see class 4. It is an announce-vs-effective date conflict, and it generalises. New watch (aa). |
| 8 | Escalate five items | **DONE** — below, all five carried, one hardened. |

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged.
- **(b) First named post-deadline NCA marketing-side action** — **day-33 silence HOLDS, five-jurisdiction-tested, and tested at both NCAs with an advertising-conduct track record.** Scope unchanged: named marketing-side actions against identified authorised firms. **Phase-2 wording must be the "non-public channels" formulation, not "silence".**
- **(c) Capture panel** — **2/2 re-tested still live at day 3; 2 new surfaces found.** Sub-items: (i) EEA-egress read still open, bar moved; (ii) **08-09 time-to-teardown measurement is now the highest-value scheduled item in the repo**; (iii) Gate + Coinbase own-channel sweep still unswept; (iv) **NEW: the denominator problem** — the corpus does not know how many surfaces any of these campaigns had, and must say so.
- **(d) Agency panel staleness — 49 days.** Stable-by-decision; §6 wording must change. **4th run.**
- **(e′) Cadence** — **08-03 fired.** Two clean days since the 07-31 miss. **No trend claim made.**
- **(f) Friday nomination cadence** — next check **08-07**. No `inbound-nominations.md` exists; none have ever arrived.
- **(g) Coinbase n=1** — void as filed; re-file only after backfill.
- **(h′) Layoff rationale correlates with firm type** — unchanged, n=9 with counter-example. **Do not print.**
- **(i) Kraken paid-media build-out** — unchanged; survives. **Kraken is now quintuple-loaded**: 05-14 cut · 07-23 reqs ×2 · three lapsed owned surfaces · a three-way internal date conflict · the Forbes badge conflict.
- **(j) Senior-leader exits** — **superseded in part by new watch (aa).** Conlan and Kalifowitz both now known to have announce/effective date splits.
- **(k) Chrome-lane instrumentation gap** — unchanged.
- **(l) §4 inventory too narrow AND provenance-blind** — unchanged, **5th costing**. Class 4 static 2nd day, 1 item in 8 days.
- **(m) Ad-platform gating** — unchanged.
- **(n) Full-range re-sweep of classes 3 and 5** — classes 1 and 2 historical backfill still not run.
- **(o) Date the document, never an event held about it** — held, and **(aa) is its sharper sibling.**
- **(p) Absence claims tested against firms' OWN channels** — **advanced:** Kraken (3 surfaces), OKX (2 fetched + 1 identified). **Still unswept: Coinbase, Gate, Bybit, Crypto.com, Gemini, Sui, all of Strata 2 and 4.**
- **(q) Agency matrix measures the crypto-native segment** — unchanged.
- **(r) Absence panel needs a "structural withdrawal" category** — unchanged.
- **(s) Robinhood row misclassified** — unchanged, **5th run**.
- **(t′) Class 1 is a FLOW register presented as a STOCK register** — unchanged; flow = 5 rows / 4 firms / 28 days.
- **(u) Brand absorption defeats name-keyed sweeps** — unchanged; alias table still unbuilt.
- **(v) NCA sweep** — **5 of 6.** FR, DE, IT, CY, **NL** all replicate perimeter-not-conduct. **ES partial.** The designated falsifier did not break it.
- **(w) Class-3 sweep vocabulary AND method** — **method proven.** Direct NCA-index fetch executed for AFM and it outperformed every search-engine pass. **ESMA index still unswept; apply the same method there next.**
- **(x) `fetch_errors` null** — closed.
- **(y) Pre-2026 class-1 rows are arithmetic inferences** — unchanged, unaddressed.
- **(z) Promotional surfaces decoupled from operational state** — **strengthened and given a second mechanism.** Day 3: not one page left up, but a *multi-surface campaign whose teardown is scoped narrower than its launch*. **Cheapest panel-wide test still unrun.**
- **(aa) NEW — the corpus conflates announcement dates with effective dates.** Conlan: announced 12 May, effective ~15 Jun, publisher says "June". Kalifowitz: announced 5 May, effective 30 Jun. **Every Theme-1 claim about "the MiCA deadline month" is exposed to this.** Fix before Phase 2: every personnel and campaign row needs `date_announced` and `date_effective` as separate fields, and no synthesis claim may rest on a date whose type is unrecorded.

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2; 0 new postings, 18 agency files, 8 matrix rows.
2. Direct read of `prospects/open-positions.json` `scan_metadata` → feed-health guard HEALTHY, 2,087 fetched / 0 new.
3. Repo dedup baseline reads — 08-02 run record, layoff tracker (17 rows), regulator/operator/campaign indexes, findings tail.
4. **`web_fetch https://www.afm.nl/en/sector/actueel`** → HTTP 200. **The run's best result: 12 dated items, no crypto since 16 Apr, 2 non-crypto Measures.**
5. **`web_fetch https://www.afm.nl/en/sector/actueel/2026/apr/pb-reclame-informatie-casps`** → HTTP 200; re-verified the April primary and recovered the index URL into provenance.
6. **`web_fetch https://www.afm.nl/en/consumenten/waarschuwingen`** → HTTP 200; four boiler-room warnings, `/boilerroom/` path, **no dates captured**.
7. WebSearch — AFM waarschuwing crypto reclame augustus 2026 → nothing post-deadline.
8. WebSearch — AFM crypto advertising enforcement 2026 CASP → surfaced the April primary + AFM sector pages.
9. WebSearch — AFM nieuws juli 2026 MiCA handhaving → nothing AFM-published post-deadline.
10. WebSearch — CNMV advertencia criptoactivos julio 2026 publicidad → surfaced the Circular 1/2022 material.
11. **`web_fetch cuatrecasas.com/…/cnmv-incoa-expediente-publicidad-criptoactivos`** → HTTP 200; **the MIOLO expediente, 11 Dec 2023, flagged OUT OF WINDOW.**
12. WebSearch — Kraken europe-switch €1M prize draw → surfaced the landing page, support article **and the blog post**.
13. **`web_fetch https://www.kraken.com/europe-switch`** → HTTP 200, **live day 3**, copy unchanged 72h.
14. **`web_fetch https://blog.kraken.com/news/industry-news/europe-mica-switch`** → HTTP 200, **THIRD Kraken surface**, published+modified 19 Jun, never touched, tagged *"Promotions"*, three live CTAs, **19-June start date (2-vs-1 against the landing page)**, UK FCA banner on an EEA-only offer, Mulvenny quote refused on the §4 role gate.
15. WebSearch — OKX Europe 8% deposit bonus MiCA → surfaced the **`/en-eu/`** and **`/en-sg/`** paths.
16. **`web_fetch https://www.okx.com/en-eu/learn/okx-europe-deposit-bonus-mica-deadline`** → HTTP 200, **EEA-locale twin, live day 3**, updated 30 Jun and untouched since, **and the US geo-notice served above a live EEA-only offer.**
17. WebSearch — crypto exchange CMO / head of marketing August 2026 → **0 qualifying class-4 items**; surfaced the Kalifowitz exit (already held).
18. WebSearch — crypto layoffs August 2026 marketing → **0 net-new**; everything already tracked.
19. `web_fetch coindesk.com/…/crypto-com-s-high-rolling-head-of-marketing…` → **empty body returned; not usable, not cited.**
20. **Not reached / not guessed:** ESMA news index · CNMV `Advertencias` register · CONSOB July `comunicazione` · AFM individual warning pages · `okx.com/en-sg/learn/mica-deposit-bonus-campaign` · Bitpanda day-3 re-read · Gate and Coinbase own channels · Gnosis X post and forum primaries. **All recorded as open, none fabricated.**

---

## Net-new / changed this run

- `corpus/regulator-filings/afm-cnmv-post-deadline-index-sweep-2026-08-03.md` — **NEW.** AFM own-index sweep (109-day crypto null, 2 non-crypto Measures, boiler-room warning shape); CNMV Circular 1/2022 conduct precedent flagged out-of-window; watch (v) → 5/6; the "non-public channels" Phase-2 wording.
- `corpus/marketing-campaigns/promotional-teardown-checkpoint-2026-08-03.md` — **NEW.** Day-3 replication 2/2; Kraken 3rd surface; OKX EEA-locale surface + `/en-sg/` identified; date conflict now 2-vs-1; UK banner on EEA-only offer; §4 role-gate refusal logged; the geo-notice evidence; the denominator problem.
- `findings/longitudinal-2026-06.md` — three shifts appended.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` — date re-stamps (sync).
- `corpus/agency-claims/*.csv` (18), `corpus/agency-overlap-matrix.csv` — dated snapshots (sync).
- **Layoff tracker: unchanged at 17 rows.** Operator statements: unchanged at 5 files.

---

## Recommendation for next run

1. **Sweep ESMA's own news index with today's method.** Direct NCA-index fetch was the single highest-yield technique this run and ESMA is the one index that has never been swept. It is also where the 29-day class-3 miss (the 03 July binary-options statement) came from.
2. **Fetch `okx.com/en-sg/learn/mica-deposit-bonus-campaign`.** Cheapest high-value fetch in the repo. If an EEA-only MiCA promotion is live on a Singapore locale path, the finding gets materially larger.
3. **08-09 time-to-teardown measurement.** Now pre-committed and dated. It is the metric no competing report will have.
4. **Test watch (z) across the panel** — for each tracked firm, does any owned surface currently advertise a state the firm has publicly exited? Carried a second run; still the generalised version of the corpus's best finding.
5. **Implement watch (aa) before Phase 2** — split `date_announced` / `date_effective` on every personnel and campaign record. It is a schema fix, it is cheap now, and it is expensive after synthesis is written.
6. **Capture the CONSOB July primary** and close the 24 / 1,793 / 233 `[VERIFY]`, second run open.
7. **Escalate to Jukka — five items, in order:**
   - **(i) `methodology.md` §1 must be re-scoped.** Unchanged and unaddressed for a fourth run. Class 1 cannot evidence "rolling 12 months": its entire flow register is 5 rows across 4 firms in a 28-day July window, and its deepest rows are arithmetic inferences from relative board labels. **Still the one thing in this repo that could embarrass the report.**
   - **(ii) `methodology.md` §4 needs two changes** — widen the inventory *and* add an earned-vs-placed provenance field. Class 4 is static for a second day and has produced one item in eight days.
   - **(iii) The four upstream company-list gaps — OKX (Tier-1), Securitize, Rabby, Relai — are unfixed, FOURTH run.** OKX supplied two of today's strongest primaries while being invisible to the class-1 instrument. **This needs an owner outside the corpus run.**
   - **(iv) §6's "daily 18-agency panel" is inaccurate at 49 days stale.** Re-word or re-feed. Fourth run.
   - **(v) NEW — §3's day-N null needs its Phase-2 wording fixed now, while it is still cheap.** "No enforcement" is not what the evidence says. What the evidence says is that the response is running through **non-public channels**: supervisory letters, cross-border referrals, perimeter warnings. That version is defensible at five jurisdictions and survives a hostile read; "silence" does not.

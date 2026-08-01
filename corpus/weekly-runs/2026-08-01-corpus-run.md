# Corpus-assembly daily run — 2026-08-01 **(day 31 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-01.
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, taken from the 07-30 recommendations:** (1) the 07-31 capture-panel checkpoints — Kraken MiCA-lapse, OKX 8% campaign end, Friday nomination check; (2) test the watch (t′) class-1 backfill; (3) sweep NCA warning lists once (watch v); (4) `[VERIFY]` the Gnosis primaries.
**Dedup baseline read before writing:** `2026-07-30-corpus-run.md` in full (headline, six-class trail, watch list, recommendations); `findings/longitudinal-2026-06.md` tail; `layoff-tracker/2026-layoff-tracker.csv` (16 rows pre-run, all firm names + Exodus/Gnosis/Luno notes in full); `regulator-filings/` (9 files); `operator-statements/` (4); `marketing-campaigns/` (6); `job-postings/` listing + `_absence.csv` + `_absence-cohort-audit.csv`. Repo-wide greps for `polygon`, `exodus`, `bitmart`, `7254`, `47 companies`, `okx.com`, `8%`, `31 Jul`, `finfluencer` run before any file was written.

---

## ⚠️ FIRST: THE 07-31 RUN DID NOT FIRE

There is **no `2026-07-31-corpus-run.md`**, and `git log` shows **no 07-31 corpus commit** (last was `0db5204`, 07-30). The loop skipped a day — and it skipped **the single date the two preceding run records had both flagged as "the heaviest date on the calendar."**

Watch **(e)** has been carrying *"loop cadence — third clean single-fire day running, trend is good"* for ten consecutive runs. **That watch is now falsified.** It is re-opened as **(e′): the cadence is not reliable, and the failure landed on the one pre-calendared date in the corpus.** All three 07-31 items were executed today instead, one day late; the lapse checkpoint is arguably *better* on 08-01 than on 07-31, but that is luck, not design, and it does not generalise. **Escalate to Jukka.**

---

## Headline result

**Four things, in descending order of consequence.**

**1. Both MiCA capture campaigns were still publicly live, in the present tense, the day after they closed.** Direct primary fetch on 2026-08-01: Kraken's `/europe-switch` still says *"Switch now and enter our €1M prize draw"* with a working **"Enter the €1M draw"** button and *"Lottery closes July 31"*; OKX's campaign page still says *"From 29 June until 31 July 2026… **receives** an 8% bonus"* with a live **"Claim your deposit bonus"** CTA. **2 of 2**, two mechanics, two NCAs, same failure mode. → `../marketing-campaigns/mica-capture-campaign-lapse-checkpoint-2026-08-01.md` (NEW FILE).

**2. A class-3 item sat unfound for 29 days, and it is the most marketing-relevant EU instrument in the post-deadline window.** **ESMA Public Statement ESMA35-243228190-8148, 2026-07-03**: event contracts / prediction markets that are financial instruments *"fall within the scope of the existing national product intervention measures on binary options… **prohibiting their marketing, distribution or sale to retail clients**."* It was missed because every prior class-3 sweep was keyed on MiCA/crypto-marketing vocabulary and this instrument speaks MiFID II product-intervention. **It was found incidentally, in a "related topics" rail on a page fetched for another reason.** → `../regulator-filings/esma-binary-options-event-contracts-prediction-markets-2026-07.md` (NEW FILE); watch **(w)** opened.

**3. Watch (t′) was measured, and the 07-30 run undercounted it by 80% — including two Tier-1 exchanges.** 07-30 recorded *"≥5 qualifying roles at 3 tracked firms"* missing from class 1. Direct reconciliation of `jobs_seen` against every corpus CSV: **9 roles at 6 tracked slugs**, and the ones 07-30 missed are **Coinbase ×2 and Kraken ×1**. **Watch (g) — "Coinbase brand-rebuild signal, n=1 on postings" — is therefore not measuring Coinbase. It is measuring the instrument.** → `../job-postings/_backfill-queue.csv` (NEW FILE, 9 rows).

**4. And the (t′) decision Jukka was asked to make is now answered by the data: re-scope, do not backfill.** `jobs_seen`'s **earliest entry in the entire upstream state file is 2026-04-28**. The deepest recoverable memory anywhere in this pipeline is **~3 months**, against `methodology.md` §1's promise of a **rolling 12 months**. **Even a perfect, fully successful backfill cannot deliver the published window.** The §1 claim must be re-scoped. The backfill is still worth running — it is worth ~4 months instead of ~2 — but it is an improvement, not a fix.

**Day-31 named marketing-side enforcement silence HOLDS — and is now better-founded than at any prior point,** because watch (v) was swept for France and the null survived it.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-08-01
source A (jobs)   scan_date: 2026-08-01
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

**Feed-health guard: HEALTHY.** `scan_metadata` — `scanned_at_utc 2026-07-31T22:46:54Z`, `scan_date 2026-08-01`, 147 companies (87 API, 60 pending Chrome), **2,088 jobs fetched**, 27 after filter, **`new_count` 0**, **`url_verification_dropped` 0**, `still_open_count` 27 (28 → 27; one role closed). `fetch_errors: null` this run — **note the change**: 07-28 and 07-30 both reported six fetch-errors incl. the standing Aave Lever-404. A null error list is *not* self-evidently good news; it may mean the field was not populated. **Aave nevertheless still appears in the no-coverage list**, so its absence is intact. `[VERIFY]` the error-field semantics before treating "0 errors" as an improvement.

Repo diff from the sync: `_absence.csv` and `_chrome-queue.csv` date re-stamps only. **The 0-new result is genuine idempotency, not an infra artefact.**

#### Watch (t′) — MEASURED. The number is 9, not 5, and the window promise is unrecoverable.

Method, fully deterministic and re-runnable, no network: read `prospects/scanner/state/last-scan.json` → `jobs_seen` (121 entries), map `ats:slug` → firm via `prospects/scanner/config.json` (147 companies), filter to tracked slugs, filter to `first_seen < 2026-06-26` (the sync script's creation date), then check each job ID against the `source_url` of **every** row in `corpus/job-postings/*.csv` (16 rows total).

| firm | ats:slug | job id first-seen | in corpus? |
|---|---|---|---|
| **Coinbase** | `greenhouse:coinbase` | 2026-04-29 | **MISSING** |
| **Coinbase** | `greenhouse:coinbase` | 2026-04-29 | **MISSING** |
| Trust Wallet | `ashby:trust-wallet` | 2026-04-29 | **MISSING** |
| **Kraken** | `ashby:kraken.com` | 2026-05-07 | **MISSING** |
| Arbitrum Foundation | `lever:arbitrumfoundation` | 2026-05-08 | **MISSING** |
| Offchain Labs | `lever:offchainlabs` | 2026-05-12 | **MISSING** |
| Ava Labs | `ashby:ava-labs` | 2026-06-10 | **MISSING** |
| Offchain Labs | `lever:offchainlabs` | 2026-06-10 | **MISSING** |
| Trust Wallet | `ashby:trust-wallet` | 2026-06-23 | **MISSING** |

**9 / 9 missing. 6 distinct tracked slugs. 63 of the 121 `jobs_seen` entries are pre-epoch across the whole panel** (Apr 14 / May 23 / Jun 26), so the tracked-firm loss above is one slice of a much larger flow-loss.

**Two consequences that change what Phase 2 may print:**

- **Watch (g) is void as filed.** It read *"Coinbase brand-rebuild signal — unchanged at n=1 on postings."* Coinbase's corpus file holds **1 row, earliest `date_posted` 2026-07-17** — but `jobs_seen` proves **two** qualifying Coinbase marketing roles were open on 2026-04-29. The "n=1" is an artefact of the epoch, not an observation about Coinbase. **Any watch item whose evidence is a class-1 count for a period before 2026-06-26 is measuring the instrument.** That is a general rule, not a Coinbase rule — it should be applied across the watch list.
- **The 12-month window is unrecoverable, so §1 must be re-scoped rather than backfilled.** `min(jobs_seen.values()) = 2026-04-28`. There is no deeper store. `methodology.md` §1 promises "rolling 12 months ending August 31, 2026". **Recommended replacement text, for Jukka's decision:** *"Class 1 captures marketing roles observed open at any tracked firm between 2026-04-28 and 2026-08-31, via daily ATS API scan. Roles opened and closed before 2026-04-28 are outside the instrument's memory and are not claimed."* Honest, defensible, and still the only 4-month dated ATS panel of its kind that this report is likely to face competition from.

**Backfill staged, not executed.** `../job-postings/_backfill-queue.csv` (NEW, 9 rows) carries firm / ats / slug / job_id / first_seen_date / a **CONSTRUCTED, UNVERIFIED** candidate URL / recovery status. **These rows are deliberately NOT in the corpus CSVs and must not be promoted until each URL is fetched and confirmed.** `jobs_seen` stores IDs and dates only — no titles, jurisdictions, seniority or verified URLs.

**Why it was not executed here, precisely:** this run's fetch layer is **provenance-gated** — it will only retrieve URLs that appeared in a prior search result or fetch. Direct ATS API calls (`api.lever.co/v0/postings/...`) were **refused**. This is not an ATS failure and not a 404; it is a capability boundary of the corpus run. **The backfill therefore belongs in the upstream scanner lane, which already queries these exact APIs daily with sanctioned egress — not in the corpus run.** That is a better home for it anyway: one script, in `prospects/scanner`, re-querying `jobs_seen` IDs and emitting corpus-schema rows.

#### Absence panel — unchanged
`_absence.csv`: Aave (Lever 404) + Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys (proprietary, chrome-pending). The four genuine company-list gaps from 07-30 — **OKX, Securitize, Rabby, Relai** — are **not fixed** (no config write attempted this run; that is an upstream repo, and an autonomous corpus run should not silently edit the sales funnel's scanner config). **Carried, and escalated.**

### 2. Agency claims / overlap matrix (deterministic)

18 agency-claims files rewritten; 8 matrix rows; **1 OVERLAP: Sui (coinbound, rzlt)** — unchanged. **`trend-data.json` `lastUpdated` is still 2026-06-15 — the panel is now 47 days stale** (was 45 on 07-30). Watch (d) remains stable-by-decision, but at 47 days the phrase "daily 18-agency panel" in `methodology.md` §6 is no longer accurate as written and should be re-worded before Phase 2. Sui remains the corpus's only firm degraded on three instruments at once (broken ATS slug, only overlap row, unswept own-channels).

### 3. Regulator — **1 NET-NEW (in-window, primary). Watch (v) DISCHARGED for France. Day-31 named-enforcement silence HOLDS.**

#### (a) NET-NEW: ESMA Public Statement on binary-option measures and event contracts, **2026-07-03**
→ `../regulator-filings/esma-binary-options-event-contracts-prediction-markets-2026-07.md`. Primary PDF `esma.europa.eu/.../ESMA35-243228190-8148_...pdf`; captured via the AMF's dated republication. **Operative marketing sentence:** event contracts that are financial instruments fall inside national measures *"prohibiting their **marketing**, distribution or sale to retail clients."*

**Scoping, held tightly:** supervisory reminder, **not** enforcement, **not** firm-named, **not** MiCA (MiFID II product intervention). The day-N null is scoped to *named marketing-side enforcement actions against identified firms* and is untouched. The correct dual reading: **post-deadline, EU regulators have been active on the marketing perimeter without taking a single named marketing-side enforcement action. Activity ≠ enforcement.**

**Cross-class link, and it is the strongest one this corpus has produced:** 2026-02-05 Gemini exits UK/EU/AU (−25%, resources to US + Predictions) → **2026-07-03 ESMA fences prediction-market *marketing* to EU retail** → 2026-07-29 Gemini posts a **Predictions Partnerships Marketing Lead, New York** (the corpus's only Gemini class-1 row, captured 07-30). Three legs, three primaries, all already in this corpus. Stated as sequence, not causation.

#### (b) Watch (v) — NCA warning lists, **swept for France, DISCHARGED for France**
→ `../regulator-filings/amf-warning-list-sweep-2026-07.md` (NEW FILE). Three in-window AMF/ACPR public warnings captured — **2026-07-08** (crypto-assets, unauthorised entities), **2026-07-08** (miscellaneous assets), **2026-07-09** (AMF+ACPR, Forex + crypto-asset derivatives). **Every one is an unauthorised-entity / perimeter warning. Not one is a marketing-conduct action against an authorised CASP.**

> **The regulator's post-deadline output is perimeter enforcement, not conduct enforcement.** France named firms publicly three times in two days — for being outside the perimeter. It has named nobody for how they market inside it.

**The null now survives a sweep of the instrument class most likely to falsify it.** (v) stays open for **BaFin, CONSOB, AFM, CySEC, CNMV `Advertencias`** — and the expectation is replication; a non-replication in any of the five is the story.

Marketing-adjacent nuance kept for Theme 4: the AMF's stated toolkit for unauthorised crypto services includes **public blacklisting and website blocking** — remedies that act directly on the marketing and distribution surface rather than the balance sheet.

#### (c) REFUSED — out of window
AMF, *"Cryptoassets… publishes a new 'blacklist'"* (9 sites incl. MEXC, CoinEx) — page dated **05 June 2024**. Excluded per the pre-Dec-2024 rule; **not entered**. Recorded only because it was the fetch that incidentally surfaced item (a).

#### (d) REFUSED — unverified aggregate
A search-engine summary asserted the AMF/ACPR added **31** Forex / **26** crypto-derivative / **23** crypto-asset-service names "since the start of 2026." **Reproduced on no primary page captured this run. Barred from the corpus and from Phase 2.** `[VERIFY]`

### 4. Operator statements — **0 net-new. Two candidates examined, both correctly refused.**

- **James Lanigan, CEO, Luno** — *"leaner and adapted structure is both necessary and appropriate"*; investments in automation had "altered the resources required to run the exchange." **REFUSED for class 4:** methodology §4 admits CMO / VP Marketing / Head of Brand / Head of Growth. A CEO is not a marketing operator. Retained in the class-5 note only.
- **Friederike Ernst, co-founder, Gnosis** — *"growth has been linear, and linear is not good enough"* (Q2-2026 report, 2026-07-17). **REFUSED for class 4** on the same rule (co-founder, not a marketing role). Retained as class-5 corroboration.

Class 4 remains at **4 files**, unchanged since 07-27. Watch **(l)** — the §4 source inventory is too narrow (podcast-list-only; no marketing trade press, no regional-language media, no firm-owned channels) — is now **costed a third time**. The §4 rewrite is not optional for Phase 2.

### 5. Layoff tracker — **0 net-new rows (16 → 16). One existing row materially strengthened. One search-summary claim caught and refused.**

**A fabricated attribution was caught before it entered the corpus. Record it.** A search-result summary asserted, of the July wave, that *"Marketing and sales teams felt the brunt, as many firms scaled back aggressive user-acquisition spend."* Fetched to the primary article (crypto.news, 2026-07-30) — **that sentence does not exist in it**, and the article states the opposite of the implied specificity: *"Lanigan did not disclose the number of employees affected **or identify the regions and departments included**."* **Had it been taken on trust it would have been the single most load-bearing false claim in the report** — the tracker's entire standing finding is about whether anyone names marketing. → **standing rule, re-affirmed: a search-engine summary is never a source. Fetch the primary or drop the claim.**

**Gnosis `[VERIFY]` — ADVANCED, NOT CLOSED, and the movement is toward *narrower*.** crypto.news (2026-07-30) independently corroborates the **underlying event** — Gnosis reduced the Gnosis App team, per its own Q2-2026 report published 2026-07-17 at `forum.gnosis.io/t/gnosis-ltd-quarterly-report-q2-2026/12391`, with Ernst quoted verbatim, plus the Q3 spin-out plan and the 800-active-card-user figure. **But crypto.news, reading the same quarterly report, does not mention marketing at all.** That is consistent with the marketing function-list originating in the **X post only**, not the report. **Net effect: the event is now double-sourced; the marketing claim is not, and is slightly weaker than it looked on 07-30.** Both primaries remain uncaptured (provenance rule). Row notes updated; `[VERIFY]` stays open and stays the corpus's highest-value verification item.

**Exodus figure conflict, logged not resolved:** the row carries the **primary SEC Exhibit 99.1** (~25%, $2.5–3.5M charges, $10–13M annualised savings). crypto.news reports the same filing as **"about 77 employees and individual service providers"**, while the CryptoJobsList tracker lists **54** for Exodus. **77 (SEC-sourced) vs 54 (aggregator) — the primary wins; the aggregator's per-firm figures are therefore not reliable enough to import.** Noted in the row.

**Candidates seen and deliberately NOT entered:** BitMart (550 — the largest single July cut), Dango, Odos (10), AscendEX, Zapper, Yield Guild Games (35). All **perimeter**, and all sourced only to the CryptoJobsList aggregate as relayed by crypto.news. **No primary announcement captured for any of them → no rows.** BitMart at 550 is worth one direct check next run purely for scale.

**Aggregate context, caveat travelling with it (unchanged, not a row):** CryptoJobsList — 12 July firms, 894 disclosed jobs across six named reductions; 7,254 disclosed cuts across 47 companies in 2026. Includes fintech/crypto-adjacent firms and is skewed by Block's 4,000 in February. Broad indicator, not an audited total.

**Watch (h′) unchanged and still not printable** (n=9 with a consumer-side non-AI counter-example). Nothing this run moves it.

### 6. Longitudinal shift for synthesis

Three shifts, all written into `findings/longitudinal-2026-06.md`:

1. **Campaign compliance is designed at launch and not maintained at teardown.** 2/2 capture campaigns outlived their own stated close dates on their own pages. New, printable, falsifiable — and cheaply testable to n=6.
2. **The regulated marketing perimeter is wider than MiCA, and the corpus's sweep vocabulary was narrower than the perimeter.** ESMA's most marketing-relevant post-deadline instrument speaks MiFID II, and 29 daily runs did not see it.
3. **The instrument is now a bigger source of error than the subject.** Today: watch (t) falsified (07-30), watch (t′) undercounted by 80% (today), watch (g) void, watch (e) falsified. **Four watch items broken by measurement in two runs, and not one broken by new external evidence.**

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged; still France-reported-only.
- **(b) First named post-deadline NCA marketing-side action** — **day-31 silence HOLDS, and is now better-founded**: the warning-list class has been swept for France and returned perimeter-only actions. Scope stays MiCA-era.
- **(c) Capture panel** — **07-31 checkpoints EXECUTED 08-01 (one day late).** Both campaigns found still live post-close. **New sub-item: replicate on Coinbase / Bitpanda / Bitvavo / Gate — converts n=2 to n=6 in one run.**
- **(d) Agency panel staleness — 47 days.** Stable-by-decision, but §6's "daily" wording must change before Phase 2.
- **(e) ~~Loop cadence — trend is good~~** — **FALSIFIED. The 07-31 run did not fire, on the one pre-calendared date in the corpus.** Superseded by (e′).
- **(e′) NEW — cadence is unreliable and the failure was not random.** Ten consecutive runs recorded "cadence good" and the eleventh missed the flagged date. **Escalate to Jukka.**
- **(f) Friday nomination cadence** — 07-31 check missed with the run; performed today. **No `inbound-nominations.md` exists; no nominations have ever arrived.** Next check 08-07.
- **(g) ~~Coinbase brand-rebuild signal, n=1 on postings~~** — **VOID AS FILED.** `jobs_seen` shows 2 qualifying Coinbase roles on 2026-04-29 that class 1 never captured. The n was the epoch, not Coinbase. **Re-file only after the backfill.**
- **(h′) Layoff rationale correlates with firm type** — unchanged, n=9 with counter-example. **Do not print.**
- **(i) Kraken paid-media build-out** — unchanged; **now with a fourth dated leg**: the `/europe-switch` page still live post-close on 08-01.
- **(j) Senior-leader exits trailing contractions** — Coinbase CPO still unverified, **seventh run**.
- **(k) Chrome-lane instrumentation gap** — unchanged; the 07-25 Binance Dubai req remains unrecoverable.
- **(l) `methodology.md` §4 inventory too narrow** — **costed a third time** (Lanigan, Ernst both correctly refused; class 4 static at 4 files since 07-27).
- **(m) Ad-platform gating** — unchanged (Google France, 2026-07-01).
- **(n) Full-range re-sweep of classes 3 and 5** — class 3 re-swept today and **it found a 29-day-old miss**, which is the argument for (w). Classes 1 and 2 historical backfill still not run.
- **(o) Date the document, never an event held about it** — held.
- **(p) Absence claims tested against firms' OWN channels** — **partially advanced**: Kraken and OKX own-channel reads executed today (campaign pages). Still unswept: Bybit, Coinbase, Crypto.com, Gemini, Sui, all of Strata 2 and 4.
- **(q) Agency matrix measures the crypto-native segment** — unchanged.
- **(r) Absence panel needs a "structural withdrawal" category** — Gemini; **reinforced** by the ESMA cross-link (withdrawn from EU, hiring marketing in the product the EU just fenced, on the other side of the fence).
- **(s) Robinhood row misclassified** — unchanged, third run, still no evidence either way.
- **(t′) Class 1 is a FLOW register presented as a STOCK register** — **MEASURED AND RE-SIZED: 9 roles / 6 tracked slugs, not 5 / 3, including Coinbase ×2 and Kraken.** **And decided: `jobs_seen` bottoms out at 2026-04-28, so §1's 12-month promise is unrecoverable by any backfill. Re-scope §1; run the backfill as an improvement, not a fix.** Queue staged at `_backfill-queue.csv`. Execution belongs in the upstream scanner lane, not the corpus run.
- **(u) Brand absorption defeats name-keyed sweeps** — unchanged; alias table still unbuilt.
- **(v) NCA warning lists** — **DISCHARGED for France** (perimeter-only, negative result with structure). Open for BaFin, CONSOB, AFM, CySEC, CNMV.
- **(w) NEW — the class-3 sweep vocabulary is too narrow, and the miss is proven not hypothetical.** ESMA's 2026-07-03 statement went unfound for 29 days because sweeps keyed on MiCA/crypto-marketing terms and it speaks MiFID II product-intervention. **Fix: sweep NCA/ESMA news indexes directly (not via search engines), with vocabulary covering product intervention, event contracts/prediction markets, financial promotion, advertising, inducements, and gambling-adjacency.**
- **(x) NEW — `fetch_errors: null` in `scan_metadata`, RESOLVED SAME RUN as a reporting artefact, not a data loss.** 07-28 and 07-30 both reported six errors incl. the standing Aave 404; today the top-level field is `null`. **Checked rather than assumed:** `corpus/job-postings/_absence.csv` carries `Aave,api-fetch-error,network error fetching https://api.lever.co/v0/postings/aave?mode=json: HTTP Error 404: Not Found,2026-08-01` — **the error is captured, dated today, with full detail; only the `scan_metadata` summary field is empty.** No absence claim is affected. **Standing rule it produces:** never read a null summary field as an improvement without checking the detail file — and never read one as a loss either. Closed.

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2, 0 new postings, 18 agency files, 8 matrix rows.
2. Direct read of `prospects/scanner/state/last-scan.json` (`jobs_seen`, 121 entries) + `config.json` (147 companies) + all 16 rows of `corpus/job-postings/*.csv` → **watch (t′) re-sized to 9/6; `min(first_seen) = 2026-04-28` established.**
3. WebSearch — CNMV advertencias / unregistered crypto entities July 2026 → context only, no primary entered.
4. WebSearch — Kraken MiCA licence lapse July 2026 → surfaced `kraken.com/europe-switch`.
5. **Fetch `https://www.kraken.com/europe-switch`** → HTTP 200, **campaign live post-close**, full copy captured.
6. WebSearch — OKX Europe deposit bonus campaign end 31 July 2026 → surfaced the OKX primary.
7. **Fetch `https://www.okx.com/en-us/learn/okx-europe-deposit-bonus-mica-deadline`** → HTTP 200, **campaign live post-close**; €50M pool, MFSA licence stack, and the 07-29 "Rewardmaxxing" stack article captured.
8. WebSearch — BaFin/CySEC/CONSOB crypto marketing enforcement July 2026 → **nil**; no coordinated or named marketing action found.
9. WebSearch — crypto marketing-team layoffs July 2026 → surfaced Polygon/Exodus/Luno; **all already in the tracker**.
10. WebSearch — Polygon Labs July 16 layoffs → already tracked; ~60 roles, Coinme/payments pivot, non-AI rationale. No row change.
11. **Fetch `https://crypto.news/luno-cuts-20-percent-of-staff-as-crypto-layoffs-widen/`** → **falsified the search summary's "marketing felt the brunt" claim**; produced Exodus 77-vs-54 conflict, Ernst verbatim quote, Gnosis forum-report corroboration.
12. WebSearch — AMF/AFM/CySEC warning lists July 2026 → surfaced the AMF warning estate.
13. **Fetch AMF "new blacklist" release** → **dated 05 June 2024, OUT OF WINDOW, refused** — but its related-topics rail surfaced item 14.
14. **Fetch `https://www.amf-france.org/en/news-publications/news/esma-public-statement-...binary-option-measures`** → **the run's net-new class-3 item**, plus the three dated in-window AMF/ACPR warnings for the watch-(v) sweep.
15. **Refused by provenance gate:** `api.lever.co/v0/postings/arbitrumfoundation/...` and `api.lever.co/v0/postings/offchainlabs/...` → **the (t′) backfill could not be executed from this run**; re-homed to the upstream scanner lane and recorded as such.

---

## Net-new / changed this run

- `corpus/regulator-filings/esma-binary-options-event-contracts-prediction-markets-2026-07.md` — **NEW.** Class-3 net-new, in-window, primary-anchored; 29-day sweep miss diagnosed; Gemini Predictions cross-link.
- `corpus/regulator-filings/amf-warning-list-sweep-2026-07.md` — **NEW.** Watch (v) discharged for France; three dated warnings; perimeter-vs-conduct distinction established; out-of-window and unverified-aggregate refusals logged.
- `corpus/marketing-campaigns/mica-capture-campaign-lapse-checkpoint-2026-08-01.md` — **NEW.** Both campaigns live post-close, verbatim copy captured; OKX rewards-stack absorption; licence stacks captured first-party.
- `corpus/job-postings/_backfill-queue.csv` — **NEW.** 9 staged rows, constructed-URL column explicitly marked unverified and barred from promotion.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` — date re-stamps (sync).
- `corpus/agency-claims/*.csv` (18), `corpus/agency-overlap-matrix.csv` — dated snapshots (sync).
- `corpus/layoff-tracker/2026-layoff-tracker.csv` — Gnosis and Exodus row notes updated (verification state + figure conflict). **No new rows.**
- `findings/longitudinal-2026-06.md` — three longitudinal shifts appended.

---

## Recommendation for next run

1. **Replicate the lapse checkpoint on Coinbase, Bitpanda, Bitvavo and Gate.** Cheapest high-value item available: turns n=2 into n=6 and decides whether "compliance designed at launch, not maintained at teardown" is a finding or an anecdote.
2. **Resolve the geofence caveat** on the lapse finding via the chrome lane with EEA egress. Until then the finding carries an explicit "as served to a non-EEA fetch" qualifier — **do not print it without that qualifier.**
3. **Sweep the remaining warning lists (watch v):** BaFin, CONSOB, AFM, CySEC, CNMV `Advertencias`. Expect replication; a non-replication is the story.
4. **Execute watch (w):** re-sweep classes 3 and 5 from **2026-07-01** with the widened vocabulary, **against NCA/ESMA news indexes directly**. The ESMA miss is proof the current method has a blind spot, and there is no reason to think it found only one thing.
5. **Re-run the watch-list audit with the (g) rule applied generally:** any watch item resting on a class-1 count before 2026-06-26 is measuring the instrument. Sweep them all; expect (g) not to be the only casualty.
6. **Build the backfill in the upstream scanner lane**, not the corpus run — re-query `jobs_seen` IDs through the adapters that already have egress, emit corpus-schema rows, and promote from `_backfill-queue.csv` only on a verified 200.
7. **Escalate to Jukka — four items, in order:**
   - **(i) `methodology.md` §1 must be re-scoped, and the decision is now forced, not optional.** The upstream memory bottoms out at 2026-04-28; the published "rolling 12 months" cannot be met by any backfill. Proposed replacement text is in §1 above. **This is a methodology-integrity item and it is the one thing in this repo that could embarrass the report.**
   - **(ii) The 07-31 run did not fire, on the pre-calendared date.** Cadence needs one human look (watch e′).
   - **(iii) The four upstream company-list gaps — OKX (Tier-1), Securitize, Rabby, Relai — are unfixed**, and the corpus run should not be the thing that edits the sales funnel's scanner config. Needs an owner.
   - **(iv) `methodology.md` §6's "daily 18-agency panel" is inaccurate at 47 days stale.** Re-word or re-feed.

# Corpus-assembly daily run — 2026-08-05 **(day 35 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-05 (Wednesday).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, taken verbatim from the 08-03 recommendations:** (1) sweep ESMA's own news index with the AFM method; (2) fetch `okx.com/en-sg/learn/mica-deposit-bonus-campaign`; (3) 08-09 time-to-teardown measurement (scheduled, not today); (4) test watch (z) across the panel; (5) implement watch (aa) schema split; (6) capture the CONSOB July primary; (7) escalate five items.
**Dedup baseline read before writing:** `2026-08-03-corpus-run.md` in full; `promotional-teardown-checkpoint-2026-08-03.md`; `layoff-tracker/2026-layoff-tracker.csv` all 17 rows; `regulator-filings/` (13 files, index); `operator-statements/` (5); `marketing-campaigns/` (9); `findings/longitudinal-2026-06.md` tail; `_absence.csv`; `open-positions.json` `scan_metadata`; repo-wide greps for `openai`, `falconx`, `en-sg`, `switch-to-okx`.
**CADENCE: 08-04 WAS MISSED.** Last run 08-03. **Two gaps now (07-31, 08-04).** See watch (e′).

---

## Headline result

**Four things, in descending order of consequence.**

**1. The teardown finding's innocent explanation is dead.** Every prior checkpoint left open that nobody had looked at these pages. Today `okx.com/en-eu/learn/okx-europe-deposit-bonus-mica-deadline` returned **"Published on Jun 12, 2026 · Updated on Aug 05, 2026"** — **edited today** — and still opens *"The EU's MiCA deadline **lands** on 1 July 2026… move before then,"* with the closed 8% offer in present tense and three live acquisition CTAs. **Someone maintained the page five days after the campaign closed and did not retire the offer.** The finding upgrades from hygiene to governance: *the teardown is not being missed; it is not in the workflow.* → `../marketing-campaigns/promotional-teardown-checkpoint-2026-08-05.md` (NEW FILE).

**2. CONSOB holds a statutory power to order the removal of advertising campaigns, and 21 weeks of its own register contains not one.** The `oscuramenti` register was fetched at source. Its stated legal bases include **art. 36 c.2-*quaterdecies*** TUF (L. 21/2024): *"La Consob può ordinare … la rimozione delle **campagne pubblicitarie**…"* Alongside it, 18 dated `comunicati stampa` back to 6 March 2026, every one a site-blocking order against an **unauthorised** entity. **The marketing-specific instrument exists, is described on the same page as the register, and has not been visibly used.** Watch **(v) → 6 of 6.** → `../regulator-filings/esma-consob-post-deadline-index-sweep-2026-08-05.md` (NEW FILE).

**3. The MiCA deadline is not visible in the enforcement data.** CONSOB's own crypto-blocking counter: **+16 crypto sites in the 21 post-deadline days (3–24 July)** against **+33 in the 14 pre-deadline days (23 April – 7 May)**. **The pre-deadline rate was higher.** Any Phase-2 claim that the transitional-period end triggered a supervisory surge is falsified for Italy by the regulator's own number.

**4. A whole Theme-1 event at a Tier-1 tracked firm was sitting in the public record since April and the corpus did not hold it.** Six named senior Coinbase marketers, including CMO **Kate Rouch**, moved to **OpenAI** between Nov 2024 and Dec 2025; the Base marketing lead moved to **Anthropic** in April 2026. Coinbase's on-the-record reply contains **the only firm-stated marketing-team headcount the corpus holds for any tracked firm: "over 150 people."** → `../../findings/theme-1-marketing-function-attrition-coinbase-openai.md` (NEW FILE).

**Day-35 named marketing-side enforcement silence HOLDS**, now six-jurisdiction-tested and tested at ESMA's own index for the first time.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-08-05
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

**FEED-HEALTH GUARD: NOT HEALTHY — DEGRADED. This is the first time this guard has failed and it must not be buried.**

`scan_metadata` is **byte-identical to the 08-03 run**: `scanned_at_utc 2026-08-02T21:46:03Z`, `scan_date 2026-08-03`, 147 companies, 2,087 fetched, 27 after filter, `new_count` 0, `url_verification_dropped` 0, `still_open_count` 27.

**The upstream ATS scan has not run since 2026-08-02 21:46 UTC — roughly 66 hours.** The 08-03 run correctly read a 0-new day as genuine idempotency because the fetch total had moved. **Today it has not moved at all.** Today's "0 new postings" is therefore **not evidence that no tracked firm posted a marketing role** — it is evidence that **nobody looked.** The class-1 instrument is stale, not quiet.

**This is exactly the defect the corpus just documented in OKX's estate, occurring inside the corpus's own pipeline: a surface reporting a state it has not re-verified.** Recorded without irony and without exemption. **New watch (bb).**

**Consequence for the record:** no absence claim may be made for class 1 for 08-04 or 08-05. The correct entry is **"class 1 unobserved for two days,"** not "class 1 produced nothing."

**Watch (y) unchanged and unaddressed:** class 1's only pre-2026 rows remain arithmetic inferences from relative Getro board labels.

#### Absence panel — four upstream gaps unfixed for a **fifth** run
`_absence.csv`: Aave (Lever 404) + Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys (proprietary, chrome-pending). **OKX (Tier-1), Securitize, Rabby, Relai remain missing from the upstream company list.** No config write attempted — that is the sales funnel's repo.

**The OKX irony compounds for a fifth run.** OKX is invisible to the class-1 instrument, and today supplied **four** of the run's strongest primaries: the edited-today `/en-eu/` page, the Singapore-locale surface, the self-cancelling `my.okx.com` campaign page, and the disclaimer-asymmetry artefact. **It needs an owner outside the corpus run.**

### 2. Agency claims / overlap matrix (deterministic)

18 agency-claims files rewritten; 8 matrix rows; **1 OVERLAP: Sui (coinbound, rzlt)** — unchanged. **`trend-data.json` `lastUpdated` still 2026-06-15 — the panel is now 51 days stale.** Watch (d) stable-by-decision; `methodology.md` §6's phrase *"daily 18-agency panel"* remains inaccurate as written. Escalation stands, **fifth run**.

### 3. Regulator — **1 NET-NEW FILE. Watch (w) DISCHARGED for ESMA. Watch (v) → 6/6. The 3-run CONSOB `[VERIFY]` CLOSED at the primary.**

→ `../regulator-filings/esma-consob-post-deadline-index-sweep-2026-08-05.md` (NEW).

**ESMA — own news index, fetched direct for the first time.** Ten dated items, **10 July → 3 August 2026**. **Zero crypto items of any kind.** The two *Digital Finance and Innovation* items are an ESAs paper on ICT risk from frontier AI models (31/07) and a routine Q&A release (10/07); neither is marketing-side. The one supervision-of-conduct item (cross-border investment services, 20/07) is MiFID-perimeter.

> **BOUNDED CLAIM, stated in the file and repeated here:** page 1 covers post-deadline **days 9–33 only**. Days 1–8 are **unswept**, and pagination was not followed. The claim is *"across the 24 days page 1 covers, ESMA published no crypto-marketing item"* — **not** "ESMA has published nothing since the deadline." The known 29-day class-3 miss (03 July binary-options statement) sits in the unswept stretch, which is the argument for paginating next run.

**CONSOB — the register, at source, and it is the best class-3 artefact the corpus has.**

- **`[VERIFY]` CLOSED.** The carried figures **24 sites / 1,793 / 233 crypto** are **confirmed verbatim** in the *comunicato stampa del 24 luglio 2026*. Exact match. Three runs open, now shut.
- **18-point longitudinal series captured** (6 Mar → 24 Jul 2026), CONSOB's own cumulative counters for total and crypto-attributed blocks. Full table in the file.
- **The deadline is invisible in the series** — post-deadline crypto blocking ran *slower* than pre-deadline.
- **The advertising-campaign removal power (art. 36 c.2-*quaterdecies*, L. 21/2024) is named on the register page and appears nowhere in 21 weeks of the register's contents.**
- **Honest qualifier that ships with it:** that power is **perimeter-scoped by statute** — it reaches advertising *by unauthorised persons*, not the conduct of licensed CASPs. Which sharpens rather than weakens the structural read:

> **The EU marketing-enforcement toolkit, as legislated and as deployed, is perimeter-shaped.** Six jurisdictions swept; no published instrument aimed at the marketing conduct of an authorised CASP.

**That is the Phase-2 wording.** It supersedes both "silence" and the 08-03 "non-public channels" formulation — or rather, it is the structural half and "non-public channels" is the procedural half. **Print both.**

**NOT REACHED, NOT GUESSED:** ESMA index pages 2+ · individual CONSOB comunicato PDFs · CONSOB `Avvisi`/`Avvertenze` registers · BaFin/AMF/CySEC re-sweeps · **MAS and VARA, never swept at source** (now more relevant — see class 5). **No URL was fabricated.**

### 4. Operator statements — **0 NET-NEW. Class 4 stays at 5 files. One high-value item REFUSED on the role gate.**

The August CMO / Head-of-Marketing sweep surfaced no in-window verbatim statement by a qualifying marketing operator at a tracked firm.

**The refusal, logged because the gate only means something when applying it costs something.** The Coinbase→OpenAI story carries an **on-the-record company statement quoting a marketing-team headcount** — *"The marketing team at Coinbase is over 150 people…"* It is dated, verbatim, first-party, at a Stratum-1 firm, and it is the single most useful sentence found this run. **It is attributed to an unnamed "Coinbase spokesperson" — a communications seat, not a marketing seat. It fails §4. Not counted.** Recorded in the findings file instead. Second consecutive run in which the best quote found was refused on the role gate (cf. Mulvenny, 08-03).

**Class 4 is static for a 4th day and has produced 1 item in 10 days.** Watch (l) unchanged and now **6th costing**: §4's inventory is too narrow *and* provenance-blind. **The evidence that it is too narrow is that the two best marketing-function statements found in three days were both structurally ineligible.**

**Watch (aa) escalates into a worse shape — see class 5/findings.** Every date in the Coinbase→OpenAI table is a **destination start date**, not a Coinbase departure date. Sarah Russell left Coinbase **Jan 2023** and started at OpenAI **Nov 2024** — a 22-month gap. `date_announced`/`date_effective` is **insufficient**; personnel records need `date_departed_source_firm` and `date_started_destination`. A Theme-1 claim of the form *"N marketing leaders left firm X in window W"* built from destination start dates is **wrong by construction**, and the corpus was one synthesis pass from making it.

### 5. Layoffs — **1 NET-NEW ROW. Tracker 17 → 18.**

**FalconX [PERIMETER]**, 2026-08-03, ~10% of ~350 (≈35 roles), digital-asset prime broker. Rationale **explicitly non-AI**: sustained market slump (BTC ~−50% from its October peak near $126,000 to below $64,000) plus a pivot to **crypto derivatives** and **European expansion**. **6th consecutive non-AI 2026 contraction rationale** — watch (h′) continues to weaken.

**Weakest provenance chain in the tracker, and it is labelled as such in the row.** Bloomberg (2026-08-03) citing *"people familiar with the matter"*; **company had not publicly confirmed**; Bloomberg original **paywalled, not fetched, no URL asserted**. The captured source is The Cryptonomist 2026-08-04 (HTTP 200, publish/modify timestamps in metadata) — **which discloses that it was "produced with the assistance of artificial intelligence."** An AI-assisted secondary relaying an anonymously-sourced paywalled primary. Figures entered as **reported, not confirmed**, with `[VERIFY]`.

**THEME-4 REASON THIS PERIMETER ROW EARNS ITS PLACE:** FalconX is reported to be **withdrawing its licence application with the Monetary Authority of Singapore** while expanding in Europe — a firm re-selecting its regulatory jurisdiction *toward* the EU, mid-contraction, in the opposite direction from the EU exits already tracked (Gemini 02-05, Binance 06). **MAS has never been swept at source by this corpus.** Standing gap, now materially more relevant.

**FLAGGED, NOT ENTERED:** the same article asserts an **Ethereum Foundation −20% workforce reduction** — undated, no primary, single-sourced inside an AI-assisted aggregator piece. `[VERIFY]` before it is ever entered.

**Standing finding unchanged, cohort-scoped: no TRACKED firm's 2026 contraction has named marketing as an affected function.** The tracker-scoped version remains broken by the perimeter Gnosis row, whose marketing claim is still single-sourced to an X post and whose two primaries remain uncaptured. **Still the corpus's highest-value verification item; not advanced this run.**

### 6. NorthPoint longitudinal panel

`trend-data.json` **51 days stale**. No trend claim made.

---

## What this run did to the mandate

| # | 08-03 recommendation | status |
|---|---|---|
| 1 | Sweep ESMA's own news index with the AFM method | **DONE.** Watch (w) discharged for ESMA. Bounded to days 9–33; pagination not followed and said so. |
| 2 | Fetch `okx.com/en-sg/…mica-deposit-bonus-campaign` | **DONE, and it paid.** Live at day 5 under an **"OKX Singapore"** masthead. The 08-03 conditional — *"if live, the finding gets materially larger"* — is met. |
| 3 | 08-09 time-to-teardown measurement | **on schedule.** Day-5 read done today; 08-09 remains the pre-committed measurement. |
| 4 | Test watch (z) across the panel | **NOT DONE for the panel.** Deepened at OKX/Kraken instead. Carried, **3rd run**. |
| 5 | Implement watch (aa) | **NOT IMPLEMENTED — and its scope grew.** It now needs four date fields, not two. See class 4. |
| 6 | Capture the CONSOB July primary | **DONE. `[VERIFY]` closed, exact match, plus an 18-point series and the c.2-*quaterdecies* finding.** |
| 7 | Escalate five items | **DONE — below, all five carried, two hardened, one new.** |

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged.
- **(b) First named post-deadline NCA marketing-side action** — **day-35 silence HOLDS, six jurisdictions + ESMA's own index.** Phase-2 wording now has two halves: **structural** ("the toolkit as legislated and deployed is perimeter-shaped") and **procedural** ("the response runs through non-public channels — supervisory letters, cross-border referrals, perimeter warnings"). **Print both. Never print "silence."**
- **(c) Capture panel** — **2/2 re-tested live at day 5; denominator floor established at ≥34 surfaces.** Sub-items: (i) EEA-egress read open, bar moved again (2 surfaces × 2 days of geo-notice evidence); (ii) **08-09 time-to-teardown remains the highest-value scheduled item in the repo**; (iii) Gate/Coinbase/Bybit/Crypto.com/Gemini/Sui own-channel sweeps unrun; (iv) **denominator problem partially SOLVED** — OKX ≥31 identified surfaces across 15 locales, 4 fetched; the corpus now has a floor, not a value.
- **(d) Agency panel staleness — 51 days.** Stable-by-decision; §6 wording must change. **5th run.**
- **(e′) Cadence — DEGRADED. 08-04 MISSED.** Two gaps (07-31, 08-04). No trend claim made.
- **(f) Friday nomination cadence** — next check **08-07**. No `inbound-nominations.md` exists; none have ever arrived.
- **(g) Coinbase n=1** — void as filed; re-file only after backfill.
- **(h′) Layoff rationale correlates with firm type** — **weakened further.** FalconX is the 6th consecutive non-AI rationale. **Do not print.**
- **(i) Kraken paid-media build-out** — **Kraken is now sextuple-loaded**: 05-14 cut · 07-23 reqs ×2 · three lapsed owned surfaces at day 5 · a **2-v-2** start-date conflict · **two conflicting Forbes accolades on one page** · a competitor-named SEO title.
- **(j) Senior-leader exits** — superseded by (aa), which now has a third and worse form.
- **(k) Chrome-lane instrumentation gap** — unchanged.
- **(l) §4 inventory too narrow AND provenance-blind** — **6th costing, and now with an argument rather than a complaint:** the two best marketing-function statements found in three days (Mulvenny 08-03, Coinbase spokesperson 08-05) were **both structurally ineligible**. Class 4: 1 item in 10 days.
- **(m) Ad-platform gating** — unchanged.
- **(n) Full-range re-sweep of classes 3 and 5** — **THIRD STRIKE, and now class 4 too.** OP Labs (Mar, found Jul), Kraken (May, found Jul), **Coinbase→OpenAI (Apr, found Aug)**. The sweeps catch *new* events and systematically miss *in-window* ones. **A full-range re-sweep back to Dec 2024 is no longer optional before Phase 2.**
- **(o) Date the document, never an event held about it** — held.
- **(p) Absence claims tested against firms' OWN channels** — advanced at OKX (4 surfaces) and Kraken (re-read). **Still unswept: Coinbase, Gate, Bybit, Crypto.com, Gemini, Sui, all of Strata 2 and 4.**
- **(q) Agency matrix measures the crypto-native segment** — unchanged.
- **(r) Absence panel needs a "structural withdrawal" category** — unchanged. **FalconX supplies the inverse case** (jurisdictional *entry* to the EU mid-contraction) and the category should be two-directional.
- **(s) Robinhood row misclassified** — unchanged, **6th run**.
- **(t′) Class 1 is a FLOW register presented as a STOCK register** — unchanged.
- **(u) Brand absorption defeats name-keyed sweeps** — unchanged; alias table still unbuilt.
- **(v) NCA sweep** — **6 of 6. COMPLETE.** FR, DE, IT, CY, NL, ES all replicate perimeter-not-conduct. **Italy is the strongest case in the set** because the unused instrument there is a literal advertising-takedown power.
- **(w) Class-3 sweep vocabulary AND method** — **DISCHARGED for ESMA and CONSOB.** Direct index fetch is now 3-for-3 on outperforming search passes. **Remaining: ESMA pagination, MAS, VARA.**
- **(x) `fetch_errors` null** — closed.
- **(y) Pre-2026 class-1 rows are arithmetic inferences** — unchanged.
- **(z) Promotional surfaces decoupled from operational state** — **UPGRADED, and this is the run's main result.** The `Updated on Aug 05, 2026` timestamp on a page still advertising a closed offer removes neglect as an explanation. The claim is now: *promotional surfaces are actively maintained while advertising expired offers.* **Panel-wide test still unrun — 3rd run.**
- **(aa) Announcement vs effective dates** — **ESCALATED. Two fields is not enough.** Personnel records need `date_departed_source_firm` and `date_started_destination` in addition to `date_announced`/`date_effective`. The Coinbase→OpenAI table is built entirely from destination start dates and contains a 22-month gap case (Russell). **Fix the schema before Phase 2 or retract after it.**
- **(bb) NEW — the class-1 feed-health guard has failed for the first time, and the corpus nearly published its own defect.** `open-positions.json` has not been re-scanned since 2026-08-02 21:46 UTC (~66h). Today's "0 new postings" means **unobserved**, not **absent**. The guard must distinguish *idempotent* (metadata moved, no new rows) from *stale* (metadata frozen) and refuse to emit an absence claim in the stale case. **This is the same failure mode the corpus documented at OKX today: a surface reporting a state it has not re-verified.**

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2; 0 new postings, 18 agency files, 8 matrix rows.
2. Direct read of `prospects/open-positions.json` `scan_metadata` → **feed-health guard FAILED (frozen 66h)**; and `competitor-intelligence/trend-data.json` `lastUpdated` → 51 days stale.
3. Repo dedup baseline reads — 08-03 run record, tracker (17 rows), regulator/operator/campaign indexes, findings tail, plus greps for `openai` / `falconx` / `en-sg` / `switch-to-okx` / CONSOB figures.
4. WebSearch — ESMA news index August 2026 crypto marketing MiCA.
5. WebSearch — `esma.europa.eu press-news esma-news` → surfaced the index URL into provenance.
6. **`web_fetch https://www.esma.europa.eu/press-news/esma-news`** → HTTP 200. **10 dated items 10 Jul–3 Aug, zero crypto. Watch (w) discharged for ESMA.**
7. WebSearch — OKX Europe deposit bonus MiCA `en-sg` → surfaced the `/en-sg/` and `my.okx.com/campaigns/` URLs.
8. **`web_fetch https://www.okx.com/en-sg/learn/mica-deposit-bonus-campaign`** → HTTP 200. **LIVE day 5, "OKX Singapore" masthead, pub 16 Jul / upd 22 Jul, 2 live CTAs.** 08-03 `[VERIFY]` closed.
9. **`web_fetch https://my.okx.com/en-eu/campaigns/switch-to-okx-deposit-bonus`** → HTTP 200. **NEW SURFACE.** States its own early close (28 Jun) and serves "Join now" at day 38; "The MiCA deadline **is coming**"; tiered 5–8% / $500k cap; **carries the MiCA marketing-communication statement the `/learn/` surfaces omit**; **14 locales enumerated.**
10. **`web_fetch https://www.okx.com/en-eu/learn/okx-europe-deposit-bonus-mica-deadline`** → HTTP 200. **"Updated on Aug 05, 2026" — EDITED TODAY, offer intact, 3 live CTAs, 13 locales enumerated.** The run's principal result.
11. WebSearch — Kraken europe-switch €1M prize draw.
12. **`web_fetch https://www.kraken.com/europe-switch`** → HTTP 200. **LIVE day 5**, copy byte-comparable; **June 22 stated twice** (2-v-2 against blog/support's June 19); **two conflicting Forbes accolades on one page**; title tag *"MiCA-Licensed Binance Alternative (EU)"*.
13. WebSearch — CONSOB comunicazione luglio 2026 oscuramento cripto-attività.
14. **`web_fetch https://www.consob.it/web/area-pubblica/oscuramenti`** → HTTP 200 (86.6KB, read in full from the spill file). **`[VERIFY]` closed at exact match; 18-point series; art. 36 c.2-*quaterdecies* advertising power.**
15. WebSearch — crypto exchange CMO / head of marketing August 2026 → **0 qualifying class-4 items**; surfaced the CoinDesk OpenAI piece.
16. **`web_fetch https://www.coindesk.com/business/2026/04/23/openai-appears-to-be-poaching-coinbase-s-marketing-team`** → HTTP 200. **Backfill: 6 named senior Coinbase marketers → OpenAI; Base marketing lead → Anthropic; "over 150 people" on the record.** Class-4 refused on role gate.
17. WebSearch — crypto layoffs August 2026 marketing → surfaced FalconX.
18. **`web_fetch https://en.cryptonomist.ch/2026/08/04/falconx-crypto-layoffs/`** → HTTP 200. **Tracker row 18.** AI-assisted-secondary provenance caveat recorded.
19. **Not reached / not guessed:** ESMA index pages 2+ · CONSOB comunicato PDFs · CONSOB `Avvisi`/`Avvertenze` · MAS · VARA · ~27 unfetched OKX locale surfaces · `okx.com/en-eu/learn/mica-deposit-bonus-campaign` · `rewardmaxxing-okx-stack-rewards` · Bitpanda `bya-june-26` (3rd run carried) · Kraken blog/support re-reads · Bloomberg FalconX original (paywalled) · Gnosis X post + forum primaries · LinkedIn profiles behind the CoinDesk table. **All recorded as open. No URL was fabricated.**

---

## Net-new / changed this run

- `corpus/regulator-filings/esma-consob-post-deadline-index-sweep-2026-08-05.md` — **NEW.** ESMA own-index sweep (bounded, days 9–33, zero crypto); CONSOB register at source — `[VERIFY]` closed at exact match, 18-point longitudinal series, deadline invisible in the data, **art. 36 c.2-*quaterdecies* advertising-takedown power unused across 21 weeks**; watch (v) → 6/6; the perimeter-shaped-toolkit Phase-2 wording.
- `corpus/marketing-campaigns/promotional-teardown-checkpoint-2026-08-05.md` — **NEW.** `Updated on Aug 05, 2026` kills the neglect explanation; `/en-sg/` fetched and live; `my.okx.com` self-cancelling campaign page; **disclaimer asymmetry within one campaign**; surface denominator floor ≥34; Kraken day-5 with 2-v-2 date conflict and dual Forbes claims; geo-notice evidence ×2.
- `findings/theme-1-marketing-function-attrition-coinbase-openai.md` — **NEW.** 7 named senior marketing departures to AI labs; the *"over 150 people"* firm-stated headcount; class-4 refusal logged; watch (aa) escalated to four date fields; watch (n) third strike.
- `corpus/layoff-tracker/2026-layoff-tracker.csv` — **17 → 18 rows.** FalconX [PERIMETER] 2026-08-03, non-AI rationale, MAS withdrawal, weakest-provenance caveat, Ethereum Foundation claim flagged-not-entered.
- `findings/longitudinal-2026-06.md` — shifts appended.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` — date re-stamps (sync).
- `corpus/agency-claims/*.csv` (18), `corpus/agency-overlap-matrix.csv` — dated snapshots (sync).
- **Operator statements: unchanged at 5 files.**

---

## Recommendation for next run

1. **Fix the feed-health guard (watch bb) before anything else.** It is a five-line change — compare `scanned_at_utc` to today and refuse to emit an absence claim when frozen — and until it lands, every "0 new postings" line in this repo is ambiguous between *absent* and *unobserved*. **The corpus is currently vulnerable to exactly the defect it is publishing about other firms.**
2. **Paginate the ESMA index to cover post-deadline days 1–8.** The one known class-3 miss lives there. Direct-index fetch is 3-for-3; finish the job.
3. **08-09 time-to-teardown measurement.** Pre-committed, dated, four days out. The metric no competing report will have. **Design it to measure teardown *rate* against the ≥34-surface denominator, not teardown *fact*.**
4. **Sweep MAS at source.** Never done, and FalconX's reported MAS withdrawal plus OKX's Singapore-locale surface now give it two independent reasons.
5. **Test watch (z) across the panel** — carried a **third** run. For each tracked firm, does any owned surface currently advertise a state the firm has publicly exited? It is the generalised version of the corpus's best finding and it keeps not getting run.
6. **Implement the four-field date schema (watch aa).** Scope grew this run. Cheap now; a retraction after synthesis.
7. **Escalate to Jukka — five items, in order:**
   - **(i) `methodology.md` §1 must be re-scoped. FIFTH run, unaddressed.** Class 1 cannot evidence "rolling 12 months": its flow register is a handful of rows in a 28-day window, its deepest rows are arithmetic inferences, and **as of today its upstream feed has been frozen for 66 hours without the guard catching it.** Still the one thing in this repo that could embarrass the report.
   - **(ii) `methodology.md` §4 needs two changes** — widen the inventory *and* add an earned-vs-placed provenance field. **The argument is now empirical:** the two best marketing-function statements found in three days were both structurally ineligible under §4 as written. Class 4: 1 item in 10 days.
   - **(iii) The four upstream company-list gaps — OKX (Tier-1), Securitize, Rabby, Relai — unfixed, FIFTH run.** OKX supplied four of today's strongest primaries while being invisible to the class-1 instrument. **Needs an owner outside the corpus run.**
   - **(iv) §6's "daily 18-agency panel" is inaccurate at 51 days stale.** Re-word or re-feed. Fifth run.
   - **(v) NEW — commission the full-range re-sweep (watch n) now.** Three in-window events at tracked firms have been found late by accident: OP Labs (Mar→Jul), Kraken (May→Jul), Coinbase→OpenAI (Apr→Aug). That is a pattern, not luck. **The corpus does not know what else is sitting in the public record from Dec 2024 onward, and Phase 2 starts in ten days.**

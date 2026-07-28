# Corpus-assembly daily run — 2026-07-28 **(day 27 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-07-28 ~16:05 CEST.
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Mandate for this run, taken directly from the 07-27 run-#2 recommendations:** execute **watch (n)** — the full-range (Sep-2025 → present) re-sweep of classes 3 and 5, reading NCA and firm sources directly rather than aggregate search — before Phase 2 writes any absence sentence.
**Dedup baseline read before searching:** `2026-07-27-corpus-run-2.md` in full; the tail of `findings/longitudinal-2026-06.md`; `layoff-tracker/2026-layoff-tracker.csv` (12 rows pre-run); `regulator-filings/` (6 files pre-run); `operator-statements/` (3 files); `marketing-campaigns/` (2 files pre-run). Repo-wide greps run for `gemini`, `payward`, `kraken layoff`, `150 workers`, `serviceplan`, `zverev`, `demuth`, `bitpanda`, `2025-01-21`, `study-advertisement-information` before any file was written.

---

## Headline result

**Watch (n) was the highest-priority item in this corpus. It was executed, and it was right: four net-new entries, every one of them months old, every one of them at a tracked firm or a named NCA, every one of them publicly available the entire time.**

Two of the four are at **Tier-1 tracked exchanges** and both were missing from the layoff tracker while the corpus was asserting things about them.

1. **AFM (Netherlands), 2026-01-21 → the two-point regulator time series is complete.** The AFM's **baseline study** into CASP advertisements and cost disclosure, published 21 January 2025, names eight specific defect classes. The April-2026 review re-tested the market fifteen months later and found **the same defects at scale** (14/33 advertising, 19/33 cost). This was recommendation #2 from the last run and it is the strongest longitudinal marketing-compliance evidence available to this report from any regulator.
2. **BaFin date CORRECTED — the `[VERIFY]` flag caught a real three-week error.** *Risks in Focus 2026* was published **28 January 2026**, not 18 February 2026. Four-point primary verification on bafin.de. BaFin therefore **opens** the class-3 sequence rather than sitting mid-way through it.
3. **Gemini (TRACKED, Stratum 1) — 2026-02-05: exits the UK, EU and Australia, cuts 25%.** The corpus's Gemini row was undated, unsourced and flagged non-AI. All three were wrong. **Gemini, not Binance, is the first Tier-1 tracked exchange to leave the EU** — five months before the deadline.
4. **Kraken (TRACKED, Stratum 1) — 2026-05-14/15: ~150 cut (~5%), AI-attributed.** No Kraken row existed, yet the corpus has been asserting since 07-20 that AI framing "dominates Crypto.com/Coinbase/**Kraken**/Gemini." It now has a row — and a caveat: **Kraken's AI rationale is anonymously sourced, not firm-stated.**

Plus a fifth entry that closes a five-run absence claim: **Bitpanda's global brand campaign (2025-09-25)** — the firm recorded as producing "zero public marketing signal" on four consecutive runs has a four-language TV/OOH campaign with five football clubs, a mainstream agency and named creators, published on its own blog.

**The headline null survives intact. Day-27 named marketing-side enforcement silence HOLDS** — none of the five is an enforcement case.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-07-28
source A (jobs)   scan_date: 2026-07-28
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

**Feed-health guard: HEALTHY.** `scan_metadata` — `scanned_at_utc 2026-07-27T22:45:11Z`, `scan_date 2026-07-28`, 147 companies scanned (87 via API, 60 pending Chrome), **2,123 jobs fetched**, 28 after filter, **`new_count` 0**, **`url_verification_dropped` 0**, `still_open_count` 28. Six fetch-errors, of which **only Aave is tracked** (`api.lever.co/v0/postings/aave` → 404, unchanged for weeks); the other five (Wormhole, Injective, Bitwise, Chainlink Labs, Elliptic) are non-cohort. Drops breakdown: 1,611 excluded function · 357 no marketing keyword · 88 no seniority signal · 23 excluded seniority · 12 tracker · 4 excluded location.

Working-tree change was **date re-stamps only** — `_absence.csv` and `_chrome-queue.csv`, `as_of` 2026-07-27 → 2026-07-28, 7 rows each, no row added or removed. Kraken's two 07-23 Director, Paid Marketing reqs remain the most recent class-1 event and are unchanged.

### 2. Agency claims / overlap matrix (deterministic)

**Net-new: 0.** Source B `trend-data.json` `lastUpdated` **2026-06-15 — 43rd day unchanged.** Matrix idempotent at 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots rewritten identically. **NOT re-escalated** — stable-by-decision per the 07-10 Path-2 ruling.

**But the matrix took a substantive hit from elsewhere in this run** — see the Bitpanda/Serviceplan finding under class 4. The matrix cannot see mainstream agencies, and at the top of Stratum 1 that is where the brand work goes. This does not change a single row; it changes what the rows *mean*.

### 3. Regulator — **1 net-new entry + 1 material date correction. Full-range re-sweep executed.**

**Net-new named marketing-side ENFORCEMENT cases: still 0. Day-27 silence holds, unbroken.**

#### (a) NET-NEW — AFM (Netherlands), baseline study, **2025-01-21**

→ `../regulator-filings/afm-casp-advertising-cost-information-baseline-2025-01.md`

| field | value |
|---|---|
| documents | News item *"MiCAR requirements for advertising and the provision of information"* (21/01/25) + report *"Study into advertisements and information disclosure on costs by CASPs"* (January 2025) |
| URLs | `https://www.afm.nl/en/sector/actueel/2025/jan/sb-crypto-reclame` · `https://www.afm.nl/~/profmedia/files/rapporten/2025/study-advertisement-information-casp-en.pdf` |
| date verification | on-page stamp `News 21/01/25` + URL path `/2025/jan/` + PDF cover "January 2025" + `© Copyright AFM 2025` |
| fieldwork | advertisements studied 2023 **and** 2024; cost information studied 2023 — all **pre-MiCAR**, stated by the AFM |

**This completes a two-point time series at one regulator on one defect set — and that, not the document itself, is the finding.**

| | T0 — 2025-01-21 | T1 — 2026-04-16 |
|---|---|---|
| instrument | guidance + published defect classes | thematic supervisory review |
| measurement | none — qualitative examples | **33 CASPs; 14 advertising; 19 cost** |
| posture | *"we urge CASPs to apply the guidance"* | *"The period of leniency has ended"* (van Beusekom) |
| the defect | *"trading 'safely' in cryptos … it is essential to provide further explanation or context"* | *"statements referring to 'safe' trading in crypto, without further explanation or clarification of the associated risks"* |

**The same defect, in near-identical wording, fifteen months apart, now with a count attached.** The report can therefore make a claim much harder than "regulators are paying attention": *a supervisor published specific, actionable guidance; waited fifteen months; re-tested; and found the same defects at scale.* That converts the "quiet copy" read from an inference about firm behaviour into a **measured non-response to published guidance**.

**The single most operationally usable sentence any NCA has published on this surface**, captured verbatim:

> "One way of ensuring that the information is in a prominent place is to locate it **one click away from the homepage, or two clicks if using a drop-down menu**."

That is testable by any reader against any CASP website in under a minute. It belongs in Chapter 5 and probably in the appendix as a checklist item. Also captured verbatim: the AFM calling *"investing/trading in crypto-assets has/involves risks"* **"too generic"**, and the full eight defect classes with their Art. 66(2)/(3)/(4) MiCAR hooks.

**Leads recorded, not entered (out of window):** AFM's *"Crypto apps are not yet tailored to customers' interests"* (early 2024) and an earlier AFM **exploratory study into finfluencers** (undated in source). The finfluencer study is worth a targeted check — a second NCA on the same channel as BaFin would materially strengthen Chapter 4.

#### (b) CORRECTION — BaFin *Risks in Focus 2026* is dated **2026-01-28**, not 2026-02-18

→ `../regulator-filings/bafin-risks-in-focus-crypto-finfluencer-2026-01.md` (supersedes the `-2026-02` file, retained as a tombstone stub)

**Four-point primary verification, all on bafin.de:** on-page field `28.01.2026` · byline `| Press release | 28 January 2026` · URL slug `pm_2026_01_28_PK_Risiken_im_Fokus_en.html` · companion speech slug `re_260128_…`. Internally corroborated: the release says the report "was presented on Wednesday in Frankfurt" — **28 January 2026 was a Wednesday; 18 February was not.**

**The 07-27 `[VERIFY]` flag was the correct call and it caught a real error exactly one run later.** Root cause: the chapter page has no machine-readable date, so the run fell back to SAFE Frankfurt's write-up — which dates **the presentation event it attended**, not the publication. This is **watch (o) in a second costume**: *date the statement, never the write-up* → **date the document, never an event held about the document.**

**Consequence, and it is not housekeeping.** BaFin becomes the **first** NCA in the corpus to name the promotional channel as a 2026 supervisory priority:

| Date | Regulator | Instrument |
|---|---|---|
| 2025-01-21 | AFM (NL) | Baseline study + published defect classes |
| **2026-01-28** | **BaFin (DE)** | **Top-three consumer risk; finfluencer screening committed** |
| 2026-04-16 | AFM (NL) | Thematic review — 33 CASPs, defect rates, supervisory letters |
| 2026-06 | ESMA / AMF | Transitional-period-end statements |

**Additional primary datum captured with the correction:** BaFin ranked consumer risks in *Risks in Focus* **for the first time** in the 2026 edition, and *"retail investors making investment decisions fuelled by social media, especially relating to cryptoassets"* is **one of exactly three inaugural entries**. The 07-27 capture established *that* BaFin named the channel; this establishes **how high it was placed**. Presented by BaFin President **Mark Branson**, Frankfurt, 28 January 2026.

#### (c) Full-range sweep — checked and NOT entered, with reasons

- **CONSOB (Italy), Communication No. 16/25, 2025-12-04** — investor warning + operator call-to-attention ahead of the 30 December 2025 OAM/VASP deadline. Primary PDF read (`https://www.consob.it/documents/d/asset-library-1912910/pr_20251204`). **Not entered: not marketing-side.** It is a transitional-perimeter instrument, the class Chapter 1 already covers, and it names no marketing conduct. Recorded here because it dates Italy's national transitional close (30 Dec 2025 → operations to 30 June 2026 for applicants) and confirms CONSOB's marketing-communications remit exists on paper without having been exercised.
- **CySEC (Cyprus), circular 2026-07-09** — AML-control strengthening drawing on AMLA guidance. **Not entered: AML, not marketing-side.** Consistent with the out-of-window CySEC AML item excluded on 07-24.
- **AMF (France)** — thematic-review page swept; only transitional-period reminders and the wind-down/blacklisting regime surfaced, already covered in `amf-mica-transitional-period-end-2026-06.md`. **No net-new marketing-side item.**
- **CNMV (Spain)** — no marketing-side item surfaced in this sweep. Carry to next run with a direct site read rather than aggregate search.

### 4. Operator statements — **0 net-new qualifying; 1 net-new campaign artefact; one five-run absence claim demolished**

**Net-new class-4 operator statements: 0.** Every candidate verified and excluded for a stated reason.

#### The Bitpanda finding — an absence claim that was an instrumentation artefact

→ `../marketing-campaigns/bitpanda-when-crypto-then-bitpanda-2025-09.md`

Bitpanda has been recorded as producing **zero in-window public marketing signal on four consecutive runs**, each time flagged as remarkable for a firm `tracked-firms.md` marks "deep MiCA readiness signal expected."

**Bitpanda published a global brand campaign on its own blog on 2025-09-25** — *"When crypto, then Bitpanda"* — in **four languages** (EN/DE/FR/IT), with **TV, out-of-home, digital and social** deployment, **five football clubs** (PSG, Bayern Munich, AC Milan, FC Basel, **Arsenal**), **Alexander Zverev**, creators **Melissa Satta** and **Caro Daur**, creative by **Serviceplan**, production by **27km**. Date verified: on-page byline `25.09.2025` + asset filename `250922_ATL_Thumbnails_Blog.png`.

> **The class-4 sweep was reading interview and podcast surfaces and not reading firms' own owned channels.** The 07-25 fix widened the *time* axis; this is the *surface* axis, and it was never widened. **Before Phase 2 writes any absence sentence, every tracked firm's own blog/newsroom/press page must be swept.** An absence panel built from media surfaces measures media bookings, not marketing visibility. → new watch **(p)**.

**Three findings from it, one per theme:**

- **THEME 3 — the agency matrix has a blind spot that changes what its rows mean.** Serviceplan and 27km are mainstream European agencies, not crypto-native, and will never appear in the 18-agency panel or the overlap matrix. Any Theme-3 claim of the form *"N tracked firms have no named agency relationship"* is actually measuring **absence from the crypto-native panel**. Phase 2 must distinguish *no named agency* from *named non-crypto-native agency*. Bitpanda is the first documented instance; there are likely more at the top of Stratum 1.
- **THEME 4 — a good-practice exemplar, which the corpus was short of.** The page self-labels *"This Promotion"* (Art. 66(2) "identified as such") and warns *"the invested amount may be **lost completely**"* — which is precisely the specificity the AFM's January-2025 study demanded when it called generic risk boilerplate **"too generic."** Chapter 5 has defect examples and few contrasting positives; this is one, dated and primary. **Caveat printed, not smoothed:** this is the blog post *about* the campaign; the TV/OOH/social/creator executions have not been verified. Do **not** print "Bitpanda's campaign is compliant."
- **THEME 4 — two collisions with material already in the corpus.** (i) **Arsenal FC** ↔ `fca-premier-league-sponsorship-warning-2026-06.md`, with Bitpanda stating it is "expanding its UK presence." (ii) **Caro Daur**, a German-language Instagram creator, ↔ BaFin's commitment to *"a random market screening of selected German-speaking finfluencers on … YouTube and Instagram"* (2026-01-28). **Not an allegation of any breach** — a documented instance of the exact configuration a regulator named four months later.

**Role exclusion applied.** The only quoted individual is **CEO Eric Demuth** → **not a class-4 operator statement**, consistent with Ghoos / Liniger / Armstrong / Gauthier. **Bitpanda's in-window senior-marketing-operator count stays at ZERO for a fifth run** — but the character of that zero has changed decisively, from *"produces no public marketing signal"* (false) to **"ships a fully-resourced multi-market brand campaign and its marketing leadership never speaks publicly about it."** That is a Theme-1 gate-stack-visibility finding, not missing data.

**Loose ends closed this run:**
- **Magdalena Hörhager / Rival** — the "undated" flag carried since 07-23 is **resolved: the interview is from 2023**, and she appears there as **VP of Growth**, not CMO. Out of window; not entered.
- **Marta Radi** identified as Bitpanda **Head of Marketing** (secondary: The Org). `[VERIFY]` before any use.

### 5. Layoff tracker — **1 net-new row + 1 major row correction; tracker 12 → 13; two Tier-1 tracked firms were missing**

#### (a) NET-NEW — **Kraken (Payward), TRACKED Stratum 1**

| field | value |
|---|---|
| cuts executed | **Thursday 2026-05-14**; first reported **Friday 2026-05-15** (Bloomberg) |
| headcount | **~150**, approx **5%** of a ~3,000-person workforce |
| rationale | AI efficiency — **anonymously sourced, NOT firm-stated** |
| primary/near-primary | Bloomberg 2026-05-15 (source slug date) · Cointelegraph 2026-05-18 · Unchained 2026-05-18 (`article:published_time 2026-05-18T09:24:58+00:00`) · CoinDesk independently confirmed headcount |

**The sourcing distinction is the finding, and it must survive into the report.** Bloomberg attributes the AI rationale to *"a person familiar with the matter who was not authorized to speak publicly."* Kraken has made **no on-the-record public statement of rationale**; Cointelegraph "reached out to Kraken but did not receive an immediate response."

**Kraken is therefore the only AI-framed row in the tracker whose framing is anonymously sourced.** Every other AI row is firm-stated: Coinbase (Armstrong memo), Crypto.com (CEO on record), Gemini (company announcement). Every non-AI row is firm-stated too: OP Labs (CEO on X), Polygon (CEO on X), Exodus (SEC Exhibit 99.1).

**This corrects an unsourced corpus assertion.** The Polygon Labs row, added 07-20, already asserted *"the AI-efficiency framing that dominates Crypto.com/Coinbase/**Kraken**/Gemini"* — when no Kraken row existed and no Kraken source had ever been captured. It has one now, with the caveat it always needed.

**REJECTED and NOT entered:** an aggregator (`interviewpal.com`) claims the cuts fell on *"customer service, compliance, and trading support"* and that an AI chatbot handles *"~80% of customer inquiries."* **Neither claim appears in Bloomberg, Cointelegraph, Unchained or CoinDesk.** Both were tempting — the compliance-cut claim in particular would have been a strong Theme-4 datum six weeks before the MiCA deadline — and both are unsourced. Not entered.

**THEME-2 DATED SEQUENCE, both legs already in this corpus:** AI-attributed cut **2026-05-14/15** → CGMO **Mayur Gupta** describes a *"natively AI growth engine"* in an interview published **2026-05-19** (`../operator-statements/kraken-gupta-growth-operating-model-2026-05.md`). **Four days.** It mirrors the Coinbase Ferdon (04-09) → Armstrong (05-05) pairing **in the opposite order**: cut first, operator statement after. State the sequence; refuse the causal story.

Context recorded: cuts framed internally as pre-IPO optimisation; IPO may slip to 2027; confidential S-1 Nov-2025, listing paused Mar-2026; co-CEO Arjun Sethi says "80% ready" at Consensus Miami; $20B private valuation vs ~$13.3B implied by secondaries; concurrent acquisitions (NinjaTrader $1.5B, Reap $600M agreed, Bitnomial $550M closed 05-04) and an OCC national trust bank charter filing.

**Kraken is now triple-loaded:** the 05-14 cut + the 07-23 US/UK paid-Director pair + the **07-31 MiCA-lapse checkpoint, three days out.**

#### (b) CORRECTED — **Gemini, TRACKED Stratum 1** — the row was wrong on date, source and rationale

The pre-run row read: `Gemini,2026-Q1,,-30% YTD,,N,Cumulative cuts across Q1` — **undated, unsourced, and flagged non-AI. All three wrong.**

| field | corrected value |
|---|---|
| date | **2026-02-05** (Thursday) |
| event | **Exit from the United Kingdom, European Union and Australia** + **25% workforce reduction**, announced together |
| rationale | **AI-framed and FIRM-STATED** — AI automating labour, engineers *"100x"* more efficient, plus a harder UK/EU/AU business environment |
| source | Cointelegraph 2026-02-05, quoting the company announcement directly |

Verbatim from the announcement:

> "These foreign markets have proven hard to win in for various reasons, and we find ourselves **stretched thin with a level of organizational and operational complexity that drives our cost structure up and slows us down**."

> "**We don't have the demand in these regions to justify them.** The reality is that America has the world's greatest capital markets."

Resources redirected to the US business and to **Gemini Predictions** (launched Dec-2025; 10,000+ users, $24M volume at announcement): *"Our thesis is that prediction markets will be as big or bigger than today's capital markets."*

**THEME 4 — this is the part that matters. Gemini, not Binance, is the first Tier-1 tracked exchange to leave the EU.** 2026-02-05, **five months before** the 1 July transitional deadline and **four months before** Binance's exit (`../regulator-filings/binance-mica-eu-exit-2026-06.md`). The corpus has been treating the Binance exit as the leading case. It was not the first.

**And it creates a second, cleaner category of absence.** A tracked firm that exits the EU removes its entire EU marketing surface from the report's observable universe. That is an absence **with a documented cause** — a different object from an absence with none, and the absence panel must separate them or it will read structural withdrawal as reticence.

**Figure reconciliation, unresolved and flagged.** The old row's "-30% YTD" had no source; the primary-reported 2026-02-05 figure is **25%**. Compatible if further Q1 cuts followed, but the corpus has no source for the extra ~5pp. **25% is the only citable figure.** `[VERIFY]` before Phase 2 prints the YTD aggregate. Also `[VERIFY]`: locate and archive Gemini's own announcement post for a fully primary anchor (present anchor is near-primary).

#### Standing Theme-5 findings after this run

- **Across all 13 rows, not one names marketing as the affected function.** Thirteen now, not twelve. Kraken and Gemini both fit the pattern.
- **Watch (h′) goes n=4 → n=6, and the split holds and strengthens.** AI framing at **consumer exchanges**: Crypto.com (Mar), Coinbase (05-05), **Gemini (02-05)**, **Kraken (05-14)** — four of four. Non-AI framing at **infrastructure/protocol firms**: OP Labs (03-12), Polygon Labs (07-16) — two of two. The hypothesis survives its first real test. **It is not yet safe to print** — n=6, and Kraken's framing is anonymously sourced, which weakens one of the four consumer-exchange legs.
- **Chronology corrected again.** Gemini (02-05) now precedes Crypto.com (03) as the earliest 2026 tracked-firm cut in the tracker, and it is AI-framed. The AI-cover narrative starts earlier than the corpus thought **and** the counter-pattern starts earlier than the corpus thought (OP Labs, 03-12). Both ends moved this week.
- **Also checked, not entered:** Dune (~25%, week of 05-15) — non-tracked data company, perimeter. Block's tracker row says "2026-Q2, 4000" while Cointelegraph places the cut in **February** — `[VERIFY]`, unchanged this run. Coinbase CPO departure **still unentered for a fourth consecutive run** (no primary, conflicting dates) — watch (j) unchanged.

### 6. Longitudinal shift for synthesis

Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-28 section), with corrections written back into `../../findings/00-opening-register-first-cases-later.md`:

1. **Class-3 chronology re-ordered** — AFM baseline (2025-01-21) → BaFin (2026-01-28, corrected) → AFM review (2026-04-16) → ESMA/AMF (2026-06). The regulator sequence now starts **fifteen months before** the transitional deadline, not two.
2. **The AFM two-point series** replaces an inference with a measurement: guidance published, market re-tested fifteen months later, same defects at scale.
3. **Layoff-record count 12 → 13**; Gemini row corrected; watch (h′) n=4 → n=6.
4. **Theme 4 gains a Tier-1 EU exit that predates Binance's by four months**, and the absence panel gains a required distinction between structural withdrawal and reticence.
5. **Theme 3 gains a documented blind spot** in the agency matrix (mainstream agencies at the top of Stratum 1).

Methodology guards applied and satisfied: multi-point date verification before every entry (AFM: on-page stamp + URL path + PDF cover; BaFin: four-point + weekday cross-check; Kraken: Bloomberg slug + Unchained `article:published_time` + CoinDesk corroboration; Gemini: publication date + "Thursday" cross-check; Bitpanda: byline + asset filename); verbatim reproduction without silent correction; **explicit refusal to enter an unsourced aggregator claim that would have strengthened the report** (Kraken function breakdown); role-eligibility enforced against a quote the corpus wanted (Demuth); corrections logged rather than silently fixed (BaFin date, Gemini row, Kraken assertion).

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged; still France-reported-only.
- **(b) First named post-deadline NCA marketing-side action** — **day-27 silence HOLDS.** Reading NCA sites directly remains the productive method. Remaining: CNMV and CONSOB direct reads; the **AFM finfluencer study** (a second NCA on BaFin's channel) is the highest-value outstanding class-3 target.
- **(c) Capture panel** — six firms. **Kraken MiCA-lapse checkpoint 07-31 is 3 days out** (with OKX 8% campaign end). Relai lead unchanged.
- **(d) Agency panel staleness — 43 days.** Stable-by-decision; not re-escalated. But see (q).
- **(e) Loop cadence** — 07-28 fired normally and on schedule; first clean single-fire day in over a week. **Eighth consecutive run carrying this item; still needs Jukka's eyes**, but the trend improved today.
- **(f) Friday nomination cadence** — next check Friday **07-31**. No `inbound-nominations.md` exists.
- **(g) Coinbase brand-rebuild signal** — unchanged at n=1 on postings (Creative Director, 07-17); qualitative half anchored by Ferdon.
- **(h′) Layoff-rationale correlates with firm type** — **n=4 → n=6 and the split held.** Consumer exchanges AI-framed 4/4; infrastructure/protocol non-AI 2/2. **Do not print yet**: n is small and Kraken's leg is anonymously sourced.
- **(i) Kraken paid-media build-out** — re-scoped 07-27 to the jurisdictional-split question (US + UK pair on 07-23). **Now materially richer**: the same firm cut ~150 staff on 05-14 citing AI, and its CGMO described an AI-native growth engine four days later, and it opened two paid-Director reqs ten weeks after that. Three dated legs at one tracked firm. Sequence only; no causal claim.
- **(j) Senior-leader exits trailing contractions** — unchanged; Coinbase CPO still unverified, fourth run.
- **(k) Chrome-lane instrumentation gap** — unchanged; the 07-25 Binance Dubai req remains unrecoverable.
- **(l) `methodology.md` §4 inventory too narrow** — **now demonstrably costly, and the fix is bigger than first scoped.** §4 lists podcasts and conference surfaces. It does not list **firms' own blogs and newsrooms**, which is where Bitpanda's campaign sat for ten months. Widen §4 to: marketing trade press + regional-language media + **firm-owned channels**.
- **(m) Ad-platform gating** — unchanged (Google France, 2026-07-01).
- **(n) Full-range re-sweep — ✅ EXECUTED for classes 3 and 5, and it returned four net-new entries including two Tier-1 tracked-firm layoffs.** The defect is confirmed real and was costing the corpus material at the centre of its cohort. **Not closed:** classes 3 and 5 have had *one* pass; class 4's surface axis is still open (see (p)); and the sweep has not yet been run for classes 1 and 2's historical backfill.
- **(o) Date the statement, never the write-up** — **VINDICATED within one run.** BaFin's date was three weeks wrong because a secondary source dated a presentation event rather than the publication. **Extended:** *date the document, never an event held about the document.*
- **(p) NEW — absence claims must be tested against firms' OWN channels before they are written.** Bitpanda was recorded as producing zero public marketing signal on four consecutive runs while running a four-language TV/OOH campaign on its own blog. The 07-25 correction widened the *time* axis of the class-4 sweep; the *surface* axis was never widened. **Before Phase 2 writes any absence sentence: sweep every tracked firm's blog / newsroom / press page.** This is now the highest-priority method item, replacing (n) at the top.
- **(q) NEW — the agency overlap matrix measures the crypto-native segment, not "agency relationships".** Bitpanda's Serviceplan engagement is invisible to it by construction. Every Theme-3 absence claim needs re-reading in that light, and Phase 2 must distinguish *no named agency* from *named non-crypto-native agency*.
- **(r) NEW — the absence panel needs a "structural withdrawal" category.** Gemini exited the UK/EU/AU on 2026-02-05. A firm that has left the market produces no EU marketing signal for a documented reason. Reading that as reticence would be a straightforward error, and the panel currently has no way to distinguish the two.

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2 deterministic; 0 net-new both; date re-stamps only. Summary captured above.
2. Feed-health guard: direct read of `prospects/open-positions.json` `scan_metadata` / `drops_summary` / `new_since_last_scan` / `fetch_errors`.
3. `git status` / `git diff --stat` / `git log origin/main..HEAD` / `git branch -vv` → clean tree at 225500c, already on origin/main.
4. Dedup baseline reads: 07-27 run #2 in full, `longitudinal-2026-06.md` tail, layoff tracker, `regulator-filings/` + `operator-statements/` + `marketing-campaigns/` listings, BaFin file head.
5. WebSearch (domain-restricted, `afm.nl`) `AFM report crypto advertising cost information CASPs 2025 earlier study` → **located the January-2025 baseline study** — the exact target of the last run's recommendation #2.
6. `web_fetch` `afm.nl/en/sector/actueel/2025/jan/sb-crypto-reclame` → **primary verification**: `News 21/01/25`, the pre-MiCAR fieldwork statement, the "safe trading" defect, the report-PDF link. **→ ADDED as class 3.**
7. `web_fetch` `afm.nl/~/profmedia/files/rapporten/2025/study-advertisement-information-casp-en.pdf` → **full report read**: eight defect classes verbatim, the "one click from the homepage" standard, Art. 66(2)/(3)/(4) hooks, "too generic" ruling, out-of-window leads.
8. WebSearch `CONSOB crypto marketing communications MiCA CASP supervisory action 2026` → surfaced Communication 16/25.
9. `web_fetch` `consob.it/documents/d/asset-library-1912910/pr_20251204` → **primary PDF read**; **not entered** (perimeter/transitional, not marketing-side).
10. WebSearch `CySEC circular crypto asset service provider marketing communications 2026` → 07-09 AML circular; **not entered** (AML, not marketing-side).
11. WebSearch `AMF France communication promotionnelle crypto PSAN MiCA contrôle thématique 2026` → transitional/wind-down material only; no net-new.
12. WebSearch (domain-restricted, `bafin.de`) `"Risks in Focus 2026" BaFin publication date press release February 2026` → **press release with `pm_2026_01_28` slug surfaced; the recorded date was wrong.**
13. `web_fetch` bafin.de `…/pm_2026_01_28_PK_Risiken_im_Fokus_en.html` → **four-point date verification + the "first time … consumer risks" datum + Branson attribution. → DATE CORRECTED.**
14. WebSearch `crypto exchange marketing team layoffs 2025 2026 growth department restructuring brand team cut` (full-range, per watch (n)) → surfaced **Kraken** and **Gemini** as 2026 cutters absent or under-recorded in the tracker.
15. WebSearch `Kraken layoffs 2026 workforce reduction staff cut announcement` → Bloomberg/CoinDesk/Cointelegraph/Unchained cluster.
16. `web_fetch` `cointelegraph.com/news/kraken-parent-payward-cuts-150-staff-potentially-delaying-ipo-report` → published 2026-05-18; Bloomberg reported Friday; **anonymous-source attribution captured verbatim**; no Kraken response.
17. `web_fetch` `unchainedcrypto.com/kraken-cuts-150-workers-…` → `article:published_time 2026-05-18T09:24:58Z`; **cuts executed Thursday**; ~5% of ~3,000; CoinDesk corroboration; IPO/acquisition context. **→ ADDED as class 5.**
18. `web_fetch` `cointelegraph.com/news/gemini-exit-uk-eu-australia-slashes-workforce` → **published 2026-02-05**; UK/EU/AU exit + 25% cut; **AI + "100x" rationale verbatim from the company announcement**. **→ Gemini row CORRECTED.**
19. `web_fetch` `cointelegraph.com/features/how-ai-cryptos-favorite-reason-cut-staff` → **empty body; nothing extracted; nothing entered.** Recorded because it would have been a useful synthesis corroboration.
20. WebSearch `Bitpanda OR Bitstamp OR Phantom OR "Sui Foundation" head of marketing CMO interview 2026 brand campaign MiCA` → surfaced the **Bitpanda brand-campaign blog post**, Marta Radi as Head of Marketing, and **dated the Hörhager/Rival interview to 2023**.
21. `web_fetch` `blog.bitpanda.com/en/experience-our-new-brand-campaign-now` → **primary verification**: `25.09.2025` byline, four localisations, five clubs, Zverev, Satta/Daur, Serviceplan, 27km, channel plan, "This Promotion" disclaimer verbatim, Demuth quote. **→ ADDED as marketing-campaigns; Demuth excluded by role.**
22. Repo-wide dedup greps (`gemini`, `payward`, `kraken layoff`, `150 workers`, `serviceplan`, `zverev`, `demuth`, `bitpanda`, `2025-01-21`, `study-advertisement-information`) → all five additions confirmed net-new before writing.

## Net-new / changed this run

- `corpus/regulator-filings/afm-casp-advertising-cost-information-baseline-2025-01.md` (**NEW FILE — 1 net-new class-3 entry**; AFM 2025-01-21 baseline, eight defect classes verbatim, the "one click from the homepage" standard, Art. 66 hooks, T0/T1 time-series framing, out-of-window leads logged)
- `corpus/regulator-filings/bafin-risks-in-focus-crypto-finfluencer-2026-01.md` (**NEW PATH — supersedes the `-2026-02` file**; date corrected 2026-02-18 → **2026-01-28** with four-point primary verification; `[VERIFY]` cleared; class-3 chronology re-ordered; press-release "first time … consumer risks" datum added; numeric-hygiene flag preserved)
- `corpus/regulator-filings/bafin-risks-in-focus-crypto-finfluencer-2026-02.md` (**overwritten as a TOMBSTONE STUB** pointing to the corrected file. *Recorded because it is a workaround, not a preference: the repo mount returns `Operation not permitted` on `unlink`, so autonomous runs cannot delete files or complete a `git mv`. The old path is cited in the 07-27 run record, in `longitudinal-2026-06.md`, and in commit `225500c` which is already on origin/main — a dangling citation would be worse than a stub. **Jukka: a manual `git rm` on a local checkout retires this cleanly.***)
- `corpus/layoff-tracker/2026-layoff-tracker.csv` (**+1 row (Kraken, TRACKED Stratum 1) and 1 row corrected (Gemini — date, source, rationale, AI flag N→Y); tracker 12 → 13**. Written with `lineterminator='\n'` per the convention fixed 07-27; file re-parsed after write — 13 data rows, 7 fields each, LF-clean, no field corruption.)
- `corpus/marketing-campaigns/bitpanda-when-crypto-then-bitpanda-2025-09.md` (**NEW FILE**; Bitpanda global campaign 2025-09-25, full participant list, agency blind-spot finding, compliance-exemplar reading with caveat, Arsenal/FCA and Daur/BaFin collisions, Demuth role exclusion, Hörhager loose end closed)
- `findings/00-opening-register-first-cases-later.md` (**draft chapter corrected** — class-3 chronology re-ordered and extended back to 2025-01; BaFin date fixed; layoff count 12 → 13; Gemini EU exit added ahead of Binance; citation anchors updated)
- `findings/longitudinal-2026-06.md` (2026-07-28 section)
- `corpus/weekly-runs/2026-07-28-corpus-run.md` (this record)
- **Not changed:** `job-postings/*.csv` (0 adds; `_absence.csv` + `_chrome-queue.csv` date re-stamps only); `agency-overlap-matrix.csv` + `agency-claims/*` (idempotent); `operator-statements/*` (0 adds — every candidate verified and excluded for a stated reason)

## Recommendation for next run

1. **Watch (p) is now the highest-priority method item: sweep every tracked firm's own blog / newsroom / press page.** Bitpanda proves the class-4 absence panel is measuring media bookings rather than marketing visibility. Start with the firms currently recorded at zero: Bitstamp, Sui, Phantom, Ledger, Bybit, OKX.
2. **07-31 is the nearest dated checkpoint — three days out:** Kraken MiCA lapse + OKX 8% campaign end + Friday nomination check. Kraken is triple-loaded; prepare the capture before the date rather than after.
3. **Find the AFM finfluencer study.** A second NCA on BaFin's exact channel would make Chapter 4's finfluencer thread two-regulator rather than one, and the AFM has already proven it publishes quantified follow-ups.
4. **`[VERIFY]` the two open figures:** Gemini's ~30% YTD aggregate (only 25% is citable) and Block's tracker date (row says Q2; Cointelegraph says February).
5. **Locate Gemini's own announcement post** to upgrade the 02-05 row from near-primary to primary. It is a load-bearing Theme-4 row now — the first Tier-1 EU exit — and it deserves a primary anchor.
6. **Phase 2 blocker, stated plainly:** three absence claims were exposed as instrumentation artefacts on 07-27, and a fourth (Bitpanda) today. **No "no public signal" sentence should be written until watch (p) has been executed once, in full, across the cohort.**
7. **Escalate to Jukka:** (i) the mount's `unlink` block, which now costs a stub file per rename in addition to the `.git/index.lock` workaround; (ii) scheduler cadence, though 07-28 fired cleanly.

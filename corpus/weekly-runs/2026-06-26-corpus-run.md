# Corpus-assembly weekly run — 2026-06-26 (window: June 21–26, 2026)

**Run type:** Phase-1 corpus assembly (automated weekly, Fri 15:00 cadence — run executed 2026-06-26).
**Methodology:** public-source synthesis only. Every entry anchored to a primary/public source with a URL. No off-the-record, no anonymised, no guessed URLs. Absence of public signal is recorded as data (per `../../methodology.md`).
**Cohort:** the Stratum 1–4 tracked firms + the 18-agency comparison panel in `../../tracked-firms.md`.
**Dedup baseline read before searching:** prior run `weekly-runs/2026-06-20-corpus-run.md`; existing `regulator-filings/fca-premier-league-sponsorship-warning-2026-06.md`; `operator-statements/sport-sponsorship-reset-2026-05.md`; `layoff-tracker/2026-layoff-tracker.csv` (6 rows); `job-postings/*.csv` (all empty scaffolds); `findings/longitudinal-2026-06.md`.

> **Note on directory naming:** following the repo's existing structure (`corpus/regulator-filings/`), not the `corpus/regulator/` path used in `methodology.md`. Consistent with the 2026-06-20 run.

---

## Headline result

**One NET-NEW, in-window (June 21–26), public-source-verifiable item this week — a regulator statement.**

The MiCA transitional period ends **1 July 2026**, and ESMA issued a **Public Statement on 23 June 2026** (ref. ESMA75-113276571-1710) instructing unauthorised CASPs to wind down in an orderly manner — with **"cease marketing activities and solicitation"** named as the first operative obligation. This is the first EU-level regulator document in the corpus that treats marketing cessation as a front-line, observable compliance act, and it is genuinely net-new (distinct reference number from, and operatively beyond, the 17 April 2026 ESMA statement). Added to the regulator corpus and folded into the June longitudinal note.

Across the other five source classes: **0 net-new verifiable items.** The big June crypto-marketing personnel signals (Crypto.com CMO Steven Kalifowitz's exit executing **30 June 2026**; Binance CMO Rachel Conlan's mid-June departure with Eowyn Chen interim) remain **longitudinal confirmations, already captured** — not net-new. Per methodology, those absences are themselves Phase-2 data.

---

## By source class

### 1. Job postings (senior crypto-marketing roles at tracked firms)
**Net-new this week: 0 verifiable.** No senior brand/growth/PMM/community/agency-mgmt/regulatory-comms posting at a tracked firm could be anchored to a primary source with a confirmed in-window posting date (June 21–26). Same structural gating issue as prior runs: job-board aggregators surface undated generic listings; WebSearch alone cannot date-stamp ATS postings reliably. Firm CSV scaffolds remain empty pending a Chrome-MCP rendered-DOM pass of each tracked firm's Greenhouse/Lever/Ashby board. Recommendation carried forward (see below).

### 2. Agency claims (18-agency panel)
**Net-new this week: 0 verifiable.** Searches again returned only 2026 "top crypto marketing/PR agency" listicles (MEXC News, ICODA, Coinbound, Crypto Daily, DailyCoin, TechBullion) — not firm-side case studies or dated client-claim press releases from a tracked agency inside the window. No new entrant to `agency-claims/`; `agency-overlap-matrix.csv` still not seeded (requires ≥1 verifiable net-new claim to seed honestly).

### 3. Regulator (ESMA, BaFin, AMF, CONSOB, AFM, CySEC, FCA, MAS, VARA)
**Net-new in-window: 1.** **ESMA Public Statement, 23 June 2026 (ESMA75-113276571-1710)** — orderly wind-down of unauthorised CASPs as the MiCA transitional period ends 1 July 2026; first enumerated obligation is to "cease marketing activities and solicitation"; extends to extraterritorial B2B solicitation (narrow reverse-solicitation carve-out); requires repeated client wind-down communications; signals coordinated NCA action post-deadline. Primary PDF fetched + read verbatim. Filed: `../regulator-filings/esma-mica-transitional-period-end-2026-06.md`. Coordinated same-day national statements (AMF, MFSA) logged as secondary corroboration in that file. Other items reviewed and dated OUT of window or already-known: BaFin finfluencer/"Risks in Focus 2026" (Jan 2026); AMF unauthorised-entity warnings (April 2026); ESMA 17 April 2026 statement (already flagged for Theme-4 backfill); FCA→clubs sponsorship warning (already in corpus).

### 4. Operator statements (senior operators at tracked firms)
**Net-new this week: 0 verifiable.** In-window context: **Crypto.com CMO Steven Kalifowitz's** departure executes **30 June 2026** (captured May; CoinDesk 2026-05-05) — a longitudinal tick, not a new on-the-record statement. Blockworks' flagship conference ran **24–26 June 2026 (Brooklyn)**, but no public verbatim statement by a *tracked-firm* CMO/VP/Head-of-Brand/Growth on the marketing-comms surface could be anchored with speaker + URL + date inside the window. No operator-statement entry added.

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new this week: 0 verifiable.** No new public 2026 marketing-team contraction with a stated rationale surfaced in-window. Existing `2026-layoff-tracker.csv` (Crypto.com, Gemini, Algorand, Coinbase, Block, MARA) unchanged. No row added.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md`. Core advance this week: the June regulatory-pressure read now spans **both layers simultaneously** — placement/channel (FCA → club sponsorship, 06-02/03) and entity-permission/solicitation (ESMA → cease marketing & solicitation, 06-23, biting at the 1-July deadline). For Theme 4, marketing-going-dark becomes the first publicly observable signal of an unauthorised CASP's wind-down — i.e., the methodology's "what is publicly visible" filter is now directly load-bearing on the enforcement read.

---

## Searches run (audit trail)
1. crypto marketing financial-promotion enforcement June 2026 ESMA/FCA/MiCA → MiCA 1-July deadline backdrop; no named-firm marketing enforcement.
2. crypto exchange CMO marketing layoffs/appointment week of June 22 2026 → Kalifowitz (30 June) + Conlan/Chen (already captured).
3. BaFin/CONSOB/AMF/CySEC crypto advertising warning June 2026 → all out-of-window (Jan/April 2026).
4. crypto marketing news week of June 24 2026 (exchange brand/growth hire) → agency listicles only.
5. "June 2026" agency case study Coinbound/MarketAcross/Serotonin → listicles only; no dated firm-side claim.
6. MiCA transitional period ends 1 July 2026 / ESMA wind-down → surfaced the 23 June 2026 ESMA statement.
7. crypto CMO/head-of-marketing conference statement late June 2026 → Blockworks 24–26 June (no anchorable tracked-firm operator quote).
8. ESMA public statement 23 June 2026 unauthorised CASPs wind down (esma.europa.eu) → located primary PDF (ESMA75-113276571-1710); verified by fetch.

## Net-new added this run
- `corpus/regulator-filings/esma-mica-transitional-period-end-2026-06.md` (+1 regulator entry)
- `findings/longitudinal-2026-06.md` updated (two-layer regulatory-pressure read; 1-July deadline)

## Recommendation for next run (carried forward)
WebSearch still cannot reliably date-stamp careers-page postings or agency case studies. To move source classes 1 and 2 off zero, the weekly run should use the Chrome MCP to render each tracked firm's ATS board (Greenhouse/Lever/Ashby) and each tracked agency's case-study page, reading posting/publication dates from the DOM. This remains the single gating fix. The **1-July MiCA deadline week** is also the highest-probability window of the cycle for a named-firm marketing-side enforcement action or a tracked-firm CMO public statement — prioritise the regulator and operator classes in the next run.

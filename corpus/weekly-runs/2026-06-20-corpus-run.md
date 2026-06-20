# Corpus-assembly weekly run — 2026-06-20 (window: June 14–20, 2026)

**Run type:** Phase-1 corpus assembly (automated weekly, Fri 15:00 cadence — run executed 2026-06-20).
**Methodology:** public-source synthesis only. Every entry anchored to a primary/public source with a URL. No off-the-record, no anonymised, no guessed URLs. Absence of public signal is recorded as data (per `../../methodology.md`).
**Cohort:** the Stratum 1–4 tracked firms + the 18-agency comparison panel in `../../tracked-firms.md`.
**Dedup baseline read before searching:** existing `job-postings/*.csv` (all empty scaffolds), `layoff-tracker/2026-layoff-tracker.csv` (6 rows), `operator-statements/sport-sponsorship-reset-2026-05.md`, empty `agency-claims/` and `regulator-filings/` dirs.

> **Note on directory naming:** `methodology.md` refers to `corpus/regulator/`; the repo's actual structure (and `corpus/README.md`) uses `corpus/regulator-filings/`. This run follows the repo's existing structure (`regulator-filings/`) rather than inventing a new path.

---

## Headline result

**No NET-NEW, in-window (June 14–20), public-source-verifiable marketing-side items surfaced across the six source classes that are not already in the corpus.** The major crypto-marketing signals landing in June 2026 (Binance CMO Rachel Conlan's departure executing 15 June; Crypto.com CMO Steven Kalifowitz's exit at end-June) were already captured in the May operator-statements cluster — their occurrence this month is **longitudinal confirmation, not net-new**. One material, uncaptured **pre-window** regulator item (FCA→football-club crypto-sponsorship warning, 2026-06-02/03) was added as the baseline entry to the previously-empty regulator corpus.

Per methodology, the absence is itself a Phase-2 finding (see `../../findings/longitudinal-2026-06.md`).

---

## By source class

### 1. Job postings (senior crypto-marketing roles at tracked firms)
**Net-new this week: 0 verifiable.** No senior brand/growth/PMM/community/agency-mgmt/regulatory-comms posting at a tracked firm could be anchored to a primary source with a confirmed posting date inside June 14–20. Job-board aggregators (CryptoJobsList, cryptocurrencyjobs.co) surface generic Kraken "Growth Marketing Manager / Regional Marketing Director" listings, but without a verifiable in-window posting date and confirmed seniority these are not added — adding them would breach the citation-anchored + dedup rules. Firm CSV scaffolds remain empty pending a JS-rendered careers-page pass (recommend Chrome MCP for Greenhouse/Lever/Ashby boards in a future run; WebSearch alone cannot date-stamp these reliably).

### 2. Agency claims (18-agency panel)
**Net-new this week: 0 verifiable.** Searches returned only 2026 "top crypto marketing agency" listicles (Coingape, ICODA, Coinbound, DailyCoin 2026-06-16, Crypto Daily) — not firm-side case studies or dated client-claim press releases from a tracked agency. No new entrant to an `agency-claims/` file; `agency-overlap-matrix.csv` not created this run (would require ≥1 verifiable net-new claim to seed honestly).

### 3. Regulator (ESMA, BaFin, AMF, CONSOB, AFM, CySEC, FCA, MAS, VARA)
**Net-new in-window: 0.** Baseline entry added (pre-window): **FCA warning to football/Premier League clubs over unauthorised crypto sponsors (2026-06-02/03)** — see `../regulator-filings/fca-premier-league-sponsorship-warning-2026-06.md`. Other recent items reviewed and dated OUT of window: ESMA "end of MiCA transitional period" statement (2026-04-17); ESMA finfluencer factsheet + CONSOB amplification (~2026-01); BaFin "Risks in Focus 2026" finfluencer report (2026-01-28); AMF unauthorised-entity crypto warnings (2026-04). These are material to Theme 4 but are not this-week net-new; flagged for the Theme-4 baseline backfill, not logged as weekly net-adds.

### 4. Operator statements (senior operators at tracked firms)
**Net-new this week: 0.** In-window event: **Rachel Conlan's Binance departure executed ~15 June 2026** (Eowyn Chen interim CMO) — already documented in `operator-statements/sport-sponsorship-reset-2026-05.md` (captured 2026-05-14 from the CoinDesk 12-May scoop); the 15-June execution is a longitudinal tick, not a new statement. Marginal pre-window structural signal noted for synthesis: **Proof of Talk 2026 (Paris, Louvre, 2026-06-02/03) launched a "Crypto Content Council"** and banned paid speaking slots — a governance-of-crypto-content signal, but a conference-structural feature, not a tracked-firm operator statement; logged in findings, not added as an operator-statement entry.

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new this week: 0 verifiable.** No new public 2026 marketing-team contraction with a stated rationale surfaced in-window. Existing `2026-layoff-tracker.csv` (Crypto.com, Gemini, Algorand, Coinbase, Block, MARA) unchanged. No row added.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md`. Core read: the sport-sponsorship reset thesis (Theme 1/5) gained a **regulatory-pressure leg** this month (FCA→clubs) on top of the operator-P&L leg already documented — the buy-side host property is now being squeezed by the regulator, not just the sell-side exchange by its own CFO.

---

## Searches run (audit trail)
1. ESMA crypto marketing-communications enforcement June 2026 → only April transitional-period statement + Jan finfluencer factsheet (out of window).
2. FCA crypto financial-promotion enforcement June 2026 → FCA→clubs sponsorship warning (2026-06-02/03, pre-window); HTX action (Feb 2026, already-known precedent).
3. Crypto exchange CMO/marketing layoffs June 2026 → Conlan/Kalifowitz (already captured); Crypto.com 12% (March, already in tracker).
4. New CMO/head-of-marketing appointments June 2026 → Eowyn Chen interim (already captured).
5. Coinbound/MarketAcross/Serotonin new client case study June 2026 → listicles only.
6. BaFin/CONSOB/AMF crypto marketing warning June 2026 → all out-of-window (Jan/April).
7. BaFin "Risks in Focus" finfluencer report date → 2026-01-28 (out of window).
8. Crypto marketing news week of June 15 2026 → agency listicles only.
9. Proof of Talk 2026 marketing keynote → Content Council launch (2026-06-02/03, structural).
10. Kraken/OKX/Bitpanda/Bybit head-of-marketing hiring June 2026 → no date-verifiable senior posting.

## Recommendation for next run
WebSearch cannot reliably date-stamp careers-page postings or agency case studies. To make source classes 1 and 2 productive, the weekly run should use the Chrome MCP to load each tracked firm's ATS board (Greenhouse/Lever/Ashby) and each tracked agency's case-study page directly and read posting dates from the rendered DOM. That is the gating fix for moving job-postings and agency-claims off zero.

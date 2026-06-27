# Corpus-assembly daily run — 2026-06-27

**Run type:** Phase-1 daily corpus assembly (automated, daily cadence per 2026-06-26 framework upgrade).
**Methodology:** public-source synthesis only. Every entry anchored to a primary/public source with a URL. No off-the-record, no anonymised, no guessed URLs. Absence of public signal is recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + the 18-agency comparison panel in `../../tracked-firms.md`.
**Dedup baseline read before searching:** prior runs `2026-06-26` + `2026-06-20`; `regulator-filings/` (FCA club-sponsorship, ESMA 23-Jun wind-down); `operator-statements/sport-sponsorship-reset-2026-05.md`; `layoff-tracker/2026-layoff-tracker.csv` (6 rows); `agency-overlap-matrix.csv` (8 rows, 1 overlap); `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

> **Directory naming:** following the repo's existing `corpus/regulator-filings/` (not `corpus/regulator/` in methodology.md). Consistent with prior runs.

---

## Headline result

**One NET-NEW, in-window, public-source-verified item — the first NAMED tracked-firm MiCA marketing-cessation instance: Binance.** Plus deterministic feed sync produced its standard classes-1+2 output (no upstream feed change since yesterday → 0 new rows, expected) and one layoff-tracker enrichment.

The 2026-06-26 longitudinal note set the watch: *"the 1-July deadline week is the highest-probability window for the first named-firm instance — a significant unauthorised cross-border CASP visibly pulling EU marketing."* That instance is now on the record: **Binance's MiCA licence bid is set to be rejected by Greece's HCMC (Reuters, 2026-06-16)**, which — combined with the ESMA 23-June "cease marketing and solicitation first" obligation — makes Binance the report's lead Theme-4 candidate for marketing-cessation-as-enforcement-signal.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0 (expected, idempotent).** Source A (`open-positions.json`) scan_date **2026-06-26** — unchanged since yesterday's run, so the dedup-by-URL producer correctly added 0 rows. Job-postings corpus stands at prior totals (Ava Labs ×2, Optimism ×1 from API; Solana ×3 from Chrome lane). Chrome work-queue unchanged: Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys, Solana(closed). Absence (no API coverage): Aave, Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys — written to `job-postings/_absence.csv`. **Absence-as-data note:** Binance appearing in `_absence.csv` (proprietary ATS, no API coverage) the same week it faces a forced EU marketing wind-down is itself a Theme-4 datapoint — the firm under the most acute EU marketing-cessation pressure is also the least publicly legible via standard ATS.

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0 (expected).** Source B (`trend-data.json`) lastUpdated **2026-06-15** — unchanged. Matrix holds at 8 tracked firms, 1 OVERLAP (**Sui — Coinbound + RZLT**). 18 dated per-agency snapshots re-written (idempotent). No new agency claim to seed.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new in-window: 1 (named-firm consequence).** **Binance — MiCA licence rejection / forced EU exit** (Reuters 2026-06-16; Greece HCMC). Filed `regulator-filings/binance-mica-eu-exit-2026-06.md`. This is the first named tracked-firm subject the ESMA 23-June wind-down rule bites on; the public leading edge of the exit is marketing cessation (ESMA's first enumerated obligation). Verified via Reuters + Binance's own X statement (2026-06-16) + Bitcoin Magazine corroboration. Logged honestly as *reported/deadline-forced*, not yet a formally confirmed enforcement action (Binance denies receiving notice). Other items reviewed and dated as already-captured or out of scope: ESMA 23-Jun statement (already in corpus); FCA→clubs (already in corpus); the generic "1,000 firms / 80% exit" projections (industry estimates, not primary-source firm actions — not added).

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new: 0 verifiable.** Binance's post-Reuters X statement is a *corporate/comms* statement, not a named senior-marketing-operator (CMO/VP/Head-of-Brand/Growth) quote — so it does NOT qualify for `operator-statements/` per methodology; logged inside the Binance regulator entry as firm response. Kalifowitz (Crypto.com, exit 30-Jun) and Conlan/Chen (Binance, ~15-Jun) remain longitudinal ticks, already captured — not net-new statements.

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0. Enrichment: 1.** No new public 2026 marketing-team contraction with stated rationale surfaced in-window. **Enriched** the existing Crypto.com row: added the primary source URL (CoinDesk 2026-03-19) and the marketing-specific impact detail (press reports concentrate the March cuts in growth + CRM — i.e., marketing-adjacent functions), per the methodology's "marketing-specific impact where reported" field. No new firm added.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md`. Core advance: the watched "first named-firm marketing-cessation instance" is now on the record (Binance). The three June regulatory legs now read: placement/channel (FCA→clubs), entity-permission/solicitation (ESMA 23-Jun), and **named-firm enforcement-exposure (Binance/Greece)** — with the competitive corollary that MiCA-licensed Tier-1s (Coinbase, Kraken) retain a *legal EU marketing surface* their largest rival may lose. Marketing surface = competitive asset under MiCA, not just a compliance line.

---

## Searches run (audit trail)
1. crypto marketing enforcement ESMA MiCA wind down unauthorised CASP June 26 2026 → ESMA 23-Jun (already captured); confirmed "cease marketing & solicitation" first obligation.
2. crypto exchange CMO marketing layoffs June 2026 → Kalifowitz/Conlan (already captured); Crypto.com March cuts in growth/CRM (enrichment).
3. crypto firm cease marketing EU exit MiCA deadline July 2026 named exchange → **surfaced Binance EU pullback / Greece rejection** (named-firm net-new).
4. crypto marketing layoffs 2026 web3 job cuts brand growth team → no net-new marketing-team contraction; OP Labs ~20 roles noted (Optimism, dev-team, not a marketing-specific cut — not added).
- Fetched + verified: Bitcoin Magazine ESMA wind-down (2026-06-23) and Binance-EU-exit (2026-06-16) articles; latter anchors to Reuters 2026-06-16 primary report + Binance X statement.

## Net-new / changed this run
- `corpus/regulator-filings/binance-mica-eu-exit-2026-06.md` (+1 regulator / named-firm Theme-4 entry)
- `corpus/layoff-tracker/2026-layoff-tracker.csv` (Crypto.com row enriched: +source URL, +marketing-specific impact)
- `findings/longitudinal-2026-06.md` (named-firm instance section; competitive/Theme-3 corollary)
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` (sync re-write; idempotent)

## Recommendation for next run (carried forward)
**Re-check the week of 1 July** for: (a) formal HCMC decision on Binance; (b) any Binance EU-market service/marketing restriction notice or visible EU campaign pull-down; (c) NCA coordinated action; (d) any *other* tracked unauthorised CASP forced to pull EU marketing at the deadline. This is the peak window of the cycle for completed named-firm marketing-cessation instances. Upstream feeds (`open-positions.json` scan_date, `trend-data.json` lastUpdated) had not refreshed since 06-26/06-15 respectively — when they do, classes 1+2 will produce rows automatically.

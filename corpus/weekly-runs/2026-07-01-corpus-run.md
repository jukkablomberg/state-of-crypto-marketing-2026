# Corpus-assembly daily run — 2026-07-01 (the MiCA deadline day)

**Run type:** Phase-1 daily corpus assembly (automated, daily cadence per 2026-06-26 framework upgrade).
**Methodology:** public-source synthesis only. Every entry anchored to a primary/public source with a URL. No off-the-record, no anonymised, no guessed URLs. Absence of public signal is recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + the 18-agency comparison panel in `../../tracked-firms.md`.
**Dedup baseline read before searching:** prior runs `2026-06-30`, `2026-06-29`, `2026-06-28`, `2026-06-27`, `2026-06-26`, `2026-06-20`; `regulator-filings/` (FCA club-sponsorship; ESMA 23-Jun wind-down; AMF national amplification; Binance MiCA EU-exit); `operator-statements/sport-sponsorship-reset-2026-05.md`; `marketing-campaigns/mica-competitive-capture-2026-06.md`; `layoff-tracker/2026-layoff-tracker.csv` (8 rows pre-run); `agency-overlap-matrix.csv` (8 rows, 1 overlap); `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

---

## Headline result

**The deadline arrived and the corpus's lead example completed.** The MiCA transitional period ended **today (1 July 2026)** — the event the entire June corpus was assembled toward. The one half of the Theme-3 symmetry that was still *anticipated/conceded* on 06-30 — the actual EU marketing/onboarding cessation going live — has now **executed and been observed.** Net totals: **0 job-posting rows, 0 agency-matrix rows, 0 net-new regulator *entries* (1 substantive in-place update), 0 operator statements, 0 layoffs, 0 new corpus files.** This is a **graduation run**: no new item, but the corpus's lead Theme-4 example (Binance EU-exit) moves from *exposure-surface inference* to a *named, dated, completed cessation instance* — the single most important qualitative advance available on this date.

Substantive advance this run:

1. **Binance EU cessation EXECUTED (Theme-4, in-place update).** On 1 July, Binance suspended for EU/EEA residents **new sign-ups, new deposits, new orders, and staking/savings products**, leaving only account consultation and withdrawal/transfer of existing holdings during the orderly exit. This closes 06-29/06-30 watch item **(b)** ("the actual EU-resident onboarding/marketing pull-down going live on/after 1 July"). Per the ESMA 23-June statement's enumerated ordering, the leading edge of this wind-down is marketing-and-solicitation cessation → the report's lead Theme-4 example is now a *completed* instance. Re-file jurisdiction (watch item (a)) partially resolves: Greek application withdrawn; France reported (not yet formally confirmed) as re-file target. → updated in place in `../regulator-filings/binance-mica-eu-exit-2026-06.md` (2026-07-01 block).
2. **Root-cause on the public record (Theme-1 context).** The authorisation blocker was the CASP owner/manager **fit-and-proper** test (CZ ~90% ownership + 2023 US guilty plea), not a marketing deficiency — yet the first publicly visible consequence still lands on marketing. Logged as context, not a new class-3 enforcement action.

Deterministic feed sync produced its standard classes-1+2 output (no upstream feed change → 0 new rows, expected and correct; date-stamp refresh only).

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0 (expected, idempotent).** Source A (`open-positions.json`) **scan_date advanced to 2026-07-01**, underlying postings unchanged by source URL → dedup-by-URL producer added **0 rows**. Job-postings corpus holds at prior totals (Ava Labs ×2, Optimism ×1 from API; Solana ×3 from Chrome lane). Chrome work-queue (proprietary tracked firms) unchanged: Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys, Solana. Absence (no API coverage): **Aave, Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys** — re-written to `job-postings/_absence.csv` with `as_of=2026-07-01` (idempotent date-stamp refresh; `_chrome-queue.csv` likewise). **Absence-as-data note (carried):** Binance and Bybit remain the least publicly legible via standard ATS scanning on the very day their EU marketing surface goes dark — the legible signal on them today is regulatory + competitive, not hiring.

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0 (expected).** Source B (`trend-data.json`) lastUpdated **2026-06-15** — unchanged for a 17th day. Matrix holds at 8 tracked firms, 1 OVERLAP (**Sui — Coinbound + RZLT**). 18 dated per-agency snapshots re-written (idempotent). The panel's 17-day staleness is now a standing flag for the July synthesis pass (agency-side signal is not refreshing while the regulatory/competitive side moves fast).

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new entries: 0. Substantive in-place update: 1.** No *new* named marketing-side enforcement action surfaced in-window. The pre-existing Binance regulator entry received a dated **2026-07-01** update block confirming the completed EU-resident cessation and the (reported) Greek-withdrawal / re-file posture. Consistent with prior-run honesty discipline: the deadline-day *completed-cessation* fact is logged on multi-source corroboration + Binance's own prior primary-sourced admission; a primary AMF/Binance-blog URL for the July-1 France cessation, and the still-pending primary verification of the ESMA non-compliant-CASP register + 244-licence/Germany-57 counts, remain held (Chrome-lane / July-synthesis capture items). No guessed URLs.

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new: 0 verifiable.** No verbatim quote by a named senior *marketing* operator (CMO/VP Marketing/Head of Brand/Head of Growth) at a tracked firm surfaced in-window. The deadline-day quotes are corporate/regional-leadership (Binance head-of-Europe framing; regional-GM "record sign-ups" colour) — excluded under the class-4 definition, consistent with the 06-27→06-30 rulings on the same speaker classes. Binance's CMO seat itself remains interim (Eowyn Chen after Conlan's ~06-15 exit) — a standing Theme-1 read, not a new statement.

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0.** No new public 2026 marketing-team contraction with stated rationale at a tracked Stratum-1–4 firm. Deadline-day layoff coverage (Crypto.com March 12%, Coinbase, BitGo 06-26, Robinhood 06-16, Messari) is either already captured, perimeter (non-tracked), or not marketing-team-specific. Tracker holds at 8 rows.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-01 section; last-updated bumped to 2026-07-01). Core advance: the Theme-3 symmetry's **cessation half is now completed, not anticipated** — the report can state "marketing going dark is the leading public indicator of CASP authorisation failure" as a named/dated/completed fact. Plus the fit-and-proper root-cause read that sharpens (rather than contradicts) the visibility-as-analysis premise.

---

## Searches run (audit trail)
1. `ESMA MiCA marketing communications enforcement action crypto June 2026` → reconfirmed ESMA 23-June wind-down statement + reverse-solicitation marketing carve-out — **already captured verbatim** in `esma-mica-transitional-period-end-2026-06.md`. No net-new.
2. `crypto marketing layoffs 2026 CMO growth team cut exchange` → Conlan (Binance, ~06-15) + Kalifowitz (Crypto.com, end-June) — **already captured** longitudinal ticks. No net-new tracked-firm marketing-team cut.
3. `crypto exchange CMO "head of marketing" MiCA marketing compliance statement June 2026` → no qualifying named senior-marketing-operator statement; OKX Europe GM (regional, non-marketing) excluded again.
4. `crypto exchange stops EU marketing MiCA July 1 2026 unauthorised wind down` → confirmed Binance EU wind-down executing on the deadline (France unit ending services 1 July) — the completed-cessation confirmation feeding the in-place update.
5. `crypto layoffs July 2026 marketing brand team job cuts` → no net-new tracked-firm marketing-team cut; BitGo (06-26)/Coinbase/Crypto.com all prior-captured or perimeter.
6. `Binance France ends crypto services July 1 2026 MiCA AMF re-file jurisdiction` → confirmed 1-July EU-resident suspension of sign-ups/deposits/orders/staking (consultation + withdrawal only); Greek application withdrawn; France reported as possible re-file jurisdiction; fit-and-proper (CZ) root cause.

## Net-new / changed this run
- `corpus/regulator-filings/binance-mica-eu-exit-2026-06.md` (**updated** — 2026-07-01 block: completed EU cessation, watch item (b) closed, re-file posture, fit-and-proper root cause)
- `findings/longitudinal-2026-06.md` (2026-07-01 section + last-updated bump to 2026-07-01)
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` (sync re-write; idempotent `as_of` date-stamp refresh only)
- `corpus/weekly-runs/2026-07-01-corpus-run.md` (this record)

## Recommendation for next run
Re-check for: (a) Binance's **named, formal** re-file jurisdiction (France reported, unconfirmed) and any interim EU-marketing restriction detail; (b) a **primary firm-page / AMF citation** for the completed July-1 France cessation (Chrome-lane capture) to harden the appendix; (c) **primary-source verification of the ESMA non-compliant-CASP register + 244-licence / Germany-57 counts** against the ESMA Interim MiCA Register (both still held); (d) whether the OKX/Coinbase/Kraken capture campaigns **escalate** now that the displaced-user pool is live, or new licensed entrants (Bitvavo, Ripple/CSSF) join the EEA bonus war; (e) any *other* tracked unauthorised CASP forced to complete an EU marketing pull-down at/after the deadline; (f) first post-deadline NCA coordinated action (BaFin/CONSOB/AFM/CySEC). Upstream feeds standing-stale: `trend-data.json` lastUpdated 2026-06-15 (17 days) — agency panel needs a refresh before the July synthesis pass; classes 1+2 will produce rows automatically once the underlying feeds refresh their content.

# Corpus-assembly daily run — 2026-07-03 (day 2 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Dedup baseline read before searching:** prior runs 2026-07-02 back to 2026-06-20; `regulator-filings/` (all 4 files); `marketing-campaigns/mica-competitive-capture-2026-06.md`; `operator-statements/`; `layoff-tracker/2026-layoff-tracker.csv` (8 rows); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

---

## Headline result

**Net totals: 0 job-posting rows, 0 agency-matrix rows, 0 net-new class-3 enforcement entries, 0 qualifying operator statements, 0 layoffs — but THREE substantive verification/expansion wins that close three carried watch items:**

1. **Watch item (c) CLOSED — the 210-vs-244 licence-count conflict resolves.** ESMA Interim MiCA Register (via Micahub's weekly CSV mirror, data as of 2026-06-27): **243 authorised CASPs** (Germany 56, France 26, Netherlands 26), 20 EMT issuers, 0 ART issuers, **157 non-compliant entities flagged by NCAs**. The ~210 Finance Magnates figure is ruled stale; the 06-29 held "35+ non-compliant CASPs" item also closes (actual register figure: 157). Mirror-not-primary caveat logged; direct ESMA CSV pull scheduled for synthesis time. → `marketing-campaigns/mica-competitive-capture-2026-06.md` (07-03 block).
2. **Watch item (e) CLOSED — capture escalation confirmed with two new firm-anchored campaigns.** **Bitpanda** (tracked Tier-1: €25 BTC welcome + 3% transfer cashback, until 07-05, first 500 users, 15 named EU markets; firm-issued PR 06-26) and **Bitvavo** (non-tracked capture-context: up to 10% APY on net-new deposits, 25 Jun–30 Sep, €10k cap; first-party help-center page fetched in full). The capture panel is now five firms, all licence-led. Bitvavo's promo page self-converts APY headline to actual yield and discloses non-MiCA-regulated staking/lending — the strongest compliance-dressed-promotion instance yet. → same file.
3. **Binance watch item (a) context hardened — the firm's own post-exit account captured (primary fetched).** Gillian Lynch CoinDesk interview, published 2026-07-03: "Is the success of MiCA that we have regulation, or is the success that the players are regulated?"; Greek application "deemed complete"; WSJ-reported ESMA private advice to disapprove (disputed by the firm, logged as reported); ">$300M/year" compliance spend; "we will be back in the market"; re-file jurisdiction still unnamed → (a) stays open. **Class-4 ruling: Lynch EXCLUDED** (regional business head, not CMO/VP Mktg/Head of Brand/Growth — consistent with Ghoos/Mulvenny precedents); logged in `regulator-filings/binance-mica-eu-exit-2026-06.md` (07-03 block).

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0.** Source A scan_date **2026-07-03**; no new URL-verified rows (Phantom 07-02 row stands as the latest). Chrome work-queue unchanged (Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys, Solana). Absence re-stamped `as_of=2026-07-03`: Aave, Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys — absence-as-data note stands.

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0.** Source B `trend-data.json` lastUpdated **2026-06-15** — **19th day unchanged.** Staleness now certain to overlap the July synthesis start → escalated to Jukka via situation.md (upstream NorthPoint feed needs a refresh; not fixable from this loop). Matrix holds 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots idempotent.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new named enforcement entries: 0.** Day-2/3 post-deadline: still **no named NCA marketing-side action** — searched coordinated-action and NCA-warning terms; results were pre-deadline material (ESMA 23-Jun, AMF reminders — captured) and secondary guides. **Absence-as-data: the silence itself continues.** The quantified register datum (157 NCA-flagged non-compliant entities) is logged under the campaigns file as the one public enforcement instrument currently in motion (register-listing-as-sanction).

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new qualifying: 0.** Lynch (Binance Head of Europe & UK, CoinDesk 07-03) — substantive, verbatim, primary-fetched, but **non-qualifying** (not a marketing operator) → logged in the Binance regulator file, not `operator-statements/`. No CMO/VP-Marketing/Head-of-Brand/Growth verbatim statement at a tracked firm surfaced in-window.

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0.** July-window searches re-surfaced only captured items (Crypto.com −12%, Coinbase −700, BitGo, Robinhood). Tracker holds at 8 rows.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-03 section; last-updated bumped): five-firm capture panel + compliance-dressing escalation, register-count resolution (243/157), Binance counter-narrative, day-2 regulator silence, agency-panel 19-day staleness escalation.

---

## Searches/fetches run (audit trail)
1. `MiCA marketing enforcement action July 2026 BaFin AMF CONSOB AFM CySEC warning unauthorised crypto` → pre-deadline material only; no named post-deadline case.
2. `crypto exchange CMO "head of marketing" statement interview July 2026 MiCA` → Lynch/CoinDesk 07-03 (actioned, class-4 excluded); Conlan/Kalifowitz departures already captured.
3. `crypto company marketing team layoffs July 2026` → all previously captured; 0 net-new.
4. `ESMA interim MiCA register CASP count July 2026` → Micahub register mirror (actioned).
5. `"first enforcement" OR "blacklist" OR "wind-down" … July 2 2026 MiCA transitional period ended` → no named case; absence logged.
6. `Bitvavo OR Bitpanda OR Coinbase OR Kraken campaign Binance users switch bonus July 2026 EU` → Bitpanda PR + Bitvavo promo surfaced (actioned).
7. Fetch (full): CoinDesk Lynch interview; Micahub register mirror; Bitpanda PR (cryptonews advertorial, firm-issued, 06-26); Bitvavo help-center promo page (first-party, updated 06-26).

## Net-new / changed this run
- `corpus/marketing-campaigns/mica-competitive-capture-2026-06.md` (**updated** — 07-03 block: Bitpanda + Bitvavo capture entries, register-count resolution 243/157, mirror caveat)
- `corpus/regulator-filings/binance-mica-eu-exit-2026-06.md` (**updated** — 07-03 block: Lynch interview verbatim, WSJ ESMA-advice allegation as reported/disputed, class-4 exclusion)
- `findings/longitudinal-2026-06.md` (2026-07-03 section + last-updated bump)
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` (idempotent `as_of` re-stamp)
- `corpus/weekly-runs/2026-07-03-corpus-run.md` (this record)

## Recommendation for next run
(a) Binance named re-file jurisdiction (still open; France reported-only); (b) **first named post-deadline NCA action** — day-2 silence logged; the 157-entity non-compliant register is the leading indicator to watch for named additions; (c) direct **ESMA CSV pull** at synthesis time to double-anchor the 243/157 counts (mirror caveat); (d) OKX + Coinbase primary firm-page/T&C capture (still geofenced — Chrome lane); (e) whether Bitpanda extends past its 07-05/500-user cap (campaign-performance signal) and any further capture entrants; (f) **agency panel now 19 days stale — ESCALATED to Jukka** (upstream `trend-data.json` feed needs refresh before July synthesis); (g) any qualifying class-4 statement as post-deadline conference/podcast content lands.

# Corpus-assembly daily run — 2026-07-02 (day 1 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated, daily cadence per 2026-06-26 framework upgrade).
**Methodology:** public-source synthesis only. Every entry anchored to a primary/public source with a URL. No off-the-record, no anonymised, no guessed URLs. Absence of public signal is recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + the 18-agency comparison panel in `../../tracked-firms.md`.
**Dedup baseline read before searching:** prior runs `2026-07-01` back to `2026-06-20`; `regulator-filings/` (ESMA wind-down; AMF amplification; FCA club-sponsorship; Binance MiCA EU-exit incl. 07-01 completed-cessation block); `operator-statements/sport-sponsorship-reset-2026-05.md`; `marketing-campaigns/mica-competitive-capture-2026-06.md`; `layoff-tracker/2026-layoff-tracker.csv` (8 rows pre-run, Coinbase −700 + Robinhood + BitGo already captured); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

---

## Headline result

**Net totals: +1 job-posting row (Phantom), 0 agency-matrix rows, 0 net-new regulator entries, 0 operator statements, 0 layoffs — plus one verification-status UPGRADE: the Kraken capture campaign's PRIMARY firm-page URL captured and fetched in full**, closing (for Kraken) the Chrome-lane primary-URL gap flagged 06-30 and correcting a press-reported campaign date against the firm's own page.

1. **Class 1 first net-new row in weeks:** **Phantom — Head of Brand Creative** (Remote-US, Ashby, posted 2026-07-01, URL-verified) via the deterministic sync. Theme-1 read in `../../findings/longitudinal-2026-06.md` (07-02 section): wallet-stratum senior brand hiring while exchange CMO seats churn.
2. **Theme-3 hardening:** Kraken's first-party campaign page (published 2026-06-19) captured verbatim → firm-stated window **19 June–31 July** (press said 22 June — primary source wins), enrolment precondition, EEA-only eligibility, T&Cs URL, and the observation that the capture promotion is itself **compliance-dressed** (risk banner + entity-level CBI/CySEC disclosures). Appended as 07-02 block to `../marketing-campaigns/mica-competitive-capture-2026-06.md`.
3. **Licence-count discrepancy logged:** Finance Magnates ~210 (~7% of 3,000+) vs Crypto Briefing 244 (06-29) — primary ESMA Interim Register verification now load-bearing; neither count enters synthesis unverified.
4. **Day-1 post-deadline regulator silence = data:** no named NCA marketing-side action within 24h of the transitional period ending. Watch item rolls forward.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 1.** Source A scan_date **2026-07-02**; sync added **Phantom / "Head of Brand Creative" / Remote-US / Head Of / https://jobs.ashbyhq.com/phantom/815cacde-243b-4e59-87b1-d8536374a125 / posted 2026-07-01** → `job-postings/phantom.csv` (new firm file). Chrome work-queue unchanged (Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys, Solana). Absence (no API coverage, re-stamped `as_of=2026-07-02`): Aave, Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys — carried absence-as-data note stands (Binance/Bybit least ATS-legible on the days their EU marketing surface is dark).

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0.** Source B `trend-data.json` lastUpdated **2026-06-15** — **18th day unchanged**; the agency-panel staleness flag for the July synthesis pass hardens. Matrix holds 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots re-written (idempotent).

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new entries: 0.** No named marketing-side enforcement action surfaced in the first 24h post-deadline — searched ESMA/NCA coordinated-action and BaFin/CONSOB/AFM/CySEC warning terms; results were pre-deadline reminders (AMF 30-Mar clock, ESMA 23-Jun statement — both already captured) and secondary guides. A press reference to an AMF "targeted enforcement sweep" (InnReg guide) carries no named case or primary URL → NOT added (no-guessing rule). **Absence-as-data:** the coordinated-action framework exists on paper; no named public case yet.

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new: 0 verifiable.** One named-speaker quote found *inside* Kraken's campaign page — **Andrew Mulvenny, Head of Crypto-Asset Service Provider Trading Platform** — ruled **non-qualifying** (platform/business lead, not CMO/VP Marketing/Head of Brand/Growth), consistent with the 06-29/06-30 Ghoos rulings; logged as first-party campaign copy instead. Kraken's actual CGMO (Mayur Gupta) surfaced only as a LinkedIn profile, no in-window verbatim statement. Binance CMO seat remains interim (Eowyn Chen).

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0.** No new public 2026 marketing-team contraction with stated rationale at a tracked firm. July-window coverage re-surfaced only already-captured items (Crypto.com −12% growth/CRM-concentrated, Coinbase −700 incl. marketing, BitGo, Robinhood — all in the tracker or ruled perimeter). Tracker holds at 8 rows.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-02 section; last-updated bumped): Phantom brand-seat signal, Kraken primary-source hardening + compliance-dressed-promotion observation, 210-vs-244 count conflict, day-1 regulator silence.

---

## Searches run (audit trail)
1. `MiCA crypto marketing enforcement July 2026 ESMA BaFin AMF CONSOB unauthorised CASP` → ESMA wind-down expectations + AMF reminders — all already captured; no named post-deadline action.
2. `crypto exchange CMO "head of marketing" statement MiCA July 2026` → Conlan/Kalifowitz departures (already captured); no qualifying class-4 quote.
3. `Binance France ends services July 1 2026 re-file MiCA jurisdiction` → France re-file intent still *reported* (Reuters-derived coverage 06-25/26, pre-captured); no formal filing confirmation → watch item (a) stays open.
4. `crypto marketing team layoffs July 2026` → Crypto.com/Coinbase/BitGo re-surfaced; all previously captured; 0 net-new.
5. `MiCA deadline aftermath Kraken Coinbase OKX bonus campaign displaced Binance users` → surfaced **blog.kraken.com/news/industry-news/europe-mica-switch** (primary) + Finance Magnates ~210-licence count → both actioned above.
6. `BaFin OR CONSOB OR AFM OR CySEC warning unauthorised crypto provider after MiCA transitional period ended` → no named post-deadline NCA action; absence logged.
7. Fetch: Kraken campaign page (full text) → verbatim mechanics, dates, Mulvenny quote, compliance dressing.

## Net-new / changed this run
- `corpus/job-postings/phantom.csv` (**NEW** — 1 row, deterministic)
- `corpus/marketing-campaigns/mica-competitive-capture-2026-06.md` (**updated** — 2026-07-02 primary-source block: Kraken firm-page URL, window correction, Mulvenny ruling, compliance-dressed observation, 210-vs-244 discrepancy)
- `findings/longitudinal-2026-06.md` (2026-07-02 section + last-updated bump)
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` (idempotent `as_of` re-stamp)
- `corpus/agency-claims/*.csv` (idempotent re-write)
- `corpus/weekly-runs/2026-07-02-corpus-run.md` (this record)

## Recommendation for next run
(a) Binance **formal** France filing confirmation (still reported-only); (b) **first named post-deadline NCA action** — day-1 silence logged, expect movement within weeks (ESMA framework + AMF blacklist powers); (c) **primary ESMA Interim Register pull** to settle 210-vs-244 (now load-bearing); (d) OKX + Coinbase **primary firm-page/T&C capture** (geofenced — Chrome lane); (e) capture-campaign escalation/new entrants (Bitvavo, Ripple/CSSF) with the displaced pool now live; (f) **agency panel 18 days stale** — `trend-data.json` needs a refresh before July synthesis (upstream NorthPoint feed, flag to Jukka); (g) any other tracked unauthorised CASP's completed EU pull-down.

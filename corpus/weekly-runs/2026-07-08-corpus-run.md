# Corpus-assembly daily run — 2026-07-08 (day 7 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Dedup baseline read before searching:** prior runs 2026-07-07 back to 2026-06-30; `regulator-filings/` (incl. the Binance EU-exit event-chain file); `marketing-campaigns/mica-competitive-capture-2026-06.md` (through the 07-07 six-firm panel); `operator-statements/`; `layoff-tracker/2026-layoff-tracker.csv` (8 rows); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

---

## Headline result

**🔴 CLASS-1 FEED DEGRADED — the deterministic job-postings input was produced during an upstream ATS-scanner network outage, so today's class-1 output is NON-DELIVERING and the honest 07-07 absence snapshot was preserved rather than overwritten. All web-search classes (3 regulator, 4 operator, 5 layoffs) net-zero; day-7 post-deadline named-enforcement silence holds.**

The single material event this run is an **integrity catch on the class-1 pipeline**, not a corpus accretion:

1. **`open-positions.json` (scan 2026-07-08 04:49 UTC) came back with `total_jobs_fetched: 0` and 87 of 87 API firms in `fetch_errors`** — every Greenhouse/Ashby/Lever/Workable/Recruitee/Breezy/Personio/Teamtailor endpoint returned the same DNS-failure signature (`network error … nodename nor servname provided, or not known`). This is a **blanket upstream network outage in NorthPoint's ATS scanner**, not a real hiring signal. `companies_via_api: 87`, `total_jobs_fetched: 0`, `new_count: 0` — the scan authenticated and ran (1626s) but reached no host.
2. **Consequence for the corpus:** if `daily-corpus-sync.py`'s output had been committed as-is, `_absence.csv` would have recorded **17 tracked firms** (Coinbase, Kraken, Bitpanda, Gemini, Ledger, Phantom, Sui, Polygon, Optimism, Ava Labs, Aptos, Arbitrum, Crypto.com, Bitstamp, Trust Wallet, Tether, Aave) as `api-fetch-error` — firms that were **API-covered in prior runs**. That would be a **false mass-absence longitudinal signal** (reads like exchanges pulling their job boards, when the truth is an infra outage). Per the methodology's honesty rule ("absence = data" must reflect real coverage gaps), the contaminated `_absence.csv` was **reverted to the 07-07 committed snapshot** (Aave Lever-404 + the 5 proprietary needs-chrome firms). The 07-07 absence file stands as the last honest class-1 snapshot.
3. **`_chrome-queue.csv`** was allowed to keep its `as_of` re-stamp to 2026-07-08 — the proprietary-ATS firm list (Binance, Bybit, HTX, Kucoin, MetaMask/ConsenSys, Solana) is a stable, outage-independent fallback list, so the date bump is honest and idempotent.
4. **0 job-posting rows added** — but this is **NOT** the usual "no new marketing roles" idempotency; it is "the upstream scanner reached no ATS today." The distinction is recorded so the zero is not misread longitudinally.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0 — but DEGRADED, not idempotent.** Source A `scan_date` 2026-07-08 (04:49 UTC), `total_jobs_fetched: 0`, **87/87 API firms in `fetch_errors` (blanket DNS/network outage upstream)**. `daily-corpus-sync.py` ran and produced 0 rows (nothing to add). Its regenerated `_absence.csv` was contaminated (17 tracked firms falsely flagged `api-fetch-error`) and was **reverted to the honest 07-07 snapshot**; `_chrome-queue.csv` kept the `as_of=2026-07-08` re-stamp (proprietary list unchanged). Phantom Head of Brand Creative (07-02) remains the latest genuine class-1 row. **Recommendation escalated to Jukka:** the ATS scanner had a total network failure at its 04:49 UTC run — confirm the scanner host's outbound network / DNS before relying on tomorrow's `open-positions.json` for absence data.

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0.** Source B `trend-data.json` `lastUpdated` **2026-06-15 — 23rd consecutive day unchanged.** Escalation to Jukka stands and hardens: the agency panel is now three-plus weeks stale and certain to overlap the Phase-2 synthesis start; upstream NorthPoint `trend-data.json` needs a refresh (not fixable from this loop). Matrix idempotent: 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots idempotent.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new named enforcement entries: 0.** Day-7 post-deadline sweep returned only pre-deadline instruments (AMF reminders, ESMA wind-down statement) and secondary CASP-list/guide trackers. AMF's earlier-2026 sweep against unlicensed operators surfaced as context but is not a net-new named marketing-side case. **Absence-as-data: the post-deadline named-enforcement silence is now seven days long** — register-first, cases-later. The ESMA non-compliant register (157 NCA-flagged entities) remains the only public enforcement instrument in motion.

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new qualifying: 0.** CMO / Head-of-Marketing sweep (Coinbase/Kraken/OKX/Bitpanda/Bybit) surfaced only previously-captured or non-qualifying material: Mayur Gupta (Kraken CGO/CMO) recurs as a Forbes CMO Summit 2026 speaker-profile with **no in-window verbatim statement**; Kalifowitz/Crypto.com departure (eff. 06-30) already captured. The class-4 drought since the May CMO churn persists and is itself a Theme-1 datum (the seats that would give post-MiCA statements sit interim/empty at Binance and Crypto.com).

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0.** July-window searches re-surfaced only captured items (Coinbase −700/−14% May 5; Crypto.com −12%; Gemini; BitGo; and the March cluster — Algorand, OP Labs, PIP Labs, Messari) via aggregator round-ups (coingabbar "5,700 layoffs 2026", CryptoRank feed) — no net-new marketing-team headcount cut at a tracked firm. Tracker holds at 8 rows.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-08 section; last-updated bumped): no corpus-content shift this run; the logged shift is a **methodology/integrity observation** — the class-1 deterministic pipeline is only as trustworthy as the upstream feed's network health, and a silent blanket-outage day would inject a false mass-absence signal if committed uncritically. The guard held.

---

## Watch items (carried, unchanged)
- **(a) Binance re-file jurisdiction** — still France-**reported**-only (Reuters/Euronews); firm names no jurisdiction formally; Teng "expects a licence in the coming months." Unchanged; already captured in `regulator-filings/binance-mica-eu-exit-2026-06.md`.
- **(b) First named post-deadline NCA marketing-side action** — day-7 silence logged; ESMA non-compliant register remains the leading indicator.
- **(c) Capture panel — no 7th entrant this run.** OKX 8% / Coinbase 5% (before 07-13) / Kraken €1M / Bitpanda (lapsed 07-05) / Bitvavo / Gate confirmed unchanged; Ripple holds a full MiCA licence but still shows **no consumer capture campaign** (licence-only). Gate/OKX/Coinbase primary-page T&C capture still pending the Chrome/EU-IP lane.

## Searches / fetches run (audit trail)
1. `MiCA crypto marketing enforcement action July 2026 BaFin AMF CONSOB CySEC AFM ESMA named CASP unauthorised warning misleading promotion` → licensing/guide material + AMF unlicensed-operator sweep context; no net-new named marketing-side case (day-7 silence).
2. `crypto exchange marketing team layoffs July 2026 Coinbase Kraken Bitpanda Gemini Crypto.com restructuring headcount cuts` → captured items + aggregator round-ups only; 0 net-new tracked-firm marketing layoff.
3. `crypto exchange CMO "head of marketing" interview podcast conference July 2026 Coinbase Kraken OKX Bitpanda Bybit statement` → Mayur Gupta speaker-profile + Kalifowitz departure (both previously captured); 0 qualifying class-4.
4. `Binance MiCA licence application France jurisdiction July 2026 CASP reapply EU re-entry Teng` → Greece withdrawal (06-24) + France-reported re-file, all previously captured; watch item (a) unchanged.
5. `crypto exchange EU deposit bonus capture campaign July 2026 Binance displaced users OKX Coinbase Kraken Bybit migrate promotion` → OKX 8% / Coinbase 5% / Kraken €1M panel re-confirmed; no 7th entrant.

## Net-new / changed this run
- `corpus/job-postings/_chrome-queue.csv` (idempotent `as_of=2026-07-08` re-stamp — proprietary firm list unchanged; the only deterministic file delta committed)
- `corpus/job-postings/_absence.csv` (**held at the honest 07-07 snapshot** — contaminated outage-driven regeneration reverted; net delta = none)
- `findings/longitudinal-2026-06.md` (2026-07-08 integrity section + last-updated bump)
- `corpus/weekly-runs/2026-07-08-corpus-run.md` (this record)

## Recommendation for next run
(a) **Confirm the ATS-scanner host's network/DNS is restored** before trusting tomorrow's `open-positions.json` absence data — today's blanket outage would have injected a false 17-firm mass-absence signal; if the outage repeats, keep holding the last honest `_absence.csv`. (b) First named post-deadline NCA marketing-side action — day-7 silence logged. (c) Gate/OKX/Coinbase primary-page T&C capture via the Chrome/EU-IP lane. (d) Any 7th capture entrant (Ripple still licence-only). (e) Qualifying class-4 statements as post-deadline conference/podcast content lands. (f) **Agency panel 23 days stale — escalation to Jukka carried/hardened** (upstream `trend-data.json` refresh needed before July synthesis).

# Corpus-assembly daily run — 2026-07-09 (day 8 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Dedup baseline read before searching:** prior runs 2026-07-08 back to 2026-06-30; `regulator-filings/` (all 4 files, incl. the Binance EU-exit event-chain file); `marketing-campaigns/mica-competitive-capture-2026-06.md` (through the 07-07 six-firm panel); `operator-statements/`; `layoff-tracker/2026-layoff-tracker.csv` (8 marketing-scope + adjacency rows); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

---

## Headline result

**All six classes net-zero net-new — but class-1 is HEALTHY-idempotent this run, not degraded. The 07-08 upstream ATS-scanner outage did NOT recur: today's `open-positions.json` fetched 2,469 jobs across 87 API firms (only 6 fetch-errors, none a core tracked exchange), so the 0-new-rows result is a true "no new marketing roles at tracked firms" idempotency, not an infra artifact. Day-8 post-deadline named-enforcement silence holds; classes 4/5 net-zero; capture panel unchanged at six firms.**

The material read this run is the **recovery of class-1 integrity** after yesterday's blanket outage, plus the continuation of the post-deadline patterns:

1. **Class-1 feed recovered.** `open-positions.json` (scan 2026-07-09 04:22 UTC) returned `total_jobs_fetched: 2469`, `companies_via_api: 87`, `new_since_last_scan: 0`, with only **6 fetch-errors** — Wormhole Foundation, Aave, Injective Labs, Bitwise, Chainlink Labs, Elliptic. Of these only **Aave** is a Stratum-2 tracked firm, and its error is the long-standing Lever-`aave` HTTP-404 (a stable structural gap already logged as absence, not a new outage). The scanner reached its hosts normally — yesterday's DNS-failure signature is gone. So today's **0 job-posting rows is genuine idempotency** ("no net-new marketing role at a tracked firm"), correctly distinguished from the 07-08 "scanner reached no host" zero.
2. **Day-8 named-enforcement silence holds (class 3 absence-as-data).** Eight days past the transitional-period end, still **no named marketing-side NCA enforcement case** (BaFin/AMF/CONSOB/AFM/CySEC/ESMA) on the public record. Today's sweep re-surfaced only the AMF unlicensed-operator blacklist (16 recent additions / 38 names YTD in 2026) — an **unauthorised-entity warning list, not a marketing-side misleading-promotion action against a tracked-cohort firm** — plus the ESMA non-compliant register (35+/157 NCA-flagged entities). The register-first, cases-later read now extends to an eight-day pattern.
3. **Capture panel unchanged at six firms — no 7th entrant.** The displaced-Binance deposit-bonus sweep re-confirmed only the panel already captured (OKX 8% / Coinbase 5% [before 07-13] / Kraken €1.1M / Bitpanda €25+3% [lapsed 07-05] / Bitvavo up-to-10%-APY / Gate up-to-10%-deposit); today's roundups (cryptoticker "5 exchanges paying you to switch", coingape/cryptonews bonus lists) aggregate the same firms. Ripple still licence-only (no consumer capture campaign).

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0 (HEALTHY-idempotent).** Source A `scan_date` **2026-07-09** (04:22 UTC), `total_jobs_fetched: 2469`, `companies_via_api: 87`, `new_since_last_scan: 0`, 6 fetch-errors (only Aave tracked = stable Lever-404). `daily-corpus-sync.py` ran clean and added 0 rows — a true no-new-roles idempotency (contrast 07-08's outage-zero). Phantom Head of Brand Creative (07-02) remains the latest genuine class-1 row. `_absence.csv` regenerated honestly to **Aave (Lever-404) + 5 proprietary needs-chrome firms (Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys)** with `as_of=2026-07-09` — matches the last honest snapshot's shape (the 07-08 outage contamination did not carry forward). `_chrome-queue.csv` idempotent `as_of=2026-07-09` re-stamp (proprietary list unchanged; Solana still `ingested`). Deterministic file deltas: `_absence.csv`, `_chrome-queue.csv` (date re-stamps only).

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0.** Source B `trend-data.json` `lastUpdated` **2026-06-15 — 24th consecutive day unchanged.** Escalation to Jukka stands and hardens further: the agency panel is now 3.5 weeks stale and certain to overlap the Phase-2 synthesis start; upstream NorthPoint `trend-data.json` needs a refresh (not fixable from this loop). Matrix idempotent: 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots idempotent.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new named enforcement entries: 0.** Day-8 post-deadline sweep (named enforcement, blacklist, misleading-promotion queries) returned only: the **AMF blacklist** (16 recent site additions; 38 names added YTD 2026) — an unauthorised-entity warning register, **not** a marketing-side misleading-promotion enforcement action against a tracked-cohort CASP, so it does **not** meet the class-3 named-enforcement bar (logged as absence-continuation context, consistent with the 07-08 read); and the ESMA non-compliant register (35+/157 NCA-flagged entities). **Absence-as-data: the post-deadline named-enforcement silence is now eight days long** — register-first, cases-later.

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new qualifying: 0.** CMO / Head-of-Marketing / conference-and-podcast sweep (Coinbase/Kraken/OKX/Bitpanda/Bybit) surfaced only non-qualifying material: conference speaker lineups feature **non-marketing** execs (Coinbase Chief Policy Officer, Kraken CEO), not marketing operators; no in-window verbatim statement by a CMO/VP-Marketing/Head-of-Brand/Head-of-Growth at a tracked firm. The class-4 drought since the May CMO churn persists and remains a Theme-1 datum (the seats that would give post-MiCA marketing statements sit interim/empty at Binance and Crypto.com).

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0.** July-window searches re-surfaced only captured items via aggregator round-ups (Coinbase −700/−14% May 5; Gemini −30% / ~445 headcount; Kraken AI-pivot; Crypto.com −12%; BitGo −15%; Robinhood −10%; the March cluster) — no net-new marketing-team headcount cut at a tracked firm. Tracker holds at 8 marketing-scope + adjacency rows.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-09 section; last-updated bumped): no corpus-content shift this run. The logged observation is the **class-1 recovery** — the deterministic pipeline is back to honest idempotency one day after the blanket outage, confirming the 07-08 guard behaved correctly (it held the outage day out of the corpus without suppressing a healthy day's zero). The methodology note stands: cross-check any future job-postings "absence spike" against `scan_metadata` (`total_jobs_fetched` + `fetch_errors` count) before treating it as data.

---

## Watch items (carried, unchanged)
- **(a) Binance re-file jurisdiction** — still France-**reported**-only; firm names no jurisdiction formally; already captured in `regulator-filings/binance-mica-eu-exit-2026-06.md`. Unchanged.
- **(b) First named post-deadline NCA marketing-side action** — day-8 silence logged; ESMA non-compliant register + AMF blacklist remain the leading (unauthorised-entity) indicators; no named marketing-side case yet.
- **(c) Capture panel** — six firms, no 7th entrant this run; Ripple still licence-only. Gate/OKX/Coinbase primary-page T&C capture still pending the Chrome/EU-IP lane.
- **(d) Agency panel staleness** — `trend-data.json` 24 days stale (06-15); escalation to Jukka hardened.

## Searches / fetches run (audit trail)
1. `MiCA crypto marketing enforcement action July 2026 BaFin AMF CONSOB CySEC AFM ESMA named CASP misleading promotion warning` → licensing/framework material + AMF unlicensed-operator context; 0 net-new named marketing-side case (day-8 silence).
2. `crypto exchange marketing team layoffs July 2026 Coinbase Kraken Bitpanda Gemini restructuring headcount` → captured items + aggregator round-ups only; 0 net-new tracked-firm marketing layoff.
3. `crypto exchange CMO "head of marketing" interview podcast conference July 2026 Coinbase Kraken OKX Bitpanda Bybit` → conference lineups of non-marketing execs only; 0 qualifying class-4.
4. `BaFin AMF CONSOB CySEC crypto CASP unauthorised warning blacklist July 2026 misleading advertising financial promotion` → AMF blacklist (16 new / 38 YTD) + ESMA register; unauthorised-entity warnings, not marketing-side enforcement; 0 net-new class-3.
5. `crypto exchange EU deposit bonus new user promotion July 2026 displaced Binance users APY reward campaign` → six-firm capture panel re-confirmed; no 7th entrant.

## Net-new / changed this run
- `corpus/job-postings/_absence.csv` (honest regeneration, `as_of=2026-07-09` — Aave Lever-404 + 5 proprietary; outage contamination did NOT recur)
- `corpus/job-postings/_chrome-queue.csv` (idempotent `as_of=2026-07-09` re-stamp — proprietary firm list unchanged)
- `findings/longitudinal-2026-06.md` (2026-07-09 class-1-recovery section + last-updated bump)
- `corpus/weekly-runs/2026-07-09-corpus-run.md` (this record)

## Recommendation for next run
(a) **Class-1 feed confirmed healthy again** — resume trusting `open-positions.json` absence data; keep the `scan_metadata` cross-check as a standing guard against a repeat silent-outage day. (b) First named post-deadline NCA marketing-side action — day-8 silence logged; watch for the transition from register/blacklist listing to a named misleading-promotion case. (c) Gate/OKX/Coinbase primary-page T&C capture via the Chrome/EU-IP lane. (d) Any 7th capture entrant (Ripple still licence-only). (e) Qualifying class-4 statements as post-deadline conference/podcast content lands. (f) **Agency panel 24 days stale — escalation to Jukka carried/hardened** (upstream `trend-data.json` refresh needed before July synthesis).

# Corpus-assembly daily run — 2026-07-10 (day 9 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Dedup baseline read before searching:** prior runs 2026-07-09 back to 2026-06-30; `regulator-filings/` (all 4 files, incl. Binance EU-exit event-chain); `marketing-campaigns/mica-competitive-capture-2026-06.md` (through the 07-07 six-firm panel); `operator-statements/`; `layoff-tracker/2026-layoff-tracker.csv` (8 marketing-scope + adjacency rows); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

---

## Headline result

**All six classes net-zero net-new, and class-1 is HEALTHY-idempotent — cleaner than yesterday. Today's `open-positions.json` (scan 2026-07-10) fetched 2,475 jobs across 87 API firms with 0 fetch-errors (yesterday had 6), so the 0-new-rows result is a true "no new marketing roles at tracked firms" idempotency, not an infra artifact. Day-9 post-deadline named-enforcement silence holds; classes 4/5 net-zero; capture panel unchanged at six firms.**

The material read this run is continuity: the post-deadline patterns extend by a ninth day with no structural shift.

1. **Class-1 feed healthy and clean.** `open-positions.json` (scan 2026-07-10, 06:02 file-write) returned `total_jobs_fetched: 2475` (up 6 from yesterday's 2,469), `companies_via_api: 87`, and **0 `fetch_errors`** in `scan_metadata`. The sync's own Aave Lever-`aave` HTTP-404 probe still logs Aave to `_absence.csv` (stable structural gap, not a new outage). The scanner reached its hosts normally; today's **0 job-posting rows is genuine idempotency** ("no net-new marketing role at a tracked firm"). Phantom Head of Brand Creative (07-02) remains the latest genuine class-1 row.
2. **Day-9 named-enforcement silence holds (class 3 absence-as-data).** Nine days past the July-1 transitional-period end, still **no named marketing-side NCA enforcement case** (BaFin/AMF/CONSOB/AFM/CySEC/ESMA) on the public record against a tracked-cohort firm. Today's sweep surfaced only framework/deadline commentary and unauthorised-entity instruments (ESMA "wind down" push; AMF unlicensed-operator posture; a BaFin finfluencer-supervision *notice* / report, not a named case). The register-first, cases-later read now extends to a nine-day pattern.
3. **Capture panel unchanged at six firms — no 7th entrant.** The displaced-Binance deposit-bonus sweep re-confirmed only the panel already captured (OKX 8% / Coinbase 5% [before 07-13] / Kraken €1.1M / Bitpanda €25+3% [lapsed 07-05] / Bitvavo up-to-10%-APY / Gate up-to-10%-deposit). Coinbase + OKX windows still run to 07-13. Roundups (cryptoticker "5 exchanges paying you to switch", coingape/finder/college-investor bonus lists) aggregate the same firms. Ripple still licence-only.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0 (HEALTHY-idempotent).** Source A `scan_date` **2026-07-10**, `total_jobs_fetched: 2475`, `companies_via_api: 87`, **0 fetch-errors** in `scan_metadata`. `daily-corpus-sync.py` ran clean, added 0 rows — a true no-new-roles idempotency. `_absence.csv` regenerated honestly to **Aave (Lever-404) + 5 proprietary needs-chrome firms (Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys)** with `as_of=2026-07-10`. `_chrome-queue.csv` idempotent `as_of=2026-07-10` re-stamp (proprietary list unchanged: Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys pending-chrome; Solana `ingested`). Deterministic file deltas: `_absence.csv`, `_chrome-queue.csv` (date re-stamps only).

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0.** Source B `trend-data.json` `lastUpdated` **2026-06-15 — 25th consecutive day unchanged.** Escalation to Jukka stands and hardens: the agency panel is now 3.5+ weeks stale and certain to overlap the Phase-2 synthesis start; upstream NorthPoint `trend-data.json` needs a refresh (not fixable from this loop). Matrix idempotent: 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots idempotent.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new named enforcement entries: 0.** Day-9 post-deadline sweep (named enforcement, blacklist, misleading-promotion queries) returned only: ESMA's wind-down expectation for unauthorised CASPs; AMF's unlicensed-operator posture; and a **BaFin finfluencer-supervision notice/report** (brokers "on notice" re: finfluencers linked to risky crypto trading) — a supervisory signal, **not** a named marketing-side misleading-promotion enforcement action against a tracked-cohort CASP, so it does **not** meet the class-3 named-enforcement bar (logged as absence-continuation context). Also surfaced: US-side items outside scope (CFTC/Polymarket marketing-issues probe; a US "failed blockchain project" fine) — neither an EU NCA marketing-side action against a tracked firm. **Absence-as-data: the post-deadline named-enforcement silence is now nine days long** — register-first, cases-later.

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new qualifying: 0.** CMO / Head-of-Marketing / conference-and-podcast sweep (Coinbase/Kraken/OKX/Bitpanda) surfaced only non-qualifying material: crypto-marketing podcast catalogue features non-tracked-firm operators (Gate.io CMO Marie Tatibouet — Gate is non-tracked capture-context, and the episode is not in-window; Blocknative CMO John Jefferies; Octant Labs CMO). No in-window verbatim statement by a CMO/VP-Marketing/Head-of-Brand/Head-of-Growth at a tracked firm. The class-4 drought since the May CMO churn persists and remains a Theme-1 datum (interim/empty marketing seats at Binance and Crypto.com).

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0.** July-window searches re-surfaced only captured items via aggregator round-ups (Coinbase −700/−14% May 5; Gemini −30% / ~445 headcount / $582M loss framing; Kraken AI-pivot; Crypto.com −12%; BitGo −15%; Robinhood −10%; "5,700+ crypto layoffs in 2026" round-ups) — no net-new marketing-team headcount cut at a tracked firm. Tracker holds at 8 marketing-scope + adjacency rows.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-10 section; last-updated bumped): no corpus-content shift this run. The logged observation is **clean continuity** — class-1 healthy-idempotent (0 fetch-errors, the cleanest scan since the 07-08 outage), day-9 enforcement silence, six-firm capture panel unchanged. The methodology guard stands: cross-check any future job-postings "absence spike" against `scan_metadata` (`total_jobs_fetched` + `fetch_errors` count) before treating it as data.

---

## Watch items (carried, unchanged)
- **(a) Binance re-file jurisdiction** — still France-**reported**-only; firm names no jurisdiction formally; captured in `regulator-filings/binance-mica-eu-exit-2026-06.md`. Unchanged.
- **(b) First named post-deadline NCA marketing-side action** — day-9 silence logged; ESMA non-compliant register + AMF/BaFin unauthorised-entity + finfluencer-supervision instruments remain the leading indicators; no named marketing-side case yet.
- **(c) Capture panel** — six firms, no 7th entrant this run; Ripple still licence-only. Gate/OKX/Coinbase primary-page T&C capture still pending the Chrome/EU-IP lane; OKX+Coinbase windows lapse 07-13 (next campaign-lifecycle datapoints).
- **(d) Agency panel staleness** — `trend-data.json` 25 days stale (06-15); escalation to Jukka hardened.

## Searches / fetches run (audit trail)
1. `MiCA crypto marketing enforcement action July 2026 BaFin AMF CONSOB CySEC ESMA named CASP misleading promotion` → framework/deadline commentary + unauthorised-entity/finfluencer-supervision material; 0 net-new named marketing-side case (day-9 silence).
2. `crypto exchange marketing team layoffs July 2026 Coinbase Kraken Bitpanda Gemini headcount restructuring` → captured items + aggregator round-ups only; 0 net-new tracked-firm marketing layoff.
3. `crypto exchange CMO "head of marketing" "head of growth" interview podcast conference July 2026 Coinbase Kraken OKX Bitpanda` → non-tracked-firm marketing operators only (Gate.io/Blocknative/Octant); 0 qualifying class-4.
4. `crypto exchange EU deposit bonus promotion July 2026 displaced Binance users switch reward campaign` → six-firm capture panel re-confirmed (OKX/Coinbase/Gate + roundups); no 7th entrant.

## Net-new / changed this run
- `corpus/job-postings/_absence.csv` (honest regeneration, `as_of=2026-07-10` — Aave Lever-404 + 5 proprietary; feed healthy, 0 upstream fetch-errors)
- `corpus/job-postings/_chrome-queue.csv` (idempotent `as_of=2026-07-10` re-stamp — proprietary firm list unchanged)
- `findings/longitudinal-2026-06.md` (2026-07-10 continuity section + last-updated bump)
- `corpus/weekly-runs/2026-07-10-corpus-run.md` (this record)

## Recommendation for next run
(a) **Class-1 feed healthy** — resume trusting `open-positions.json` absence data; keep the `scan_metadata` cross-check as a standing guard. (b) First named post-deadline NCA marketing-side action — day-9 silence logged; watch for the transition from register/blacklist/finfluencer-notice to a named misleading-promotion case. (c) Gate/OKX/Coinbase primary-page T&C capture via the Chrome/EU-IP lane; **07-13 is the next campaign-lifecycle checkpoint** (OKX + Coinbase windows lapse). (d) Any 7th capture entrant (Ripple still licence-only). (e) Qualifying class-4 statements as post-deadline conference/podcast content lands. (f) **Agency panel 25 days stale — escalation to Jukka carried/hardened** (upstream `trend-data.json` refresh needed before July synthesis).

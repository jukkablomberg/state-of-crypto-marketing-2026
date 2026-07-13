# Corpus-assembly daily run — 2026-07-13 (day 12 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Dedup baseline read before searching:** prior runs 2026-07-12 back to 2026-06-30; `regulator-filings/` (incl. Binance EU-exit event-chain, ESMA/AMF/FCA filings); `marketing-campaigns/mica-competitive-capture-2026-06.md` (six-firm capture panel); `operator-statements/`; `layoff-tracker/2026-layoff-tracker.csv` (8 marketing-scope + adjacency rows); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

---

## Headline result

**All six classes net-zero net-new; class-1 HEALTHY-idempotent for a fourth straight day. Today's `open-positions.json` (scan 2026-07-13) reports `scan_date: 2026-07-13` with 0 job-posting rows added and no fetch-error flags surfaced by the sync — genuine "no new marketing roles at tracked firms" idempotency, not an infra artifact. The one material event this run is a campaign-lifecycle datapoint, not a new corpus row: today (07-13) is the confirmed lapse date of Coinbase's 5% displaced-Binance-user transfer bonus — the first clean post-Bitpanda (07-05) completed-lifecycle datapoint, per the corrected 07-12 sequence. Day-12 post-deadline named-enforcement silence holds; classes 4/5 net-zero; capture panel unchanged at six firms with no 7th entrant. The material read remains continuity — the post-deadline patterns extend to a twelfth day with no structural shift; OKX + Kraken windows (07-31) are the next checkpoints.**

1. **Class-1 feed healthy and clean.** `daily-corpus-sync.py` ran clean on `open-positions.json` (`scan_date: 2026-07-13`), added **0 job-posting rows** (`firms: []`), and regenerated `_absence.csv` / `_chrome-queue.csv` as date re-stamps only (content identical to 07-12). `_absence.csv` honest at **Aave (Lever-404) + 5 proprietary needs-chrome firms** (Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys). Chrome work-queue unchanged (proprietary list: Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys pending-chrome; Solana ingested). Phantom Head of Brand Creative (07-02) remains the latest genuine class-1 row. Four consecutive clean scans (07-10/11/12/13) confirm the 07-08 outage was isolated.
2. **Day-12 named-enforcement silence holds (class 3 absence-as-data).** Twelve days past the July-1 transitional-period end, still **no named marketing-side NCA enforcement case** (BaFin/AMF/CONSOB/AFM/CySEC/ESMA) on the public record against a tracked-cohort firm. Today's sweep surfaced only framework/deadline material and unauthorised-entity/wind-down instruments (ESMA orderly-wind-down expectation; AMF unlicensed-operator sweep posture; the recurring KuCoin Austrian-FMA ban is a Feb-2026 out-of-window entity action, not a marketing-side promotion case). None meets the class-3 named-enforcement bar. Register-first, cases-later now extends to a twelve-day pattern.
3. **Coinbase 5% capture campaign reaches its lapse date (Theme-4 lifecycle datapoint).** Today, 07-13, is the confirmed end date of Coinbase's 5%-transfer-bonus campaign aimed at displaced Binance-EU users (Coinbase One–gated; genuine external transfers only; DE/FR/IT/BE/PL/SE/UK). This is the **first clean post-Bitpanda (07-05) completed campaign-lifecycle datapoint** in the six-firm capture panel and confirms the corrected 07-12 sequence (Bitpanda 07-05 → Coinbase 07-13 → OKX + Kraken 07-31). Recorded as a longitudinal lifecycle event; **not a new capture-panel entrant** and not a new marketing-campaigns corpus row (the panel firm was already captured). Watch for a lapse-vs-extend confirmation over the next few days.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0 (HEALTHY-idempotent).** Source A `scan_date` **2026-07-13**. `daily-corpus-sync.py` ran clean, added 0 rows (`job postings ADDED: 0  firms: []`), 0 via Chrome inbox — a true no-new-roles idempotency. `_absence.csv` regenerated honestly to **Aave (Lever-404) + 5 proprietary needs-chrome firms** (Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys), `as_of=2026-07-13`. `_chrome-queue.csv` idempotent `as_of=2026-07-13` re-stamp (proprietary list unchanged: Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys pending-chrome; Solana `ingested`). Deterministic file deltas: `_absence.csv`, `_chrome-queue.csv` (date re-stamps only — diff confirms content identical to 07-12).

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0.** Source B `trend-data.json` `lastUpdated` **2026-06-15 — 28th consecutive day unchanged.** Escalation to Jukka stands and hardens: the agency panel is now four weeks stale and certain to overlap the Phase-2 synthesis start; upstream NorthPoint `trend-data.json` needs a refresh (not fixable from this loop). Matrix idempotent: 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots idempotent.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new named enforcement entries: 0.** Day-12 post-deadline sweep (named enforcement, blacklist, misleading-promotion queries) returned only: ESMA's orderly-wind-down expectation for unauthorised CASPs; AMF's unlicensed-operator sweep posture; general deadline/penalty-framework commentary; and the recurring KuCoin Austrian-FMA ban (Feb-2026, out-of-window entity action, not a marketing-side promotion case). None is a named marketing-side misleading-promotion enforcement action against a tracked-cohort CASP, so none meets the class-3 named-enforcement bar (logged as absence-continuation context). **Absence-as-data: the post-deadline named-enforcement silence is now twelve days long** — register-first, cases-later.

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new qualifying: 0.** CMO / Head-of-Marketing / Head-of-Brand / Head-of-Growth sweep surfaced only non-qualifying material. The in-window MiCA-migration commentary that recurs is from **OKX Europe CEO Erald Ghoos** ("~80% of exchanges won't survive MiCA," MiCA "Europe's first crypto user-migration test") — a **CEO, not a marketing-function operator**, so it does not meet the class-4 CMO/VP-Marketing/Head-of-Brand/Head-of-Growth bar (logged, excluded). No in-window verbatim statement by a qualifying marketing operator at a tracked firm. The class-4 drought since the May CMO churn persists and remains a Theme-1 datum (interim/empty marketing seats at Binance and Crypto.com).

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0.** July-window searches re-surfaced only captured items via aggregator round-ups (Coinbase ~500–700 with ~$50–60M Q2 restructuring charge; Gemini −30% / ~200–445 headcount / $582M loss framing; Kraken ~30% AI-pivot; Crypto.com −12%; BitGo −15%; "5,700+ crypto layoffs in 2026" round-ups) — no net-new marketing-team headcount cut at a tracked firm, and none of the surfaced cuts names marketing/growth as the affected function. Tracker holds at 8 marketing-scope + adjacency rows.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-13 section; last-updated bumped). The one logged shift this run is the **Coinbase 5% capture-campaign lapse (07-13)** — the first clean post-Bitpanda completed campaign-lifecycle datapoint, confirming the corrected sequence (Bitpanda 07-05 → Coinbase 07-13 → OKX + Kraken 07-31). Otherwise clean continuity — class-1 healthy-idempotent for a fourth straight day, day-12 enforcement silence, six-firm capture panel unchanged, class-4 drought. The methodology guard stands: cross-check any future job-postings "absence spike" against `scan_metadata` (`total_jobs_fetched` + `fetch_errors` count) before treating it as data.

---

## Watch items (carried, unchanged except where noted)
- **(a) Binance re-file jurisdiction** — still France-**reported**-only; firm names no jurisdiction formally; captured in `regulator-filings/binance-mica-eu-exit-2026-06.md`. Unchanged.
- **(b) First named post-deadline NCA marketing-side action** — day-12 silence logged; ESMA non-compliant register + AMF/BaFin unauthorised-entity instruments + EBA/AMLA coordinated-enforcement readiness remain the leading indicators; no named marketing-side case yet.
- **(c) Capture panel** — six firms, no 7th entrant this run; Ripple still licence-only. **Lifecycle sequence: Bitpanda lapsed 07-05 → Coinbase lapses 07-13 (today, first clean post-Bitpanda datapoint) → OKX + Kraken lapse 07-31.** Gate/OKX/Coinbase primary-page T&C capture still pending the Chrome/EU-IP lane.
- **(d) Agency panel staleness** — `trend-data.json` 28 days stale (06-15); escalation to Jukka hardened.

## Searches / fetches run (audit trail)
1. `MiCA crypto marketing enforcement action July 2026 BaFin AMF CONSOB CySEC ESMA named CASP misleading promotion` → framework/deadline + wind-down/unauthorised-entity + KuCoin-Austria(Feb, out-of-window) material; 0 net-new named marketing-side case (day-12 silence).
2. `crypto exchange marketing team layoffs July 2026 Coinbase Kraken Gemini growth marketing headcount cut` → captured items + aggregator round-ups only (Coinbase ~500–700/$50–60M Q2, Gemini −30%, Kraken ~30%); 0 net-new tracked-firm marketing-scope layoff.
3. `crypto exchange CMO "head of marketing" "head of brand" interview podcast July 2026 Coinbase Kraken OKX Bitpanda MiCA` → only CEO-level MiCA-migration commentary (OKX Europe CEO Erald Ghoos); 0 qualifying class-4 marketing-operator statement.
4. `Coinbase EU deposit bonus 5% transfer promotion end date July 2026 displaced Binance users campaign` → FinanceFeeds/Digg/gncrypto confirm the Coinbase 5% transfer bonus **ends 07-13** (Coinbase One–gated, genuine external transfers only, DE/FR/IT/BE/PL/SE/UK) → today's capture-lifecycle datapoint.
5. `crypto marketing VP / head of growth statement LinkedIn July 2026 MiCA financial promotion compliance` → general MiCA compliance material + an unrelated job posting; 0 qualifying class-4.

## Net-new / changed this run
- `corpus/job-postings/_absence.csv` (honest regeneration, `as_of=2026-07-13` — Aave Lever-404 + 5 proprietary; feed healthy)
- `corpus/job-postings/_chrome-queue.csv` (idempotent `as_of=2026-07-13` re-stamp — proprietary firm list unchanged)
- `findings/longitudinal-2026-06.md` (2026-07-13 continuity + Coinbase-lapse lifecycle section + last-updated bump)
- `corpus/weekly-runs/2026-07-13-corpus-run.md` (this record)

## Recommendation for next run
(a) **Class-1 feed healthy** — resume trusting `open-positions.json` absence data; keep the `scan_metadata` cross-check as a standing guard. (b) First named post-deadline NCA marketing-side action — day-12 silence logged; watch for the transition from register/blacklist/coordinated-readiness to a named misleading-promotion case. (c) **Confirm the Coinbase 5% lapse (vs a quiet extension)** over the next few days; **OKX + Kraken (07-31)** are the next campaign-lifecycle checkpoints. (d) Any 7th capture entrant (Ripple still licence-only). (e) Qualifying class-4 statements as post-deadline conference/podcast content lands — note CEO-level MiCA commentary keeps surfacing but does not meet the marketing-operator bar. (f) **Agency panel 28 days stale — escalation to Jukka carried/hardened** (upstream `trend-data.json` refresh needed before July synthesis).

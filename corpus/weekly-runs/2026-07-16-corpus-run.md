# Corpus-assembly daily run — 2026-07-16 (day 15 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated). **First run since 2026-07-13** — the `07-14` and `07-15` runs did not fire (two-day loop gap; see Headline §0).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Dedup baseline read before searching:** prior runs 2026-07-13 back to 2026-06-30; `regulator-filings/` (incl. Binance EU-exit event-chain, ESMA/AMF/FCA filings); `marketing-campaigns/mica-competitive-capture-2026-06.md` (six-firm capture panel); `operator-statements/`; `layoff-tracker/2026-layoff-tracker.csv` (8 marketing-scope + adjacency rows); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

---

## Headline result

**First run after a two-day loop gap (07-14/07-15 did not fire); all six classes net-zero net-new; class-1 HEALTHY-idempotent. The idempotent sync + fully-dedup'd web-search classes mean the gap cost the corpus nothing — today re-establishes the audit trail from current feed state. `open-positions.json` reports `scan_metadata.scan_date: 2026-07-15` (feed one day in arrears — normal morning-run state, not an outage), 2,317 jobs fetched / 87 API firms / 0 fetch-error mass-signature, `new_count: 1` — but that single new role does not map to a Stratum 1–4 tracked-firm marketing seat, so 0 corpus rows added (genuine no-new-marketing-roles idempotency). Day-15 post-deadline named-enforcement silence holds; classes 4/5 net-zero; capture panel unchanged at six firms with no 7th entrant. No campaign-lifecycle event fell in the 07-14→07-16 window (next checkpoint: OKX 8% + Kraken lapse 07-31). The material read remains continuity — the post-deadline patterns extend to a fifteenth day with no structural shift.**

0. **Two-day loop gap logged (operational, not a corpus signal).** No `07-14`/`07-15` run record exists — the daily task skipped two days. Because `daily-corpus-sync.py` is idempotent and the web-search classes are dedup'd against the full prior corpus, nothing was lost: the missed days carry no independent corpus cost (class-1 was genuine no-new-roles idempotency; classes 3/4/5 remained net-zero across the window, re-verified this run). Flagged so the gap is visible in run history, not silently papered over.
1. **Class-1 feed healthy and clean.** `daily-corpus-sync.py` ran clean on `open-positions.json` (`scan_metadata.scan_date: 2026-07-15`; 2,317 jobs / 147 companies scanned / 87 via API; no mass fetch-error signature), added **0 job-posting rows** (`firms: []`), and regenerated `_absence.csv` / `_chrome-queue.csv` as date re-stamps only. `_absence.csv` honest at **Aave (Lever-404) + 5 proprietary needs-chrome firms** (Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys). Phantom Head of Brand Creative (07-02) remains the latest genuine class-1 row.
2. **Day-15 named-enforcement silence holds (class 3 absence-as-data).** Fifteen days past the July-1 transitional-period end, still **no named marketing-side NCA enforcement case** (BaFin/AMF/CONSOB/AFM/CySEC/ESMA) on the public record against a tracked-cohort firm. Today's sweep surfaced only framework/deadline material and unauthorised-entity/wind-down instruments (ESMA wind-down + "cease marketing and solicitation"; AMF unlicensed-operator sweep; Art. 59 up-to-€15M-or-5%-turnover penalty framing; the recurring FCA→HTX action is the Feb-2026 out-of-window UK financial-promotion case, already captured). None meets the class-3 named-enforcement bar. Register-first, cases-later now extends to a fifteen-day pattern.
3. **Capture panel + campaign-lifecycle unchanged.** No 7th capture-panel entrant; Ripple still licence-only. No lifecycle event in the 07-14→07-16 window; next checkpoint is **OKX 8% + Kraken lapse 07-31** (corrected sequence: Bitpanda 07-05 → Coinbase 07-13 → OKX + Kraken 07-31).

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0 (HEALTHY-idempotent).** Source A `scan_metadata.scan_date` **2026-07-15** (scan ran 21:45 UTC 07-15; the 07-16 scan had not yet posted at run time — feed one day in arrears, the expected morning-run state). Metadata: `total_jobs_fetched: 2317`, `companies_scanned: 147`, `companies_via_api: 87`, `total_jobs_after_filter: 24`, `new_count: 1`, `still_open_count: 23` — no mass fetch-error signature (07-08 outage pattern absent). The single `new_count: 1` role did **not** map to a Stratum 1–4 tracked-firm marketing/growth seat, so the sync added **0 rows** (`job postings ADDED: 0  firms: []`), 0 via Chrome inbox — genuine no-new-marketing-roles idempotency. `_absence.csv` regenerated honestly to **Aave (Lever-404) + 5 proprietary needs-chrome firms** (Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys), `as_of=2026-07-16`. `_chrome-queue.csv` idempotent `as_of=2026-07-16` re-stamp (proprietary list unchanged: Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys pending-chrome; Solana ingested). Deterministic file deltas: `_absence.csv`, `_chrome-queue.csv` (date re-stamps only — diff confirms content identical to 07-13 apart from `as_of`).

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0.** Source B `trend-data.json` `lastUpdated` **2026-06-15 — 31st consecutive day unchanged.** Escalation to Jukka stands and hardens: the agency panel is now over a month stale and squarely inside the Phase-2 synthesis window; upstream NorthPoint `trend-data.json` needs a refresh (not fixable from this loop). Matrix idempotent: 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots idempotent.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new named enforcement entries: 0.** Day-15 post-deadline sweep (named enforcement, misleading-promotion, financial-promotion fine queries) returned only: ESMA's orderly-wind-down / "cease marketing and solicitation" expectation for unauthorised CASPs; AMF's unlicensed-operator sweep posture; Art. 59 penalty-exposure framing (up to €15M or 5% of annual turnover); and the recurring **FCA→HTX** financial-promotion action (Feb-2026, out-of-window UK case, already captured). None is a named marketing-side misleading-promotion enforcement action against a tracked-cohort CASP, so none meets the class-3 named-enforcement bar (logged as absence-continuation context). **Absence-as-data: the post-deadline named-enforcement silence is now fifteen days long** — register-first, cases-later.

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new qualifying: 0.** CMO / Head-of-Marketing / Head-of-Brand / Head-of-Growth sweep surfaced only non-qualifying material: OKX Global CMO **Haider Rafique** recurs as a standing profile (no in-window verbatim July-2026 statement); the recurring in-window MiCA-migration commentary is from **OKX Europe CEO Erald Ghoos** (a CEO, not a marketing-function operator — excluded from the class-4 bar). No in-window verbatim statement by a qualifying marketing operator at a tracked firm. The class-4 drought since the May CMO churn persists and remains a Theme-1 datum (interim/empty marketing seats at Binance and Crypto.com).

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0.** July-window searches re-surfaced only captured items via aggregator round-ups (Coinbase ~500–700 with ~$50–60M Q2 restructuring charge; Gemini −30% / ~$582M-loss framing; Kraken ~30% AI-pivot; Crypto.com −12%; BitGo −15%; "5,700+ crypto layoffs in 2026" round-ups) — no net-new marketing-team headcount cut at a tracked firm, and none of the surfaced cuts names marketing/growth as the affected function. Tracker holds at 8 marketing-scope + adjacency rows.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-16 section; last-updated bumped). No new longitudinal shift this run — clean continuity: class-1 healthy-idempotent, day-15 enforcement silence, six-firm capture panel unchanged, class-4 drought. The two-day loop gap is logged as an operational note (§0), not a corpus signal. The methodology guard stands: cross-check any future job-postings "absence spike" against `scan_metadata` (`total_jobs_fetched` + `fetch_errors` count) before treating it as data.

---

## Watch items (carried, unchanged except where noted)
- **(a) Binance re-file jurisdiction** — still France-**reported**-only; firm names no jurisdiction formally; captured in `regulator-filings/binance-mica-eu-exit-2026-06.md`. Unchanged.
- **(b) First named post-deadline NCA marketing-side action** — day-15 silence logged; ESMA non-compliant register + AMF/BaFin unauthorised-entity instruments + EBA/AMLA coordinated-enforcement readiness remain the leading indicators; no named marketing-side case yet.
- **(c) Capture panel** — six firms, no 7th entrant this run; Ripple still licence-only. **Lifecycle sequence: Bitpanda lapsed 07-05 → Coinbase lapsed 07-13 → OKX + Kraken lapse 07-31.** Gate/OKX/Coinbase primary-page T&C capture still pending the Chrome/EU-IP lane.
- **(d) Agency panel staleness** — `trend-data.json` 31 days stale (06-15); escalation to Jukka hardened (now inside Phase-2 synthesis window).
- **(e) Loop cadence** — 07-14/07-15 runs did not fire; if the gap recurs, the scheduled task itself needs a health check (separate from the corpus).

## Searches / fetches run (audit trail)
1. `MiCA crypto marketing enforcement action July 2026 BaFin AMF CONSOB CySEC ESMA named CASP misleading promotion` → framework/deadline + ESMA wind-down/"cease marketing and solicitation" + AMF unlicensed-operator + Art. 59 penalty framing; 0 net-new named marketing-side case (day-15 silence).
2. `crypto exchange marketing growth team layoffs July 2026 Coinbase Kraken Gemini headcount cut` → captured items + aggregator round-ups only (Coinbase ~500–700/$50–60M Q2, Gemini −30%/$582M, Kraken ~30% AI-pivot, BitGo −15%, 5,700+ round-up); 0 net-new tracked-firm marketing-scope layoff.
3. `crypto exchange CMO "head of marketing" "head of brand" "head of growth" interview podcast July 2026 MiCA Coinbase Kraken OKX Bitpanda Bitstamp` → OKX Global CMO Haider Rafique standing profile (no in-window verbatim) + OKX Europe CEO Ghoos (CEO, excluded) + MiCA-market-structure commentary; 0 qualifying class-4 marketing-operator statement.
4. `crypto financial promotion enforcement fine misleading advertising exchange July 2026 BaFin CONSOB AFM FCA` → finfluencer-crackdown framing + FCA crypto-promotions regime material + recurring FCA→HTX (Feb-2026, out-of-window, captured); 0 net-new named marketing-side EU case.

## Net-new / changed this run
- `corpus/job-postings/_absence.csv` (honest regeneration, `as_of=2026-07-16` — Aave Lever-404 + 5 proprietary; feed healthy)
- `corpus/job-postings/_chrome-queue.csv` (idempotent `as_of=2026-07-16` re-stamp — proprietary firm list unchanged)
- `findings/longitudinal-2026-06.md` (2026-07-16 continuity + loop-gap note + last-updated bump)
- `corpus/weekly-runs/2026-07-16-corpus-run.md` (this record)

## Recommendation for next run
(a) **Class-1 feed healthy** — resume trusting `open-positions.json` absence data; keep the `scan_metadata` cross-check as a standing guard. (b) First named post-deadline NCA marketing-side action — day-15 silence logged; watch for the transition from register/blacklist/coordinated-readiness to a named misleading-promotion case. (c) **OKX 8% + Kraken (07-31)** are the next campaign-lifecycle checkpoints; watch for a 7th capture entrant (Ripple still licence-only). (d) Qualifying class-4 statements as post-deadline conference/podcast content lands — note CEO-level MiCA commentary keeps surfacing but does not meet the marketing-operator bar. (e) **Agency panel 31 days stale — escalation to Jukka carried/hardened** (upstream `trend-data.json` refresh needed inside July synthesis). (f) **Loop cadence** — confirm the daily task is firing after the 07-14/07-15 gap.

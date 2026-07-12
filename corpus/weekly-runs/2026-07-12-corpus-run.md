# Corpus-assembly daily run — 2026-07-12 (day 11 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Dedup baseline read before searching:** prior runs 2026-07-11 back to 2026-06-30; `regulator-filings/` (incl. Binance EU-exit event-chain); `marketing-campaigns/mica-competitive-capture-2026-06.md` (six-firm capture panel); `operator-statements/`; `layoff-tracker/2026-layoff-tracker.csv` (8 marketing-scope + adjacency rows); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

---

## Headline result

**All six classes net-zero net-new; class-1 HEALTHY-idempotent for a third straight day. Today's `open-positions.json` (scan 2026-07-12) fetched 2,303 jobs across 87 API firms with 0 fetch-errors, so the 0-new-rows result is genuine "no new marketing roles at tracked firms" idempotency, not an infra artifact. Day-11 post-deadline named-enforcement silence holds; classes 4/5 net-zero; capture panel unchanged at six firms. The material read is continuity — the post-deadline patterns extend to an eleventh day with no structural shift, one day out from the 07-13 Coinbase campaign-lifecycle checkpoint. Correction logged: the 07-13 lapse is Coinbase's 5% window only; OKX's 8% deposit bonus runs to 07-31 per its primary campaign page (prior runs conflated the two).**

1. **Class-1 feed healthy and clean.** `open-positions.json` (scan 2026-07-12) returned `total_jobs_fetched: 2303` (essentially flat vs yesterday's 2,304 — normal daily churn), `companies_via_api: 87`, and **0 `fetch_errors`** in `scan_metadata`. The sync's own Aave Lever-`aave` HTTP-404 probe still logs Aave to `_absence.csv` (stable structural gap, not a new outage). Today's **0 job-posting rows is genuine idempotency**. Phantom Head of Brand Creative (07-02) remains the latest genuine class-1 row. Three consecutive clean scans (07-10, 07-11, 07-12) confirm the 07-08 outage was isolated.
2. **Day-11 named-enforcement silence holds (class 3 absence-as-data).** Eleven days past the July-1 transitional-period end, still **no named marketing-side NCA enforcement case** (BaFin/AMF/CONSOB/AFM/CySEC/ESMA) on the public record against a tracked-cohort firm. Today's sweep surfaced only framework/deadline commentary and unauthorised-entity/wind-down instruments (ESMA orderly-wind-down expectation; AMF unlicensed-operator sweep posture; up-to-€15M-or-12.5%-revenue penalty framing). None is a named marketing-side misleading-promotion enforcement action against a tracked-cohort CASP. The register-first, cases-later read now extends to an eleven-day pattern.
3. **Capture panel unchanged at six firms — no 7th entrant.** The displaced-Binance/Bybit deposit-bonus sweep re-confirmed only the panel already captured (OKX 8% up-to-€20k-USDC over 52 weeks / Coinbase 5% [before 07-13] / Kraken €1M prize draw [22 Jun–31 Jul] / Bitpanda [lapsed 07-05] / Bitvavo / Gate). No net-new campaign, no 7th entrant. Ripple still licence-only. **Window-date correction:** OKX's primary campaign page (`okx.com/en-eu/learn/okx-europe-deposit-bonus-mica-deadline`) states the offer runs **29 Jun – 31 Jul 2026**; only **Coinbase's 5% transfer bonus lapses 07-13**. Prior run records ("OKX + Coinbase windows lapse 07-13") conflated the two — corrected here for the campaign-lifecycle timeline.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0 (HEALTHY-idempotent).** Source A `scan_date` **2026-07-12**, `total_jobs_fetched: 2303`, `companies_via_api: 87`, **0 fetch-errors** in `scan_metadata`. `daily-corpus-sync.py` ran clean, added 0 rows — a true no-new-roles idempotency. `_absence.csv` regenerated honestly to **Aave (Lever-404) + 5 proprietary needs-chrome firms (Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys)** with `as_of=2026-07-12`. `_chrome-queue.csv` idempotent `as_of=2026-07-12` re-stamp (proprietary list unchanged: Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys pending-chrome; Solana `ingested`). Deterministic file deltas: `_absence.csv`, `_chrome-queue.csv` (date re-stamps only — diff confirms content identical to 07-11).

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0.** Source B `trend-data.json` `lastUpdated` **2026-06-15 — 27th consecutive day unchanged.** Escalation to Jukka stands and hardens: the agency panel is now ~4 weeks stale and certain to overlap the Phase-2 synthesis start; upstream NorthPoint `trend-data.json` needs a refresh (not fixable from this loop). Matrix idempotent: 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots idempotent.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new named enforcement entries: 0.** Day-11 post-deadline sweep (named enforcement, blacklist, misleading-promotion queries) returned only: ESMA's orderly-wind-down expectation for unauthorised CASPs; AMF's unlicensed-operator sweep posture; and penalty-exposure framing (up to €15M or 12.5% of annual revenue for post-deadline unauthorised operation). None is a named marketing-side misleading-promotion enforcement action against a tracked-cohort CASP, so none meets the class-3 named-enforcement bar (logged as absence-continuation context). **Absence-as-data: the post-deadline named-enforcement silence is now eleven days long** — register-first, cases-later.

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new qualifying: 0.** CMO / Head-of-Marketing / conference-and-podcast sweep surfaced only non-qualifying material: the recurring OKX CMO Haider Rafique profile is a **March 2025 Drum interview** (out of the Dec-2024+ window and previously reviewed), and general podcast catalogues (Coinbase Markets Podcast, CoinDesk Public Keys) feature non-marketing hosts/guests. No in-window verbatim statement by a CMO/VP-Marketing/Head-of-Brand/Head-of-Growth at a tracked firm. The class-4 drought since the May CMO churn persists and remains a Theme-1 datum (interim/empty marketing seats at Binance and Crypto.com).

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0.** July-window searches re-surfaced only captured items via aggregator round-ups (Coinbase ~700 / −14% with $50–60M Q2 restructuring charge; Gemini −30% / ~445 headcount / $582M loss framing; Kraken AI-pivot; Crypto.com −12%; BitGo −15%; "5,700+ crypto layoffs in 2026" round-ups) — no net-new marketing-team headcount cut at a tracked firm, and none of the surfaced cuts names marketing/growth as the affected function. Tracker holds at 8 marketing-scope + adjacency rows. (Note: the Coinbase figure appears in H1 round-ups as both "~500" and "about 700 / restructuring ~$50–60M Q2" framings; both describe the same disclosed Q2 restructuring event, not a net-new cut.)

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-12 section; last-updated bumped). No corpus-content shift this run. The logged observation is **clean continuity** — class-1 healthy-idempotent for a third straight day (0 fetch-errors), day-11 enforcement silence, six-firm capture panel unchanged, one day out from the 07-13 Coinbase checkpoint, plus the OKX/Coinbase window-date correction. The methodology guard stands: cross-check any future job-postings "absence spike" against `scan_metadata` (`total_jobs_fetched` + `fetch_errors` count) before treating it as data.

---

## Watch items (carried, unchanged except where noted)
- **(a) Binance re-file jurisdiction** — still France-**reported**-only; firm names no jurisdiction formally; captured in `regulator-filings/binance-mica-eu-exit-2026-06.md`. Unchanged.
- **(b) First named post-deadline NCA marketing-side action** — day-11 silence logged; ESMA non-compliant register + AMF/BaFin unauthorised-entity instruments + EBA/AMLA coordinated-enforcement readiness remain the leading indicators; no named marketing-side case yet.
- **(c) Capture panel** — six firms, no 7th entrant this run; Ripple still licence-only. **Corrected timeline: Coinbase's 5% window lapses 07-13 (tomorrow — first completed-lifecycle datapoint after Bitpanda 07-05); OKX 8% runs to 07-31; Kraken €1M draw to 07-31.** Gate/OKX/Coinbase primary-page T&C capture still pending the Chrome/EU-IP lane.
- **(d) Agency panel staleness** — `trend-data.json` 27 days stale (06-15); escalation to Jukka hardened.

## Searches / fetches run (audit trail)
1. `MiCA crypto marketing enforcement action July 2026 BaFin AMF CONSOB CySEC ESMA named CASP misleading promotion` → framework/deadline + wind-down/unauthorised-entity + penalty-exposure material; 0 net-new named marketing-side case (day-11 silence).
2. `crypto exchange marketing team layoffs July 2026 Coinbase Kraken Gemini growth marketing headcount cut` → captured items + aggregator round-ups only (Coinbase ~700/$50–60M Q2, Gemini −30%); 0 net-new tracked-firm marketing-scope layoff.
3. `crypto exchange CMO "head of marketing" "head of brand" interview podcast July 2026 Coinbase Kraken OKX Bitpanda` → out-of-window OKX CMO profile (Mar-2025) + generic podcast catalogues; 0 qualifying class-4.
4. `crypto exchange EU deposit bonus promotion July 2026 OKX Coinbase Kraken displaced Binance users reward campaign` → six-firm capture panel re-confirmed; OKX primary page confirms 29 Jun–31 Jul window (Coinbase lapses 07-13); no 7th entrant.

## Net-new / changed this run
- `corpus/job-postings/_absence.csv` (honest regeneration, `as_of=2026-07-12` — Aave Lever-404 + 5 proprietary; feed healthy, 0 upstream fetch-errors)
- `corpus/job-postings/_chrome-queue.csv` (idempotent `as_of=2026-07-12` re-stamp — proprietary firm list unchanged)
- `findings/longitudinal-2026-06.md` (2026-07-12 continuity section + OKX/Coinbase window-date correction + last-updated bump)
- `corpus/weekly-runs/2026-07-12-corpus-run.md` (this record)

## Recommendation for next run
(a) **Class-1 feed healthy** — resume trusting `open-positions.json` absence data; keep the `scan_metadata` cross-check as a standing guard. (b) First named post-deadline NCA marketing-side action — day-11 silence logged; watch for the transition from register/blacklist/coordinated-readiness to a named misleading-promotion case. (c) **07-13 is the Coinbase campaign-lifecycle checkpoint (5% window lapses)** — check for lapse-vs-extend, the first completed-lifecycle datapoint after Bitpanda (07-05); OKX (07-31) and Kraken (07-31) are the later ones. (d) Any 7th capture entrant (Ripple still licence-only). (e) Qualifying class-4 statements as post-deadline conference/podcast content lands. (f) **Agency panel 27 days stale — escalation to Jukka carried/hardened** (upstream `trend-data.json` refresh needed before July synthesis).

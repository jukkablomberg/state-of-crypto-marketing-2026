# Corpus-assembly daily run — 2026-07-20 (day 19 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Single fire, morning CEST. Cadence note: 07-19 was a double-fire day; 07-20 has fired once so far (see watch item (e)).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Dedup baseline read before searching:** prior runs 2026-07-19 (morning + intraday) back to 2026-06-30; `regulator-filings/` (Binance EU-exit event-chain, ESMA/AMF/FCA filings); `marketing-campaigns/mica-competitive-capture-2026-06.md`; `operator-statements/`; `layoff-tracker/2026-layoff-tracker.csv` (8 rows pre-run); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

---

## Headline result

**Day 19 post-deadline. The material result of this run is a genuine net-new class-5 row: Polygon Labs (Stratum 2, in-cohort) announced a second 2026 layoff round on 2026-07-16, primary-sourced to CEO Marc Boiron's own X post — and its stated rationale is repositioning/M&A integration, not the AI-efficiency framing that has dominated every other tracked-firm 2026 cut.** This is the **first in-cohort layoff row added since Coinbase (05-05)**; every row added in between (Robinhood, BitGo, Block, MARA) was adjacency-perimeter. Class 1 returned to idempotency (0 rows) against a **current and healthy** feed (`scan_date: 2026-07-20`, 2,295 jobs, `new_count: 0`, `url_verification_dropped: 0`) — the 07-19 Coinbase Creative Director capture is now confirmed complete by a fourth consecutive read. Class 2 unchanged and **now 35 days stale**. Class 3 net-zero: **day-19 named-enforcement silence holds**. Class 4 net-zero: drought persists.

1. **Class 5 breaks — Polygon Labs, and it breaks the AI-cover pattern (the material result).** Boiron announced the cut on X on 2026-07-16, framing it as completing the transformation "from a blockchain foundation into a blockchain-enabled payments company", integrating the acquired Coinme team, and targeting profitability in 2027. Verbatim from the internal note as reported: *"the market has shifted from building differentiated components to delivering one integrated stack through a single API, a change that requires different talent and organization"* and *"I would rather make the right call now than delay it."* He explicitly stated the cuts are **not** performance-tied. **Theme-5 relevance:** every prior 2026 tracked-firm cut in the tracker (Crypto.com −12%, Coinbase −14%, Kraken ~30%, plus adjacency BitGo) carries an AI-efficiency or AI-infra stated rationale. Polygon is the first to state a **repositioning/M&A** rationale instead. That is a counter-instance to the "AI-as-stated-rationale" pattern, and counter-instances are load-bearing for a report that intends to make a claim about it.
2. **Figure discipline — an aggregator error caught and not propagated.** Search round-ups (Yahoo/TheStreet summary framing) attach "roughly 100 employees, about 20% of staff" to this event. **That is wrong**: reading both primary write-ups at source, those figures belong to Polygon Labs' **February 2023** round. Both the TheStreet/Yahoo piece and AMBCrypto (2026-07-16) state that specific figures for the July-2026 round were **not disclosed**. The tracker row therefore records `undisclosed / undisclosed` with the misattribution logged in the notes. No fabricated number entered the corpus.
3. **Day-19 named-enforcement silence holds (class 3 absence-as-data).** Nineteen days past the July-1 transitional-period end, still **no named marketing-side NCA enforcement case** against a tracked-cohort firm. ESMA's own posture confirms the structural reason: ESMA states unauthorised CASPs must "cease marketing activities and solicitation", but **policing falls to the 27 national competent authorities** — register-first, cases-later, now a nineteen-day pattern.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0 (genuine idempotency).** Printed summary:
```
date: 2026-07-20
source A (jobs)   scan_date: 2026-07-20
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```
**Standing `scan_metadata` cross-check guard applied and satisfied** — the zero is genuine, not an outage: `scanned_at_utc: 2026-07-19T22:45:13Z`, `scan_date: 2026-07-20`, `companies_scanned: 147` (87 via API, 60 chrome-pending), `total_jobs_fetched: 2295`, `total_jobs_after_filter: 25`, `new_count: 0`, `still_open_count: 25`, `url_verification_enabled: true`, `url_verification_dropped: 0`. No fetch-error mass-signature. This is the **fourth consecutive read** confirming the 07-19 Coinbase Creative Director row is complete.

`_absence.csv` regenerated honestly to **Aave (Lever-404) + 5 proprietary needs-chrome firms** (Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys), `as_of=2026-07-20`. `_chrome-queue.csv` idempotent `as_of=2026-07-20` re-stamp (proprietary list unchanged). `git status` after the sync showed **only these two `_` files modified — date-only re-stamps**, no data rows changed. Coinbase brand-rebuild watch item (g) stays at **n=1**: no second Tier-1 senior brand/creative requisition this run.

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0.** Source B `trend-data.json` `lastUpdated` **2026-06-15 — 35th consecutive day unchanged.** Matrix idempotent: 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots written (idempotent). **Escalation to Jukka carried and hardening for a 35th day.** The agency panel is now over five weeks stale and sits squarely inside the Phase-2 synthesis window; a class-2 finding written today would be describing mid-June reality. This is upstream of this loop and remains **the single highest-value unblock available to the report**.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new named enforcement entries: 0.** Day-19 sweep across EU NCA named-action and financial-promotion queries returned only already-captured or out-of-scope material:
- **ESMA public statement on the end of the transitional period** (`ESMA75-113276571-1710`, June 2026) — already captured in `regulator-filings/esma-mica-transitional-period-end-2026-06.md`. Re-read this run for one specific reason: it confirms the structural cause of the silence — unauthorised CASPs must "immediately stop onboarding new EU clients… and **cease marketing activities and solicitation**", but **actual policing falls to national competent authorities across 27 member states**. A centralised ESMA marketing-enforcement action was never the mechanism; the cases, when they come, come from NCAs one at a time.
- **Authorisation-conversion context (not a case):** ~1,200 entities registered under national regimes vs **~210–244 with full MiCA authorisation** — a **~17–20% conversion rate**. Recorded here as corroborating context for the Theme-4 absence panel, not as a class-3 entry.
- **AMF** unlicensed-operator posture; **CySEC** AML/sanctions supervisory activity (not marketing-side); recurring **FCA→HTX** financial-promotion action (out-of-window UK case, already captured); platform ad-policy changes (X/Meta/Google — **platform policy is not regulator enforcement**, does not meet the class-3 bar).

**Absence-as-data: the post-deadline named-enforcement silence is now nineteen days long.** Register-first, cases-later.

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new qualifying: 0.** CMO / Head-of-Brand / Head-of-Growth sweep surfaced only non-qualifying material:
- **Paul Afshar, CMO, Paybis** — a qualifying *seniority*, but **Paybis is not in the tracked cohort**. Excluded.
- **Binance CMO Rachel Conlan → Eowyn Chen (interim)** — already captured (Conlan departed 15 June after ~3 years, stays on as adviser; Chen ex-Trust Wallet CEO). Re-surfaced, not net-new.
- **Kraken CGMO Mayur Gupta** — still profile-only, no in-window dated verbatim. Carried as the highest-probability next qualifying source.
- **OKX Global CMO Haider Rafique** — The Drum interview (2025-03-11) remains the logged JS-render retry candidate from the 07-19 intraday run. **Not retried this run** (deterministic classes + a genuine class-5 capture took the run's budget); carried unchanged.

The class-4 drought since the May CMO churn persists and remains a Theme-1 datum in its own right: the marketing seats at Binance (interim) and Crypto.com (vacated) are precisely the seats that would otherwise be speaking publicly in the post-deadline window, and they are empty.

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 1 — tracker moves 8 → 9.** Row written to `corpus/layoff-tracker/2026-layoff-tracker.csv`:

| field | value |
|---|---|
| firm | Polygon Labs (**Stratum 2, in-cohort**) |
| date_announced | 2026-07-16 |
| headcount_change / percentage | **undisclosed / undisclosed** (see figure-discipline note) |
| source_url | `https://x.com/0xMarcB/status/2077734931434790989` (CEO Marc Boiron, X) |
| ai_cover_narrative | **N** |
| marketing-specific? | **No** — no function named |

Corroborating secondary reads (both 2026-07-16, both confirm figures not disclosed): TheStreet via Yahoo Finance, `https://finance.yahoo.com/markets/crypto/articles/polygon-cuts-jobs-second-time-211500568.html`; AMBCrypto, `https://ambcrypto.com/polygon-labs-announces-second-round-of-2026-layoffs-as-it-targets-profitability-in-2027/`.

Sequence context (verified, not conflated): ~100 / ~20% cut **February 2023**; 19% / 60 people **February 2024**; 60 people **January 2026** (post-$250M Coinme + Sequence acquisition); this round **July 2026** — second of 2026, at least fourth in four years.

Everything else in the July sweep was already-captured aggregator round-up material (Coinbase −14%, Gemini −30% YTD, Kraken ~30%, Crypto.com −12%, Algorand −25%, "5,700+ crypto layoffs in 2026"). No net-new *marketing-team-specific* cut at any tracked firm — that absence continues to hold across the whole 2026 tracker: **not one row names marketing as the affected function**, which is itself the Theme-5 finding.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-20 section). **One genuine shift:** the AI-as-stated-rationale pattern acquires its first tracked-firm counter-instance. Prior to today the tracker's stated-rationale column read as near-uniform AI framing among tracked firms; Polygon states repositioning/M&A instead. The synthesis claim must therefore be written as *"AI framing dominates but is not universal"*, with Polygon named as the counter-instance — a stronger, more defensible claim than the unqualified version, and one that survives an adversarial read. Methodology guards restated: (i) cross-check any job-postings "absence spike" against `scan_metadata` before treating it as data; (ii) **cross-check aggregator-attached headcount figures against the primary write-up before entering them** — today's Polygon case is the second instance of a round-up misattributing an older round's numbers to a current event.

---

## Watch items
- **(a) Binance re-file jurisdiction** — still France-**reported**-only; firm names no jurisdiction formally. Unchanged.
- **(b) First named post-deadline NCA marketing-side action** — **day-19 silence logged.** ESMA statement re-read this run clarifies why: enforcement is NCA-level across 27 member states, not centralised. Leading indicators remain the ESMA non-compliant register + AMF/BaFin unauthorised-entity instruments.
- **(c) Capture panel** — six firms, no 7th entrant; Ripple still licence-only. **Next lifecycle checkpoint: OKX 8% + Kraken lapse 07-31** (11 days out).
- **(d) Agency panel staleness — 35 days** (`trend-data.json` 06-15). Escalation carried and hardening. Highest-value unblock available to the report.
- **(e) Loop cadence** — 07-20 fired once (clean) after 07-19's double-fire. Pattern over nine days: 07-14 no-fire → 07-15 no-fire → 07-16 double → 07-17 clean → 07-18 no-fire → 07-19 double → 07-20 clean. **Six irregular days out of nine.** Corpus remains fully protected (idempotent sync + corpus-wide dedup on search classes); the **scheduler** still needs a health check. Escalation to Jukka unchanged.
- **(f) Friday nomination cadence** — today is **Monday 07-20**, not a nomination day. No `inbound-nominations.md` exists yet. Next check **Friday 07-24**.
- **(g) Coinbase brand-rebuild signal** — holds at **n=1**. No second Tier-1 senior brand/creative requisition today.
- **(h) NEW — layoff-rationale divergence** — watch whether a second tracked firm states a non-AI rationale. One counter-instance qualifies the Theme-5 claim; two would make "AI framing is a narrative choice, not a description" a defensible synthesis claim in its own right.

## Searches / fetches run (audit trail)
1. `MiCA marketing communications enforcement action July 2026 BaFin AMF CONSOB CySEC AFM named crypto exchange misleading promotion` → MiCA truth-in-marketing framework + NCA supervisory-review posture + AMF unlicensed-operator sweep; **0 net-new named marketing-side case**.
2. `ESMA non-compliant CASP register July 2026 national competent authority action cease marketing crypto firm named` → ESMA public statement `ESMA75-113276571-1710` (captured); "cease marketing activities and solicitation" wording; policing devolved to 27 NCAs; ~210–244 of ~1,200 authorised (~17–20% conversion); **0 named firm-level marketing action**.
3. `crypto exchange CMO "head of brand" "head of growth" interview podcast July 2026 Kraken OKX Coinbase Bitpanda marketing` → OKX Rafique (The Drum, Mar-2025, carried retry candidate); **0 qualifying class-4 statement**.
4. `"chief marketing officer" OR "VP marketing" crypto exchange July 2026 statement LinkedIn conference MiCA brand strategy` → Paybis CMO (non-cohort), Binance Conlan→Chen (captured); **0 qualifying class-4 statement**.
5. `crypto marketing team layoffs July 2026 growth brand headcount cut exchange announcement` → **Polygon Labs 07-16 (net-new, in-cohort)** + captured round-ups.
6. `Polygon Labs layoffs July 16 2026 Marc Boiron Coinme how many employees percentage` → **figure-discipline check**: confirmed figures not disclosed; ~100/20% belongs to Feb-2023.
7. `web_fetch` AMBCrypto 2026-07-16 → verified date, CEO attribution, Coinme framing, "specific figures were not shared".
8. `web_fetch` Yahoo/TheStreet 2026-07-16 → verified primary X URL, verbatim internal-note quotes, full round sequence 2023/2024/Jan-2026/Jul-2026.

## Net-new / changed this run
- `corpus/layoff-tracker/2026-layoff-tracker.csv` (**1 genuine net-new class-5 row** — Polygon Labs 2026-07-16, in-cohort, primary-sourced, AI-cover=N; tracker 8 → 9 rows)
- `corpus/job-postings/_absence.csv` (honest regeneration, `as_of=2026-07-20` — Aave Lever-404 + 5 proprietary; feed healthy/current)
- `corpus/job-postings/_chrome-queue.csv` (idempotent `as_of=2026-07-20` re-stamp — proprietary firm list unchanged)
- `findings/longitudinal-2026-06.md` (2026-07-20 section: AI-rationale counter-instance; aggregator figure-misattribution guard added)
- `corpus/weekly-runs/2026-07-20-corpus-run.md` (this record)

## Recommendation for next run
(a) **Watch for a second non-AI layoff rationale** — new watch item (h); it converts today's counter-instance into a synthesis claim about narrative choice. (b) **OKX 8% + Kraken lapse 07-31** is now the nearest dated checkpoint (11 days) — watch lapse-vs-extend and for a 7th capture-panel entrant. (c) First named post-deadline NCA marketing-side action — day-19 silence; watch NCA sites directly rather than aggregate search, since ESMA has confirmed enforcement is devolved. (d) **Agency panel 35 days stale — escalation carried; still the highest-value unblock.** (e) Kraken CGMO Mayur Gupta remains the highest-probability next class-4 source; the OKX/Rafique JS-render retry is available on a run with spare budget. (f) Friday 07-24 is the next inbound-nomination check. (g) Coinbase brand-rebuild signal holds at n=1.

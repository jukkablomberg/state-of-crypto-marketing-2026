# Corpus-assembly daily run — 2026-07-18 (day 17 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated). First run of 2026-07-18. Follows a clean single-fire 07-17 run — cadence normalising after the 07-14/07-15 no-fire gap and the 07-16 double-fire (carried watch item (e)).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Dedup baseline read before searching:** prior runs 2026-07-17 back to 2026-06-30; `regulator-filings/` (Binance EU-exit event-chain, ESMA/AMF/FCA filings); `marketing-campaigns/mica-competitive-capture-2026-06.md` (six-firm capture panel); `operator-statements/`; `layoff-tracker/2026-layoff-tracker.csv` (8 marketing-scope + adjacency rows); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

---

## Headline result

**Day 17 post-deadline. The 15-day class-1 idempotency streak BREAKS with a genuine net-new corpus row: `daily-corpus-sync.py` added 1 job posting — Coinbase, Creative Director (Director/brand seniority), Remote-Canada, posted 2026-07-17, greenhouse ATS, URL-verified. This creates `corpus/job-postings/coinbase.csv` — a new per-firm file, and the first genuine class-1 addition since Phantom Head of Brand Creative (07-02).** The feed is fully current (`scan_metadata.scan_date: 2026-07-18`, 2,298 jobs fetched, `new_count: 2`, no fetch-error mass-signature). Classes 3/4/5 all net-zero net-new: day-17 named-enforcement silence holds (only ESMA wind-down / "cease marketing and solicitation", CySEC AML/sanctions supervisory activity, the recurring out-of-window FCA→HTX Feb-2026 case, and the June-2025 nine-regulator finfluencer week-of-action — no named marketing-side promotion case against a tracked CASP); class-4 drought persists (Kraken CGMO Mayur Gupta = standing LinkedIn profile, no in-window verbatim; Bybit CEO Zhou = CEO and out-of-window; Bitget CMO = non-cohort; Binance Conlan→Chen and Crypto.com Kalifowitz departures already captured); class-5 tracker holds at 8 rows. Capture panel unchanged at six firms, no 7th entrant, Ripple licence-only; next lifecycle checkpoint **OKX 8% + Kraken lapse 07-31**. Agency panel now **33 days stale** (`trend-data.json` 06-15) — escalation hardens further.

1. **Class-1 breaks idempotency with a real row (the material result of this run).** Coinbase Creative Director, `date_posted: 2026-07-17`, jurisdiction Remote-Canada, seniority Director/brand, source `https://www.coinbase.com/careers/positions/8054862?gh_jid=8054862` (greenhouse, `url_verified=True`). Theme-1 relevance: Coinbase is the Tier-1 firm whose May-2026 Armstrong memo publicly named "AI-native pods" as the new operating unit alongside a −14% cut — a **brand-side Director** requisition posted 10 weeks later is the first public class-1 signal of that firm rebuilding senior creative capacity post-restructure. Recorded as a corpus row, not yet as a synthesis claim (n=1).
2. **Day-17 named-enforcement silence holds (class 3 absence-as-data).** Seventeen days past the July-1 transitional-period end, still **no named marketing-side NCA enforcement case** (BaFin/AMF/CONSOB/AFM/CySEC/ESMA) on the public record against a tracked-cohort firm. Register-first, cases-later now extends to a seventeen-day pattern.
3. **Capture panel + campaign-lifecycle unchanged.** No 7th capture-panel entrant; Ripple still licence-only. No lifecycle event in the 07-17→07-18 window; next checkpoint is **OKX 8% + Kraken lapse 07-31**.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 1 (idempotency streak broken — genuine new marketing role).** Source A `scan_metadata.scan_date` **2026-07-18** (feed current, no arrears). Metadata healthy: **2,298 jobs fetched**, `new_count: 2`, no fetch-error mass-signature. Printed summary: `job postings ADDED: 1  firms: ['Coinbase']`; `of which via Chrome inbox: 0`.

New row written to **`corpus/job-postings/coinbase.csv`** (new file):
```
2026-07-17,Creative Director,Remote - Canada,Director / brand,
https://www.coinbase.com/careers/positions/8054862?gh_jid=8054862,2026-07-18,
ATS=greenhouse; url_verified=True; src=open-positions.json 2026-07-18
```
Of the feed's `new_count: 2`, one role mapped to a Stratum 1–4 tracked-firm marketing/growth seat (the above) and one did not. `_absence.csv` regenerated honestly to **Aave (Lever-404) + 5 proprietary needs-chrome firms** (Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys), `as_of=2026-07-18`. `_chrome-queue.csv` idempotent `as_of=2026-07-18` re-stamp (proprietary list unchanged: Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys pending-chrome; Solana ingested). `git diff` confirms both `_` files are date-only re-stamps, byte-identical to 07-17 apart from `as_of`. Standing `scan_metadata` cross-check guard holds.

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0.** Source B `trend-data.json` `lastUpdated` **2026-06-15 — 33rd consecutive day unchanged.** Escalation to Jukka stands and hardens further: the agency panel is now over a month stale and squarely inside the Phase-2 synthesis window; upstream NorthPoint `trend-data.json` needs a refresh (not fixable from this loop). Matrix idempotent: 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots written (idempotent).

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new named enforcement entries: 0.** Day-17 post-deadline sweep (named enforcement, misleading-promotion, financial-promotion fine queries across EU NCAs + FCA/MAS/VARA) returned only: ESMA's orderly-wind-down / "cease marketing and solicitation" expectation for unauthorised CASPs (already captured, `esma-mica-transitional-period-end-2026-06.md`); CySEC supervisory-activity reporting (≈600 on-site/off-site inspections in 2025; €2.3M in AML/sanctions fines Jan-2026 — **not marketing-side**, and the fines are AML/sanctions-scope); AMF unlicensed-operator blacklist posture; the recurring **FCA→HTX** financial-promotion action (High Court proceedings 21 Oct 2025; FCA statement 10 Feb 2026 that HTX continued publishing promotions in breach across TikTok/X/Facebook/Instagram/YouTube — out-of-window UK case, already captured); and the **June-2025 nine-regulator finfluencer week-of-action** (out-of-window, finfluencer/entity-level). Also noted (not a case): standing MiCA administrative-penalty framing and platform-side ad-policy changes (X paid-promotion disclosure rules 2026; Meta/Google crypto ad policies) — **platform policy is not regulator enforcement** and does not meet the class-3 bar. None meets the class-3 named-enforcement bar. **Absence-as-data: the post-deadline named-enforcement silence is now seventeen days long** — register-first, cases-later.

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new qualifying: 0.** CMO / Head-of-Marketing / Head-of-Brand / Head-of-Growth sweep surfaced only non-qualifying material: **Kraken's Mayur Gupta** (Chief Growth & Marketing Officer — a *qualifying role at a tracked firm*, but what surfaced is a standing LinkedIn profile/role description, **no in-window dated verbatim statement**, so it fails the class-4 bar of quote + URL + date); **Bybit CEO Ben Zhou** on MiCA-plus-MiFID/EMI licensing (April 2026 — CEO, not a marketing operator, and out-of-window); **Bitget CMO** on exchanges evolving beyond trading (Bitget is **not in the tracked cohort**); and the already-captured leadership departures — Binance CMO **Rachel Conlan** (left 15 June; **Eowyn Chen**, ex-Trust Wallet CEO, interim CMO) and Crypto.com CMO **Steven Kalifowitz** (stepped down effective 30 June after ~6 years, continuing as advisor to the CEO). No in-window verbatim statement by a qualifying marketing operator at a tracked firm. The class-4 drought since the May CMO churn persists and remains a Theme-1 datum (interim/empty marketing seats at Binance and Crypto.com). **Watch item added:** Mayur Gupta (Kraken CGMO) is the highest-probability next qualifying class-4 source — a dated interview/podcast/conference appearance from him would clear the bar immediately.

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0.** July-window searches re-surfaced only captured items via aggregator round-ups (Coinbase −14% / ~500–700; Gemini −30% with headcount now ≈445 after a $582M loss; Kraken ~30% with AI-pivot framing; Crypto.com −12%; "5,700+ crypto layoffs in 2026" round-ups) — no net-new marketing-team headcount cut at a tracked firm, and none of the surfaced cuts names marketing/growth as the affected function. Tracker holds at 8 marketing-scope + adjacency rows. The AI-as-rationale framing continues to dominate stated rationales across Gemini/Kraken/Coinbase — already a captured Theme-5 pattern, no new row.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-18 section; last-updated bumped). **One genuine shift this run:** the class-1 idempotency streak breaks with the Coinbase Creative Director row — the first Tier-1 senior brand-side requisition captured post-restructure, and a Theme-1/Theme-5 datapoint worth watching for a second instance before it becomes a synthesis claim. Methodology guard stands: cross-check any future job-postings "absence spike" against `scan_metadata` (`total_jobs_fetched` + `fetch_errors`) before treating it as data.

---

## Watch items (carried, unchanged except where noted)
- **(a) Binance re-file jurisdiction** — still France-**reported**-only; firm names no jurisdiction formally; captured in `regulator-filings/binance-mica-eu-exit-2026-06.md`. Unchanged.
- **(b) First named post-deadline NCA marketing-side action** — day-17 silence logged; ESMA non-compliant register + AMF/BaFin unauthorised-entity instruments remain the leading indicators; no named marketing-side case yet.
- **(c) Capture panel** — six firms, no 7th entrant this run; Ripple still licence-only. **Lifecycle sequence: Bitpanda lapsed 07-05 → Coinbase lapsed 07-13 → OKX + Kraken lapse 07-31.**
- **(d) Agency panel staleness** — `trend-data.json` **33 days stale** (06-15); escalation to Jukka hardened (well inside Phase-2 synthesis window).
- **(e) Loop cadence** — 07-17 and 07-18 each fired once and cleanly; the 07-14/07-15 gap + 07-16 double-fire now looks like an isolated irregularity. Downgraded to passive watch.
- **(f) Friday nomination cadence** — README reads inbound nominations (`hello@northpoint.fi`) every Friday; **today is Saturday 07-18, not a nomination day**. No `inbound-nominations.md` exists yet. Next check Friday 07-24.
- **(g) NEW — Coinbase brand-rebuild signal** — watch for a second Coinbase (or other Tier-1) senior brand/creative requisition. One row is a datapoint; two would support a Theme-5 "post-AI-pod rebuild" synthesis claim.

## Searches / fetches run (audit trail)
1. `MiCA crypto marketing enforcement action July 2026 BaFin AMF CONSOB CySEC ESMA named CASP misleading promotion fine` → ESMA wind-down/"cease marketing and solicitation" + CySEC supervisory activity (600 inspections 2025; €2.3M AML/sanctions fines, not marketing-side) + AMF unlicensed-operator posture + MiCA truth-in-marketing framework; 0 net-new named marketing-side case (day-17 silence).
2. `crypto exchange CMO "head of marketing" "head of brand" "head of growth" interview July 2026 MiCA Coinbase Kraken OKX Bitpanda Bybit` → Kraken CGMO Mayur Gupta (qualifying role, profile only — no in-window verbatim) + Bybit CEO Zhou (CEO, out-of-window) + Bitget CMO (non-cohort) + captured Binance Conlan→Chen and Crypto.com Kalifowitz departures; 0 qualifying class-4 statement.
3. `crypto exchange marketing growth team layoffs July 2026 Coinbase Kraken Gemini Bitpanda headcount cut` → captured items + aggregator round-ups only (Coinbase −14%/~500, Gemini −30%/≈445 headcount/$582M, Kraken ~30% AI-pivot, Crypto.com −12%, 5,700+ 2026 round-ups); 0 net-new tracked-firm marketing-scope layoff; no Bitpanda layoff signal.
4. `crypto financial promotion enforcement fine misleading advertising exchange July 2026 FCA CONSOB AFM VARA MAS named action` → recurring FCA→HTX (Oct-2025 High Court / Feb-2026 statement, out-of-window, captured) + June-2025 nine-regulator finfluencer week-of-action (out-of-window) + penalty-framework material (VARA AED 100k–5M range; FCA "fair, clear and not misleading" standard; FCA finding of potential violations in 70% of crypto communications) + platform ad-policy changes (X/Meta/Google — not regulator enforcement); 0 net-new named marketing-side EU case.

## Net-new / changed this run
- `corpus/job-postings/coinbase.csv` (**NEW FILE — 1 genuine net-new class-1 row**: Coinbase Creative Director, 2026-07-17, greenhouse, URL-verified)
- `corpus/job-postings/_absence.csv` (honest regeneration, `as_of=2026-07-18` — Aave Lever-404 + 5 proprietary; feed healthy/current)
- `corpus/job-postings/_chrome-queue.csv` (idempotent `as_of=2026-07-18` re-stamp — proprietary firm list unchanged)
- `findings/longitudinal-2026-06.md` (2026-07-18 section: idempotency-streak break + Coinbase brand-rebuild signal; last-updated bumped)
- `corpus/weekly-runs/2026-07-18-corpus-run.md` (this record)

## Recommendation for next run
(a) **Watch for a second Tier-1 senior brand/creative requisition** — today's Coinbase Creative Director row is n=1; a second instance converts it from datapoint to Theme-5 synthesis claim about post-restructure brand rebuilding. (b) First named post-deadline NCA marketing-side action — day-17 silence logged; watch for the transition from register/blacklist to a named misleading-promotion case. (c) **OKX 8% + Kraken (07-31)** are the next campaign-lifecycle checkpoints; watch lapse-vs-extend and for a 7th capture entrant (Ripple still licence-only). (d) **Kraken CGMO Mayur Gupta is the highest-probability next class-4 source** — a dated interview/podcast/stage appearance clears the bar; CEO-level MiCA commentary keeps surfacing but never meets the marketing-operator bar. (e) **Agency panel 33 days stale — escalation to Jukka carried and hardened** (upstream `trend-data.json` refresh needed inside July synthesis; the single highest-value unblock available to this report right now). (f) Friday 07-24 is the next inbound-nomination check.

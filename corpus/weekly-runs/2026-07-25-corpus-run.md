# Corpus-assembly daily run — 2026-07-25 (day 24 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired on cadence the morning after 2026-07-24. Single fire.
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Dedup baseline read before searching:** run records 2026-07-24 back to 2026-06-20; `regulator-filings/` (ESMA/AMF/FCA/Binance-EU-exit chain); `operator-statements/` (sport-sponsorship-reset cluster); `marketing-campaigns/mica-competitive-capture-2026-06.md`; `layoff-tracker/2026-layoff-tracker.csv` (11 rows pre-run); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`. Repo-wide greps run for `gupta`, `incrypted`, `ferdon`, `rouch`, `ukraine`, `natively AI`, `mica-enforcement-begins` to confirm net-newness before writing.
**Operating-context note:** the staged synthesis-first task prompt (`../../../STAGED-corpus-task-prompt.md`) remains **unapproved and unapplied**, so this run correctly executes as full six-class corpus assembly. Today's result is a strong argument for keeping the collection lane alive — see Headline.

---

## Headline result

**Day 24 post-deadline. This run breaks the class-4 drought with the single most valuable operator statement in the corpus to date — and it does so by finding the source 24 prior runs looked for and missed.** A long-form Incrypted interview with **Mayur Gupta, Kraken's Chief Growth & Marketing Officer**, published **2026-05-19**, supplies dated verbatim quotes in which he (i) names an AI-native marketing operating model at a **second** Tier-1 exchange — *"we are now pushing towards being a natively AI growth engine… engineers are designing product ideas, marketers are shipping products"* — two weeks after Armstrong's Coinbase memo, taking the **Theme-1 spine from n=1 to n=2**; (ii) explicitly repudiates the KOL/agency launch playbook the tracked 18-agency panel sells — *"partner with local KOLs, run a tournament, claim the win. Ukrainian users see right through that"*; and (iii) states the organic-growth thesis **on a date**, which makes the paid/organic tension opened by watch item (i) on 07-24 a **datable sequence** rather than an inference. A second net-new firm-side artifact was also captured: **Kraken Institutional's 2026-06-23 MiCA post**, the institutional/B2B counterpart to the already-captured retail capture campaigns. Class 1 idempotent-against-a-healthy-feed (0 adds; the feed's one new role is Anthropic, non-cohort) — **but the Chrome lane surfaced a first-ever Binance marketing role that falls below the corpus bar**, which is itself a class-1 finding. Class 2 unchanged (`trend-data.json` still 06-15 — 40th day; stable-by-decision, not re-escalated). Class 3 net-zero: **day-24 named-enforcement silence holds**. Class 5 net-zero: no new 2026 marketing-team contraction; the surfaced 07-24 Coinbase item is an executive resignation, not a layoff round.

1. **Class 4 breaks — and it is the item the corpus has been missing (the material result).** New file `corpus/operator-statements/kraken-gupta-growth-operating-model-2026-05.md`. Full analysis in that file; the three load-bearing captures are the AI-native-growth-engine quote (Theme 1/2, n=2 instance), the KOL-playbook repudiation (Theme 3, first firm-side senior-operator attack on the agency panel's core service), and the dated organic claim (Theme 2). **Honest window qualification recorded in the file:** 2026-05-19 is in-window per methodology (post-Dec-2024) but **pre-deadline** — the report must not imply it is a post-deadline statement. **Provenance caveats also recorded, not suppressed:** the publishing outlet operates a commercial marketing/KOL arm, and the page carries a Kraken *affiliate referral link* rather than a plain kraken.com link — so whether this is an organic editorial or a partner placement cannot be determined publicly. Materially ironic given the KOL quote, and flagged for a footnote if the quote is cited.
2. **Second net-new firm-side artifact — the institutional half of the MiCA capture play.** New file `corpus/marketing-campaigns/kraken-institutional-mica-counterparty-2026-06.md`. Kraken's own blog, **2026-06-23**, sells the MiCA licence to institutions as a **counterparty-risk / audit-defensibility** argument ("reaches CCO sign-off, LP reporting, and audit defensibility"), names competitors' regulatory status in promotional copy with a visible compliance hedge (*"Binance's MiCA application in Greece has **reportedly** faced rejection, **a characterization the company disputes**"*), and carries a fully visible gate-stack (~600 words of entity-level disclosure). Pairs with the existing retail-side capture file to show the licence monetised across two buyer tiers by two different mechanisms. **Absence-as-data pairing:** the corporate channel argued MiCA in detail on 06-23 while the CGMO discussed a full market entry on 05-19 without naming MiCA once.
3. **Day-24 named-enforcement silence holds (class 3 absence-as-data).** Twenty-four days past the transitional-period end, still no named marketing-side NCA enforcement case against a tracked-cohort firm. Three separate sweeps this run returned only framework/guide material and already-captured out-of-window items (the FCA→HTX High Court action, Feb 2026). Register-first, cases-later is now a twenty-four-day pattern.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0 — genuine idempotency against a healthy, current feed.** Printed summary:
```
date: 2026-07-25
source A (jobs)   scan_date: 2026-07-25
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```
**Standing `scan_metadata` cross-check guard applied and satisfied:** `scanned_at_utc 2026-07-24T22:45:36Z`, `scan_date 2026-07-25`, `companies_scanned 147` (87 API / 60 chrome-pending), `total_jobs_fetched 2110`, `total_jobs_after_filter 29`, `new_count 1`, `still_open_count 28`, `url_verification_enabled true`, `url_verification_dropped 0`, `fetch_errors 6` (Wormhole, **Aave**, Injective, Bitwise, Chainlink, Elliptic — identical set to 07-23/07-24; only Aave is tracked, and its error remains the long-standing Lever-`aave` HTTP-404, not a new outage). No mass-fetch-error signature. **The feed's single new role is `Anthropic — "Brand Marketing Lead, Enterprise"` (Greenhouse, posted 07-24) — non-cohort, correctly excluded.** Kraken's two 07-23 Director-Paid-Marketing rows are now in `still_open_from_prior_scans`, consistent with yesterday's capture being complete.

`_absence.csv` and `_chrome-queue.csv` are **date-only re-stamps** (2026-07-24 → 2026-07-25); `git diff` confirms 14 insertions / 14 deletions with byte-identical content otherwise — no data rows changed.

**Class-1 finding (new, and it is absence-as-data in the strict sense): the Chrome lane surfaced a first-ever Binance marketing role, and it falls below the corpus bar.** `open-positions.json → chrome_supplementary.new_since_last_scan` contains **Binance — "Global Product Marketing Lead" (UAE, Dubai), Marketing dept, `first_seen 2026-07-25`, `url_verified: true` via chrome_navigation**. It was **not** ingested, and correctly so: `posted_at` is **null** and the URL is the generic board (`https://www.binance.com/en/careers/job-openings`), not a per-posting permalink — so it fails the corpus requirements of a posting date and a primary per-item source URL. **Binance therefore stays in `_absence.csv`.** This is the bounded residual gap named in `scripts/README.md` behaving exactly as documented: the Chrome lane can *see* proprietary-ATS roles but does not yet emit corpus-grade rows. Two consequences worth recording: (a) the absence panel's Binance entry is now demonstrably an *instrumentation* absence, not a *firm-silence* absence — a distinction the report must not blur; (b) closing the gap needs the Chrome lane to capture per-posting permalinks + dates into `corpus/job-postings/_chrome-inbox.json` (the existing hand-curated Solana Foundation rows are the working template). Also surfaced and excluded: **Ripple — "Director, Corporate & Product Communications"** (Tier 2, not in the Stratum 1–4 cohort; Ripple remains licence-only per watch item (c)).

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0.** Source B `trend-data.json` `lastUpdated` **2026-06-15 — 40th consecutive day unchanged.** Matrix idempotent: 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots written (idempotent). **NOT re-escalated** — per the 07-10 Path-2 decision (Jukka) this is a deliberate snapshot: Theme 3 cites the panel as-of 2026-06-15 by design. Recorded as a stable known state.

**Note for Theme 3, however:** today's class-4 capture puts real pressure on the agency panel's positioning, and it does so with a *May 2026* quote against a *June 15, 2026* panel snapshot — i.e. the two are contemporaneous. The staleness that would have weakened this pairing does not, in this instance, bite.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new named enforcement entries: 0.** Three sweeps run (see audit trail below). What surfaced:
- **Framework/guide material only** — MiCA Art. 7/9/66 marketing-communication obligations, the up-to-**12.5%-of-global-turnover** penalty ceiling for serious violations, and the ESMA April-2026 supervisory statement calling on all 27 NCAs to apply uniform enforcement standards. All already captured or below the class-3 bar (no named firm, no marketing-side case).
- **FCA → HTX High Court action** recurred across results (Freeths, DLA Piper, "first enforcement action under the UK crypto marketing regime", Feb 2026) — **already captured, out-of-window UK case.** Not re-added.
- **CSSF (Luxembourg)** published a transition-period-ended notice (2026-07) — a framework notice, not an enforcement action; below the bar.
- No net-new named marketing-side action from BaFin, AMF, CONSOB, AFM, CySEC, MAS or VARA.

**Absence-as-data: the post-deadline named-enforcement silence is now twenty-four days long.** The mechanism remains as recorded on 07-20: unauthorised CASPs must cease marketing and solicitation immediately (ESMA `ESMA75-113276571-1710`), but policing is devolved to 27 NCAs — a centralised marketing-enforcement action was never the mechanism. Cases, when they come, arrive from NCAs one at a time. **Standing methodological caution restated:** aggregate search is a poor instrument for this class; NCA sites should be read directly (watch item (b)).

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new qualifying: 1 — the drought breaks.** Written to `corpus/operator-statements/kraken-gupta-growth-operating-model-2026-05.md`.

| field | value |
|---|---|
| speaker / role | **Mayur Gupta — Chief Growth & Marketing Officer, Kraken** (role at time of statement) |
| firm / stratum | Kraken — **Stratum 1** (Tier-1, MiCA-authorised via Central Bank of Ireland) |
| date published | **2026-05-19** (in-window per methodology; **pre-deadline** — flagged explicitly) |
| format | long-form written interview, Incrypted, by Oleksandr Pishenin |
| URL | `https://incrypted.com/en/krakens-chief-growth-officer-depth-interview/` |
| date verification | three independent points on the page — byline stamp, closing "Published: 19.05.2026", `/2026/05/` image path |
| themes | 1 (function shape) · 2 (AI in stack / paid-vs-organic) · 3 (KOL/agency playbook) · 4 (regulatory posture, by absence) |

**Why 24 prior runs missed it:** every prior sweep queried Gupta against **July 2026** and against podcast/conference surfaces, and kept landing on the 20VC page (Apr 25, 2025) and undated aggregator summaries of the "80% organic" line. The qualifying primary is a **May 2026 written interview in a regional Eastern-European outlet** — outside both the date window the queries assumed and the source inventory listed in `methodology.md` §4 (which names eight English-language podcasts and no regional written media). **Methodology consequence, recorded as a standing guard:** class-4 sweeps should query the **full in-window range (Dec 2024 →)**, not just the current month, and should include **regional/non-English crypto media** as a surface. A drought declared from an English-podcast-shaped query set is a measurement artifact, not a finding — and this corpus carried that artifact for weeks.

Also checked and **not** added this run: **Coinbase CMO Cat Ferdon** long-term-strategy framing (surfaced only via a Phemex aggregator write-up; no dated primary located — carried, unchanged); **Kate Rouch** (predecessor, profile-only); **OKX CMO Haider Rafique** (The Drum 2025-03-11 — out of window; Adweek "rebuild crypto trust" piece undated in results — carried as the JS-render retry candidate, not retried); **Erald Ghoos** (OKX Europe GM — regional GM, not a senior *marketing* operator; excluded consistently with the 06-29 and 06-30 rulings).

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0. Tracker holds at 11.** Sweeps for July-24/25 announcements surfaced:
- **Coinbase — Lawrence Brock (Chief People Officer) resigned 2026-07-24**, eleven weeks after the 700-role (−14%) May cut he led. **Not a layoff row** — an executive departure, not a workforce reduction, and CPO is not a marketing seat. **Not added to the tracker.** Recorded here because it fits an existing Theme-1/5 pattern the corpus is already tracking: *senior-leadership exits trailing the contraction they executed* (cf. Crypto.com CMO Kalifowitz exiting six weeks after the March cut; BitMEX CGO exiting before the wind-down). Two of those three are people-side/marketing-side leaders. Carried as new watch item (j) rather than logged as a class-5 row, because the pattern is about *who leaves after the cut*, not the cut itself. **Reporting caveat:** the surfaced write-ups give conflicting dates for the same resignation (2026-07-24 vs an "August 17, 2026" effective/step-down date, which is in the future relative to this run) — **no date is entered into the corpus** until a primary source (Coinbase filing or own-channel statement) is read. Flagged, not recorded.
- **Exodus (07-17), Polygon Labs (07-16), BitMEX (07-23), Crypto.com (03), Gemini, Algorand, Coinbase (05-05), Messari** — all already captured or previously assessed. No net-new.

**Standing Theme-5 finding unchanged and worth restating:** across all **11** tracker rows, **not one names marketing as the affected function.** Every marketing-specific read in the corpus is an inference from a subsequent exit or from press attribution. That absence is the finding.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-25 section). **Three shifts:** (i) **Theme 1 goes from n=1 to n=2** — a second Tier-1 exchange, via its own CGMO, names an AI-native marketing operating model two weeks after Coinbase's CEO named one; the claim upgrades from anecdote to category shift. (ii) **Theme 3 gains a firm-side attack on the agency panel's core product** — a Tier-1 CGMO names "partner with local KOLs, run a tournament, claim the win" as the mistake, contemporaneous with the panel snapshot. (iii) **A measurement-artifact correction** — the class-4 "drought" was partly an artifact of month-scoped, English-podcast-shaped queries; the guard is now written down. Methodology guards applied and satisfied this run: `scan_metadata` cross-check before treating class-1 counts as signal (done); primary-source date verification before entry (done, three-point on the Gupta page); refusal to enter a conflicting-date item (done, Coinbase CPO); verbatim reproduction without silent correction (done, two published typos preserved).

---

## Watch items
- **(a) Binance re-file jurisdiction** — still France-**reported**-only; firm names no jurisdiction formally. Unchanged.
- **(b) First named post-deadline NCA marketing-side action** — **day-24 silence logged.** Read NCA sites directly; aggregate search is the wrong instrument.
- **(c) Capture panel** — six firms, no 7th entrant; Ripple still licence-only (and its Director-Comms req surfaced today is non-cohort). **Nearest lifecycle checkpoint: OKX 8% + Kraken lapse 07-31 — 6 days out.**
- **(d) Agency panel staleness — 40 days** (`trend-data.json` 06-15). Stable-by-decision, **not** a blocker, **not** re-escalated. Note that today's May-2026 class-4 capture is contemporaneous with the June-15 snapshot, so the pairing is unaffected.
- **(e) Loop cadence** — 07-25 fired cleanly on cadence after a clean 07-24. Scheduler health check carried (07-21/07-22 gap + 07-24 duplicate trigger still in recent history).
- **(f) Friday nomination cadence** — 07-25 is Saturday; last check 07-24 (no `inbound-nominations.md` exists). Next check Friday **07-31**.
- **(g) Coinbase brand-rebuild signal** — holds at **n=1** (Creative Director, 07-17). Not advanced.
- **(h) Layoff-rationale divergence** — unchanged; still needs a second **tracked** firm with a non-AI **layoff** rationale. Polygon (tracked) + Exodus/BitMEX (perimeter) do not satisfy it.
- **(i) Kraken paid-media build-out — SHARPENED, still open.** The organic-first thesis is now **dated** (05-19) and the paid-Director double-hire is dated (07-23), so the sequence is factual. What remains open is the reconciliation: **Gupta has not publicly addressed the paid build-out.** That specific statement is still the highest-value outstanding class-4 capture. Also still open: the JD bodies' AI-tooling requirements (Theme 2).
- **(j) NEW — senior-leader exits trailing the contraction they executed.** Crypto.com CMO Kalifowitz (~6 weeks after the March cut) · BitMEX CGO Polansky (before the wind-down) · Coinbase CPO Brock (reported 11 weeks after the May cut, **date unverified — not in corpus**). Watch for a fourth instance and for whether marketing/people-side leaders are over-represented. Requires a primary source before any of it is written as a finding.
- **(k) NEW — Chrome-lane instrumentation gap is now demonstrable.** Binance's "Global Product Marketing Lead" (Dubai) was *seen* by the Chrome lane on 07-25 and *excluded* for want of a posting date and per-posting permalink. The absence panel's Binance entry is therefore an **instrumentation** absence, not a **firm-silence** absence — the report must not conflate them. Closing it = Chrome lane emits permalink+date rows into `_chrome-inbox.json`.

## Searches / fetches run (audit trail)
1. `python3 scripts/daily-corpus-sync.py --sales ../../northpoint/sales-funnel` → classes 1+2 deterministic; **0 net-new both**; printed summary captured above.
2. Direct read of `prospects/open-positions.json` (`scan_metadata`, `fetch_errors`, `new_since_last_scan`, `chrome_supplementary`, `still_open_from_prior_scans`) → feed-health guard satisfied; **surfaced the excluded Binance + Ripple Chrome-lane items** (finding (k)).
3. WebSearch `MiCA marketing communications enforcement action July 2026 BaFin AMF CONSOB AFM CySEC named crypto exchange misleading promotion` → framework/guide material only; **0 net-new class-3**.
4. WebSearch `"financial promotion" OR "marketing communication" crypto enforcement fine July 2026 national competent authority CASP misleading advertising` → Art. 7/9/66 obligations, 12.5%-turnover ceiling, ESMA April-2026 statement, recurring out-of-window FCA→HTX; **0 net-new class-3**.
5. WebSearch `Kraken Mayur Gupta paid marketing organic growth statement July 2026` → surfaced the **Incrypted interview** (the material find) alongside the known out-of-window 20VC page.
6. `web_fetch` Incrypted Gupta interview → **primary verification**: date 2026-05-19 (three-point), role, verbatim quotes, provenance caveats (affiliate referral link, outlet's commercial marketing arm). **→ ADDED as class 4.**
7. WebSearch `crypto CMO "head of brand" OR "head of growth" interview July 2026 Coinbase OKX Bitpanda Bitstamp marketing strategy` → Rafique (out of window), Ferdon/Rouch (aggregator/profile-only); **0 further class-4**.
8. WebSearch `crypto marketing team layoffs July 2026 exchange headcount cut growth team` → all already captured (Crypto.com, Exodus, Gemini, Algorand, OP Labs); **0 net-new class-5**.
9. WebSearch `crypto company layoffs announced July 24 2026 OR July 25 2026 workforce reduction` → surfaced the **Coinbase CPO resignation** (not a layoff; conflicting dates → **not entered**); **0 net-new class-5**.
10. `web_fetch` Kraken Institutional MiCA post → **primary verification** of `published_time 2026-06-23`, verbatim positioning copy, named-competitor hedge, disclosure stack. **→ ADDED as firm-side marketing artifact.**
11. Repo-wide dedup greps (`gupta`, `incrypted`, `ferdon`, `rouch`, `ukraine`, `natively AI`, `mica-enforcement-begins`) → both additions confirmed net-new before writing.

## Net-new / changed this run
- `corpus/operator-statements/kraken-gupta-growth-operating-model-2026-05.md` (**NEW FILE — the material result; 1 net-new class-4 capture**, Kraken CGMO Mayur Gupta, 2026-05-19, verbatim + URL + speaker + role + date, window and provenance caveats recorded)
- `corpus/marketing-campaigns/kraken-institutional-mica-counterparty-2026-06.md` (**NEW FILE — 1 net-new firm-side marketing artifact**, Kraken Institutional MiCA counterparty-risk post, 2026-06-23)
- `corpus/job-postings/_absence.csv` (date-only re-stamp `as_of=2026-07-25`; content byte-identical — Aave Lever-404 + 5 proprietary needs-chrome firms unchanged)
- `corpus/job-postings/_chrome-queue.csv` (date-only re-stamp `as_of=2026-07-25`; proprietary firm list unchanged)
- `findings/longitudinal-2026-06.md` (2026-07-25 section: Theme-1 n=1→n=2, Theme-3 firm-side attack on the agency playbook, class-4 measurement-artifact correction)
- `corpus/weekly-runs/2026-07-25-corpus-run.md` (this record)
- **Not changed:** `layoff-tracker/2026-layoff-tracker.csv` (holds at 11 — the Coinbase CPO item is an exec departure with conflicting dates, deliberately not entered); `agency-overlap-matrix.csv` + `agency-claims/*` (idempotent); `job-postings/*.csv` data rows (0 adds)

## Recommendation for next run
(a) **Re-run the class-4 sweep with the corrected query shape** — full in-window range (Dec 2024 →) rather than current-month, and include regional/non-English crypto media (Incrypted, BeInCrypto regional editions, Cointelegraph language editions, DACH/IT/ES outlets). Today proves the drought was partly a measurement artifact; there are likely **more** qualifying statements already published and unfound. Highest-value action available to this report right now. Candidate targets in priority order: OKX/Rafique, Coinbase/Ferdon, Bitpanda, Bitstamp, Relai/Bábics (DACH+IT posting velocity makes regional media likely), Sui Foundation.
(b) **Watch item (i) is the one to close** — an in-window Gupta statement reconciling the paid-Director double-hire with the dated organic thesis. Kraken remains triple-loaded.
(c) **OKX 8% + Kraken lapse 07-31 is the nearest dated checkpoint (6 days)** — watch lapse-vs-extend and for a 7th capture-panel entrant.
(d) **Consider closing the Chrome-lane gap (finding (k))** — it is now demonstrable, bounded, and it is the difference between an instrumentation absence and a firm-silence absence for Binance/Bybit/HTX/KuCoin/ConsenSys. Not fixable from inside this loop; the fix is upstream in the Chrome lane's output schema. Worth one `queues/needs-jukka.md` row if it is not already covered.
(e) Class 3: day-24 silence — read NCA sites directly rather than aggregate search.
(f) Class 5: verify the Coinbase CPO departure date against a primary source before it is used anywhere; watch item (j) needs a fourth instance.
(g) Agency panel stable-by-decision (06-15) — do **not** re-escalate.
(h) Next nomination check Friday **07-31**.
**Operating-context flag for Jukka:** the staged synthesis-first prompt is still unapplied. Today is the strongest evidence yet that the collection lane is not exhausted — it produced the corpus's best class-4 item and a methodology correction on day 24 of a supposed drought. Recommend the staged prompt be revised to run **synthesis-first with a retained collection pass**, rather than replacing collection outright.

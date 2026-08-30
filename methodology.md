# State of Crypto Marketing 2026 — Methodology

> **Public-source synthesis, not interview-based research.** The corpus is built from primary sources anyone can independently verify. No interviewees, no anonymous quotes, no off-the-record reads. The visibility filter — what the firm has shipped publicly — is itself the analysis.

## Source corpus design

The corpus is anchored to six source classes, gathered continuously between now and ship date.

### 1. Job postings, by jurisdiction, by month
- **Capture window:** rolling 12 months ending August 31, 2026.
- **Firms tracked:** see `./tracked-firms.md` (**27 named firms** across exchanges, L1/L2 foundations, wallets, CASP-licensed firms; the "~30" of the report's framing language is the target, not the count).
- **Sources:** firm careers pages, LinkedIn job postings, web3.career, CryptoJobsList.
- **What we extract:** seniority, function (brand / growth / PMM / community / agency-mgmt / regulatory-comms), geography, posting date, time-to-fill, JD-stated AI-tooling requirements.
- **Storage:** `./corpus/job-postings/` — one CSV per firm per month.

#### ⚠ What `_absence.csv` does and does not mean (recorded 2026-08-30)

`corpus/job-postings/_absence.csv` lists tracked firms the scan **could not reach**. It is a record of **instrument reach**, not of firm behaviour, and the two must never be conflated:

| Statement | Supported by `_absence.csv`? |
|---|---|
| "The scanner had no API route to this firm's ATS on this date." | 🟢 **Yes.** This is exactly what the file records. |
| "This firm posted no marketing roles." | 🔴 **No.** Never. Binance, Bybit, HTX and KuCoin run proprietary ATSs; Aave's Lever board 404s. Their postings are *unobserved*, not absent. |
| "This firm is publicly silent on the marketing function." | 🔴 **No.** That is a class-3/4 claim and needs class-3/4 evidence. |

Two further limits, both recorded against real incidents rather than in the abstract:

1. **The panel has never contained an absence in the second sense.** Every firm that has ever appeared in it is there because of a proprietary ATS or an HTTP error — i.e. because of *our* reach. As of 2026-08-30 its membership has been the same five firms (Aave, Binance ×2, Bybit, HTX, KuCoin) on every run since the cohort expansion.
2. **The file's `as_of` column is written from the sync's run clock, not from the upstream `scan_date`.** On 2026-08-29 the upstream ATS scan was frozen and `_absence.csv` still rolled its `as_of` to `2026-08-29` — asserting an observation that no 2026-08-29 scan produced. The feed-health guard refused the *absence claim* that day, but the file itself was not corrected. **Generalised rule: any corpus file carrying a date must date itself from the artifact observed, not from the run that wrote it.** Until the sync is patched, read `as_of` against `_feed-fingerprint.json`, which records the true `scanned_at_utc` and `scan_date` per run.

Therefore Themes 1 and 4 draw absence claims **only** from classes 3 and 4 (what a firm has and has not said publicly), never from class 1's reach. `findings/theme-4-mica-exposure-surface.md` was written to this constraint deliberately.

### 2. Agency case studies and press releases
- **Agencies tracked:** Coinbound, Lunar Strategy, MarketAcross, Outset PR, RZLT, ICODA, NinjaPromo, Blockwiz, Bond Finance, Crowdcreate, GuerrillaBuzz, TokenMinds, Single Grain, Flexe.io, Blue Manakin, Majinx, X10, Serotonin (the existing competitor-intelligence panel of 18).
- **Cross-reference:** which firms each agency publicly claims as a client; map overlap (firms with multiple agencies, agencies with multiple competing firms in same vertical).
- **Storage:** `./corpus/agency-claims/` — JSON file per agency with claimed-clients array; cross-reference matrix in `./corpus/agency-overlap-matrix.csv`.

### 3. Regulator filings and statements
- **Primary documents:** ESMA Statement on the end of transitional periods (April 17, 2026), MiCA Regulation (EU) 2023/1114, Commission Delegated Regulation on marketing communications, MAS guidelines, VARA marketing-comms guidance, FCA financial promotion rules.
- **Public regulator-action register:** every public marketing-side enforcement case in Q2 2026 (ESMA, BaFin, AMF, CONSOB, AFM, CySEC).
- **Storage:** `./corpus/regulator-filings/` — primary-source records + extraction notes.

### 4. Conference recordings, podcast transcripts, public LinkedIn posts
- **Captured:** any public statement by a senior marketing operator (CMO / VP Marketing / Head of Brand / Head of Growth at a tracked firm) on a podcast, conference stage, LinkedIn post, X thread, or media interview.
- **Initial podcast inventory:** Coinbound podcast (Episode 84+), Lunar Strategy podcast, Real Vision Crypto, Bankless, On the Margin, The Defiant Podcast, Onchain Growth Club, Crypto Curious.
- **Storage:** `./corpus/operator-statements/` — one markdown file per source with verbatim relevant quote + URL + speaker + date + role at time of statement.

### 5. Layoff announcements and earnings disclosures
- **Capture:** every public 2026 workforce contraction at a tracked or perimeter firm (Crypto.com -12%, Gemini -25% firm-stated/SEC-filed, Algorand -25% firm-stated, plus any new ones through August), with the firm's stated rationale and independent press analysis. **Marketing-specific impact is recorded only where a public source names it** — most 2026 crypto cuts are company-wide, and the tracker must not be read as a count of marketing-team contractions.
- **Storage:** `./corpus/layoff-tracker/2026-layoff-tracker.csv` — firm, date_announced, headcount_change, headcount_grade, percentage, percentage_grade, source_url, ai_cover_narrative, ai_cover_grade, notes.

### 6. NorthPoint competitor-intelligence pipeline (⚠ last refreshed 2026-06-15)
- **Source:** `./competitor-intelligence/trend-data.json`, `./competitor-intelligence/action-flags.json`, daily HTML snapshots in `./competitor-intelligence/YYYY-MM-DD.html` from April 8, 2026 onward.
- **What it gives the report:** longitudinal signal — what shifted, when, in which direction. Most one-shot research projects do not have an 18-month panel of agency-side content gravity. This one does.

## Automated daily feeds (added 2026-06-26)

Source classes 1 (job postings) and 2 (agency claims) are produced **deterministically from NorthPoint's existing daily data feeds**, not from web search — web search cannot reliably date-stamp ATS postings or agency claims. `scripts/daily-corpus-sync.py` consumes:

- **`open-positions.json`** — daily ATS API scan (greenhouse/ashby/lever/breezy/workable), URL-verified and dated → per-firm CSVs in `corpus/job-postings/`, mapped to the Stratum 1–4 cohort, dedup by source URL. Proprietary-ATS firms with no API coverage are logged in `corpus/job-postings/_absence.csv` (absence = data).
- **`trend-data.json`** — 18-agency panel with `recentClientsNamed`, **`lastUpdated` 2026-06-15 and unchanged since; the class-2 outputs have been byte-identical on every run after that date** → `corpus/agency-overlap-matrix.csv` (firm × agency, overlap-flagged) + dated `corpus/agency-claims/<agency>.csv` snapshots.

Classes 3 (regulator), 4 (operator statements), and 5 (layoffs) remain web-search/fetch driven, verified against primary sources. The run is **daily**; the sync script is idempotent. See `scripts/README.md`.

## Corpus coverage rules

- **If a thing is not publicly visible, it does not go in the report.** No private knowledge, no hearsay, no "an operator told me." Either there is a citation, or the claim is omitted.
- **Every claim is anchored to at least one primary source.** Synthesis claims (i.e., aggregating across the corpus) are anchored to the underlying source records the synthesis derives from.
- **Sources older than December 2024 are excluded** unless they remain materially relevant (e.g., MiCA Regulation (EU) 2023/1114 itself).
- **Where a firm has shipped no public signal on a theme, that absence is itself a finding.** The MiCA-readiness theme in particular hinges on what firms have publicly said versus what they have publicly avoided saying.

## Synthesis approach

- Themes coded continuously as corpus grows. Working notes in `./findings/` (one file per theme).
- Mid-cycle structural review at end of June (corpus snapshot, theme outline lock).
- Phase 3 synthesis (August): write the report, design pass, regulator-readability pass, internal review.

## Why no interviews

Three reasons make a public-source synthesis structurally stronger than an interview-based one for this report:

1. **Verifiability.** Every claim is independently checkable by a reader who disagrees. An anonymised quote is not.
2. **Visibility-as-analysis.** What is publicly visible about a firm's marketing function is precisely what the regulator can verify. The report's read is therefore the same read a regulator would do — which is the only read that matters in Q3 enforcement.
3. **Velocity.** Public-source research compounds and updates cleanly. Interview research is captive to scheduling, anonymisation politics, and quote-clearance loops. Ships faster, holds longer.

## What the report is NOT

- Not a vendor comparison.
- Not a "best agency of 2026" award.
- Not a benchmarking exercise where NorthPoint is the benchmark-setter.
- Not interview-based; no anonymised quotes appear anywhere in the report.
- NorthPoint's commercial offering appears in the appendix, in one paragraph, with one link.

## Inbound nominations

External nominations of public signals to add to the corpus arrive via `hello@northpoint.fi`. The corpus is updated **daily** (see `./corpus/weekly-runs/` for the dated run records); nominations are read on the next daily run. Tracked in `./inbound-nominations.md` (created when first nomination arrives). ⚠ **Known limit, recorded 2026-08-29:** the corpus-assembly loop has no mailbox access, so no nomination has ever been read by it. Nominations must be relayed into the repo by hand.

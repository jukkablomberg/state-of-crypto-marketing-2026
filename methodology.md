# State of Crypto Marketing 2026 — Methodology

> **Public-source synthesis, not interview-based research.** The corpus is built from primary sources anyone can independently verify. No interviewees, no anonymous quotes, no off-the-record reads. The visibility filter — what the firm has shipped publicly — is itself the analysis.

## Source corpus design

The corpus is anchored to six source classes, gathered continuously between now and ship date.

### 1. Job postings, by jurisdiction, by month
- **Capture window:** rolling 12 months ending August 31, 2026.
- **Firms tracked:** see `./tracked-firms.md` (~30 firms across exchanges, L1/L2 foundations, wallets, CASP-licensed firms).
- **Sources:** firm careers pages, LinkedIn job postings, web3.career, CryptoJobsList.
- **What we extract:** seniority, function (brand / growth / PMM / community / agency-mgmt / regulatory-comms), geography, posting date, time-to-fill, JD-stated AI-tooling requirements.
- **Storage:** `./corpus/job-postings/` — one CSV per firm per month.

### 2. Agency case studies and press releases
- **Agencies tracked:** Coinbound, Lunar Strategy, MarketAcross, Outset PR, RZLT, ICODA, NinjaPromo, Blockwiz, Bond Finance, Crowdcreate, GuerrillaBuzz, TokenMinds, Single Grain, Flexe.io, Blue Manakin, Majinx, X10, Serotonin (the existing competitor-intelligence panel of 18).
- **Cross-reference:** which firms each agency publicly claims as a client; map overlap (firms with multiple agencies, agencies with multiple competing firms in same vertical).
- **Storage:** `./corpus/agency-claims/` — JSON file per agency with claimed-clients array; cross-reference matrix in `./corpus/agency-overlap-matrix.csv`.

### 3. Regulator filings and statements
- **Primary documents:** ESMA Statement on the end of transitional periods (April 17, 2026), MiCA Regulation (EU) 2023/1114, Commission Delegated Regulation on marketing communications, MAS guidelines, VARA marketing-comms guidance, FCA financial promotion rules.
- **Public regulator-action register:** every public marketing-side enforcement case in Q2 2026 (ESMA, BaFin, AMF, CONSOB, AFM, CySEC).
- **Storage:** `./corpus/regulator/` — PDFs + extraction notes.

### 4. Conference recordings, podcast transcripts, public LinkedIn posts
- **Captured:** any public statement by a senior marketing operator (CMO / VP Marketing / Head of Brand / Head of Growth at a tracked firm) on a podcast, conference stage, LinkedIn post, X thread, or media interview.
- **Initial podcast inventory:** Coinbound podcast (Episode 84+), Lunar Strategy podcast, Real Vision Crypto, Bankless, On the Margin, The Defiant Podcast, Onchain Growth Club, Crypto Curious.
- **Storage:** `./corpus/operator-statements/` — one markdown file per source with verbatim relevant quote + URL + speaker + date + role at time of statement.

### 5. Layoff announcements and earnings disclosures
- **Capture:** every public 2026 marketing-team contraction (Crypto.com -12%, Gemini -30%, Algorand -25%, plus any new ones through August), with the firm's stated rationale and independent press analysis.
- **Storage:** `./corpus/layoff-tracker.csv` — firm, date, percentage, stated rationale, independent rationale, marketing-specific impact (where reported).

### 6. NorthPoint daily competitor-intelligence pipeline
- **Source:** `./competitor-intelligence/trend-data.json`, `./competitor-intelligence/action-flags.json`, daily HTML snapshots in `./competitor-intelligence/YYYY-MM-DD.html` from April 8, 2026 onward.
- **What it gives the report:** longitudinal signal — what shifted, when, in which direction. Most one-shot research projects do not have an 18-month panel of agency-side content gravity. This one does.

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

External nominations of public signals to add to the corpus arrive via `hello@northpoint.fi`. Read every Friday; corpus updated weekly through August. Tracked in `./inbound-nominations.md` (created when first nomination arrives).

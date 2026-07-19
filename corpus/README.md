# Corpus — State of Crypto Marketing 2026

Public-source corpus organised by source class. Every file in this tree is citation-anchored — each row references a primary source any reader can independently verify.

## Source classes (six)

1. **`job-postings/`** — Senior marketing job postings, by firm, past 12 months. One CSV per firm. Columns: `date_posted, title, jurisdiction, seniority, source_url, captured_date, notes`.
2. **`agency-claims/`** — Agency case studies + press releases naming a firm. Used to build the firm-overlap matrix. One CSV per agency.
3. **`regulator-filings/`** — ESMA, MiCA delegated reg, MAS, VARA, FCA filings + public regulator-action register. Filed as PDFs/HTML extracts with citation index.
4. **`operator-statements/`** — Conference talks, podcast transcripts, public LinkedIn posts where senior operators speak on the record. One Markdown file per firm; each entry timestamped + URL'd.
5. **`layoff-tracker/`** — Public 2026 marketing-team contractions. Single CSV: `firm, date_announced, headcount_change, percentage, source_url, ai_cover_narrative_y_n, notes`.
6. **`agency-overlap-matrix.csv`** — Cross-reference: which firms each agency newly claims; updated weekly Friday cadence.

## Workflow

- Weekly corpus refresh runs Friday. Inbound nominations (per the May 6 cycle-opener essay open call) get evaluated Friday and added if they fit corpus criteria.
- Phase 1 (May–June): build to coverage. Phase 2 (July): synthesise findings. Phase 3 (August–September): ship.
- All entries must be citation-anchored — no claim enters the corpus without a primary-source URL.

## Index of currently active files

- `job-postings/` — per-firm CSVs produced daily by `scripts/daily-corpus-sync.py` from the URL-verified ATS feed (ava-labs, bitpanda, bitstamp, bybit, crypto-com, kucoin, optimism, phantom, solana, **coinbase — added 2026-07-18**). `_absence.csv` carries tracked firms with no API coverage (Aave Lever-404 + 5 proprietary: Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys) — absence is data. `_chrome-queue.csv` tracks the proprietary-ATS backlog.
- `layoff-tracker/2026-layoff-tracker.csv` — seeded with Crypto.com (Mar -12%), Gemini (-30% YTD), Algorand (-25%), Coinbase (May 5 -14%), Block (-4,000), MARA (-40)
- `operator-statements/sport-sponsorship-reset-2026-05.md` — multi-incident sport-sponsorship reset cluster (captured 2026-05-14)
- `regulator-filings/fca-premier-league-sponsorship-warning-2026-06.md` — FCA→football-club crypto-sponsorship warning (2026-06-02/03)
- `regulator-filings/esma-mica-transitional-period-end-2026-06.md` — ESMA Public Statement (23 June 2026, ESMA75-113276571-1710): unauthorised CASPs must "cease marketing activities and solicitation" as the MiCA transitional period ends 1 July 2026
- `weekly-runs/` — dated daily corpus-assembly run records (six-class audit trail + absence-as-data). Latest: `2026-07-18-corpus-run.md`

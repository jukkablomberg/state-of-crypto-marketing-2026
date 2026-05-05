# State of Crypto Marketing 2026

> An operator-grade public-source synthesis of how senior crypto marketing leaders run the function in 2026.
> Built from the public record, citation by citation. Ships **September 1, 2026.**

This repository is the live corpus and methodology for the report. Every claim in the published report will be anchored to a primary source you can independently verify from this repo.

**Author:** [Jukka Blomberg](https://www.linkedin.com/in/jukkab/) — ex-CMO at international crypto exchanges, founder of [NorthPoint](https://northpoint.fi).
**License:** MIT (corpus, methodology, framework). The report itself ships under the same license on Sep 1, 2026.
**Cycle-opener essay:** [northpoint.fi/resources/writing/state-of-crypto-marketing-2026](https://northpoint.fi/resources/writing/state-of-crypto-marketing-2026)

---

## Why this exists

The crypto marketing category has plenty of agency-side reports — vendor comparisons, "best of" lists, awards-shop benchmarks. None of them read the function from the operator's seat, and none of them survive a regulator's reading.

This report does both. It is built from public sources only — job postings, agency case studies, regulator filings, conference recordings, podcast transcripts, layoff disclosures, and 18 months of NorthPoint's own daily competitor-intelligence panel. **Nothing in the report comes from off-the-record interviews or anonymised quotes.** If a thing is not publicly visible, it does not go in.

That choice is deliberate. The visibility filter — what each firm has shipped publicly — is itself the analysis. It is also the same read a regulator can do, which is the only read that matters in Q3 enforcement.

---

## What ships on September 1, 2026

A 40-page report — *State of Crypto Marketing 2026. Built from the public record.* — covering five themes:

1. **The shape of the marketing function.** Split-IC patterns, gate-stack visibility, who owns what across thirty firms.
2. **AI in the stack.** Claimed adoption vs. JD-confirmed adoption.
3. **The agency overlap matrix.** What three agencies on one firm tells you about the gate-stack vacancy.
4. **MiCA readiness — exposure surface by firm.** Which Tier-1 firms have a publicly visible MiCA-marketing-comms seat. Which do not.
5. **The 2026 layoff cycle and what it hit first.** Where marketing got cut and where it didn't.

Plus a regulator-readable appendix with the full citation index.

A companion PDF + interactive HTML version goes live on northpoint.fi the same day.

---

## Methodology — six source classes

The corpus is anchored to six source classes, gathered continuously between now and ship date.

### 1. Job postings, by jurisdiction, by month
- Capture window: rolling 12 months ending August 31, 2026.
- Sources: firm careers pages, LinkedIn, web3.career, CryptoJobsList.
- Extracted: seniority, function (brand / growth / PMM / community / agency-mgmt / regulatory-comms), geography, posting date, time-to-fill, JD-stated AI-tooling requirements.
- Storage: `corpus/job-postings/` — one CSV per firm per month.

### 2. Agency case studies and press releases
- Eighteen agencies tracked (see comparison panel below).
- Cross-reference matrix: which firms each agency publicly claims, and where claims overlap or contradict the firm's own postings.
- Storage: `corpus/agency-claims/` — JSON per agency; matrix in `corpus/agency-overlap-matrix.csv`.

### 3. Regulator filings and statements
- Primary documents: ESMA Statement on the end of transitional periods (April 17, 2026), MiCA Regulation (EU) 2023/1114, Commission Delegated Regulation on marketing communications, MAS guidelines, VARA marketing-comms guidance, FCA financial promotion rules.
- Public regulator-action register: every public marketing-side enforcement case in Q2 2026 (ESMA, BaFin, AMF, CONSOB, AFM, CySEC).
- Storage: `corpus/regulator/` — PDFs + extraction notes.

### 4. Conference recordings, podcast transcripts, public LinkedIn posts
- Captured: any public statement by a senior marketing operator (CMO / VP Marketing / Head of Brand / Head of Growth at a tracked firm).
- Initial podcast inventory: Coinbound, Lunar Strategy, Real Vision Crypto, Bankless, On the Margin, The Defiant, Onchain Growth Club, Crypto Curious.
- Storage: `corpus/operator-statements/` — markdown per source with verbatim quote + URL + speaker + date + role at time of statement.

### 5. Layoff announcements and earnings disclosures
- Capture: every public 2026 marketing-team contraction (Crypto.com -12%, Gemini -30%, Algorand -25%, plus any new ones through August), with the firm's stated rationale and independent press analysis.
- Storage: `corpus/layoff-tracker.csv`.

### 6. NorthPoint daily competitor-intelligence panel
- Source: an 18-month longitudinal panel of agency-side content gravity, refreshed daily.
- What it gives the report: longitudinal signal — what shifted, when, in which direction.

### Coverage rules
- If a thing is not publicly visible, it does not go in.
- Every claim is anchored to at least one primary source. Synthesis claims (aggregating across the corpus) cite the underlying source records.
- Sources older than December 2024 are excluded unless they remain materially relevant (e.g., MiCA Regulation itself).
- Where a firm has shipped no public signal on a theme, **that absence is itself a finding.**

---

## Tracked firms — substantive synthesis cohort (~30)

### Tier-1 exchanges
Binance · OKX · Bybit · KuCoin · Coinbase · Kraken · Crypto.com · Gemini · Bitstamp · Bitpanda · HTX

### L1 / L2 foundations
Sui Foundation · Aptos · Solana Foundation · Aave · Polygon · Optimism Foundation · Arbitrum Foundation · Ava Labs

### Wallets / consumer crypto
MetaMask / ConsenSys · Phantom · Ledger · Trust Wallet · Rabby

### CASP-licensed (non-exchange)
Securitize · Tether · plus additional CASP-licensed asset managers, custodians, and agentic-commerce protocols (resolved during corpus build, May–June)

### Comparison panel — 18 agencies (tracked from outside; not the analysis subject)
Coinbound · Lunar Strategy · MarketAcross · Outset PR · RZLT · ICODA · NinjaPromo · Blockwiz · Bond Finance · Crowdcreate · GuerrillaBuzz · TokenMinds · Single Grain · Flexe.io · Blue Manakin · Majinx · X10 · Serotonin

Selection criterion: a firm enters the cohort if it (1) operates a regulated or about-to-be-regulated crypto-marketing function at meaningful scale, and (2) has shipped enough public signal in the last 12 months to support multi-theme synthesis. Firms that meet (1) but produce minimal public signal are flagged in a separate **absence panel** — their lack of public signal is itself a data point under Theme 4 and Theme 1.

---

## What this report is NOT

- Not a vendor comparison.
- Not a "best agency of 2026" award.
- Not a benchmarking exercise where NorthPoint is the benchmark-setter.
- Not interview-based. No anonymised quotes appear anywhere in the report.
- NorthPoint's commercial offering appears in the appendix, in one paragraph, with one link.

---

## Open call — nominate a public signal

If you know of a public signal that should be in the corpus — a job posting, a podcast appearance, a regulator filing, a layoff disclosure, a case study — send it to **hello@northpoint.fi**.

Inbound nominations are read every Friday and evaluated against the corpus coverage rules above. If a nomination fits, it enters the corpus and the contributor is acknowledged by name in the report's appendix on Sep 1 (unless the contributor requests otherwise).

We are particularly interested in:
- Public marketing-side enforcement cases under MiCA, MAS, VARA, FCA in 2026.
- Public statements by a CMO / VP Marketing / Head of Brand at any tracked firm on the post-MiCA marketing-comms surface.
- Layoff disclosures that name marketing/growth as the affected function.
- CASP-licensed asset managers, custodians, or agentic-commerce protocols that should be in Stratum 4.

---

## Cycle phases

| Phase | Window | Output |
|---|---|---|
| **1 — Corpus assembly** | May–June 2026 | Public-source corpus across 30 tracked firms × 6 source classes |
| **2 — Theme synthesis** | July 2026 | Each of the five themes drafted against the citation-anchored corpus |
| **3 — Ship** | August 15 – September 1, 2026 | Design pass, regulator-readability pass, press kit, ship |

Weekly drip essays publish at [northpoint.fi/resources](https://northpoint.fi/resources) and the corpus updates here every Friday.

---

## Repository layout (as it builds out)

```
corpus/
  job-postings/           # CSV per firm per month
  agency-claims/          # JSON per agency
  agency-overlap-matrix.csv
  regulator/              # PDFs + extraction notes
  operator-statements/    # markdown per public statement
  layoff-tracker.csv
findings/                 # working notes, one file per theme
methodology.md            # this document, versioned
tracked-firms.md          # the substantive synthesis cohort
research-framework.md     # five themes × per-theme evidence inputs
LICENSE
README.md
```

---

## License

MIT — for the corpus, methodology, framework, and the report itself on Sep 1, 2026. Cite as:

> Blomberg, Jukka. *State of Crypto Marketing 2026. Built from the public record.* NorthPoint, September 1, 2026. https://northpoint.fi/resources/writing/state-of-crypto-marketing-2026

---

## Contact

- Email: [hello@northpoint.fi](mailto:hello@northpoint.fi) (nominations) · [jukka@northpoint.fi](mailto:jukka@northpoint.fi) (direct)
- Web: [northpoint.fi](https://northpoint.fi)
- LinkedIn: [linkedin.com/in/jukkab](https://www.linkedin.com/in/jukkab/)

# State of Crypto Marketing 2026

> A public-source read of how crypto marketing was actually run in the twelve months to 31 August 2026 — who may market, who does the work, what was shipped, where the talent went, and what nobody discloses.
> Built from the public record, citation by citation. **Publishes 24 September 2026.**

**Author:** [Jukka Blomberg](https://www.linkedin.com/in/jukkab/) — ex-CMO at two international crypto exchanges, founder of [NorthPoint](https://northpoint.fi).
**Publisher:** NorthPoint Research · *State of the Market* · No. 1.
**License:** MIT — corpus, canonical dataset, methodology, and the report itself.
**Report page:** [northpoint.fi/state-of-crypto-marketing-2026](https://northpoint.fi/state-of-crypto-marketing-2026) (the PDF, the HTML edition and the one-page summary go live there on 24 September; the same three files land in `report/` here the same morning).

---

## What the report says

Nineteen pages: a one-page summary, a contents page, four chapters on seven pages with nine exhibits — the ESMA licence field, two real campaign executions, the six capture offers in their own terms, the Coinbase-to-AI moves, the agency claims matrix, an agency buyer's table, the disclosed marketing money — then an appendix with the four canonical tables and every source.

1. **Regulation rewrote crypto marketing.** Two of 27 tracked firms — Binance and HTX — lost the right to acquire EEA customers on 1 July 2026. Around the deadline six licensed exchanges — four of them in the cohort — ran dated, quantified capture offers at the stranded users, and the licence became the offer: *“Most exchanges aren't licensed after July 1. Kraken is.”* Google had already made a MiCA authorisation a condition of advertising an exchange or software wallet in the EU (23 April 2025), extended to the whole EEA and hardware wallets in August 2026.
2. **AI and the marketing function.** Seven Coinbase marketers, including its CMO, went to OpenAI and Anthropic. The job boards the daily scan can read show few open marketing roles at the 27 and many at the AI labs — but the largest exchanges' boards cannot be read, so the report prints no count (the raw scan and its absence panel are in `corpus/job-postings/`). Nine of 26 contraction rows carry an AI frame; five in the firm's own words. A measurable part of the AI-layoff narrative is the press's, not the firms'.
3. **The agency stack.** Seven of the ten tracked firms any agency names are named by two or more agencies — KuCoin by three. Claims on the agencies' own surfaces; not one firm-side statement about any of them is on the record.
4. **Nobody will say who runs marketing.** Eighteen of 27 companies have never put a number on their marketing — not a headcount, not a budget. The three that do file it with the SEC because they must (Coinbase: $1.06 billion in 2025). Binance publishes its compliance headcount and spend, and nothing about marketing. Two of the largest exchanges lost their CMO in June with no permanent successor named.

**Editions.** The published edition (v9, 16 September 2026) prints the agency panel as 17: one agency captured in the 18-agency panel is omitted from the report at the author's discretion; it named none of the 27 and no count changes. The dataset here keeps all 18. The report's `CLAIM-LEDGER.md` (published with it in `report/`) records, for every headline, the passage relied on and the wording allowed.

Every figure is derived from one frozen dataset (`corpus/_canonical/`), carries its denominator, and reconciles to the appendix tables. Absence is recorded as absence and never promoted to intent. Agency claims are claims. Figures a firm did not itself state are not printed as facts.

---

## What is in this repository

```
corpus/
  _canonical/             # the five files every figure in the report derives from (frozen 2026-09-10)
  layoff-tracker/         # the 26-row contraction tracker + adjudication and provenance records
  job-postings/           # daily ATS scan extracts, the absence panel, cohort audits
  agency-claims/          # per-agency claim records; agency-overlap-matrix.csv
  regulator-filings/      # ESMA / NCA / FCA / Google records with extraction notes; ESMA register snapshots
  marketing-campaigns/    # the capture campaigns, page captures, lapse checkpoints
  operator-statements/    # verbatim public statements by named marketing executives
  ad-platform-gates/      # Google Ads CASP policy captures
  weekly-runs/            # dated run records — what was captured when, and what was rejected
findings/                 # the longitudinal jobs read and the fact sheets the chapters lean on
methodology.md            # source classes, coverage rules, limits
tracked-firms.md          # the 27-firm cohort and the 18-agency panel, with selection criteria
research-framework.md     # the five-theme framework the corpus was gathered under (May 2026) — historical
report/                   # added on 24 September: report.pdf · report.html · summary.pdf
```

The canonical files are the contract: `AGENCIES.md` · `EEA-MARKETING-ELIGIBILITY.md` · `QUOTES-BANK.md` · `TEAM-SIZE-AND-BUDGET.md` · `NUMBERS-THAT-SELL.md`. Where a number in the report and a number in a corpus note disagree, the canonical file wins, and a correction is made there with a dated note — never by patching the report.

---

## Method, in brief

- **Public sources only.** No interviews, no anonymous quotes of our own, no off-the-record reads. If a thing is not publicly visible it is not in the report.
- **Population.** 27 named firms — 11 exchanges, 8 L1/L2 foundations, 5 wallets, 3 licensed non-exchanges — plus an 18-agency comparison panel. Selection criteria in `tracked-firms.md`.
- **Window.** Rolling twelve months to 31 August 2026. Sources older than December 2024 excluded unless materially relevant.
- **Six source classes.** Job postings · agency case studies · regulator filings and registers · operator statements · contraction disclosures · NorthPoint's competitor-intelligence panel (last refreshed 15 June 2026).
- **Limits, stated where they bite.** The job scan cannot reach five tracked firms' careers systems. The agency panel sees crypto-native agencies only. One advertising platform of at least seven was read at source. Every campaign page was fetched from outside the EEA.

Full text: `methodology.md`.

---

## Corrections

The report says what the corpus can show and stops. If you find a figure that does not survive its own source, open an issue naming the canonical file and the line, or write to **hello@northpoint.fi**. Corrections are made in the canonical file with a dated note and the report is rebuilt from it.

---

## How to cite

> Blomberg, Jukka. *State of Crypto Marketing 2026. Built from the public record.* NorthPoint Research, State of the Market No. 1, 24 September 2026. https://northpoint.fi/state-of-crypto-marketing-2026

---

## Contact

- [jukka@northpoint.fi](mailto:jukka@northpoint.fi) · [northpoint.fi](https://northpoint.fi) · [linkedin.com/in/jukkab](https://www.linkedin.com/in/jukkab/)

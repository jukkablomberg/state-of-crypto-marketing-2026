# State of Crypto Marketing 2026

> A public-source read of how crypto marketing was actually run in the twelve months to 31 August 2026 — who may market, who does the work, what was shipped, where the talent went, and what nobody discloses.
> Built from the public record, citation by citation. **Publishes 24 September 2026.**

**Author:** [Jukka Blomberg](https://www.linkedin.com/in/jukkab/) — ex-CMO at two international crypto exchanges, founder of [NorthPoint](https://northpoint.fi).
**Publisher:** NorthPoint Research · *State of the Market* · No. 1.
**License:** MIT — corpus, canonical dataset, methodology, and the report itself.
**Report page:** [northpoint.fi/state-of-crypto-marketing-2026](https://northpoint.fi/state-of-crypto-marketing-2026) (the PDF, the HTML edition and the two-page summary go live there on 24 September; the same three files land in `report/` here the same morning).

---

## What the report says

Seven pages, four chapters, five exhibits, then an appendix with the method, the four canonical tables and every source.

1. **Regulation rewrote crypto marketing.** Two of 27 tracked firms — Binance and HTX — lost the right to acquire EEA customers on 1 July 2026. Around the deadline six licensed exchanges ran dated, quantified capture offers at the stranded users, and the licence became the offer: *“Most exchanges aren't licensed after July 1. Kraken is.”* Google had already turned the ESMA register into an inventory flag.
2. **AI and the marketing function.** Six senior Coinbase marketers went to OpenAI and a seventh to Anthropic. On the window's last day: 2 open marketing or growth roles across 27 crypto firms, 25 at four AI labs. Nine of 26 contraction rows carry an AI frame; five in the firm's own words. A measurable part of the AI-layoff narrative is the press's, not the firms'.
3. **The agency stack.** Seven of the ten tracked firms any agency names are claimed by two or more agencies at once — KuCoin by three. Claims on the agencies' own surfaces; not one firm-side statement about any of them is on the record.
4. **Nobody will say who runs marketing.** One firm in 27 has stated a marketing team size, none a budget. Binance states more than 1,500 compliance staff and more than $300 million a year of compliance spend. Two Tier-1 CMO seats vacated in June with no permanent successor named.

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

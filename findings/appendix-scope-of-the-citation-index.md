# Appendix language — what the citation index certifies, and what it does not

**Status:** ready to paste. Written 2026-09-01 (ship day) to discharge recommendation 3 of the
2026-08-31 run record, which asked for "two sentences the appendix should carry, both honest and
both cheap" and left them as prose in a run record no reader of the report will ever open.

**Why this file exists rather than a recommendation:** a recommendation Jukka has to re-derive into
publishable sentences is a format problem, not a supply problem. The text below is final; it needs
a paste, not a decision. Cut it, shorten it, or reject it — but it does not need rewriting first.

---

## 1. Scope of the citation index (recommended: immediately above the index itself)

> **What this index certifies.** Every entry below has been checked for two things: that the source
> exists at the URL given, and that the date the corpus records for it is consistent with the date
> the source itself asserts. Where a source's own URL carries a publication date, that date was
> compared against the corpus record at the coarser of the two precisions, and inconsistencies were
> adjudicated by hand.
>
> **What this index does not certify.** It does not certify that a source supports the sentence that
> cites it. Existence and dating are machine-checkable and were checked mechanically on every run;
> whether a citation bears the weight of the claim pointing at it is a reading, and readings were
> done by hand, unevenly, as the cycle's time allowed. On 2026-08-31 — the day before publication —
> one such reading was performed on a claim this report had carried since May. The source existed,
> was correctly dated, and contradicted three of the claim's four limbs. Those limbs were cut. We
> record this because the same check has not been run on every citation here, and a reader is
> entitled to know the difference between the guarantee we can make and the one we cannot.

**Provenance:** the incident is `corpus/operator-statements/binance-conlan-cmo-exit-primary-2026-08-31.md`;
the structural finding is item 2 of `corpus/weekly-runs/2026-08-31-corpus-run.md`.

---

## 2. Two known limits in the class-1 dataset (recommended: methodology appendix, §1)

> **Company identity in the job-posting dataset is derived from applicant-tracking-system slugs, and
> is reconciled against nothing.** A posting's employer is inferred from the ATS account that hosts
> it; the firm's tier and category are joined from a separate table keyed on display name. The two
> are not cross-checked. This is a live failure mode, not a theoretical one: on 2026-08-30 two
> URL-verified, correctly dated postings labelled as a stablecoin issuer belonged to a
> similarly-named community-software company, and were excluded only because that name sits outside
> the cohort — a filter on the name, when the name was the error. All tracked-firm rows in the
> shipped dataset were reconciled by hand; no contamination was found. Firms with common-word names
> carry the residual risk.
>
> **The absence panel records when the scanner last looked, not when the firm last spoke.** The five
> firms listed there are absent from the dataset because their careers infrastructure is not
> reachable by the API scan, not because they published nothing. The panel's `as_of` field is
> written from the run clock rather than from the observed scan, so it should be read against
> `corpus/job-postings/_feed-fingerprint.json`, which records the true scan timestamp for every run
> of the cycle.

**Provenance:** watch (al) and watch (ai); `methodology.md` §1 carries the second in full.

---

## 3. One observation Theme 2 should not ship without (recommended: Theme 2 body, not the appendix)

Carried forward from the 2026-08-31 record, unchanged, because ship day did not change it:

> On the final day of a twelve-month capture window, the same daily scan that observed **two** open
> marketing or growth roles across the entire twenty-seven-firm crypto cohort observed **twenty-five**
> at four AI labs outside it.

**Handling.** The AI labs are outside the cohort and no claim in this report is derived from them.
The number is offered as context for where the marketing function's hiring went in 2026, and it
should be attributed to NorthPoint's own daily scan rather than presented as a market statistic —
the denominator is our tracked list, not the industry.

**Provenance:** watch (ag), advanced to n=6 on 2026-09-01. Series held flat at 25:2 across the
window's final two days.

---

*Written by the corpus-assembly loop, 2026-09-01. Nothing above is a new finding; every sentence
restates something the run records already establish, in the form the report can print.*

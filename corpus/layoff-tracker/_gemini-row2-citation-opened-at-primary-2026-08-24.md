# Layoff-tracker row 2 (Gemini) — citation opened at the true primary, which turned out to be an SEC filing

**Class:** 5 (layoff announcements) — with a class-4-adjacent finding attached
**Captured:** 2026-08-24
**Cohort status:** IN-COHORT — Stratum 1 tracked firm (`tracked-firms.md`)
**Why this row:** recommendation 1 of the 2026-08-23 run. Gemini −30% is **the last of the three layoff examples advertised in the public `README.md` that had not been inspected — and the other two both failed inspection** (Algorand had no citation at all, 08-21; Crypto.com's 180 turned out to be the outlet's arithmetic, 08-22).

---

## §0 — Headline: it failed too, and the primary is stronger than anything else in the tracker

**Three for three. Every layoff example this report advertises publicly has been found carrying a defect when its citation was finally opened.**

But the same fetch that broke the number produced **the best-sourced row in the entire tracker** and **the closest any tracked firm has come, in a filed document, to placing non-engineering functions inside the AI-substitution frame.**

---

## §1 — Source promotion: near-primary → SEC-filed exhibit

| | Before (from 2026-07-28) | After (2026-08-24) |
|---|---|---|
| `source_url` | `cointelegraph.com/news/gemini-exit-uk-eu-australia-slashes-workforce` (near-primary; quotes the announcement) | **`https://www.sec.gov/Archives/edgar/data/2055592/000205559226000008/a8kblogpostfeb52026.htm`** |
| Source class | crypto-media secondary | **Gemini Space Station, Inc. — Form 8-K, EXHIBIT 99.1 ("BLOG POST"). Period 2026-02-05. Filed 2026-02-05.** |
| Capture | not fetched first-party | **HTTP 200, full body, fetched 2026-08-24** |

**The firm's announcement is a filed regulatory document.** That makes this row's primary stronger than any other in the tracker — stronger than a CEO's X post, stronger than a forum report, stronger than a captured news article quoting either.

**The 2026-07-28 `[VERIFY]` — *"locate and archive Gemini's own announcement post for a fully primary anchor"* — is CLOSED.**

⚠ **Routing note, recorded because it is watch (i) again:** `https://www.gemini.com/en-GB/blog/gemini-2-0-a-bridge-to-the-future-of-money-and-markets` was **REFUSED by the fetch provenance set** even though it was a hyperlink inside a page fetched moments earlier in the same run. The SEC-filed copy of the same text was reachable via search-then-fetch and is strictly the better artifact. **The workaround paid for the seventh consecutive time — and once again only because a second copy of the document happened to exist.**

---

## §2 — 🔴 The −30% YTD is STRUCK. It was never firm-stated and its arithmetic does not reconcile.

The firm states its own headcount history verbatim, in the filed exhibit:

> *"In 2022, our workforce peaked around approximately 1,100. Heading into the end of 2025, we were about 50% of that size. Today, we are reducing our size again by roughly 25%."*

Read as the firm wrote it: **~1,100 (2022 peak) → ~550 (end-2025) → −25% (2026-02-05).**

**The 25% and the 50% are cumulative-since-2022 reductions. Neither is a 2026 year-to-date figure. There is no firm-stated −30% YTD anywhere in the document.**

The `-30% YTD` had sat in this row since before 2026-07-28 with no source. Its lineage is now visible: **aggregator reporting** — surfaced in today's class-5 search — states *"Gemini reduced its workforce by roughly 30% since the start of 2026, bringing total headcount to around 445."* That is an aggregator's aggregate, not a company disclosure.

**The 2026-07-28 `[VERIFY]` on the YTD aggregate is CLOSED — by striking it, not by sourcing it.**
**`percentage` now reads: `-25% [FIRM-STATED VERBATIM, SEC-FILED]`. DO NOT PRINT −30%.**

---

## §3 — 🔴 The "200 jobs" figure is not firm-stated either — and it is the first propagated figure the corpus has found that does not reconcile with the firm's own numbers

Secondary outlets report *"up to 200 positions."* Aggregators report *"~445 headcount."*

**The firm stated a percentage and nothing else.** No headcount appears anywhere in the filed exhibit.

And the arithmetic diverges: **25% of the firm's own stated ~550 base is ~137, not 200.** The corpus takes no view on what base the reporters used — that is not knowable from here, and asserting they are wrong would be the same error in the opposite direction. **The point is narrower and certain: the firm disclosed a percentage, the headcount is someone else's, and the two do not obviously reconcile against the firm's own published base.**

`headcount_change` now reads: `undisclosed by the firm (firm stated a PERCENTAGE only). DO NOT PRINT 200.`

### Watch (vv) is now six-for-six across four consecutive runs

| Run | Row | Defect found on opening the citation |
|---|---|---|
| 08-21 | Algorand | **no `source_url` at all** — while printed as a README example |
| 08-22 | Crypto.com | `180` is **the outlet's own arithmetic**, stated as such in the article |
| 08-23 | Luno | `−20%` is **Bloomberg's**; CEO confirmed cuts, *declined* the number |
| 08-23 | BitGo | **unstable aggregator citation** which had silently supplied a wrong date |
| **08-24** | **Gemini** | **`−30% YTD` unsourced and unreconcilable; `200` not firm-stated** |

**Not one number in this tracker has survived having its citation opened without a correction. Four runs, five rows, five defects.**

---

## §4 — ⭐ What the capture GIVES the report, and it is the best thing in it

### 4.1 `ai_cover_narrative = Y` is confirmed firm-stated, and it is the strongest Y in the tracker

The document's own subtitle, verbatim:

> **"A message from our founders on AI, prediction markets, and focus"**

**AI is the first named section of the announcement.** It is not a rationale mentioned in passing or extracted by a reporter — it is the organising frame the founders chose, in a document they filed.

Verbatim, from the **AI** section:

> *"rapid breakthroughs in AI have begun to dramatically transform the way we work at Gemini"*

> *"AI has completely changed the game, expanding this paradigm by another order of magnitude (at a minimum), making a 10xer now a 100xer."*

> *"Doing more with less has never been more true or possible and we believe this trend line is only just beginning."*

**The 2026-07-28 note's summary of the AI framing — including the "100x" characterisation — is CONFIRMED CORRECT and is now verbatim-anchored rather than paraphrased.** Recorded emphatically because the last three rows opened all had their claims *weakened*; this one had its claim *confirmed*, and both outcomes have to be reported the same way.

### 4.2 ⭐⭐ The single most report-relevant sentence in the capture, and it is about non-engineering work

Verbatim, immediately following the 100x claim:

> *"Critically, we are seeing that this step change holds true for every engineer who adopts AI into their workflows. **And it also holds true for non-engineering work.**"*

**A Tier-1 tracked exchange states, in an SEC-filed document, in the same paragraph as a 25% headcount reduction, that the 100x AI productivity claim extends beyond engineering.**

**Marketing is non-engineering work.**

🔴 **THE FIRM DOES NOT NAME MARKETING, AND NO MARKETING CLAIM MAY BE ATTRIBUTED TO IT.** "Non-engineering work" covers finance, legal, support, operations and marketing alike, and the corpus does not get to pick. But this is the closest any tracked firm has come to placing the marketing function inside the AI-substitution frame **in a document filed with a securities regulator** — and it is a materially different object from a CEO's post or a reporter's paraphrase, because of where it was filed.

**This is watch (l) arriving from a third direction.** `methodology.md` §4 admits statements by a *titled operator* at a tracked firm. This is a firm speaking, in a filed exhibit, about work it does not attach a title to. §4 cannot see it — the same perimeter failure the Gnosis quarterly exposed on 08-23, on a stronger document.

### 4.3 Theme-4 anchor upgraded to a filed document

> *"we will be reducing areas in which we operate by exiting the UK, EU, and Australian markets."*

The corpus's standing finding — **Gemini is the first Tier-1 tracked exchange to withdraw from the EU market, 2026-02-05, five months before the 1 July transitional deadline and four months before Binance's exit** — now rests on an SEC exhibit rather than on crypto-media reporting. A tracked firm exiting the EU removes its entire EU marketing surface from the report's observable universe: **an absence with a documented cause, which is a different object from an absence with none.**

Also captured, and useful context for the Theme-4 read on *why* firms leave: the firm's own stated reason is commercial, not regulatory — *"These foreign markets have proven hard to win in for various reasons and we find ourselves stretched thin with a level of organizational and operational complexity that drives our cost structure up and slows us down. And we don't have the demand in these regions to justify them."* **MiCA is not mentioned in the exit rationale. Do not attribute the exit to MiCA.**

---

## §5 — Explicit non-claims

1. **NOT claimed:** that Gemini cut its marketing team, or that marketing was among the reduced functions. **No function is named anywhere in the document.**
2. **NOT claimed:** that "non-engineering work" means marketing. It includes marketing; the firm scopes it no further and neither does the corpus.
3. **NOT claimed:** −30% YTD, 200 jobs, or 445 headcount. None is firm-stated; all three are struck or refused.
4. **NOT claimed:** that the reporters who published 200 were wrong. Only that the firm did not say it, and that it does not reconcile against the firm's own stated base.
5. **NOT claimed:** that Gemini's EU exit was caused by MiCA. The firm's stated rationale is commercial and does not mention it.
6. **NOT ENTERED — a search summary asserted content that is not in the filed exhibit.** A summary of the `www.gemini.com` copy of this post asserted named C-suite departures (CFO Dan Chen, CLO Tyler Meade, COO Marshall Beard). **No such names appear anywhere in the SEC-filed exhibit captured here.** Not admitted, not attributed, recorded as a non-claim. **⚠ This is watch (ss) in a new form: a search summary supplied specific, checkable, senior-personnel facts that the primary document does not contain. Had they been admitted, they would have been three fabricated class-4 datapoints about a tracked firm.**

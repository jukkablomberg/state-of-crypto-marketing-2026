# `ai_cover_narrative` — end-to-end grading audit of every `Y` row

**Class:** 5 (layoff tracker) — column integrity audit
**Run:** 2026-08-24
**Mandate:** recommendation 2 of the 2026-08-23 run, closing new watch **(xx)**: *"Every `Y` row, checked for the automation → AI substitution found on Luno, and graded firm-stated / reported / inferred. The AI-cover share is a Theme-5 headline number and it currently cannot be printed honestly."*
**Method:** every `Y` row read via `csv.DictReader` against its own captured note and, where the note carried one, its verbatim quote. No re-fetches except row 2 (Gemini), opened first-party the same run.
**Schema change:** a new column **`ai_cover_grade`** is added to `2026-layoff-tracker.csv`. 26 rows, 8 fields. All 17 `N` rows carry `n/a`.

---

## §0 — The two results, and the second one matters more than the first

**RESULT 1 — the substitution defect does NOT propagate.** The audit was mandated because Luno's *automation → AI* substitution might be systemic. **It is not.** Of the nine `Y` rows, **eight rest on the token "AI" appearing in the source; exactly one (Luno) rests on the word "automation" with no "AI" anywhere.** The defect is confined to the row it was found on. The AI-cover count is **not** inflated by silent word-substitution.

**RESULT 2 — 🔴 and this is the real finding: the column mixes five distinct epistemic grades, and only four of twenty-six rows are firm-stated with a verbatim quote captured first-party.** A naive "AI-cover share" of **9/26 = 35%** collapses to **4/26 = 15%** once the column is graded. **That 20-point gap is the number Theme 5 was about to print wrong.**

---

## §1 — The grading ladder

| Grade | Meaning |
|---|---|
| **A** | Firm-stated, **verbatim quote captured first-party** in this corpus |
| **B** | Firm-stated, but **relayed** — the quote reaches us through a captured outlet and the firm's own primary was not fetched |
| **C** | **Outlet characterisation** — no firm quote at all; a reporter describes the rationale as AI-driven |
| **D** | **Anonymously sourced** — attributed by the outlet to an unnamed person, with no on-record firm statement |
| **E** | **Inferred** — the firm did not say "AI"; the corpus read it in |

---

## §2 — All nine `Y` rows, graded

| # | Firm | Cohort | Grade | Basis |
|---|---|---|---|---|
| 1 | Crypto.com | **TRACKED S1** | **A** | CEO Kris Marszalek, verbatim: *"We are joining the list of companies integrating enterprise-wide AI."* |
| 2 | Gemini | **TRACKED S1** | **A** | **SEC-filed 8-K EX-99.1.** Subtitle verbatim: *"A message from our founders on AI, prediction markets, and focus."* AI is the announcement's own first section. **Strongest Y in the tracker.** |
| 4 | Coinbase | **TRACKED S1** | **B** | Armstrong memo ("AI-native pods"). ⚠ **The row itself carries no verbatim quote**; the memo is documented in `findings/theme-1-firm-estate-instrument-coinbase-2026-08-16.md`. Firm-stated, but this row does not carry its own evidence. |
| 5 | Block, Inc. | perimeter | **C** | The Block characterises Dorsey's framing as *"a smaller, flatter, AI-driven organisation."* **No Dorsey quote captured.** Underlying primary `theblock.co/post/391520` linked by two captured articles but **still unfetched since 2026-08-06**. |
| 8 | BitGo | perimeter | **A** | CEO Mike Belshe, verbatim: *"…security, trading, stablecoins, settlement, and **AI-powered infrastructure**."* The CEO's own phrase, not a reporter's gloss. |
| 13 | Kraken | **TRACKED S1** | **D** | Bloomberg attributes the AI rationale to *"a person familiar with the matter who was not authorized to speak publicly."* **Kraken has made no on-record statement of rationale.** |
| 15 | Luno | perimeter | **E** | CEO Lanigan's word is **"automation."** Neither the firm nor CoinDesk says *AI* anywhere in the capture. |
| 19 | Messari | perimeter | **B** | *"AI-first"* attributed to CTO/incoming CEO Diran Li **by The Block**. Li's X post linked but **unfetched**. |
| 26 | Dune Analytics | perimeter | **A** | CEO Fredrik Haga, verbatim, with an explicit product-AI-to-headcount link. |

---

## §3 — 🔴 The numbers Theme 5 may and may not print

**Of 26 tracker rows:**

- **9 carry `ai_cover_narrative = Y`** → the naive share is **35%**
- **4 are Grade A** (firm-stated, verbatim, captured first-party): Crypto.com, Gemini, BitGo, Dune → **15%**
- 2 are Grade B (firm-stated, relayed): Coinbase, Messari → A+B = **6/26 = 23%**
- 1 is Grade C (outlet characterisation only): Block
- 1 is Grade D (anonymous): Kraken
- 1 is Grade E (inference from "automation"): Luno

### The sentence that may be printed

> *Of 26 public crypto workforce reductions recorded in 2026, nine are framed around AI. But only four carry a verbatim statement from the firm itself. Of the remaining five: two reach us relayed through a reporter, one is a reporter's characterisation with no company quote at all, one rests on an anonymous source the company has never corroborated on the record, and one is our own inference from the word "automation." **The AI-cover narrative is substantially thinner in the primary record than in the coverage of it.***

### 🔴 The sentence that may NOT be printed

> ~~"35% of 2026 crypto layoffs cite AI."~~

**Ungraded, that number treats an SEC filing and an unnamed source as the same evidence. It must not ship.**

---

## §4 — Cohort split, because it cuts against the convenient reading

The four Grade-A rows are **two tracked Stratum-1 exchanges (Crypto.com, Gemini)** and **two perimeter firms (BitGo, Dune)**.

Both **tracked** firms whose AI framing is *weakest* are also Stratum 1: **Kraken (D, anonymous)** and **Coinbase (B, memo not carried in-row)**.

**So among the four Tier-1 tracked exchanges with an AI-framed layoff, the evidence grade splits 2 A / 1 B / 1 D.** Half the tracked-firm AI-cover evidence is firm-verbatim; half is not. **Any Theme-5 claim restricted to tracked firms rests on n=4 with two different evidentiary grades. State the n. State the grades.**

---

## §5 — What this audit did NOT do, stated plainly

1. **It did not re-fetch eight of the nine rows.** Grades are assigned from notes and quotes already captured. **A Grade A means the corpus holds a verbatim quote — not that the quote was re-verified today.**
2. **It did not resolve the two open primaries** that would upgrade C→A and B→A: `theblock.co/post/391520` (Block/Dorsey, open since 08-06) and `x.com/diran_li/status/2033641098795729141` (Messari/Li, open since 08-06). Both remain on the work queue, both unfetchable under the current provenance rule.
3. **It did not audit the `N` rows for the reverse error** — a firm that *did* invoke AI but was recorded `N`. **That is the symmetric defect and it has never been checked.** Watch (ss) says the error that confirms is the one that goes unexamined; the AI-cover share is the number the report *wants* to be high, so the rows that would raise it got audited today and the rows that would lower it did not. **Flagged as the next sweep.**
4. **It did not grade `headcount_change` or `percentage` by the same ladder** — though watch (vv) is now six-for-six and those columns plainly need it. **The figure columns need this exact treatment before Phase 2.**

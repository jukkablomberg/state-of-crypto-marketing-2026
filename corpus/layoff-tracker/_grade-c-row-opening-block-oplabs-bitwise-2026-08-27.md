# Layoff tracker — the three Grade-C rows the ladder named, opened

**Run:** 2026-08-27 (day 57 post-deadline). **Class 5.**
**Mandate:** recommendation 1 of the 08-25 run — *"OPEN ROWS 5, 12 AND 13 — THE LADDER HAS NAMED THEM. All three are Grade C on both figure columns, which is the shape all six prior defects took."*
**Executed:** rows **5 (Block, Inc.)** and **12 (OP Labs)** opened first-party. Row **13 (Kraken)** **NOT** opened — Bloomberg, paywalled, no non-paywalled primary exists. A fourth row, **24 (Bitwise)**, was opened opportunistically when a class-5 search surfaced a *second independent outlet* for it.

---

## Headline

**Watch (vv) is now seven-for-seven — but for the first time the movement went UP.** Six prior citation-openings each found a defect. Today's three found **two upgrades and one confirmed-worse**, and together they produce a finding the aggregate ladder could not see.

### ⭐ THE CROSS-ROW RESULT — the percentage is the weaker field, and the 08-25 ladder said the opposite

The 08-25 grading found **4 Grade-A percentages against 1 Grade-A headcount** and concluded, correctly for the aggregate, that headcounts were the weaker column. **Inside these three rows the relationship inverts, and it inverts every time:**

| Row | Headcount | Percentage | Which is better sourced? |
|---|---|---|---|
| **5 — Block, Inc.** | "nearly 4,000 jobs", attributed to Dorsey's announcement → **B** | "40%" — **The Block's headline only**, unattributed in the body → **C** | headcount |
| **12 — OP Labs** | "laid off 20 employees … according to a message shared by the group's leadership" → **B** | **absent from the cited source entirely** — CoinDesk says it *asked* and prints no figure → **C** | headcount |
| **24 — Bitwise** | "to around 155", firm-stated → **B**; the ~25 *delta* still derived → **E** | "by 14%", firm-stated in an emailed CEO statement → **B** | both, but the endpoint beats the delta |

> 🟢 **PERMITTED, scoped to these three rows:** *In each of the three worst-graded rows in this tracker, the headcount figure traces to the firm and the percentage does not. In two of the three, the percentage is the outlet's own arithmetic or headline framing rather than anything the firm said.*
> 🔴 **PROHIBITED:** generalising this to the tracker. n=3, and they were selected *because* they were Grade C on both columns. **The aggregate ladder of 08-25 stands unamended.**

---

## Row 5 — Block, Inc. [PERIMETER] — three fields moved

**Primary:** The Block, *"Block Inc slashes 40% of its staff as Jack Dorsey pushes 'smaller, flatter' AI strategy"*, Jason Shubnell, **published February 26, 2026 4:58PM EST, updated 5:29PM EST.**
`theblock.co/post/391520/…` → canonical `https://www.theblock.co/news/business/2026-02-26-block-inc-slashes-40-staff-jack-dorsey-pushes-smaller-flatter-ai-strategy-391520`

⚠ **Provenance-refused on the first attempt** (`web_fetch`: *"URL not in provenance set"*) and **rescued by search-then-fetch** — the documented path, which failed for ConsenSys on 08-25 and worked here. Watch (i), thirteenth run.

### 🟢 Date: `2026-02` → **`2026-02-26`**, and the 08-06 derivation is vindicated
The 08-06 correction moved this row from a wrong "2026-Q2" to a derived "2026-02", reasoning from two March articles that said "last month". **The derivation was right and is now exact.** Three independent confirmations: the canonical URL path (`2026-02-26`), the byline, and Dorsey having *"wrote Thursday in a post on X"* — 26 February 2026 is a Thursday. CNN's own URL path (`cnn.com/2026/02/26/business/block-layoffs-ai-jack-dorsey`) carries the same date.

### 🔴 The open "4,000 / 40% reconciliation" is resolved — against the percentage
Dorsey stated **endpoints**, in a note to the company: *"reducing its staff from over 10,000 people to just under 6,000."*

- **"nearly 4,000 jobs"** is attributed to his announcement → **C → B**.
- **"40%"** appears **only in The Block's headline**, is **not attributed to Dorsey anywhere in the body**, and is **arithmetically a floor**: *over* 10,000 falling to *just under* 6,000 is a reduction of **more than** 40%. → **stays C, deliberately.**

**This is the Crypto.com defect running the other way.** At Crypto.com the firm stated the percentage and the outlet derived the headcount (`180`, struck 08-22). Here the firm stated the endpoints and the outlet derived **both**. The safest printable Block figure is neither: it is **"over 10,000 → just under 6,000."**

### 🟢 AI cover: **C → A**
Dorsey's own words, via his note and X post: restructuring to become **"smaller"**, **"flatter,"** and AI-first; AI and **"intelligence tools"** are *"fundamentally changing how the company operates"*; verbatim: **"A decision at this scale carries risk, but so does standing still."**
⚠ The X post (`x.com/jack/status/2027129697092731343`) is **linked but not fetched** — X is not reachable from this lane. The quotes are The Block's verbatim reproduction. Grade A is assigned on a firm statement *captured verbatim by the outlet*, which is the ladder's definition.

**Effect on the tracker-wide figure:** Grade-A AI-cover **4/25 (16.0%) → 5/25 (20.0%)**. Block, Inc. joins Crypto.com, Gemini, BitGo and Dune Analytics.

### New context entered
Bloomberg reported on **2026-02-08** that Block was looking to cut **up to 10%** of its workforce. The executed cut was ~40%. **A four-fold gap between the trailed figure and the executed one, eighteen days apart.** Severance: 20 weeks' pay plus one week per year of tenure. Stock closed $54.53 and rose >20% after-hours; >900 employees cut about a year earlier.

**Still not asserted:** any marketing-function impact. No captured source names a function.

---

## Row 12 — OP Labs (Optimism) [TRACKED — Stratum 2] — one upgrade, one confirmed-worse

**Primary:** CoinDesk, *"Ethereum layer-2 developer OP Labs cuts roles to 'narrow focus'"*, Margaux Nijkerk, edited by Nikhilesh De. `meta-parsely-pub-date: 2026-03-12T16:19:31.389Z`.
⚠ Also provenance-refused first, also rescued by search-then-fetch.

- **Date `2026-03-12` confirmed exact** from the article's own machine-readable publication field — the strongest form of date corroboration this corpus has, and the one `date-provenance-audit.py` was built to look for.
- **Headcount `20` → Grade B.** *"has laid off 20 employees … according to a message shared by the group's leadership."*
- 🔴 **Percentage stays C, and the row's caveat is confirmed correct at source — the source does not contain the figure at all.** CoinDesk's own closing line: *"CoinDesk reached out to OP Labs for comment and to clarify the percentage of staff that was laid off."* The ~19.6%/20% comes from **The Block's headline**, not from this row's `source_url`. **The corpus recorded "secondary-reported, not firm-confirmed" without having read the source; the source turns out to be stronger evidence for the caveat than the caveat was.**
- **All three verbatim quotes confirmed word-for-word**, so the `N` label is firm-stated and stands: *"This is not about finances"* / *"OP Labs is well capitalized with years of runway"* (Slack message shared alongside the X post) / *"do fewer things … exceptionally well."*
- **New detail:** the token move the row carried as "the OP token fell" is now dated and quantified — *"down roughly 3% over the last 24 hours"* as of 2026-03-12. Ecosystem context confirmed at source: Base, Unichain and Soneium all build on the OP Stack.
- **Not entered** (secondary only): severance reported elsewhere as 3–5 months' base pay plus 6 months' healthcare.

---

## Row 24 — Bitwise [PERIMETER] — the corpus's first figure-grade UPGRADE, and a date tension that was never a conflict

**Second, independent primary:** The Block, *"Bitwise cuts 14% of staff as crypto layoffs mount during market downturn"*, Timmy Shen, **August 12, 2026 1:52AM EDT** — `https://www.theblock.co/news/business/2026-08-12-bitwise-layoffs-411522`. Fetched clean, first attempt.

The row was built entirely on **The Crypto Times relaying Bloomberg**. The Block is a **separate chain** and it carries something the first capture did not: **a direct firm statement to a named outlet.**

- 🟢 **Percentage `-14%`: C → B.** *"Bitwise Asset Management said it has trimmed its global team by 14% to 155 employees"* / *"CEO Hunter Horsley told The Block **in an emailed statement**…"*
- **Headcount: the `155` endpoint is now firm-stated (B); the `~25` delta stays E.** The Block never states 180 — that starting point is still back-derived from 155/(1−0.14). **Print "to around 155", not "about 25 cut."**
- 🟢 **The `N` label gains a firm verbatim**, replacing a paraphrase of a paraphrase. Horsley: the adjustment **"equips us well for the ongoing growth we've seen this year and expect to continue as crypto further integrates into the global economy."** No AI framing from the firm.

### ⭐ The four-candidate date problem was a FIELD-SEMANTICS problem all along
The row carried three candidates — 08-07 (CryptoJobsList), 08-11 (Bloomberg URL slug), 08-12 (Crypto Times prose) — recorded as unresolved tension under watches (o) and (aa).

**Horsley told The Block the team was trimmed "last week," relative to publication on Wednesday 12 August 2026.** That places the **cut** in the week of **3–9 August** — which **corroborates the aggregator's 08-07 as an *event* date** and leaves 08-11 and 08-12 as ***reporting* dates.**

> **The three candidates were never in conflict. `date_announced` conflates "when the cut happened" with "when it was first reported."**
> **The cell stays `2026-08-11 [VERIFY]`** — not because the evidence is thin, but because **the field's own definition is what is ambiguous**, and redefining a schema field five days from ship is a worse error than carrying a labelled one.
> ⚠ **Note for ship: the source the corpus trusted least — a jobs aggregator — is the one the CEO's own words support.** Recorded as an instance of watch (ss) inverted: a *disconfirming-looking* item got less scrutiny than the authoritative-looking slug that turned out to be a reporting date.

### ⭐ Outlet-level AI framing, observable inside one document
The Block's own *"Layoffs continue"* section opens: *"Crypto industry layoffs continued into mid-2026 as companies responded to weaker market conditions and shifted toward AI-driven efficiencies"* — **in the same article in which the firm being reported on gives a purely non-AI rationale.** This is exactly what the Grade-C category exists to catch, and here it is visible in a single piece rather than inferred across sources.

**Market context at source:** BITW net assets fell **31% in the first seven months of 2026** (Bitwise's own fact sheet, linked by The Block, **not fetched**). Bitwise completed its acquisition of staking provider Chorus One in February 2026.

---

## Row 13 — Kraken — NOT OPENED, and why

`source_url` is Bloomberg (`bloomberg.com/news/articles/2026-05-15/kraken-cuts-150-workers-after-deploying-ai-ipo-may-slip-to-2027`) — **paywalled, and no non-paywalled primary exists** for the figures. The row's grades (C / C on figures, **D** on AI cover) already encode the strongest sourcing available: Bloomberg's `~150` and `−5%` are the outlet's, and the AI framing is attributed to *"a person familiar with the matter who was not authorized to speak publicly."*

**No attempt was made to route around the paywall.** Carried forward; **the row's grades are correct as they stand and do not need the fetch to be honest.**

---

## Updated tracker distributions (26 rows, 10 fields, post-edit)

| Column | A | B | C | D | E | UNCITED | n/a |
|---|---:|---:|---:|---:|---:|---:|---:|
| `headcount_grade` (14 graded) | 1 | **2** | 4 | 1 | 5 | 1 | 12 |
| `percentage_grade` (16 graded) | 4 | **3** | 8 | 1 | — | — | 10 |
| `ai_cover_grade` | **5** | 2 | — | 1 | 1 | — | 17 |

**Movements today:** headcount B 0→2 (Block, OP Labs) · percentage B 2→3 (Bitwise) · AI-cover A 4→5 (Block).

> 🔴 **UNCHANGED AND STILL PROHIBITED:** any aggregate headcount sentence. **Fourteen rows carry a headcount figure and exactly one is Grade A** (Gnosis, scoped to two teams at a perimeter firm). Two are now Grade B. That is three of fourteen with any firm attribution at all.
> 🟢 **PERMITTED, updated:** *Of the twenty-five adjudicable 2026 crypto workforce reductions this corpus records, nine are framed around AI and **five** carry a verbatim statement from the firm itself — **20%**.*
> 🔴 **The adjudicable denominator remains 25, not 26.** Row 6 (MARA) was never labelled, remains uncited, and remains flagged to STRIKE at ship.

---

## Explicit non-claims

1. **No figure was changed.** `headcount_change` and `percentage` cells are byte-identical to before this run in all 26 rows; only `date_announced` on row 5, three grade cells, and three notes fields moved.
2. **No marketing-function impact is asserted for any of the three rows.** None of the captured sources names a function.
3. **The percentage-is-weaker finding is scoped to rows 5, 12 and 24** and is stated as selection-biased on its face.
4. **Bitwise's `date_announced` is not resolved**, only better understood; no candidate is promoted.
5. **Dorsey's X post and Jing Wang's X post were not fetched.** Both are quoted only as the outlets reproduce them, and both are labelled that way.
6. **No paywall was circumvented.** Row 13 stands unopened and is recorded as unopened.

# Citation-opening sweep — 2026-08-22 — **three citations opened, three corpus defects found**

**Instruction executed:** recommendation 1 of the 2026-08-21 run — *"open the ten unread citations; do three per run."* Watch (uu).
**Method:** fetch the row's own cited article first-party; read the publication metadata, the firm-primary link, the verbatim rationale, and any figure the outlet attributes to itself rather than to the firm.
**Result: 3 of 3 fetches changed the row.** One closed a `[VERIFY]`, one downgraded a figure the report was carrying as firm-stated, one strengthened a finding the row was understating.

---

## 🔴 First, the blocker — and it is recommendation 1's own blocker

**The URLs already committed in `2026-layoff-tracker.csv` cannot be fetched directly.** `web_fetch` returned:

> *"URL not in provenance set. web_fetch can only retrieve URLs that appeared in a user message, a prior web_fetch result, or a WebSearch result."*

**This is escalation (i) / watch (jj), now nine runs old, and today it blocked the single piece of work the last run named as the highest-yield remaining in the corpus.** A URL this repo has carried in a committed file for weeks is not reachable by the run that committed it.

**Workaround used, and it should be written into the method rather than rediscovered:** run a `WebSearch` that surfaces the article, which admits its URL to the provenance set, then fetch. **It cost one extra search per citation and it worked 3 for 3.** It is not free — it only works for articles a search can find, so a row whose citation is an X post, a PDF, or an SEC EDGAR document (rows 9, 10, 17) stays blocked.

**Fix remains one edit:** paste the tracker's URLs verbatim into the scheduled-task prompt.

---

## 1. Row 1 — Crypto.com — 🔴 **THE FIGURE IS DERIVED, NOT DISCLOSED. SAME DEFECT AS ALGORAND.**

**Captured:** The Block, *"Crypto.com cuts around 12% of staff as CEO pushes enterprise-wide AI integration"*, by Brian Danga, **published 2026-03-19 06:43 EDT**.
`https://www.theblock.co/news/markets/2026-03-19-crypto-com-cuts-around-12-of-staff-as-ceo-pushes-ai-integration-394318`

The tracker carried **`headcount_change = 180`** with a `[VERIFY]` open since 08-11. The capture closes it — **and disqualifies the number as a firm disclosure.** The outlet says so itself:

> *"The reduction affects roughly 180 employees, **based on the company's previously disclosed headcount of over 1,500**."*

**The firm disclosed a percentage. The 180 is the outlet's arithmetic on a headcount figure from an earlier disclosure.** Relabelled **`~180 [DERIVED — NOT FIRM-STATED]`**.

**This is the Algorand defect again, one run later, in a different row.** On 08-21 the corpus found it was advertising a percentage it could not source. Today it finds it is carrying a headcount the firm never said. **Two of the three named class-5 examples in `README.md` have now failed inspection in two consecutive runs.** That is no longer a coincidence about two rows; it is a fact about how numbers entered this tracker.

**Verbatim firm rationale** (CEO Kris Marszalek, via the captured outlet; X post `https://x.com/kris/status/2034539285232398798` **named, not fetched, not guessed**):

> *"We are joining the list of companies integrating enterprise-wide AI. Companies that do not make this pivot immediately will fail. Companies that move slowly will be left behind. Companies that move immediately and pair the best AI tools with top-performers will achieve a level of scale and precision that was previously impossible."*

— and the cuts target roles that **"do not adapt."** **No function is named. Marketing is not named.**

**Class-4 candidate refused on role grounds:** Marszalek is CEO, not a marketing operator. `methodology.md` §4 requires CMO / VP Marketing / Head of Brand / Head of Growth. **Not admitted.** Recorded so a later run does not re-discover and re-refuse it. (Watch (l): this is the fourth costing of the §4 role perimeter in nine runs, and it keeps refusing the most quotable AI-and-headcount material in the corpus.)

---

## 2. Row 23 — MVMT Labs — **`[VERIFY]` closed on the event, still open on the day**

**Captured:** CoinDesk, *"Movement Labs files for Chapter 11 bankruptcy months after token scandal"*, Helene Braun and **"AI Boost"**, edited by Nikhilesh De. `parsely-pub-date` **2026-07-21T17:54:40.853Z**; UPDATE 17:58 UTC; CORRECTION 18:26 UTC.

**Citation upgraded** from a 2026-08-09 shakeout round-up (25 days after the event → `LAG-EXCEEDED`) to the event article itself (6 days → **`SELF-DATED`**, flag clears). **Class-5 `LAG-EXCEEDED` count: 2 → 1.**

Confirmed first-party: Chapter 11 by **MVMT Labs, Inc.**; under 1,000 creditors; assets $100,000–$500,000; liabilities north of $1 million; largest creditors include co-founder Rushi Manche, the Delaware Division of Revenue and Anchorage Digital.

**The article carries its own correction and the corpus must honour it:** the June pivot to stablecoin payments was by **Move Industries**, *"a separate legal entity from MVMT Labs, the company that filed for bankruptcy."* Any report sentence merging the two is wrong.

⚠ **The 2026-07-15 filing date is NOT first-party.** The captured article states no filing date. 07-15 rests on secondary round-ups only. Carried as **`[DATE-VERIFY]`** — **the event is verified, the day is not.** Docket named, not fetched, not guessed: `https://www.pacermonitor.com/public/case/65708680/MVMT_Labs,_Inc`.

**No function named. Not a marketing cut.**

### ⭐ A source-quality observation that belongs in the methodology appendix

**This CoinDesk article lists an AI system as a co-author** (`meta-author_2: ai-boost`) and carries:

> *"AI Disclaimer: Parts of this article were generated with the assistance from AI tools and reviewed by our editorial team to ensure accuracy and adherence to our standards."*

**A report about AI's effect on crypto marketing is partly evidenced by articles that are themselves partly AI-generated.** That is not a reason to reject the source — CoinDesk discloses it, an editor is named, and the article carries a same-day human correction, which is more provenance than most of the corpus's citations offer. **It is a reason to say so out loud.** The corpus already records `capture_ai_disclosure` on class-4 files (see the Cointelegraph note in the 08-11 candidate). **Recommendation: extend that field to class 5, and put one honest line in the methodology appendix.** It is the same move as publishing the corpus — the credibility comes from disclosing it first.

---

## 3. Row 25 — MANTRA — ⭐ **THE ROW WAS UNDERSTATING ITSELF**

**Captured:** The Block, *"MANTRA cuts staff amid restructuring as OM token remains 99% below peak"*, by Brian Danga, **published 2026-01-14 08:56 EST, updated 09:12 EST**. Recorded date **confirmed to the day**.

The row was labelled `[PERIMETER — NAMES MARKETING]`. **The capture shows marketing is not merely named among affected functions — it is named in the set affected *disproportionately*:**

> *"The decision impacts teams across the organization, with functions like **business development, marketing, and HR affected more than others**, according to the post."*

**This is now the strongest function-level statement in the tracker.** Of 25 rows: 23 name no function at all; Gnosis (row 14) names marketing inside a six-function list of roles the firm was helping place; **MANTRA names marketing inside a three-function set the firm says was hit harder than the rest.**

**Firm primary** (CEO John Patrick Mullin, X post `https://x.com/jp_mullin888/status/2011367190868738403` — **named, not fetched, not guessed**), verbatim via the captured outlet:

> the *"incredibly unfortunate and frankly unfair events of April 2025"*, a prolonged market downturn and increased competition rendered the cost structure **"unsustainable"**
> *"To thrive in this environment and take back our market-leading position, we must become more capital-efficient and laser-focused."*

**Rationale is market conditions and competition. AI appears nowhere in the capture.** Headcount **refused** — the firm said *"an unspecified number."*

⚠ **Limit, and it is the same one that governs the whole Theme-5 read:** this is a **perimeter** firm, not a Stratum 1–4 tracked firm. **Both rows that name marketing are perimeter rows.** No tracked-cohort firm has named marketing as an affected function in any of the 25. **That contrast is the finding — do not print the marketing-is-hit-hardest line as though it were a cohort result.**

---

## Cross-verification bonus — yesterday's repair independently reproduced

The Crypto.com capture, fetched for an unrelated row, independently reproduces the **Algorand** repair made on 08-21:

> *"On Wednesday, the Algorand Foundation [said] it reduced its workforce by **25%**, citing **'the uncertain global macro environment as well as the broader downturn in crypto markets.'**"* — linking `https://x.com/AlgoFoundation/status/2034298850878652616`

**Same percentage, same verbatim rationale, same firm X post, from a second outlet captured for a different reason.** The 08-21 repair holds under independent corroboration.

The same article also corroborates rows 2 (Gemini — *"cut up to 200 positions … about a quarter of its workforce"*, February), 5 (Block — *"roughly 40%"*) and 19 (Messari — *"parted ways with many teammates"* as part of becoming an **"AI-first"** company).

---

## Running score on the non-AI streak

| Row opened today | Stated rationale | AI cover? |
|---|---|---|
| Crypto.com | enterprise-wide AI; roles that *"do not adapt"* | **YES — explicit** |
| MVMT Labs | Chapter 11; token scandal, governance, failed strategic reset | no |
| MANTRA | April 2025 events, market downturn, competition | **no — AI absent from the capture** |

**Watch (h′) is still rejected and still untested.** Nothing here tests whether rationale correlates with firm type; three rows is not a test. **Do not print it.**

---

## Seven rows still unread

Rows **6 (MARA — uncited, strike-if-unsourced), 8 (BitGo — aggregator URL), 9 (Polygon — X post), 10 (Exodus — SEC EDGAR), 14 (Gnosis), 15 (Luno), 17 (BitMart)**.

**Rows 9, 10 and 17 will not yield to the search-then-fetch workaround** — an X post, an EDGAR exhibit and a firm support-centre article are not reliably surfaced by a keyword search. **Those three need the provenance fix in escalation (i), or they stay unread through ship.**

# Class-5 citation-opening sweep — 2026-08-23 (rows 8, 14, 15)

**Mandate:** recommendation 1 of the 08-22 run — *"KEEP OPENING CITATIONS — WATCH (vv). THREE MORE. Rows 14 (Gnosis), 15 (Luno), 8 (BitGo)."*
**Method:** search-then-fetch (WebSearch to admit the URL, then `web_fetch`), per the 08-22 workaround. **3 for 3 again; 6 for 6 across two runs.**
**Result:** 3 citations opened · 1 aggregator citation retired · 1 date corrected · 2 figure labels weakened · 1 headcount recovered · 1 new row added · 1 unrelated Theme-2 finding extracted.

---

## Headline: the sweep is now 5-for-5 on finding defects, and today it found a fourth kind

Three runs, five rows opened, five different failure modes:

| Run | Row | What reading the citation revealed | Kind of defect |
|---|---|---|---|
| 08-21 | Algorand | percentage advertised in `README.md` had **no citation at all** | missing citation |
| 08-22 | Crypto.com | headcount `180` was **the outlet's arithmetic** | derived figure printed as disclosure |
| 08-22 | MANTRA | row **understated** its own evidence | under-claim |
| **08-23** | **Luno** | `-20%` is **Bloomberg's figure; the CEO declined the number** | derived figure printed as disclosure |
| **08-23** | **BitGo** | citation was a **rolling undated aggregator page** — and it had supplied a wrong date | **unstable citation** |
| **08-23** | **Gnosis** | `undisclosed` was **disclosed**, in a reply nobody had scrolled to | under-claim |

**Watch (vv) restated, and it is now earned five times over: an unread citation makes a row wrong in an unknown direction.** Four rows remain unread and reachable; three (9, 10, 17) remain unreachable without the provenance fix.

---

## Row 8 — BitGo. The weakest citation in the tracker is gone.

**Was:** `https://cryptojobslist.com/crypto-layoffs` — a **rolling, undated aggregator page**. Its contents change under the citation; it carries no publication date; and it is the same source class row 10 (Exodus) documents as unreliable (77 SEC-sourced vs 54 aggregator for the same event).

**Now:** The Block, Danny Park, canonical `https://www.theblock.co/news/business/2026-06-25-bitgo-layoff-ai-infrastructure-406266`, published **June 25 2026, 11:43PM EDT.** Fetched HTTP 200, full body.

### What opening it produced

1. **The primary now has a durable URL.** The row has carried *"primary X post pending durable URL"* since 2026-06-28. Closed: **Mike Belshe, `https://x.com/mikebelshe/status/2070240967479996463`**, linked and quoted by The Block. (The X post itself was not fetched — provenance rule.)

2. **Verbatim CEO rationale, captured:**
   > *"The ecosystem has evolved, and the way we build financial services has changed dramatically. To keep winning for our clients, we need to be sharper, more focused, and concentrate our people and energy on the areas that matter most: security, trading, stablecoins, settlement, and AI-powered infrastructure."*

   **`ai_cover_narrative = Y` is CONFIRMED FIRM-STATED.** *"AI-powered infrastructure"* is the CEO's own phrase. This matters because today's Luno finding shows the Y column is not uniformly earned — BitGo's is; Kraken's (row 13) is anonymously sourced; Luno's (row 15) is inferred.

3. **🔴 A headcount was available and was REFUSED.** Secondary reporting derives **~90** from the 603 FTE in BitGo's 2025 annual report. **That is arithmetic, not a disclosure** — identical in kind to the Crypto.com `180` downgraded yesterday. The Block states no headcount. **The cell stays empty.** The corpus declined a number it could have had, for the second consecutive run.

4. **The date was wrong, and the retired citation is why.** See below.

5. **Context worth one line in Theme 5:** The Block reports BitGo's Q1-2026 revenue **+112.6% YoY to $3.8B** with net losses widening to **$60.7M from $25.7M**. **This is a cut made into revenue growth, not into revenue collapse** — which is a different fact from the "crypto downturn" framing most rows carry.

### 🔴 Date corrected 2026-06-26 → 2026-06-25, adjudicated by hand

`date-provenance-audit.py` raised a **DATE-INVERSION**: url date `2026-06-25` preceding recorded event date `2026-06-26` by 1 day.

**The flag was TRUE.** This is recorded emphatically because the guard's *previous* two DATE-INVERSIONs (2026-08-21) were both **script defects**, and watch (tt) requires that every flag be adjudicated by hand rather than believed or dismissed by reputation. The guard has now been wrong twice and right once, and the only way to know which is to look.

**Adjudication.** The 1-day gap is the signature of a timezone split (11:43PM EDT 25 Jun = 03:43 UTC 26 Jun). Both values are defensible in isolation. But the tracker's convention throughout is **the publisher's own stated date** — rows 4, 20, 21, 25 and 26 all match their publisher exactly. BitGo's `2026-06-26` was the sole UTC-converted row, and it was **inherited from the CryptoJobsList aggregator page that was this row's citation until today.**

**Retiring the aggregator citation also corrected the date the aggregator supplied.** That is the general lesson: an unstable citation does not merely fail to support a row, it silently *populates* it.

**🔴 Rule adopted, and a temptation refused.** The obvious "fix" was to widen the guard's tolerance to ±1 day so timezone splits stop firing. **That would have been a guard weakened by the person it inconvenienced** — the exact move refused on 08-22 for the class-4 `NO-URL` files. Instead: **`date_announced` = the publisher's own stated date, in the publisher's own timezone.** The predicate is untouched. `DATE-INVERSION` returns to 0 by fixing the corpus, not the tool.

---

## Row 15 — Luno. Two labels changed; both got weaker.

**Was:** Cointelegraph near-primary. **Now:** CoinDesk, Francisco Rodrigues, ed. Jamie Crawley, `parsely-pub-date 2026-07-30T09:54:18.801Z`. HTTP 200, full body. Bloomberg original **remains paywalled and uncaptured.**

### 1. 🔴 The −20% is not firm-stated

CoinDesk, verbatim: Luno is cutting about 20% of its global workforce *"according to a report by Bloomberg on Thursday"* — and:

> *"The firm's CEO James Lanigan confirmed the cuts to Bloomberg but declined to disclose the number of employees affected."*

**The firm confirmed THAT. The size is Bloomberg's.** Relabelled `-20% [REPORTED BY BLOOMBERG — CEO CONFIRMED THE CUTS, DECLINED THE NUMBER]`.

**Third row in three runs carrying a number no firm stated.** The pattern is now stable enough to name a mechanism: *a firm confirms an event, a reporter supplies a magnitude, and the magnitude travels as though the firm had said it.* Today's class-5 search surfaced `layoffhedge.com/company/cryptocom` titled **"Crypto.com Layoffs 2026 - 180 Jobs Cut"** — **the derived figure this corpus downgraded yesterday, now propagating through aggregators as a headline number.** The defect is not hypothetical and it is not ours alone.

### 2. ⚠ The AI label is an inference, not a quote — and this one generalises

Lanigan's word is **automation**:

> *"investments in automation and other operational improvements over the past year had changed the resources needed to run the business."*

**Neither CoinDesk nor the firm says "AI" anywhere in this capture.** Relabelled `Y [INFERRED FROM "AUTOMATION" — FIRM DID NOT SAY "AI"]`.

**🔴 This is bigger than one row.** If *automation* has been silently read as *AI* elsewhere in the tracker, **the AI-cover share is inflated** — and the AI-cover share is a headline number in Theme 5. **Audit every `Y` row for the same substitution before Phase 2 prints a proportion.** Present state of the column, on today's evidence: BitGo `Y` firm-stated · Dune `Y` firm-stated · Kraken `Y` anonymously sourced · Luno `Y` inferred. **Four rows, three different epistemic grades, one column.** The column needs a grade field or it needs to stop being counted.

### 3. New facts not previously in the row

- **A market exit:** *"Luno's decision to stop serving customers in some markets from Sept. 1 and concentrate on Africa and Southeast Asia."* A retail-brand withdrawal from named markets is a **Theme-4 promotional-surface event**, not merely a headcount event. Worth a promotional-teardown check after Sept 1 — does the marketing estate in the exited markets come down?
- **A consumer brand becoming an infrastructure supplier:** the new structure combines the 16M-user retail exchange with a **white-label service for banks, fintechs and telcos**, Luno supplying liquidity, wallets and compliance infrastructure. **Theme 1.** Convergent with Gnosis Pay's B2B2C pivot (row 14) and Exodus's payments pivot (row 10).
- **Corroboration by-product:** the same article independently confirms rows 11 (BitMEX) and 17 (BitMart) as wind-downs.

---

## Row 14 — Gnosis. The highest-value verification item in the corpus is CLOSED, and it resolved in both directions at once.

**Was:** Cointelegraph near-primary; both primaries uncaptured since 2026-07-30. **Now:** the firm's own document — `https://forum.gnosis.io/t/gnosis-ltd-quarterly-report-q2-2026/12391`, fetched HTTP 200, full body, `article:published_time 2026-07-17T14:32:46+00:00`.

### 1. The marketing claim: CONFIRMED NARROW

**The quarterly report does not name marketing as an affected function anywhere.** It contains a Marketing section, and that section describes *ongoing marketing activity*, not cuts.

**crypto.news's silence on this was correct reporting, not an omission** — the 08-01 note suspected as much and was right. The marketing claim rests **solely** on the X post (`x.com/gnosis_/status/2082042883939672541`, still uncaptured), as relayed verbatim by Cointelegraph and Coingabbar.

**🔴 RULING: do not print Gnosis as a firm that disclosed a marketing cut in its quarterly report. It did not.** It listed marketing among functions in a **hiring-referral post on X**. Those are different acts with different evidentiary weight. The tracker-scoped *"first row naming marketing"* finding survives and is now precisely bounded — which is the outcome a verification item is supposed to produce.

### 2. ⭐ The headcount was disclosed — in a reply

`headcount_change` read `undisclosed`. It was disclosed on **20 July 2026 at 3:37pm**, three days after publication, by Kenk (Gnosis Ltd), answering a governance question that asked for it directly (*"What is the exact headcount and payroll being eliminated?"*):

> *"The App and Circles teams went from 28 to 14."*

**−14 people. −50%. Firm-stated.** Recorded as `App + Circles teams 28 -> 14 [FIRM-STATED, TEAM-SCOPED — NOT COMPANY-WIDE]`. **Scope discipline: this is scoped to two product teams, not to Gnosis Ltd.** Kenk explicitly declined burn-reduction detail.

**The lesson is procedural and it is new.** The figure was public for thirty-four days, one scroll below a document the corpus had already decided it could not capture. **A forum thread's replies are part of the primary source.** Add to the class-5 capture protocol: *when the primary is a forum or comment-bearing post, read the thread, not the post.*

### 3. Verbatim rationale, now first-party

Co-founder **Friederike Ernst**:

> *"On Gnosis App: growth has been linear, and linear is not good enough for a consumer product. … The consequence was a difficult one: we significantly reduced the team."*
> *"These decisions were taken in the first week of July, after the quarter closed."*

**Two dates, recorded separately [watch (o)]: the DECISION is first week of July 2026; 2026-07-17 is the PUBLICATION.** Rationale type **non-AI**, confirmed at source.

### 4. 🔴 A second, earlier restructuring is disclosed and is not in the tracker

> *"Two things slowed the quarter: the restructuring early in Q2, and the June Gnosis Pay service halt."*

An **early-Q2 (April 2026) restructuring at Gnosis** is firm-stated, undated and unquantified. **Lead only — not entered as a row without a date and a scope.** Recorded so it is not re-discovered as new.

### 5. ⭐ The document contained something better than the row we opened it for

The same quarterly report carries a **firm-published Marketing section** stating *"We embedded AI across the marketing and comms function"*, naming SEO/**GEO** as a Q3 workstream, and describing a B2C→B2B marketing reorientation. **Full record: `../operator-statements/gnosis-q2-2026-quarterly-marketing-section-2026-07-17.md`.**

**Note what happened: a class-5 verification task produced the run's best Theme-2 evidence.** Watch (n) — the full-range re-sweep — vindicated again, and from an unexpected direction.

---

## Row 26 added — Dune Analytics [PERIMETER]

Surfaced as a by-product of opening row 8 (The Block cross-referenced it), captured first-party the same run: The Block, Daniel Kuhn, **May 14 2026 11:58AM EDT**, HTTP 200.

Primary: CEO **Fredrik Haga** on X (`https://x.com/hagaetc/status/2054937771811192837`), quoted verbatim:

> *"We're restructuring Dune to sharpen our focus around the core data products thousands of customers across the crypto industry rely on. That unfortunately means we've let 25% of the team go this week."*

> *"With Dune MCP, teams and agents can now build dashboards and workflows without needing to know anything about SQL nor data infrastructure (and associated bills)."*

**Why this row is worth having on the day the tracker learned to distrust its own percentages: the −25% is in the CEO's own words.** `-25% [FIRM-STATED VERBATIM BY CEO]`, `ai_cover_narrative Y [FIRM-STATED]` with an explicit product-AI-to-headcount link. It is the clean counter-example to Luno and Crypto.com in the same run that found them.

**Lead flagged, not admitted:** the same article reports **Blockworks and DL News both shut down their entire newsrooms in 2026** to focus on research and data products. Crypto-media contraction, adjacent to the content/marketing surface, but neither firm is in the cohort or the perimeter as currently defined. **Needs a scope decision before admission.**

---

## Tracker state after this sweep

**26 rows** (was 25). `date-provenance-audit.py` class-5 verdicts: `SELF-DATED` 13 → **15**, `NO-URL-DATE` 10 → **8**, `DATE-INVERSION` 1 → **0** (raised and cleared within the run), `NO-URL` holds at **1** (MARA Holdings — **still flagged to strike if unsourced by ship, nine days out**), `LAG-EXCEEDED` holds at **1** (Pump.fun).

## Still unread · still unreachable

- **Reachable, unread (4):** rows 2 (Gemini −30%, **named in the public README** and the last of the three advertised examples not yet inspected), 5 (Block Inc), 12 (OP Labs), 13 (Kraken).
- **🔴 Unreachable without the provenance fix (3):** row 9 (X post), row 10 (SEC EDGAR exhibit), row 17 (firm support-centre article). **Ninth run. These will ship unread.** Escalation (i).

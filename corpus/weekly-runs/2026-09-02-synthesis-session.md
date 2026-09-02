# 2026-09-02 — SYNTHESIS SESSION (CoS, out-of-band; not a 15:07 loop run)

**KPI — units done of 11: 8.** Units 1–8 complete. Remaining: 9–10 (citation audit), 11 (bundle + proof). **Publish 2026-09-15, unchanged.**

> This is not a scheduled-loop run record. It is written to the same file convention so the loop
> reads it as one, because the loop's next run must know these units are done or it will redraft
> Chapter 6 tomorrow at 15:07.

## What was done

| unit | output | words | URLs traced |
|---|---|---|---|
| 1 | `findings/05-next-twelve-months.md` — Theme 5, layoffs / next twelve months | 4,946 | 45 / 45 |
| 2 | `findings/01-shape-of-the-function.md` — Theme 1 | 4,462 | 59 / 59 |
| 3 | `findings/02-ai-in-the-stack.md` — Theme 2 | 3,684 | 29 / 29 |
| 4–5 | `findings/04-mica-readiness.md` — Theme 4, scorecard + narrative | 5,272 | 66 / 66 |
| 6 | `findings/03-agency-stack.md` — Theme 3 | 3,224 | 32 / 32 |
| 7 | `findings/06-closing-implications.md` — closing | 2,193 | derivative |
| 8 | Ch.1 correction + `report/state-of-crypto-marketing-2026.md` assembled | 21,740 total ≈ **19.8pp / 25pp** | — |

Two instruments were built rather than the work being done by hand, because both get re-run:

- **`scripts/verify_chapter_citations.py`** — the anti-fabrication gate. Every URL printed in a chapter
  must appear verbatim in a corpus record; a URL that appears nowhere else was invented and the gate
  refuses it. Handles both citation shapes in this report (full URL, and Chapter 1's bare-domain house
  style) — missing the second shape produced a silent false PASS on three chapters on the first run, and
  that is recorded here because it is exactly the failure class this cycle's post-mortem is about: **a
  check that cannot fail is not a check.** Negative-tested with two invented URLs before being trusted.
  Current state: **240 URLs across 7 chapters, 0 untraced, exit 0.**
- **`scripts/assemble_report.py`** — the report is assembled from the chapter files, never hand-written,
  so a chapter corrected in the citation audit reaches the report by re-running the script rather than by
  someone remembering. It prints every line of drafting apparatus it drops; an assembler that removes
  content silently is the same failure class as a report that re-dates itself silently.

## One correction to a chapter that already existed

**Chapter 1's "quiet copy" paragraph promised something this corpus does not contain.** It described an
audit sweep finding "live, quotable instances across dozens of firms" — *"unqualified 'maximum safety'
heroes, three-digit APY promotions with no on-page risk language, disclaimers that literally fail to
render"* — and forward-referenced a Chapter 5 per-firm scorecard in which "every entry was live-verified."

Repo-wide greps: **"maximum safety" appears only in that sentence. The highest APY figure anywhere in the
corpus is 10%. There is no record of a non-rendering disclaimer.** Public-copy observations exist for three
tracked firms (Kraken, OKX, Bitpanda), from the 08-01/02/03/05 promotional-teardown checkpoints.

The paragraph is rewritten to the record that exists — which is narrower and, on its own terms, sharper:
deadline-keyed campaign surfaces still live in the present tense with working CTAs two days after their
stated close, each read verbatim from a page fetched that day, each carrying the non-EEA-fetch qualifier.
The chapter carries a v0.4 changelog saying what was cut and why. **Nothing was cut for being inconvenient;
it was cut for being unevidenced.** Found by the Theme-4 drafting pass, not by any standing check.

## Corrections the chapters made to their own briefs (each narrows a claim)

1. **The layoff null is false as Chapter 1 stated it.** Two of 26 rows name marketing — Gnosis (07-17) and
   MANTRA (01-14), **both perimeter, zero tracked**. The cohort-scoped claim holds; the tracker-scoped one
   is retired.
2. **The AI-rationale share is 5 of 26 firm-verbatim (19%), not the naive 9 of 26 (35%).** One row is
   anonymously sourced, one is this corpus's own inference from "automation", one is `Y-ADJACENT` and
   barred. ⚠ `_ai-cover-narrative-grading-audit-2026-08-24.md` publishes **4/26** and grades Block as C;
   the CSV upgraded Block C→A on 08-27. **That audit file's share figure is stale and must be corrected
   before it is quoted.**
3. **The consumer-exchange / infrastructure split fails when tested**, and fails asymmetrically — it holds
   inside the seven tracked rows (4 vs 3) and breaks across the full record on Grade-A evidence. Reported
   as a failed test, not smoothed.
4. **Four agencies claim tracked firms, not five** — so **14 of 18** panel agencies claim no cohort firm,
   not 13. Seven name no client at all.
5. **Three `tracked-firms.md` annotations are unsupported by the 2026-06-15 panel** (KuCoin "three-agency
   overlap"; HTX "NinjaPromo relationship"; and `sport-sponsorship-reset-2026-05.md`'s "MarketAcross holds
   PR retainers at Binance and Crypto.com"). None printed; all flagged.
6. **The struck "Binance did not run a CMO search" limb is still live in two corpus files** —
   `cryptocom-kalifowitz-cmo-exit-primary-2026-08-11.md` and `longitudinal-2026-06.md` line ~1010. Not
   reproduced in any chapter. **Repair before the audit, or it returns.**
7. **Theme 4's scorecard cannot fill four columns** and says so on the page: KOL/influencer disclosure
   (zero creator posts examined for any tracked firm), regulatory-comms hire status, cost-disclosure
   prominence against the AFM's one-click/two-click standard, and risk-language outside the campaign panel.

## Post-window corpus check

None run this session — this was a synthesis session, not a loop run. The class-1 window stays frozen at
**2026-08-31** in `scripts/daily-corpus-sync.py`; nothing in this session touched it. The 09-03 15:07 run
does STEP 0 as normal and then takes **unit 9**, not unit 1.

## Open for the citation audit (units 9–10)

**47 `[VERIFY]` tags across seven chapters — that is the worklist.** The heaviest: Ferdon's quotes against
episode audio (machine transcript, ASR artefacts in the same text); the Bybit/Helen Liu datum, which is
uncited anywhere in the repo and is currently not citable; the six unread ESMA rows from the 08-25 capture;
the AMF forbearance quote (near-primary via The Block); the EEA-egress re-read of the lapsed campaign
surfaces; Bitwise's date (three candidates); and the recruitee adapter behind Tether's absence claim.

**And the standing distinction the audit exists to close:** the provenance gate certifies that a source
exists and is correctly dated. It does not certify that a source supports the sentence citing it. That
check has been run on **1 of 26** layoff rows. Units 9–10 are where that number moves.

## 🔴 Pre-existing exposure found by the end-of-session scan — surfaced, deliberately NOT patched

The loop's hard gate says *"nothing into the public repo that references the sales pipeline, prospects or
outreach."* The seven chapters and the assembled report are clean — scanned for pipeline, prospect,
outreach, cold-email, pricing and do-not-contact language, and for Ron Pruett / Boston Associates: **zero
hits in `findings/` and `report/`.**

**The tooling is not clean, and has not been since the sync script was written.** `scripts/daily-corpus-sync.py`
and `scripts/README.md` document their input paths verbatim in the public repo:

- `../northpoint/sales-funnel/prospects/open-positions.json` (docstring, `--sales` default, README table)
- `../northpoint/sales-funnel/competitor-intelligence/trend-data.json` (README table)

No prospect *data* is exposed — these are paths, not rows — but they state publicly that this report's
class-1 and class-2 feeds are produced by a sales funnel's prospect scanner, which is the association the
gate exists to prevent. It is already pushed and has been public for as long as the scripts have.

**Not patched in this session, on purpose.** `daily-corpus-sync.py` carries `CAPTURE_WINDOW_END` and the
class-1 window freeze; its path defaults are functional, and changing them to satisfy a naming concern
risks breaking the frozen-window behaviour the report's integrity now depends on, on the day the report
was finished. The safe fix is small and belongs to a session that can test it: take the feed root from an
environment variable or a required argument, and genericise the README's two table rows to "the daily ATS
scan feed" and "the 18-agency panel feed". **Recommend doing it before the 09-15 publish, since publishing
is what will send readers to this repo.** Jukka's call; one needs-jukka row's worth of decision, no more.

---

# SECOND PASS, same day — units 9, 10 and 11. **KPI: 11 of 11.**

## Unit 9–10a — the citation CONTENT audit

The provenance gate proves a printed URL exists in a corpus record. It cannot prove a source **supports the
sentence citing it**, and the appendix admitted that check stood at **1 of 26 layoff rows**. Four parallel
audits ran it against the live sources.

**318 claims adjudicated — 254 SUPPORTED · 30 PARTIAL · 25 CONTRADICTED · 9 NOT OPENED.**
Layoff-record content coverage: **1 of 26 → 24 of 26** (Kraken left unopened behind its paywall by design;
Messari not reached). Adjudications: `findings/_audit-*-content-check-2026-09-02.md`.

**Not one quotation in the report was a misquote.** Every firm-stated quote checked out verbatim. What failed,
failed in one direction: **the report overstated its own negatives, and anchored two true quotes to the wrong
document.** All 25 corrections narrow a claim.

The four worth remembering:

1. **The BaFin anchor, in three chapters.** The finfluencer-screening quote is real, exact, and on the *Risks in
   Focus 2026* chapter page — but was anchored only to the press release, which contains neither passage. **A
   compliance reader following that footnote would conclude we fabricated it.** Anchor split; substance untouched.
   This is the defect class a provenance gate structurally cannot catch: URL resolves, date right, regulator
   right, document family right, sentence not in it.
2. **The AMF "thirty-eight entries in 2026 alone" — CUT.** The register publishes no such count; the figure
   traced to a search-engine summary, and `amf-warning-list-sweep-2026-07.md` **expressly barred it from the
   report**. It reached the assembled draft anyway. A bar written into a corpus file does not enforce itself.
3. **Ferdon — cut to paraphrase in three chapters.** No publisher-issued transcript of that episode exists: the
   Acast surface was fetched (the "provenance-blocked" note was stale) and carries none and links to none. A
   machine-transcribed quotation attributed to a named executive at a tracked firm is the highest-consequence
   quotation type in this report. Substance kept, wording withdrawn.
4. **Chapter 6 overstated three refusals.** Robinhood never "explicitly declined" the AI framing — it never
   mentioned AI, and the avoidance is the reporter's inference. Uphold was called "explicitly non-AI" twice;
   **AI appears nowhere in that article.** Luno's "automation" is the outlet's paraphrase, not the CEO's word.
   Each correction makes the underlying grade *stronger*, because the inference chain is longer than stated.

Arithmetic repaired: Germany 70 → **73** of 324 (21.6% → 22.5%); a **third** source defect in the register parse
(a row delimiting fourteen member states with the letter "I" instead of a pipe) moves the pre-deadline comparator
34.1% → **33.8%** and widens the chapter's central contrast; ESMA non-compliance register 157 → **167** at source;
six non-AI July rows → seven; headcounts 14 → 13; percentages 16 → 17; firm-stated percentages 4 → 5; "nine of
twelve" US postings → **eight**; OP Labs' "about a fifth" re-attributed to The Block, which the firm never
confirmed and CoinDesk records asking for.

**The two time-sensitive claims were checked and HOLD.** The CMO succession null stands — and the documented trap
re-fired during the check and was re-caught (a "Crypto.com names new CMO" hit, document-dated **12 August 2020**,
announcing Kalifowitz himself). The FCA v Huobi stay was still in force. ⚠ **It expires 8 September, one week
BEFORE publication**, so Chapter 7's sentence was rewritten to stay true on the day and the standing caution now
lists it for a publication-morning re-check.

**The six previously-unread ESMA rows were read.** The live register is byte-identical to the 2026-08-25 capture,
and all six are German cooperative or regional banks holding domestic-only authorisations, touching no tracked
firm. **Branch A held**: every figure stays scoped "as at 2026-08-17". The gap is now measured rather than merely
disclosed, and it moves nothing except to strengthen the argument.

## A silent assembly defect, found by building the bundle

`assemble_report.py` split each chapter's citation block on `\n\*\*Citation anchors used[^\n]*\*\*`. On a one-line
anchor block full of `**bold**` spans that pattern is **greedy** — it consumed to the last `**` on the line, and
the split discarded it. **The assembled report was carrying 29 of the chapters' 82 URLs.** Roughly 53 citations
were being deleted from the report, silently, by the tool whose docstring promises it prints everything it drops.

Fixed with a lookahead split, and the assembler now carries a **citation guard**: it counts citation strings in
the chapters and in the output and fails the build if the report cites less than its chapters. Currently
**260 in, 260 through.** An instrument that could not detect its own worst failure mode now can.

## Units 10–11 — the bundle

`../publish-bundle/` (project level, outside the public repo — private until Jukka publishes):

- **`report.html`** — self-contained: no external CSS, JS, fonts or images. Print-styled. **175 live citation
  links.** The linkifier handles all three citation shapes in this report, including the one the audit created
  by upgrading bare citations to full URLs inside code spans — missing that shape produced 2 links in a report
  carrying 260 citations, and the first build shipped exactly that before it was caught.
- **`report.pdf`** — 43 pages, A4, headless-browser render. Sits inside the **40-page** figure both public
  surfaces promise. Three layout defects were found by rendering pages and reading them: markdown emphasis
  swallowed into a href on the cover; `page-break-inside:avoid` on tables taller than a page, which skipped a
  whole page and then broke the table anyway (now: repeating header rows, atomic rows); and long URLs
  overflowing the two-column back matter.
- **`PUBLISH.md`** — the runbook, including the three checks to run on the morning of 15 September.

**PUBLISH row filed** in `queues/needs-jukka.md` (144 words, linter-clean; the queue's 4 open findings are
pre-existing and elsewhere).

## What is left

Nothing this system can do. **Publishing is Jukka's act, on 15 September.** The date deliberately does not move
earlier: three public surfaces carry it, and beating a re-dated promise spends the credibility the honest
re-date bought.

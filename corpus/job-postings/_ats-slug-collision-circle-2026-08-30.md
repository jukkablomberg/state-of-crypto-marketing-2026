# Class-1 instrument defect — an ATS slug collision put a non-crypto SaaS into the crypto panel

**Source class:** 1 (job postings) — instrument record, not a corpus entry
**Published:** n/a (internal instrument finding)
**Captured:** 2026-08-30 (day 60 post-deadline)
**Status:** 🟢 **NO CORPUS CONTAMINATION.** The affected company is outside the Stratum 1–4 cohort, so the sync's cohort filter kept it out. **The defect is upstream of that filter and would not have been caught by it if the name had been in the cohort.**

---

## What happened

The 2026-08-30 upstream ATS scan returned **3 net-new marketing/growth postings**. Two of them:

| Company as labelled by the feed | Tier / category as labelled | Title | Posted | URL |
|---|---|---|---|---|
| **Circle** | **Tier 2 / Stablecoin** | Growth Lead, Discover | 2026-08-28 | `https://jobs.ashbyhq.com/circle/37d7acf2-3ce3-48cb-aa89-1120c72680f3` |
| **Circle** | **Tier 2 / Stablecoin** | Creative Director | 2026-08-28 | `https://jobs.ashbyhq.com/circle/3a63b143-e1df-4655-8a62-ec20a1e1f1eb` |

Both carry `url_verified: true`, `url_verify_reason: head_200`, a dated `posted_at`, and a `fit_score` of 100 and 85. **Every automated signal on these rows is green.**

The rows are mislabelled. The `description_excerpt` the feed captured from the postings themselves reads:

> "About Us   Circle is building the world's leading AI-powered, all-in-one platform for digital businesses. We make it possible for creators, coaches, educators, and businesses to bring together their audience with engaging discussions, live…"

That is **Circle (circle.so)** — the creator-community and online-course platform — not **Circle Internet Financial**, the USDC issuer the labels `Tier 2 / Stablecoin` describe.

## Verification

The discriminating evidence is the posting body, captured first-party by the ATS API fetch. It was corroborated independently against circle.so's own public copy, which carries the same boilerplate almost word for word: the platform "makes it possible for creators, coaches, educators, and businesses to bring together their audience with engaging discussions, live streams, events, chat, courses, and payments — all in one place, all under their own brand" (`https://circle.so/platform`).

⚠ **A search on the ATS slug alone does not resolve this.** Querying `jobs.ashbyhq.com/circle` returns *Circle Health* and *Funding Circle*, and general search for "Circle" returns the USDC issuer's description — i.e. **the search layer confirms the wrong company.** Only the posting body settles it. Recorded because the cheap check gives the wrong answer confidently.

## Corroborated by a second loop the same day

NorthPoint's Convertor (apply lane) processed **these same two rows** on 2026-08-30 and its log names the company **"Circle (circle.so)"** — identifying it correctly, because staging a job application forces a read of the job description. It additionally found the sister row (*Growth Lead, Discover*, fit 100) geo-ineligible on the JD's *"any North American time zone"* clause and recorded a **Lead Gen sourcing-filter miss** against it.

**Two loops at opposite ends of the same feed hit this within hours of each other. The one whose work requires reading the posting body caught it; the ones that consume the label did not.** That is the finding in one sentence.

## The mechanism

Company identity in the upstream feed is resolved by **ATS slug**, and `circle` on Ashby belongs to circle.so. The tier and category (`Tier 2`, `Stablecoin`) come from NorthPoint's own prospect table keyed on the display name **Circle**, which was entered for Circle Internet Financial. **The slug and the label were never checked against each other, and nothing downstream checks them either** — `url_verified: head_200` verifies that the URL resolves, not that it resolves to the company the row names.

## Why it did not reach the corpus, and why that is luck

`daily-corpus-sync.py` admits a posting only if the company maps to the Stratum 1–4 cohort. Circle is in neither `tracked-firms.md` nor any cohort alias, so both rows were dropped before the corpus saw them.

🔴 **That is a filter on the name, and the name was the thing that was wrong.** Had the colliding slug belonged to a *cohort* display name — Gemini, Phantom, Ledger and Kraken are all short, common English words with plausible non-crypto namesakes — two fabricated crypto marketing postings, URL-verified and correctly dated, would have entered `corpus/job-postings/<firm>.csv` with nothing in the pipeline positioned to object.

## Scope of the exposure, bounded

Cohort firms currently reachable by API and carrying a collision-prone common-word slug are the risk surface. A slug-vs-label reconciliation was run this session across **all 17 rows in the 13 tracked-firm posting CSVs**, extracting the company slug from each row's `source_url` and comparing it to the file's firm name.

**Result: 0 real mismatches.** The check raised two flags and **both were defects in the check, not in the corpus** — recorded in full, because a guard's first run is a test of the guard (rule adopted 2026-08-21):

| Flagged | Reality | Verdict |
|---|---|---|
| `gemini.csv` → slug `embed` | The URL is `boards.greenhouse.io/embed/job_app?**for=gemini**&token=…`. Greenhouse's embed form carries the company in a **query parameter**, not the path segment the extractor read. | 🟢 **False positive.** Identity is correct. |
| `optimism.csv` → slug `oplabs` | **OP Labs** is Optimism's development company — the same entity as layoff-tracker row 12, *"OP Labs (Optimism) [TRACKED — Stratum 2]"*. | 🟢 **Known-good alias**, not a collision. |

So the finding is **a live near-miss and a named residual risk**, not a discovered corruption. ⚠ And the reconciliation is **not a guard** — it was run by hand this session and nothing runs it on a schedule. Two of the four ATS URL shapes in use put the company in a query string rather than the path, so any future automation of this check must parse both.

## Rules adopted

1. **A URL that resolves is not a company that matches.** `head_200` is a liveness check. Identity must come from the posting body.
2. **Slug-derived identity must be reconciled against label-derived tier/category at least once per company**, not per posting.
3. Generalises **watch (aj)** (2026-08-29, a secondary chain inventing a named CEO) from class 5 to class 1: *the name attached to an item is the least-verified field on it, and it is the field every downstream filter trusts.*

## Bearing on the report

None directly — no entry was made. **Theme 1's job-postings evidence is unaffected.** The value is methodological, and it belongs in the appendix's account of how class 1 is instrumented: the report claims its postings are URL-verified and dated, and both claims remain true; this file records precisely what those two claims do *not* cover.

## Pair with

- `scripts/README.md` § feed-health guard — the class-1 guard watches *whether the scan ran*, not *whether its rows are who they say they are*. This is the second, unguarded axis.
- `_coverage-expansion-and-first-absence-panel-exit-2026-08-25.md` — the 47% feed jump that was the instrument growing, not the market moving. Same family: a class-1 number that describes the instrument and reads as a finding.
- `../weekly-runs/2026-08-30-corpus-run.md` — this run.

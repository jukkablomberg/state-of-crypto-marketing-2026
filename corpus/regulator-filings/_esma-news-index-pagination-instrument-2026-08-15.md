# Instrument note — ESMA's paginated news index silently drops items between pages (measured 2026-08-15)

**Type:** instrument property, not a finding about the market. Filed alongside `../layoff-tracker/_rootdata-dead-projects-instrument-2026-08-13.md` and `../layoff-tracker/_aggregator-crossref-2026-08-14.csv` as a measurement of a source the corpus relies on.
**Surface measured:** `https://www.esma.europa.eu/press-news/esma-news`, default sort (Reverse Chronological), pages 0–2, all HTTP 200, full bodies.
**Measured:** 2026-08-15.

---

## The measurement

| page URL | first item (newest) | last item (oldest) | items |
|---|---|---|---|
| `/press-news/esma-news` | **14/08/2026** | **10/07/2026** | 10 |
| `/press-news/esma-news?page=1` | **02/06/2026** | **07/05/2026** | 10 |
| `/press-news/esma-news?page=2` | **11/03/2026** | **23/02/2026** | 10 |

**The pages are internally reverse-chronological and mutually non-overlapping — but they are not contiguous.**

- Between page 0's oldest (10/07/2026) and page 1's newest (02/06/2026): **a 37-day gap.**
- Between page 1's oldest (07/05/2026) and page 2's newest (11/03/2026): **a 56-day gap.**

Each page returns 10 items while the offset advances by roughly 20. **Approximately half the index is not reachable by walking `?page=N` sequentially.**

## The gap is proven to contain real items — from inside this repo

This is not an inference about what *might* be missing. The corpus already holds an ESMA document that falls in the first gap:

> **`esma-mica-transitional-period-end-2026-06.md`** — ESMA Public Statement, reference **ESMA75-113276571-1710**, dated **23 June 2026**, captured 2026-06-26 from the primary PDF.

**23 June 2026 sits between 02/06/2026 and 10/07/2026 — inside the gap — and it is one of the most consequential MiCA documents in the entire corpus.** A run that had swept this index page-by-page and trusted it would have concluded ESMA published nothing between 2 June and 10 July 2026. **The corpus can falsify that from its own shelf.**

## What this costs the corpus retroactively

**`esma-consob-post-deadline-index-sweep-2026-08-05.md` (day 35) concluded:**

> *"ESMA's own news index, fetched direct, carries no crypto-marketing item in the post-deadline window it covers. Ten dated items, 10 July → 3 August 2026."*

**That statement is accurate as written — it is explicitly scoped to "the window it covers" — but the window it covers is not the window a reader will assume.** It is one page of a surface now known to drop roughly half its contents. The finding is **not withdrawn**; it is **re-scoped**, and the scope must travel with it into Phase 2.

**Today's sweep is the direct demonstration of the cost:** walking this index at source produced **two net-new class-3 captures** the corpus had missed for months — the **11 July 2025** halo-effect statement and the **24 February 2026** CFD/perpetual-futures statement — both of them squarely marketing-relevant, neither of them ever surfaced by thirteen runs of secondary-source searching.

## Standing rule adopted

**A paginated regulator index is not the regulator's record until page contiguity has been checked.** Before any absence claim is derived from a paginated index, the run must record the **first and last item date of every page fetched** and confirm the boundaries meet. Where they do not, the claim must name the measured coverage, not the nominal window.

This is the direct sibling of **watch (kk)** — *"a regulator's summary table is not the regulator's record"* (VARA, 2026-08-14), where the falsifier was one click away on the same host. **Here the falsifier was one page boundary away on the same URL.** Two consecutive runs, two different regulators, the same defect class: **the corpus was reading a rendering of the record and calling it the record.**

## Alternative surfaces — named, NOT used

These are recorded so they are not re-surfaced as novel next run, and so that naming them is not mistaken for using them (watch (ee)):

- `https://www.esma.europa.eu/press-news/esma-news?sort_by=chronological` — chronological sort; would expose whether the drop is offset-arithmetic or sort-dependent.
- The index's own **Title / From / To date-range filter form** — the correct instrument for a bounded-window sweep, and it is on the page.
- `https://www.esma.europa.eu/databases-library/esma-library` — ESMA's document library, a different surface over the same corpus.
- `https://www.esma.europa.eu/press-news/press-releases` — press-releases-only view.
- **Section-filtered views**, e.g. *Digital Finance and Innovation*, *Investor protection*, *Warnings and publications for investors*.

**None of these were fetched this run. No claim is made about what they contain.**

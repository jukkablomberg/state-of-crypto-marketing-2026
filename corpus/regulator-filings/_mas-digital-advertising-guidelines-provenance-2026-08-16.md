# MAS digital-advertising guidelines: the surface finally rendered, and the date the corpus was about to print is now in doubt

**Class:** 3 (regulator) — **INSTRUMENT / PROVENANCE NOTE. STILL NOT ADMITTED AS A CAPTURE.**
**Written:** 2026-08-16 (day 46 post-deadline)
**Discharges:** 08-15 recommendation 1 — *"go back for the MAS digital-advertising guidelines… try a different surface on the same host."*
**Verdict:** the different-surface move **worked on the third tier, not the second** — and what it returned was a date problem, not the operative text.

---

## The escalation ladder, in order, with results

| # | Surface | Method | HTTP | Body |
|---|---|---|---|---|
| 1 | `mas.gov.sg/regulation/guidelines/guidelines-on-standards-of-conduct-for-digital-advertising-activities` | `web_fetch` | 200 | **EMPTY** |
| 2 | `mas.gov.sg/-/media/…/guidelines/guidelines-on-standards-of-conduct-for-digital-advertising-activities.pdf` (operative PDF) | `web_fetch` | 200 | **EMPTY** |
| 3 | `mas.gov.sg/news/media-releases/2025/initiatives-to-promote-responsible-online-financial-content` (the announcing release) | `web_fetch` | 200 | **EMPTY** |
| 4 | `mas.gov.sg/news/parliamentary-replies/2025/content-creators-providing-unlicensed-financial-advice` | `web_fetch` | 200 | **EMPTY** |
| 5 | `mas.gov.sg/-/media/…/consultation-paper/annex-a-guidelines-…-digital-prospecting-and-marketing-activities.pdf` | `web_fetch` | 200 | **EMPTY** |
| 6 | `mas.gov.sg/publications/consultations/2023/consultation-paper-on-enhancing-safeguards-for-digital-prospecting-and-marketing-activities` | `web_fetch` | 200 | **RENDERED** (document list only) |
| 7 | `mas.gov.sg/regulation/guidelines/guidelines-on-standards-of-conduct-for-marketing-and-distribution-activities-fsg-g02` (**control**) | `web_fetch` | 200 | **RENDERED** (body text) |
| 8 | **surface 1 again, via the Chrome extension (JS-rendering)** | **`navigate` + `get_page_text`** | 200 | **✅ RENDERED** |

**The control at row 7 is the important line.** A *sibling page in the same path family* rendered fine under `web_fetch`. So the empty bodies are **not** a host-level or path-family block, and the 08-15 characterisation ("both MAS primary URLs returned empty bodies") was under-diagnosed: **these specific pages are client-rendered, and `web_fetch` does not execute JavaScript.** Escalating to a JS-rendering browser was the correct move and it is the move that worked.

**Generalisable rule, added to (mm)'s family:** an HTTP 200 with an empty body next to a *rendered sibling on the same host and path family* is a **client-rendering diagnosis, not a fetch failure**. Escalate to a rendering engine before recording it as unreachable. This corpus recorded three MAS URLs as unreachable on 08-15; at least one of them was reachable the whole time by a tool that was available.

---

## What the rendered page actually says — and what it does not

Full text returned, verbatim and complete (the page's `<article>` element in its entirety):

> **Consultations**
> **Published Date: 25 April 2023**
> Consultation Paper on Enhancing Safeguards for Proper Conduct of Digital Prospecting and Marketing Activities
> This consultation paper seeks feedback on our proposals to enhance safeguards for proper conduct of digital prospecting and marketing activities, and address conduct risks and issues associated with these activities. Two consultation responses were published: Response to Guidelines on Standards of Conduct for Digital…
> Advisory and Sales · Disclosures · Representative-related · Record Keeping · Conduct
> **Consultation number: P003-2023**
> **Start date: 25 April 2023**
> **Closing date: 30 June 2023**
> **MAS response date: 22 May 2026**

**The operative guidelines text is still not in hand.** The URL that is named "Guidelines on Standards of Conduct for Digital Advertising Activities" serves a *consultation record*, not the guidelines. The instrument remains **UNADMITTED**.

---

## 🔴 The reason this note exists: the 25 March 2026 effective date is now in tension with a primary-surface date

The 08-15 run recorded, from a compliance-vendor summary and refused on provenance:

> *MAS Guidelines on Standards of Conduct for Digital Advertising Activities, **stated effective 25 March 2026**, applying to all MAS-regulated FIs and their appointed third parties advertising via digital media.*

Today's WebSearch summary of `mas.gov.sg` results repeated the same 25 March 2026 date and added a **25 September 2025** media-release date.

**MAS's own page says the MAS response to consultation P003-2023 is dated 22 May 2026.**

A guideline issued under a consultation whose response MAS dates **22 May 2026** cannot straightforwardly have taken effect on **25 March 2026** — the effect date would precede the response by eight weeks. Three readings are available and **the corpus cannot presently distinguish them**:

1. The vendor and the search summary have the year or the day wrong.
2. The 25 March date belongs to a *different* MAS instrument (there are two adjacent titles here: *Digital Advertising Activities* and *Digital Prospecting and Marketing Activities*, plus the pre-existing FSG-G02 *Marketing and Distribution Activities* — **three near-identical names**, the exact conditions of watch (u)).
3. MAS published guidelines ahead of the consultation response, which happens but is not the default reading.

**Ruling: neither date is admitted. The corpus will not print "effective 25 March 2026", and it will not print 22 May 2026 as the guidelines' date either — 22 May 2026 is the date of a *response to a consultation*, which is watch (o) exactly: date the document, never an event held about it.**

**This is the second consecutive run in which a date the corpus was carrying from a secondary source failed on contact with a primary surface.** On 08-15 it was the standing claim that the EU had issued no operational marketing guidance. Today it is a MAS effective date. Watch (cc) — *the secondary layer is going machine-written* — gains its cleanest instance yet: **a vendor summary and a search-engine summary agreed with each other, and the primary page agreed with neither.** Agreement between two secondaries is not corroboration when both may derive from the same upstream.

---

## Why the object is still worth chasing

Unchanged from 08-15, and now better specified. If the guidelines are what the secondary layer describes — applying to MAS-regulated FIs **and their appointed third parties, including online content creators** — then they are the only instrument in the corpus that regulates the report's own **comparison panel** (agencies and influencers) rather than the firms. That is a Theme-3 object, not just a Theme-4 one. **It remains the single highest-value unadmitted class-3 object in the queue, now for a fourth consecutive run.**

**Next surface to try, named so it is carried rather than rediscovered:** the operative PDF at row 2, **via the Chrome extension** rather than `web_fetch`. Today's ladder proves the rendering escalation works on this host; it was applied to the landing page and not to the PDF, and that is a gap in this run, not in the method.

---

## Provenance

| Field | Value |
|---|---|
| Publisher | Monetary Authority of Singapore (MAS) |
| Object sought | Guidelines on Standards of Conduct for Digital Advertising Activities |
| Object obtained | Consultation record P003-2023 (25 Apr 2023 → 30 Jun 2023; MAS response 22 May 2026) |
| Fetched | 2026-08-16 — eight surfaces, seven by `web_fetch`, one by JS-rendering browser |
| Tier | **PRIMARY for the consultation record. The guidelines themselves remain UNCAPTURED.** |
| `capture_ai_disclosure` | none for the rendered page. **The 25 March 2026 date is vendor/search-summary derived and is expressly NOT admitted.** |
| Not fetched, not guessed | the operative guidelines PDF (empty under `web_fetch`, **not yet retried under Chrome**) · the two consultation responses named in the page's own text · the 25 Sep 2025 media release · the MAS enforcement register's current contents (still **NOT MEASURED**, unchanged from 08-15) |

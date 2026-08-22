# Instrument note: a window-scoped search returns pre-window articles as current signal — twice in one run, in two different classes

**Published:** N/A
**Published-provenance:** Instrument/methodology note, **not an operator statement**. Exempt from the class-4 storage rule by kind. Retained in this directory because it documents a class-4 failure mode.
**Recorded:** 2026-08-20. **Bears on:** class 4 (operator statements), class 5 (layoffs), and the report's date discipline generally.

---

## What happened

Two of this run's would-be net-new items — one in class 4, one in class 5 — turned out to be the **same defect**, arrived at from opposite directions. Both were caught. Neither was admitted. **Recording the mechanism is worth more than either item would have been.**

### Instance A — class 4. A "new CMO" announcement that announces the CMO who left

A search scoped to *"crypto exchange CMO / head of marketing appointed August 2026"* returned, among departure coverage the corpus already holds, a headline that reads as a live appointment at a **tracked Stratum-1 firm**:

> **"Crypto.com names new CMO" — marketing-interactive.com**

If real, it breaks the corpus's six-run standing null (*no 2026 appointment to any tracked firm's top marketing seat is publicly visible*) and closes the open question of who succeeds Steven Kalifowitz.

**Fetched first-party. Published date: 12 August 2020. The appointee is Steven Kalifowitz.**

It is the announcement of the hire of the man whose **2026 departure** is already corpus row `cryptocom-kalifowitz-cmo-exit-primary-2026-08-11.md`. Verbatim from the 2020 piece: *"Cryptocurrency company Crypto.com has appointed Steven Kalifowitz as its chief marketing officer."*

**Nothing admitted. The null HOLDS — seventh consecutive run.** Ten weeks after Binance's CMO departure and seven weeks after Crypto.com's took effect, **neither firm has publicly named a permanent successor.**

### Instance B — class 5. An "18% cut" dated to 2026 that happened in 2022

The layoff aggregator's highest-value unheld candidate — `Coinbase, 2026-03-05, −18%` — resolves to a **14–15 June 2022** event. Full adjudication in `../layoff-tracker/_candidate-adjudications-2026-08-20.md`. The refutation rested on capturing sources that carry the true date **inside their own URL paths** (`/2022/06/14/`, article-ID `122061500208`), which page furniture cannot restyle.

## The mechanism, stated once

**A publisher's page furniture — its rendered dateline, its "most recent" rail, its republication timestamp — is not the article's date, and a search index scoped to a window will surface pre-window articles whose furniture falls inside it.**

Instance B showed this directly: the Business Standard page carrying the 2022 Coinbase story renders a **`Wednesday, January 07, 2026`** dateline in its own furniture. Instance A showed the search-index half: a 2020 article surfaced under an August-2026-scoped query, with nothing in the result to mark it stale.

**The two instances are more useful together than apart, because they rule out the comfortable explanation.** This is not one sloppy aggregator (instance B's suspect) and it is not one sloppy search (instance A's). **It is a property of reading a dated corpus through undated intermediaries**, and this report is built entirely from dated claims about a twelve-month window.

## 🔴 Why this is more dangerous than the mechanisms already on the watch list

Watch (u) tracks four ways a **name** produces a false positive — brand collision, document-reference collision, clone-domain collision, dot-bearing-brand-as-substring. All four are **entity** errors: the wrong company matched.

**This is a *date* error, and date errors are worse for this corpus, for two reasons.**

1. **The entity is correct.** Both instances name a genuinely tracked firm, a genuinely real event, and a genuinely accurate figure. **Only the date is wrong** — and every one of the six source classes is date-keyed. A wrong date does not fail a name check, a source check, a verbatim-quote check, or a plausibility check. It fails only a date check, and nothing was running one.
2. **Both instances would have *confirmed* something.** Instance A would have closed an open question the corpus has carried for seven runs. Instance B would have supplied a bigger, earlier, more dramatic version of a finding already in the report. **A false item that resolves an open question is not scrutinised the way a surprising one is** — which is precisely why the 08-07 crossref flagged the Coinbase row as *high-value* rather than as *implausible*, and carried it for thirteen days on that basis.

## Rules adopted

1. **Every class-4 and class-5 admission must carry a publication date read from the fetched artifact itself** — not from a search summary, not from a result snippet, not from the page's "most recent" rail. If the fetched page does not state its own publication date, **the item is not admitted.**
2. **When an item would close an open question or strengthen an existing finding, date it first and read it second.** The confirming direction is the unguarded one.
3. **URL path segments and article-ID numerals are stronger date evidence than rendered datelines**, because they are set at publication and survive republication. Use them when they exist.
4. **Watch (o) — "date the document, never an event held about it" — is extended: date the document, never the page it is rendered on.**

## Explicit non-claims

- **Not claimed:** that marketing-interactive.com or business-standard.com did anything improper. Both correctly state their own publication dates on the page; the 2020 article is plainly marked *published 12 August 2020*. **The failure is in the reading, not the publishing, and both instances were caught by reading the artifact.**
- **Not claimed:** that Crypto.com or Coinbase has or has not appointed anyone. **Only that no such appointment is publicly visible**, which is the only claim this methodology permits.
- **Not fetched:** the NPR and Business Standard 2022 articles at source (their URL date-stamps were sufficient to refuse a promotion, and a refusal needs less than an admission).

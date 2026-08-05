# Theme 1 / Theme 2 — the marketing function is losing its senior layer to AI labs, not to AI tools

**Opened:** 2026-08-05 (day 35 post-deadline).
**Status:** BACKFILL — an April event at a Stratum-1 tracked firm, found on 5 August. Same instrumentation defect as the OP Labs and Kraken layoff backfills (**watch (n)**).
**Primary source captured this run:** CoinDesk, *"OpenAI appears to be poaching Coinbase's marketing team"*, Ian Allison, **published 2026-04-23 07:49, updated 07:55** — `https://www.coindesk.com/business/2026/04/23/openai-appears-to-be-poaching-coinbase-s-marketing-team`
**In window** (post-Dec-2024). **Not previously in any corpus file** — it appears only as a passing mention in two run records (07-05, 07-19), never captured.

---

## Why this matters enough to open a findings file

The report's Theme 2 is *"AI in the stack — claimed adoption vs. JD-confirmed adoption."* Every corpus artefact so far reads that theme in one direction: crypto marketing teams adopting AI tooling, and firms using AI-efficiency language to frame contractions.

**This is the same theme running the other way, and it is better evidenced than most of the first direction:**

> The senior layer of the largest US crypto exchange's marketing function did not adopt AI. It **left to work at AI companies.**

Six named senior marketing people, plus a seventh to a second AI lab, plus policy, design and data-science departures — all dated, all role-identified, all from a single Stratum-1 tracked firm.

---

## The dated record (as reported by CoinDesk from public LinkedIn profiles)

| person | role at Coinbase | destination | dated |
|---|---|---|---|
| **Sarah Russell** | Senior Director, Integrated Marketing (1y3m; left Jan 2023) | OpenAI — VP, Integrated Marketing & Ops | **Nov 2024** |
| **Kate Rouch** | **Chief Marketing Officer** (3.5 years) | OpenAI — **Chief Marketing Officer** | **Dec 2024** |
| **Elke Karstens** | *(via Finom, 3 months)* | OpenAI — Head of International Marketing | **Mar 2025** |
| **Kaitlin Gianetti** | Director, Integrated Marketing (4+ years) | OpenAI — Head of Integrated Marketing Management | **Sep 2025** |
| **Amy (Good) Robbins** | Senior Manager, Insights (3.5 years) | OpenAI — Brand Insights Lead | **Sep 2025** |
| **Nina Mogavero** | Marketing & Strategy (3 years) | OpenAI — Marketing Strategy & Ops | **Dec 2025** |
| **Sarah Wolf** | Marketing lead, **Base** (~5 years) | **Anthropic** — Head of Startup Marketing | **~Apr 2026** |

Adjacent, same direction, same firm:

| person | role at Coinbase | destination | dated |
|---|---|---|---|
| Tom Duff Gordon | VP, International Policy | OpenAI — Head of EMEA Policy | Apr 2026 |
| Alexandra Fitzroy | Head of Design, Base | OpenAI | Oct 2025 |
| Yi X | — | OpenAI — Product Manager | Apr 2025 |
| Abe Sprague | — | OpenAI — Data Science | Sep 2024 |

**Attributed mechanism, from a person familiar with the situation:** Rouch was the *"nexus"* — *"To be fair, she hired a lot of them or brought them from Facebook."* Several of the group overlapped at Meta before Coinbase. **This is an anonymous attribution and is recorded as such; it is context, not a corpus claim.**

---

## The firm-attributed statement — and the one hard number in it

Coinbase, on the record, via a spokesperson, verbatim:

> **"The marketing team at Coinbase is over 150 people and while some folks have left to join OpenAI last year, and we wish them the best, characterizing this as anything other than normal people moves would be incorrect."**

**Two things to extract.**

**1. A firm-stated marketing-team headcount at a Tier-1 tracked exchange: "over 150 people."** As far as the corpus knows, **this is the only firm-attributed marketing-function headcount figure it holds for any tracked firm.** Theme 1 is *"the shape of the marketing function"* and has until now been built entirely from job postings and org inference. This is a first-party size datum, on the record, dated 2026-04-23.

**Use it precisely:** it is a floor ("over 150"), it is undated as to its own as-of moment, and it predates the **2026-05-05 Coinbase 14% reduction** already in the layoff tracker. **Do not print it as a current figure.** The defensible sentence is: *Coinbase stated in April 2026 that its marketing team numbered over 150, twelve days before announcing a 14% company-wide reduction.*

**2. CLASS-4 ROLE GATE: REFUSED.** The statement is attributed to *"a Coinbase spokesperson,"* unnamed, in a communications seat. **It does not qualify under `methodology.md` §4**, which requires a named CMO / VP Marketing / Head of Brand / Head of Growth. **Not counted in class 4. Class 4 remains at 5 files.** (Same disposition as the Mulvenny quote refused on 2026-08-03 — the gate is applied consistently, including when it costs the corpus its best quote of the run.)

---

## What this does to existing findings

**Theme 5 / watch (h′) — the AI-cover narrative gets a second mechanism.** The tracker reads AI framing as a *rationale for cuts*. This is AI acting on the marketing function through an entirely different channel — **voluntary senior attrition to AI employers, beginning Nov 2024, fourteen months before any 2026 layoff round.** Coinbase's marketing leadership was already draining toward OpenAI while the firm was still expanding. **Sequence, not causation:** Rouch leaves Dec 2024 → five more senior marketers follow through Dec 2025 → Ferdon's "marketing vanguard" statement 2026-04-09 (`../corpus/operator-statements/coinbase-ferdon-marketing-vanguard-2026-04.md`) → CoinDesk publishes 2026-04-23 → Armstrong 14% memo + AI-native pods 2026-05-05. **State the sequence. Refuse the causal story.**

**Theme 1 — the Coinbase spine gets a second leg.** `tracked-firms.md` already calls Coinbase "the spine of Theme 1 + Theme 5" for the AI-native-pods memo. That memo describes the *operating model*. This describes *who was left to run it*.

**Watch (aa) — a third form of the date-type defect, and the worst one.** Every date in the table above is a **start date at the destination employer**, taken from LinkedIn. **None is a departure date from Coinbase.** Russell's row makes this explicit and unavoidable: she left Coinbase in **January 2023** and started at OpenAI in **November 2024** — a 22-month gap. Karstens went via a third employer for three months.

> **`date_announced` / `date_effective` is insufficient. Personnel records need `date_departed_source_firm` and `date_started_destination` as separate fields.** Any Theme-1 claim of the form "N marketing leaders left firm X during window W" built from destination start dates is **wrong by construction**, and this corpus was one synthesis pass away from making exactly that claim.

**Watch (n) — instrumentation, third strike.** An April event at a Tier-1 tracked firm, naming the marketing function specifically, surfaced in a top-tier trade outlet, and the corpus found it on 5 August. OP Labs (March, found July), Kraken (May, found July), now this (April, found August). **The corpus's sweeps are calibrated to catch *new* events and are systematically failing to catch *in-window* ones.** A full-range re-sweep of classes 4 and 5 back to December 2024 is no longer optional before Phase 2.

---

## Verification status

- **CoinDesk article: CAPTURED first-party this run**, full text, HTTP 200, publish + modify timestamps in metadata.
- **LinkedIn profiles: NOT captured.** Every role/date pair above is CoinDesk's reading of a public profile. Treated as **near-primary**, single-outlet.
- **`[VERIFY]` before Phase 2 prints any individual's role or date:** the underlying LinkedIn profiles, or a second outlet. **The "over 150" figure is the exception** — it is a direct on-the-record company statement quoted verbatim and is safe to attribute to CoinDesk's reporting of it.
- **Not entered anywhere as a layoff.** These are voluntary departures. They do not belong in `layoff-tracker/`.

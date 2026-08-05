# ESMA + CONSOB post-deadline index sweep — 2026-08-05 (day 35)

**Class:** 3 (regulator filings and statements)
**Method:** direct fetch of each authority's **own** publication index — the method proven on AFM 2026-08-03 (`afm-cnmv-post-deadline-index-sweep-2026-08-03.md`), not search-engine inference. Discharges watch **(w)** for ESMA and re-executes it for CONSOB.
**Window:** post-deadline (1 July 2026 →), read against the December-2024 corpus rule.
**Captured:** 2026-08-05.

---

## Headline

**Two results, and the second one is the stronger.**

1. **ESMA's own news index, fetched direct, carries no crypto-marketing item in the post-deadline window it covers.** Ten dated items, 10 July → 3 August 2026. Not one concerns MiCA marketing communications, CASP conduct, or any enforcement action. The two items tagged *Digital Finance and Innovation* are an ESAs paper on ICT risk from frontier AI models (31 July) and a routine Q&A release (10 July).

2. **CONSOB's own blocking register carries a 21-week quantified series — and it contains an explicit statutory power to order the removal of ADVERTISING CAMPAIGNS that has not been visibly exercised once.** This is the AFM finding replicated in Italy with a sharper instrument: in the Netherlands the unused tool was a thematic review; in Italy it is a literal advertising-takedown power, described by the regulator on the same page as the register that does not contain it.

**Day-35 named marketing-side enforcement silence HOLDS. Watch (v) → 6 of 6.**

---

## 1. ESMA — own news index, direct fetch

**Source:** `https://www.esma.europa.eu/press-news/esma-news` — fetched 2026-08-05, HTTP 200, page 1, reverse-chronological.

**The index as it stands (verbatim titles + ESMA's own dates and section tags):**

| date | section tag(s) | item |
|---|---|---|
| 03/08/2026 | Joint Committee · Trading | EBA, EIOPA and ESMA propose amendments to bilateral margin requirements |
| 31/07/2026 | **Digital Finance and Innovation** · Joint Committee | EBA, EIOPA and ESMA call for enhanced governance and consistent supervision to mitigate ICT risks from frontier AI models in the EU financial sector |
| 31/07/2026 | ESMA newsletter | ESMA publishes latest edition of its newsletter |
| 27/07/2026 | Market data · Press Releases · Trading | ESMA authorises EuroCTP as the Consolidated Tape Provider for shares and ETFs |
| 20/07/2026 | Post Trading | ESMA calls on firms to finalise preparations ahead of T+1 settlement deadlines |
| 20/07/2026 | Supervisory convergence | ESMA publishes report on cross-border investment services supervision |
| 16/07/2026 | Board of Appeal | Joint Board of Appeal dismisses appeal against the EBA |
| 10/07/2026 | Market data | ESMA launches data collection under the first phase of ESAP |
| 10/07/2026 | **Digital Finance and Innovation** · Sustainable finance · Trading | New Q&As available |
| 10/07/2026 | Market data | ESMA publishes first market capitalisation data for EU Member States |

**Findings, stated to the limit of what was read and no further:**

- **Zero crypto-marketing items.** No MiCA marketing-communications statement, no CASP conduct action, no advertising guidance, no enforcement announcement.
- **Zero crypto items of any kind** in the ten captured.
- The only two *Digital Finance and Innovation* items are ICT-risk (AI models) and a routine Q&A. **Neither is marketing-side.**
- The one item that touches supervision of firm conduct — *cross-border investment services supervision* (20/07) — is **MiFID-perimeter, not MiCA**, and was not fetched.

**BOUNDED CLAIM — do not overstate.** Page 1 spans **10 July → 3 August 2026**, i.e. post-deadline **day 9 to day 33**. It does **not** cover days 1–8 (1–9 July), and the "Load More" pagination was **not** followed. The honest claim is:

> Across the 24-day stretch of the post-deadline window that ESMA's own news index page 1 covers, ESMA published no crypto-marketing item of any kind.

**Days 1–8 remain unswept and are an open item, not a null.** The 29-day class-3 miss the corpus already logged (the 3 July binary-options statement) sits in exactly that unswept stretch — which is itself the argument for following the pagination next run.

**Watch (w): DISCHARGED for ESMA.** The index has now been read at source rather than inferred from search coverage, which is what (w) has asked for since it opened. Method is 2-for-2 on producing cleaner class-3 results than any search pass.

---

## 2. CONSOB — `Ordini di oscuramento di siti abusivi`, own register, direct fetch

**Source:** `https://www.consob.it/web/area-pubblica/oscuramenti` — fetched 2026-08-05, HTTP 200. First-party. This closes the `[VERIFY]` opened 2026-08-01 and carried through two runs.

### 2a. `[VERIFY]` CLOSED — the 24 / 1,793 / 233 figures are CONFIRMED at the primary

The corpus carried *"24 sites / 1,793 / 233 crypto"* as an unverified near-primary figure for three runs. CONSOB's own register, **comunicato stampa del 24 luglio 2026**, verbatim:

> "è stata disposta la chiusura di **10 siti** che prestavano abusivamente servizi e attività di investimento su strumenti finanziari e **14 siti** che prestavano abusivamente servizi per le cripto-attività"
>
> "Sale, così, a **1793** il numero dei siti complessivamente oscurati dalla Consob a partire da luglio 2019 […] Di questi, **233** riguardano fenomeni legati a cripto-attività."

**All three figures match exactly. `[VERIFY]` closed, primary captured, no discrepancy.**

### 2b. The longitudinal series — the corpus's first quantified class-3 time series

Read off the register's own `comunicato stampa` entries. Two columns are CONSOB's own cumulative counters: total sites blocked since July 2019, and the crypto-attributed subset.

| comunicato stampa | cumulative sites | of which crypto | crypto Δ |
|---|---|---|---|
| 6 marzo 2026 | 1588 | *(not stated)* | — |
| 13 marzo 2026 | 1599 | 136 | — |
| 19 marzo 2026 | 1608 | 136 | 0 |
| 25 marzo 2026 | 1622 | 146 | +10 |
| 3 aprile 2026 | 1654 | 168 | +22 |
| 9 aprile 2026 | 1666 | *(not stated)* | — |
| 23 aprile 2026 | 1671 | 168 | 0 |
| 4 maggio 2026 | 1681 | 178 | +10 |
| 7 maggio 2026 | 1704 | 201 | +23 |
| 15 maggio 2026 | 1712 | 204 | +3 |
| 20 maggio 2026 | 1718 | 204 | 0 |
| 1 giugno 2026 | 1723 | 204 | 0 |
| 5 giugno 2026 | 1729 | 204 | 0 |
| 12 giugno 2026 | 1736 | 204 | 0 |
| 26 giugno 2026 | 1757 | 217 | +13 |
| **— 1 July 2026: MiCA transitional period ends —** | | | |
| 3 luglio 2026 | 1763 | 217 | 0 |
| 10 luglio 2026 | 1769 | 219 | +2 |
| 24 luglio 2026 | 1793 | **233** | +14 |

**What the series shows — and this is the analytically important part:**

- **The 1 July deadline produced no step-change in CONSOB's crypto blocking rate.** Post-deadline (3–24 July, 21 days): **+16** crypto sites. A comparable pre-deadline stretch (23 April – 7 May, 14 days): **+33**. **The pre-deadline rate was higher.**
- The largest single-week crypto jumps in the entire series are **7 May (+23)** and **3 April (+22)** — both months before the deadline.
- **The deadline is not visible in the enforcement data.** Any Phase-2 claim that the transitional-period end triggered a supervisory surge is **falsified for Italy** by the regulator's own counter.

### 2c. THE FINDING — CONSOB holds an explicit advertising-campaign removal power, and the register does not contain one

The register page states its own legal bases. One of them, verbatim, is **art. 36, comma 2-*quaterdecies*** TUF, introduced by **Legge n. 21 del 5 marzo 2024**:

> "La Consob può ordinare ai soggetti di cui al comma 2-*terdecies* la rimozione delle **campagne pubblicitarie** condotte attraverso le reti telematiche o di telecomunicazione, aventi ad oggetto servizi o attività di investimento prestati da chi non vi è abilitato."

*(CONSOB may order the removal of advertising campaigns conducted over telematic or telecommunications networks, concerning investment services or activities provided by a person who is not authorised.)*

The register also cites its **MiCAR powers** — Regulation (EU) 2023/1114 + d.lgs. 129/2024 art. 4(1), invoking art. 94(1) MiCAR — expressly for blocking sites providing crypto services to Italian savers without authorisation.

**So: an EU NCA has (i) a named statutory power to take down advertising campaigns, (ii) MiCAR supervisory powers, (iii) a weekly-cadence publication habit, and (iv) 21 weeks of published output in the corpus window. And across all of it, every single instrument is a *site-blocking order against an unauthorised entity*. Not one is an advertising-campaign removal. Not one names a marketing communication. Not one concerns an authorised CASP.**

**The honest qualifier, which must ship with the finding.** Comma 2-*quaterdecies* is itself **perimeter-scoped by statute** — it reaches advertising *"by a person who is not authorised."* It is **not** a conduct power over licensed firms. So this is not "CONSOB declined to use a conduct tool"; it is something structurally more interesting:

> **The EU marketing-enforcement toolkit, as actually legislated and as actually deployed, is perimeter-shaped.** Italy's dedicated advertising-takedown power reaches only unauthorised actors. The Netherlands' quantified advertising review produced supervisory letters and cross-border referrals, none public. Spain's bespoke advertising Circular produced one published sanction file — in 2023, against an unauthorised promoter. **Across six jurisdictions the corpus has now found no published instrument aimed at the marketing conduct of an authorised CASP.**

That is a different and much stronger claim than "regulators are silent," and it is the one Phase 2 should print.

### 2d. Watch (v) → **6 of 6**

FR, DE, IT, CY, NL, ES have now all been swept. All six replicate **perimeter, not conduct**. Italy is the strongest replication in the set because it is the only one where the corpus can show a marketing-specific power sitting unused next to 21 weeks of dated output from the same authority.

---

## Not reached / not guessed

- ESMA news index **pages 2+** ("Load More" not followed) — post-deadline days 1–8 unswept. **Open, not null.**
- The individual CONSOB `comunicato stampa` PDFs (linked from the register; register text captured instead).
- CONSOB `Avvisi ai risparmiatori` and `Avvertenze` registers — not re-read this run; the 07 read stands.
- The ESMA 20/07 cross-border investment services supervision report — identified, not fetched, **MiFID-perimeter and probably out of scope**.
- BaFin, AMF, CySEC own-indexes — not re-swept this run; prior reads stand.
- MAS and VARA — never swept at source. **Standing gap.** Newly relevant: FalconX is withdrawing its MAS licence application (see `../layoff-tracker/2026-layoff-tracker.csv`, row added 2026-08-05).

**No URL was fabricated. Every figure above is quoted from a page fetched this run.**

# Theme 4 — MiCA readiness: exposure surface by firm

**Opened:** 2026-08-28 (day 58 post-deadline). **Four days to ship.**
**Status:** DRAFT PASSAGE — every figure citation-anchored to a corpus record; every prohibition inherited from the record that established it.
**Why now:** the 08-27 run's recommendation 2 read *"the Theme-4 paragraph is now writeable — write it."* The 08-28 field inventory supplied the second half. This file is the passage, with its limits attached, so that Phase-3 drafting works from adjudicated text rather than from run records.

---

## The thesis, in one paragraph

> **MiCA's marketing-communications regime attaches to a register, and the register is not shaped like the industry the regime was written for.** Of 324 authorised crypto-asset service providers, 38% may operate in one member state and 41% may operate in twenty-nine or thirty; almost nobody is in between. The firms that entered after the transitional period ended are overwhelmingly the first kind — two-thirds single-market, fourteen of thirty-five German, twelve of those fourteen cooperative or regional retail banks, **and every German entrant domestic-only**. Not one is a crypto-native firm this report tracks. Meanwhile the register's own field for the trading-platform estate distinguishes it from the corporate website in **two rows out of 329**. The regime that governs how crypto is marketed to European consumers can see, from its own primary record, who is authorised and where — and almost nothing about where they publish.

---

## The four load-bearing facts

### 1. The post-deadline authorisation rate is 10.7%, and the surge was *before* the deadline

Of 328 authorised CASPs carrying a notification date as at **2026-08-17**, **35 (10.7%)** were notified on or after 1 July 2026. The register's largest month is **June 2026 at 75** — more than four times May's 18, against 31 in July and 4 in the first seventeen days of August.

**Firms raced the deadline; they did not follow it.**

→ `corpus/regulator-filings/esma-casps-post-deadline-authorisation-rate-2026-08-27.md`
⚠ Scoped to the 08-17 capture. The +6 rows observed 08-25 are unread; no figure may cover them.

### 2. The post-deadline entrant is a German cooperative bank, and it is domestic-only

Of the 35: **14 German**, **12 of those 14 cooperative or regional retail banks** (Volksbank, Raiffeisenbank, VR-Bank, Spar- und Kreditbank), **0 tracked-cohort firms** — checked programmatically against every Stratum 1–4 name.

And on the passporting column: **23 of 35 (65.7%) post-deadline entrants are single-market, against 33.8% of the 293 pre-deadline firms — and all 14 German entrants took a domestic-only authorisation.**

→ `corpus/regulator-filings/esma-casps-post-deadline-authorisation-rate-2026-08-27.md` (composition)
→ `corpus/regulator-filings/esma-register-field-inventory-and-passporting-breadth-2026-08-28.md` §3 (breadth)
⚠ 35 rows against a multi-year back-catalogue of 293. A firm may passport later. **Nothing here says the post-deadline cohort will stay domestic.**

### 3. Authorisation in the tracked cohort is an exchange phenomenon, and its promotional surface is continental by construction

Ten tracked firms map to thirteen register entities. **Stratum 1 (Tier-1 exchanges): 9 of 11** — Binance and HTX absent. **Stratum 2 (L1/L2 foundations): 0 of 8. Stratum 3 (wallets): 0 of 5. Stratum 4: 1 of 3.**

Eleven of the thirteen entities are authorised for **26–30 member states**.

**The cohort this report studies sits almost entirely in the register's upper mode.** That is a scope disclosure the report owes its reader before it is a finding.

→ `corpus/regulator-filings/esma-casps-authorised-register-at-source-2026-08-17.md` (cross-match)
→ `.../esma-register-field-inventory-and-passporting-breadth-2026-08-28.md` §2 (breadth)
🔴 **Absence from the register is not evidence of non-compliance.** Fourteen of the sixteen "absent" tracked firms are a **category error** — foundations are not service providers, non-custodial wallets sit outside the CASP perimeter, Tether is an issuer under Titles III–IV. **Do not print them as absences** (`.../esma-casps-register-complete-capture-alternate-channel-2026-08-25.md`). What the pattern establishes is narrower and more useful: **the cohort's two most marketing-active strata operate outside the register Article 68's marketing-communications obligations attach to.**

### 4. The register cannot see the promotional estate

`ae_website_platform` — the CASPS register's field for the trading-platform surface — is populated in 47 of 329 rows; net of `n/a` values and a documented column-bleed artifact, **40 real values, of which 2 differ from the firm's corporate URL.**

→ `.../esma-register-field-inventory-and-passporting-breadth-2026-08-28.md` §5
🔴 Admissible as a statement about the register. **Inadmissible as a statement about any entity in it.**

---

## The enforcement half, and why it does not say what it looks like

**The EU marketing-side enforcement null still stands at day 58.** No named post-deadline marketing-communications action by any EU national competent authority has entered this corpus (watch (b)).

**But the null is not a thin early sample — it is a reporting artifact, and that is the stronger finding.** ESMA's non-compliance register is **98.8% Italian** (165 of 167 rows, CONSOB), while Italy has authorised **2.8%** of the EU's CASPs. **Germany, which has authorised more CASPs than any other member state, appears in the non-compliance register zero times.** Twenty-seven authorities grant authorisations; **three** have ever notified a non-compliant entity.

⚠ **The limit ships attached:** this is a *notification* asymmetry as much as an *enforcement* one — a zero can mean no action, or action not notified, or a different notification cadence, and these files cannot separate those. **And the register could not express a marketing-communications action even if one existed:** `ae_reason` is `None` in 166 of 167 rows.

→ `corpus/regulator-filings/esma-casps-authorised-register-at-source-2026-08-17.md` §1
→ `corpus/regulator-filings/esma-register-field-semantics-ae-infrigment-resolved-2026-08-24.md`

### The one jurisdiction where a marketing-side action is live is not in the EU

**FCA v Huobi Global S.A. & Others**, Chancery Division, claim issued **21 October 2025** — the FCA's own description: *"the first time we've taken enforcement action against a crypto firm illegally marketing their products to UK consumers."* The proceedings are **stayed by consent from 24 August until 8 September 2026** for settlement talks — **seven days after this report ships.**

**And the defendant structure is the Theme-1/Theme-4 artifact of the cycle:** the fourth defendant is *"PERSONS UNKNOWN (who are the persons currently in control of promotions on behalf of the HTX Exchange"* on nine named platforms; the fifth extends that class to whoever holds those accounts **on or before 31 October 2028**.

> **The marketing function is not a compliance stakeholder in this document. It is a defendant class.**

→ `corpus/regulator-filings/fca-htx-promotions-consent-order-stay-2026-08-28.md`
🔴 **No causal link between the UK proceedings and HTX's absence from ESMA's registers.** Two public facts, juxtaposed, nothing inferred. **This is the FCA under s.21 FSMA, not an EU NCA under MiCA — watch (b) is untouched and the EU null stands.**

---

## Candidate passage for the report — adjudicated, safe to set

> Fifty-eight days after MiCA's transitional period ended, ESMA's register of authorised crypto-asset service providers held 329 entries. Thirty-five had been notified since the deadline. Fourteen were German, twelve of those fourteen were cooperative or regional retail banks, and every one of the fourteen took an authorisation valid in Germany alone. None of the thirty-five was a firm this report tracks.
>
> That is not what a maturing regime looks like from the outside. The authorisation surge happened in June, in the last month before the deadline, and it was four times the size of May's. What followed the deadline was not crypto-native firms arriving late; it was retail banks adding a product line for customers they already had.
>
> The register itself is two populations under one licence name. Thirty-eight per cent of authorised firms may operate in a single member state; forty-one per cent may operate in twenty-nine or thirty. Almost nobody is in between. Every Tier-1 exchange in this report's cohort is in the second group — which means the firms whose marketing this report reads are, without exception, running continental promotional surfaces under a regime that most of its own licensees experience as a domestic one.
>
> And the regime's primary record cannot see those surfaces. ESMA's register carries a field for the trading platform, distinct from the corporate website. Of 329 authorised firms, two use it.

**Every figure above traces to a named corpus record; every record traces to a capture verified COMPLETE. Nothing in the passage names a firm as non-compliant, and nothing infers intent.**

---

## Open before ship

1. 🔴 **The +6 CASPS rows of 08-25 are still unread.** Every figure here is scoped "as at 2026-08-17" and says so. Either read them or keep the scope sentence in every instance. **Keeping the scope sentence is the safe default and costs nothing.**
2. 🔴 **The absence-panel sentence is still undecided — fourth consecutive restatement.** Theme 4 inherits a class-1 claim the corpus cannot support unless `methodology.md` §1 gains a paragraph distinguishing *firm silence* from *scanner reach on the day of the scan*. **Nothing in this file depends on it, deliberately.**
3. ⚠ **Aave / Push Virtual Assets Ireland Limited remains AMBIGUOUS** and is excluded from every count here that would change if it resolved.
4. ⚠ **HTX's absence from the EU register remains unexplained** and this file does not explain it.

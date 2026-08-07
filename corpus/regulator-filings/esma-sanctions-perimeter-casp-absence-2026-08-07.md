# ESMA's own sanctions perimeter does not include CASPs — the structural leg of the null, anchored to a primary

**Class:** 3 (regulator filings and statements)
**Captured:** 2026-08-07 (day 37 post-deadline)
**Capture method:** direct first-party fetch of three ESMA pages, HTTP 200 each. No secondary relay. No AI-assisted intermediary.
**Status:** PRIMARY (esma.europa.eu, first-party). Not an enforcement action. Not a statement about crypto marketing.
**Why it exists:** the corpus has asserted a "perimeter-shaped toolkit" reading of the post-deadline enforcement null since the 07-08 NCA sweep. Until today that reading was an *inference from absence*. It is now anchored to ESMA's own enumeration of what it may sanction.

---

## The finding

ESMA's **Sanctions and Enforcement** page enumerates the entity types over which ESMA holds direct
sanctioning power. **Crypto-asset service providers are not among them.**

Verbatim, from the page's own description (fetched 2026-08-07, HTTP 200):

> "As the single supervisor for Credit Rating Agencies (CRAs), Securitisation Repositories (SRs), Trade
> Repositories registered under EMIR and/or SFTR (TRs), Tier 2 Third-Country Central Counterparties
> (Tier 2 TC-CCPs), EU Critical Benchmark Administrators and Recognised Third-Country Administrators
> (Benchmark Administrators) as well as Data Reporting Service Providers (DRSPs) in the EU, ESMA has
> responsibilities and powers to deal with possible infringements."

- **URL requested:** `https://www.esma.europa.eu/publications-and-data/sanctions-and-enforcement`
- **Resolved / canonical:** `https://www.esma.europa.eu/esmas-activities/supervision/sanctions-and-enforcement`
- **Six entity classes named. CASPs absent. Crypto absent. MiCA absent.**

Corroborated on the same domain, same run, by the **Investigations and Inspections** page
(`https://www.esma.europa.eu/esmas-activities/supervision/investigations-and-inspections`, HTTP 200),
whose "Perimeter monitoring" section is scoped to **credit ratings only**, verbatim:

> "Through Perimeter monitoring ESMA seeks to identify companies that are providing credit ratings
> without having registered with ESMA. This is done via Internet searches, as well as referrals from
> outside entities and other stakeholders."

Note what that describes: ESMA *does* run internet-search-based perimeter monitoring for unregistered
activity — the exact instrument a marketing-side crypto sweep would need — and it is pointed at CRAs.

---

## What this does and does not establish

**ESTABLISHES.** The thirty-seven-day absence of a named EU marketing-side crypto enforcement action is
not, at the ESMA level, evidence of supervisory inattention or of a compliant market. **ESMA does not
hold direct sanctioning power over CASPs at all.** Any marketing-side MiCA action must originate with a
national competent authority. The corpus's structural reading is now sourced rather than inferred.

**DOES NOT ESTABLISH.** Nothing about NCA capacity, intent, or activity. Nothing about whether any
national action is in train. Nothing about MiCA Article 111 penalty regimes, which are notified *by*
Member States *to* ESMA — a notification duty (Art. 99, Art. 111), not a sanctioning power. This file
makes no claim about the *content* of any national penalty regime.

**NOT AN ENFORCEMENT ACTION.** No firm named. No measure imposed. No marketing communication found
deficient. **The day-37 null holds.**

---

## Consequence for the Phase-2 wording

The three-part wording adopted on 08-06 stands, and its first leg upgrades from inference to citation:

1. **Structural** — perimeter-shaped toolkit. **NOW PRIMARY-ANCHORED (this file).** ESMA's sanctioning
   perimeter is six named entity classes and CASPs are not one of them.
2. **Prioritisation** — the first post-deadline Common Supervisory Action was aimed at CASPs' *digital
   operational resilience*, not at marketing (08-06 file).
3. **Forbearance** — the AMF has deliberately declined to set a shutdown deadline, for a stated
   consumer-protection reason, on the record, named official (08-06 file).

**Never print "silence."** Print the mechanism.

---

## Instrument validation — the standing practice adopted 08-06, applied and mostly FAILING

The 08-06 run established: *an instrument may not produce an absence claim until it has been shown to
detect a known presence.* The two known ESMA presences the corpus holds are the **23 June 2026**
transitional-period Public Statement (ESMA75-113276571-1710) and the **8 July 2026** Common Supervisory
Action on CASPs' digital operational resilience.

| Route tried today | HTTP | Detects the two known items? | Verdict |
|---|---|---|---|
| MiCA activities page `/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica` | 200 | **NO** — neither item appears; its document table's newest MiCA statement is the Nov-2025 standards/format statement, and its "Statement on MiCA Transitional Measures" is the **2024-12** one | **FAILS validation. May not carry an absence claim.** |
| Investigations and Inspections | 200 | n/a — not an index | Not an absence instrument. Useful as a scope datum (above). |
| Sanctions and Enforcement | 200 | n/a — not a crypto register | Not an absence instrument. Useful as a **perimeter** datum (the finding). |
| `?sort_by=chronological` on the news index | **BLOCKED** — URL not in the fetch tool's provenance set; **not fetched, not guessed** | — | **Still untried. Carried.** |

**Watch (w) remains UN-DISCHARGED for ESMA.** Three routes tried across two runs; the news index drops
items it holds (08-06), and the MiCA topic page does not carry news at all. **Post-deadline days 1–8
remain uncovered and no route has yet passed the known-presence test.** Said plainly rather than
papered over.

---

## Incidental register datum — the 08-06 `[VERIFY]` gets harder, not easier

The MiCA activities page carries the interim MiCA register (five CSVs) and stamps it:

> *"Last update: 31 July 2026"*

with the stated cadence *"ESMA will publish the latest version of the register on weekly intervals."*

Set against the two other readings the corpus holds of the same register:

| Reading | Source | Date asserted |
|---|---|---|
| Page-level stamp, read today | ESMA MiCA page (primary) | **31 July 2026** |
| "roughly 320", list "updated Aug 5" | The Block 2026-08-06 (secondary) | 5 Aug 2026 |
| 324 distinct pairs, latest `ac_lastupdate` | NorthPoint primary CSV read 2026-08-06 | 4 Aug 2026 |

**The page's freshness stamp lags the contents of the files it links.** Three sources, three dates, one
register. **Operational rule for Phase 2: cite the CSV and its `ac_lastupdate`, never the page stamp,
and never a figure without its snapshot date and de-dup rule.** The `[VERIFY]` opened on 08-06 stays
open and is now better specified.

---

## Provenance

| Field | Value |
|---|---|
| Publisher | European Securities and Markets Authority (ESMA) |
| Documents | Sanctions and Enforcement; Investigations and Inspections; Markets in Crypto-Assets Regulation (MiCA) |
| Fetched | 2026-08-07, all three HTTP 200, first-party `esma.europa.eu` |
| Tier | **PRIMARY** |
| `capture_ai_disclosure` | **none — first-party regulator pages, no intermediary** (schema field proposed by watch (cc)) |
| Quote status | Both quotes verbatim from the fetched pages |
| Not fetched, not guessed | `?sort_by=chronological` (provenance-blocked); ESMA news index pages 3+; the linked Level 2/3 measures table PDF; the five register CSVs (held separately by NorthPoint) |

# The EU marketing-enforcement null, re-tested against a register republished after we last looked

**Class:** 3 (regulator filings). **Captured:** 2026-08-20. **Capture status: COMPLETE** (final row terminates cleanly; tail byte-identical to the committed 08-16 snapshot).

- **Source:** `https://www.esma.europa.eu/sites/default/files/2024-12/NCASP.csv` — ESMA interim MiCA register file 5/5, non-compliant entities providing crypto-asset services.
- **Register page's own stated update date:** **18 August 2026** (`.../markets-crypto-assets-regulation-mica`, fetched first-party this run).
- **Baseline compared against:** `_esma-ncasp-snapshot-2026-08-16.csv` — 24,614 bytes, md5 `31bffda0e62c3f0f33ea24bcc7aeea4b`, 167 data rows, re-verified `COMPLETE` this run by `scripts/verify-capture.py`.

---

## The result

**ESMA republished the interim MiCA register on 18 August 2026. The non-compliance file did not gain a single entry.**

| | 2026-08-16 capture | 2026-08-20 capture |
|---|---|---|
| Data rows | **167** | **167 — unchanged** |
| Newest `ae_decision_date` | **22/07/2026** (Cervo Rendisco, Flandenzo, Corona Fondenza) | **22/07/2026 — unchanged** |
| Newest `ae_lastupdate` | **31/07/2026** | **31/07/2026 — unchanged** |
| `ae_infrigment = No` | **167 of 167** | **167 of 167 — unchanged** |
| Distinct authorities (whitespace-normalised) | **3** — CONSOB 165, AFM 1, NBS 1 | **3 — unchanged** |
| Marketing-communications actions | **0** | **0** |

## Why this is a stronger statement than the one the corpus has been making

Through day 47 the null was: *"we have looked repeatedly and found no EU-NCA named marketing-side action."* The obvious objection to that is **observation cadence** — an absence found by an observer who looks on their own schedule can be an artefact of when they looked.

**That objection is now closed for this window.** The publisher of the record — not us — refreshed the register **two days ago**, on its own weekly cycle, and the non-compliance file came back **byte-stable**. The null is a property of the record, not of our looking.

**Day 50 post-deadline. Nineteenth consecutive EU-NCA zero on marketing grounds.**

### Formulation for Phase 2, with the limits attached

> The EU's consolidated register of non-compliant crypto-asset service providers held 167 entries on 16 August 2026. ESMA republished the register on 18 August 2026. On 20 August 2026 it held **the same 167 entries**, with the same newest decision date of 22 July 2026 — **twenty-nine days without a new entry from any EU authority**, across at least two publication cycles. 165 of the 167 are Italian. Not one is a marketing-communications action.

**The two limits ship in the same paragraph or the sentence reads stronger than the data bears:**

1. **Notification, not enforcement.** The register is fed by NCAs. It cannot separate *"took no action"* from *"took action, did not notify ESMA."* A stable register is evidence about the reporting channel first and the enforcement posture second.
2. **The field cannot express the finding.** `ae_infrigment` is `No` on 167 of 167 rows and `ae_reason` is `None` on 166 of them. **This register could not record a marketing-communications action even if one had been notified.** The single populated `ae_reason` — AFM on MEXC Global — is a licensing breach (*"provides crypto-asset services in the Netherlands without the required MiCAR license… in breach of section 59 MiCAR"*), not a promotional one.

## Register cadence — third observation

ESMA states a weekly publication cycle. Observed gaps between stated register update dates: **~12 days** (08-16 read), **~7 days** (08-17 read, register self-reporting 10/08), **8 days** (10/08 → 18/08, today). Three observations, mean roughly nine days. **Slower than stated, not wildly so. Recorded; not asserted as a pattern.**

## Explicit non-claims

- **Not claimed:** that no EU marketing-side enforcement has occurred. Only that none appears in this register, and that this register is structurally incapable of showing one.
- **Not claimed:** that the 18 August republication necessarily touched `NCASP.csv`. ESMA's date is stated for the register collection. **What is claimed is narrower and is what matters: after that date, the file we can read is unchanged.**
- **Not re-derived:** the CONSOB/BaFin authorisation inversion from 08-17. That rests on `CASPS.csv`, which was **not** re-fetched this run — the denominator may have moved and is not restated.
- **Not fetched, not guessed:** `CASPS.csv` at its 18/08 version · the AFM's MEXC public-warning page · the CONSOB post-deadline notice bodies · the NBS LWEX notice.

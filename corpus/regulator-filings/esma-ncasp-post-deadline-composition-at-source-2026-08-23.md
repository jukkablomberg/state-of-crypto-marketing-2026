# ESMA Register of Non-Compliant Entities (NCASP) — post-deadline composition, read at source

**Captured:** 2026-08-23 (day 53 post-deadline)
**Published:** register republished **21 August 2026** (ESMA's own MiCA page states *"Last update: 21 August 2026"*)
**Published-provenance:** first-party — the date is asserted by ESMA on the page that serves the file, not inferred by us.
**Primary source (register file):** https://www.esma.europa.eu/sites/default/files/2024-12/NCASP.csv
**Primary source (publication page):** https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica
**Legal basis:** MiCA Art. 110 — register of entities providing crypto-asset services in breach of Art. 59 or 61.
**Class:** 3 (regulator filings). **Themes:** 4 (MiCA readiness / exposure surface), 3.

---

## Why this read exists

The 08-20 run established a nineteenth consecutive zero on watch (b) — *no named post-deadline NCA marketing-side action against a tracked firm.* The 08-22 run deliberately did **not** restate it, on the ground that a null does not advance by the calendar. It was three days old.

**It has now been re-earned by observation, and the re-read produced more than the null.**

---

## 1. The register was republished two days ago. It did not move.

ESMA states the interim MiCA register is republished at **weekly intervals**, and the MiCA page dates the current version **21 August 2026**. Today's fetch of `NCASP.csv` is content-identical to the corpus's stored 2026-08-16 snapshot on every discriminator checked:

| Discriminator | 2026-08-16 stored | 2026-08-23 fetched |
|---|---|---|
| Header | 12 fields, `ae_competentAuthority … ae_lastupdate` | identical |
| Data rows | 167 | 167 |
| Composition | IT 165 · NL 1 · SK 1 | identical |
| Terminal rows | Cervo Rendisco · Flandenzo · Corona Fondenza · MEXC · LWEX | identical |
| Newest `ae_decision_date` | 22/07/2026 | 22/07/2026 |
| Newest `ae_lastupdate` | 31/07/2026 | 31/07/2026 |

**The stronger form of the null is therefore available and is claimed:** ESMA republished this register on 21 August 2026, and as of that republication it still contains **zero** entries naming any Stratum 1–4 tracked firm, and zero entries alleging a marketing or promotional infringement by anyone.

⚠ **Stated limit — no md5 comparison was made.** `verify-capture.py` was run against the **stored 08-16 file** (`COMPLETE`, exit 0, 167 rows, 24,614 bytes, md5 `31bffda0e62c3f0f33ea24bcc7aeea4b`, final row 12 of 12 fields). Today's fetch arrived through a retrieval channel that returns text, not bytes, so it was verified against those six discriminators rather than byte-for-byte. **A hand-transcribed copy of today's fetch would be a fabricated artifact, not a capture, so none was written.** Discriminator-identity is weaker than md5-identity and is labelled as such. It is, however, sufficient for the claim actually made here, which is about the presence and dates of rows.

## 2. 🔴 Five entries in fifty-three post-deadline days. All CONSOB. All shell domains. None a licensee.

The MiCA transitional period ended **1 July 2026**. Filtering the register to `ae_decision_date >= 2026-07-01` returns **five rows**, and this is the complete post-deadline content of the EU's register of non-compliant crypto-asset service providers:

| Decision date | Authority | Entity | Stated reason |
|---|---|---|---|
| 08/07/2026 | CONSOB (IT) | Reversal Investment Group | *None* |
| 08/07/2026 | CONSOB (IT) | Kortex | *None* |
| 22/07/2026 | CONSOB (IT) | Cervo Rendisco | *None* |
| 22/07/2026 | CONSOB (IT) | Flandenzo | *None* |
| 22/07/2026 | CONSOB (IT) | Corona Fondenza | *None* |

**Every post-deadline entry comes from one national authority.** Twenty-nine other EEA competent authorities have contributed nothing to this register since the deadline. All five are unbranded promotional-domain clusters of the kind CONSOB has been listing since February 2025 — the same shape as its pre-deadline entries, at the same cadence. **The deadline is not visible in this register.**

**And the register has not moved in thirty-two days.** Newest decision 22 July; newest update 31 July; republished 21 August with nothing added. On a register ESMA says it refreshes weekly, that is four consecutive empty refreshes.

## 3. ⭐ Of 167 entries, exactly one states a reason — and it is about a licence, not a promotion.

`ae_infrigment` is **`No` for all 167 rows without exception.** `ae_reason` is `None` for 166 of 167. The single populated cell is the AFM's:

> *"MEXC Global provides crypto-asset services in the Netherlands without the required MiCAR license. MEXC is in breach of section 59 MiCAR."*

It is also the only row carrying a `ae_comments` value (a pointer to the AFM's public warning, https://www.afm.nl/en/sector/actueel/2025/sep/pb-mexc, decision 16/09/2025 — **pre-deadline**).

**This is the sharpest sentence Theme 4 has: the EU's register of non-compliant crypto-asset service providers contains one hundred and sixty-seven entries, of which exactly one explains itself, and that one is about an authorisation, not an advertisement.** The register is a perimeter instrument. It records *who is outside the licence*, not *what anyone said*.

It clusters with, and is the register-side counterpart of, three findings already in the corpus: the four-NCA perimeter-not-conduct result (`nca-warning-list-sweep-de-it-cy-2026-07-08.md`), the sanctions-perimeter CASP absence (`esma-sanctions-perimeter-casp-absence-2026-08-07.md`), and the 08-22 finfluencer factsheet — **a regulator instrument that speaks about promotion and is addressed to people who hold no licence.** Taken together: *the European supervisory response to the crypto marketing surface, thirteen months after MiCA applied and fifty-three days after the transitional period closed, consists of guidance to non-licensees and a perimeter list of scam domains.*

---

## Explicit non-claims

1. **Not claimed: that no marketing-side enforcement exists in Europe.** This register would not necessarily carry it. National sanction registers are separate instruments and are tracked separately (`cnmv-sanctions-register-read-2026-07.md`, `esma-sanctions-perimeter-casp-absence-2026-08-07.md`).
2. **Not claimed: that the five post-deadline entries are unrelated to marketing.** `ae_reason` is empty for all five. **We do not know why they were listed.** Absence of a stated reason is recorded as absence of a stated reason, not as a reason.
3. **Not claimed: byte-identity with the 08-16 capture.** Six discriminators, not md5. See §1.
4. **Not claimed: that CONSOB is more diligent than other NCAs.** It may simply publish differently. The register records what NCAs submit to ESMA; submission practice is not observable from the file.
5. **Not claimed: any figure taken from an aggregator.** Third-party pages reporting "167 entries, 165 from Italy, none from BaFin" were returned by search again today. **Those are this corpus's own 08-16 at-source figures coming back to us.** Refused as circular for the second consecutive run — watch (ss). The numbers in this file are re-derived from the file, not from anyone quoting us.
6. **Not claimed: that the 21 August republication changed nothing anywhere.** Only `NCASP.csv` was re-read today. `CASPS.csv` (last read 17/08), `OTHER.csv`, `ARTZZ.csv` and `EMTWP.csv` were **not** re-read and nothing is asserted about them.

## Not fetched, not guessed (work queue — watch (oo))

- `CASPS.csv` under the **21 August 2026** republication — last read 17/08, now stale against a known newer version. **Oldest live entry in the queue.**
- The five post-deadline entities' underlying CONSOB resolutions, which may state grounds the register does not.
- ESMA's *Description of the fields in the interim MiCA register* CSV — would settle whether `ae_infrigment: No` means "no infringement type recorded" or something narrower. **Currently we do not know what that column means, and the report must not lean on it until we do.**

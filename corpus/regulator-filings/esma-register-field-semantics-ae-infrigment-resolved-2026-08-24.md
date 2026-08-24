# ESMA interim MiCA register — field semantics resolved at source; `ae_infrigment` does NOT mean what the corpus was about to read it as

**Class:** 3 (regulator filings)
**Captured:** 2026-08-24
**Source (fetched HTTP 200, `text/csv`, complete file):** https://www.esma.europa.eu/sites/default/files/2024-12/Description_of_the_fields_in_the_interim_MiCA_register.csv
**Publisher:** European Securities and Markets Authority (ESMA)
**Why it was fetched:** the 2026-08-23 run record listed this file as the item that *"would settle what `ae_infrigment: No` actually means. Until it does, the report must not lean on that column."* It was the newest entry on the "not fetched, not guessed" work queue. It is now settled.

---

## §0 — The finding, stated plainly

**`ae_infrigment` is not a field about the listed entity's conduct. It is a field about ESMA's conduct toward a national regulator.**

ESMA's own field description, verbatim from the file:

| template | field | Field name | Description | Format |
|---|---|---|---|---|
| NCASP | `ae_infrigment` | Case of infringement identified by ESMA in accordance with Article 17 of Regulation (EU) No 1095/201[0] | Case of infringement identified by ESMA in accordance with Article 17 of Regulation (EU) No 1095/201[0] | `"Yes"`, `"No"` |

**Article 17 of Regulation (EU) No 1095/2010 is the ESMA Regulation's breach-of-Union-law procedure — a procedure ESMA opens against a NATIONAL COMPETENT AUTHORITY that has failed to apply Union law, not against a firm.**

So the corpus's 2026-08-23 observation — *"`ae_infrigment` is `No` for all 167 rows without exception"* — is **factually correct and interpretively empty.** It does not mean "no infringement was found against these 167 entities." It means **ESMA has not opened a breach-of-Union-law case against any national authority in connection with any of these entries.** Those are different objects, and only one of them is about the advertisement.

---

## §1 — What this changes in the corpus

**🔴 RETRACTED, BEFORE IT WAS EVER PRINTED.** The 08-23 record built a candidate sentence on this column and correctly gated it. **The gate was right and the sentence must not ship in the form it was drafted.** Any reading of `ae_infrigment: No` as evidence about the *entities* is withdrawn.

**🟢 WHAT SURVIVES, AND IT SURVIVES INTACT — because it never rested on `ae_infrigment`.** The 08-23 finding's load-bearing half is the `ae_reason` column, and ESMA's description confirms `ae_reason` **is** an entity-level field:

| template | field | Field name | Description | Format |
|---|---|---|---|---|
| NCASP | `ae_reason` | Non compliancy reason | Non compliancy reason | Free text |

`ae_reason` is exactly what the corpus took it to be: a free-text field for the reason the listed entity is non-compliant. **It is populated for one row in 167** — the AFM's MEXC entry, citing operation *"without the required MiCAR license… in breach of section 59 MiCAR."*

**The shippable sentence, corrected and now field-semantics-verified:**

> *Of the 167 entities on the EU's register of non-compliant crypto-asset service providers, ESMA provides a free-text "non-compliancy reason" field. Exactly one entry uses it — and that one is about an authorisation, not an advertisement.*

**Do not append the `ae_infrigment` clause to that sentence.** It is a different regulator's-eye-view field and it says nothing about the 167.

**Also confirmed by the same file:** `ae_decision_date` is *"Decision date, decided by the authority, of crypto-asset services in violation of Article 59 or 61"* — which validates the 08-23 post-deadline filter (five entries on/after 01/07/2026, all CONSOB) as a filter on the authority's own decision date. That filter stands.

---

## §2 — CASPS.csv re-read: **ATTEMPTED, TRUNCATED, ABSENCE CLAIM REFUSED**

Recommendation 3 of the 08-23 run was to re-read `CASPS.csv` under the 21 August republication. It was attempted and it **failed the capture guard.**

- **Fetched:** https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv — HTTP 200, `text/csv`.
- **Returned:** 82,445 characters across 205 lines.
- **Final line, 205, verbatim tail:** `Autorité des Marchés Financiers (AMF),FR,Bpifrance Investissement,96950082Z6KUVA6TW686,FR,Bpifrance Investissement,"27-31 avenue du Général Leclerc - 94`
- **Verdict: 🔴 TRUNCATED.** `verify-capture.py`'s **primary predicate** fires: the final row does not carry the header's field count, and it is cut **mid-field, inside an unterminated quoted address**. This is the same failure mode as the 2026-08-17 truncation.
- **Corroborating structural deficit:** 205 lines against the **329 data rows verified COMPLETE on 2026-08-17** (`_esma-casps-snapshot-2026-08-17.csv`, md5 `69e7dc…`). A ~38% shortfall — `verify-capture.py`'s `--expect-rows` predicate agrees with the primary predicate.

**🔴 CLASS-3 ABSENCE CLAIM REFUSED.** No claim of the form *"firm X is absent from the CASPS register"* may be made from this capture. Positive hits inside a truncated capture remain usable; absences do not. The register question about named tracked firms **remains open and ships open unless a complete capture is obtained.**

**⚠ AND `verify-capture.py` COULD NOT BE RUN ON IT — the same limit watch (pp) hit on 08-23, hit again from the other side.** The fetch arrived through a channel that persisted it outside the repo's reachable filesystem, so it never became a file the guard could open. **The verdict above was reached by applying the guard's own primary predicate by hand, to the observed terminal row.** That is weaker than an exit code and is labelled as such. **No snapshot file was written — hand-transcribing 82,445 characters through a summarisation channel would produce a fabricated artifact, not a capture** (the 08-23 precedent, applied again).

### ⚠ A note on the retired size heuristic — recorded, and it does NOT resurrect it

Today's cut point is **82,445 characters — byte-identical to the 2026-08-17 cut point on this same file.** That is worth writing down: **the retrieval channel's budget appears stable per-channel, and the same file truncates at the same place across a seven-day gap.**

**This does not revive the byte threshold as a predicate, and the temptation to revive it is refused.** 2026-08-20 already proved a *different* cut point (64,556) exists on the same channel for a different file, and that a 24,614-character capture can be complete. A number that is reproducible is not thereby diagnostic. **Structure decided today, as it decided on 08-17 and 08-20. The heuristic stays retired and stays a printed note.**

---

## §3 — Explicit non-claims

1. **NOT claimed:** that `ae_infrigment: No` tells the reader anything about the 167 listed entities. It does not.
2. **NOT claimed:** that ESMA has found no infringements by these entities. The register's existence is the finding of non-compliance; `ae_infrigment` is a separate Article 17 flag about national authorities.
3. **NOT claimed:** any absence of any named firm from the CASPS register. Today's capture is truncated and refuses that claim.
4. **NOT claimed:** that the 21 August republication changed CASPS. The capture was too incomplete to say either way.
5. **NOT claimed:** that `verify-capture.py` returned exit 0 or exit 1 today. It was not run; its primary predicate was applied by hand and the weakening is stated.
6. **NOT claimed:** any re-reading of `NCASP.csv` today. It was read at source on 08-23 and is not restated by the calendar.

---

## §4 — Work queue this leaves

- **`CASPS.csv` — still uncaptured under the 21/08 republication, and now known-truncated on two separate attempts.** Oldest live queue entry. Needs a channel that can persist bytes to disk, or it ships unread.
- The five post-deadline CONSOB resolutions underlying the 08-23 entries — not fetched, not guessed.
- `OTHER.csv` — deliberately not attempted (standing instruction, unchanged).

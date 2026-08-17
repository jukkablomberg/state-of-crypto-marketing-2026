# Instrument note: our fetch tool silently truncated a regulator register at 49% and returned HTTP 200

**Recorded:** 2026-08-17
**Class:** instrument / methodology, not a finding about any firm or regulator
**Severity:** 🔴 **This is the second consecutive run in which our own tooling, not a source, generated a false record.**

---

## What happened

`web_fetch` was pointed at `https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv`.

It returned a body of **82,445 characters across 205 lines**, cut **mid-field** inside the address of `Bpifrance Investissement` — the real bytes continue `700 Maisons-Alfort, France`. No error, no warning, no truncation marker. The tool reported success.

The authentic file is **161,380 bytes / 386 physical lines / 329 logical CSV rows**. **The capture was missing 49% of the register.**

The full file was subsequently obtained and verified: md5 `69e7dc926b123bac8cb930ab2614ccf6`, byte-identical to a copy taken ~24h apart, so **the source is stable and the discrepancy is entirely fetch-side.** The committed snapshot `_esma-casps-snapshot-2026-08-17.csv` is the complete file.

---

## Why this is serious rather than annoying

A truncated CSV **parses cleanly**. `csv.DictReader` accepts it without complaint. Every statistic computed from the truncated capture would have been internally consistent, plausible, and wrong:

| Statistic | From the truncated capture | Truth |
|---|---|---|
| Total CASPs | ~204 | **325** |
| Authority count | fewer than 27 | **27** |
| BaFin share | inflated (alphabetical clustering) | **21.6%** |
| Tracked-firm hits | **would have missed rows past the cut** | 13 entities |

**The cohort cross-match is the part that would have failed silently.** The register is ordered by authority and the cut fell partway through the French (AMF) block. **A firm absent from the truncated file is indistinguishable from a firm absent from the register** — and "absent from the EU authorisation register" is exactly the kind of claim this report intends to make about named companies. **We came one step from publishing that a tracked firm was unlicensed because our fetch tool stopped early.**

This is the same defect class the corpus documents in other people's promotional estates: a confident claim resting on an instrument nobody checked.

---

## The pattern this completes

Three consecutive runs, three distinct ways our own tooling manufactured a false record:

| Run | Tool behaviour | What the corpus almost recorded |
|---|---|---|
| 08-05 | upstream ATS scan frozen ~66h, sync reported 0 new postings | an **absence** that was really an **unobserved** |
| 08-16 | `web_fetch` returns HTTP 200 + empty body on client-rendered pages | **three MAS URLs as "unreachable"** — at least one was reachable the whole time |
| **08-17** | **`web_fetch` returns HTTP 200 + a silently truncated body on large files** | **half a regulator register as the whole thing** |

**The generalisation, and it belongs in `methodology.md` rather than in a watch item:** every absence claim in this report must name the instrument that produced it, **including our own instruments**, and every instrument must be given a known-presence test before its silence is trusted. Watch (mm) said *"a rendering of the record is not the record"* about regulators' web front-ends. It applies with equal force to our own retrieval layer.

---

## Integrity audit performed on the existing corpus

**The obvious question: was the 08-16 NCASP capture truncated too?** Checked immediately, and it was not.

| | `_esma-ncasp-snapshot-2026-08-16.csv` |
|---|---|
| Size | **24,614 bytes** — well under the ~82KB cut point |
| Rows parsed | **167** — matches the 08-16 record exactly |
| Final row | `National Bank of Slovakia (NBS), SK, LWEX, … https://lwex.com/, No, None, 10/02/2025, , 30/05/2025` — **complete, all fields terminated** |

**The 167-row figure and every statistic derived from it — the 165/167 CONSOB concentration, `ae_infrigment: No` on 167 of 167, the five post-deadline rows, the AFM/MEXC Article 59 row, the `HTXcoin-az` clone-domain rejection — stand unaffected.** The day-46 enforcement null is intact.

---

## Operational rules adopted

1. **Any `web_fetch` result at or near ~82,000 characters is presumed truncated until proven otherwise.** The observed cut was 82,445 characters; treat anything within a few percent of that as suspect.
2. **Every committed CSV snapshot must record its byte count and md5.** Size is the cheapest truncation detector available and it was not being recorded before today. Retro-applied to the NCASP snapshot above.
3. **Structural completeness check before parsing any register capture:** does the final row terminate cleanly, and does the row count match the source's own stated or observable extent? A mid-field cut is detectable in one line of code.
4. **Never derive an absence claim about a named entity from a single large-file capture.** Absence requires either a size/checksum-verified complete file or a second independent retrieval.
5. **Prefer content-length verification over eyeballing.** "It looked like a lot of rows" is how this nearly shipped.

---

## Cross-references

- `esma-casps-authorised-register-at-source-2026-08-17.md` — the capture this note protects.
- `esma-ncasp-non-compliant-register-at-source-2026-08-16.md` — audited above, unaffected.
- `_mas-digital-advertising-guidelines-provenance-2026-08-16.md` — the empty-body sibling defect.
- `scripts/README.md` §"Feed-health guard" — the class-1 precedent for distinguishing ABSENT from UNOBSERVED. **This note is the class-3 version of the same problem, and class 3 has no guard.**

## Open item

**Class 1 has a feed-health guard with two predicates and a documented discrimination test. Class 3 has nothing equivalent.** Register captures are now load-bearing for Theme 4, and they are verified by hand. **A `scripts/verify-capture.py` doing rules 1–3 above would take an hour and would have caught this before a human looked at it.** Recommended, not built.

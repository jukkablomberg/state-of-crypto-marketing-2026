# The EU's own consolidated non-compliance register: 167 rows, 165 of them Italian, and not one of them a marketing-communications action

**Class:** 3 (regulator filings and statements)
**Captured:** 2026-08-16 (day 46 post-deadline)
**Capture method:** direct first-party fetch of ESMA's interim MiCA register CSV, HTTP 200, `Content-Type: text/csv`. Machine-parsed with `csv.DictReader`, not read by eye. No secondary relay.
**Status:** PRIMARY (`esma.europa.eu`, first-party). A register, not an enforcement action.
**Snapshot committed alongside:** `_esma-ncasp-snapshot-2026-08-16.csv` (167 data rows, byte-identical to the fetch).

---

## What was fetched

| Field | Value |
|---|---|
| Publisher | European Securities and Markets Authority (ESMA) |
| Instrument | Interim MiCA Register — file 5 of 5, **"Non-compliant entities providing crypto-asset services"** |
| Legal basis | MiCA Articles 109 and 110 (ESMA to publish a central register; content supplied by NCAs and EBA) |
| URL requested | `https://www.esma.europa.eu/sites/default/files/2024-12/NCASP.csv` |
| Linked from | `https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica` |
| Page freshness stamp read today | ***"Last update: 12 August 2026"*** |
| HTTP | 200, full body |
| Rows | **167** (excluding header) |

**Why this file and not the news index.** The 08-07 run proved the MiCA topic page **fails** the known-presence test as a *news* instrument and may not carry a news-absence claim; the 08-15 run proved the news index is page-lossy. **This is neither.** It is a register — a document the page hosts, whose contents are the record itself rather than a rendering of it. The 08-07 file listed the five register CSVs explicitly under *"Not fetched, not guessed."* They are now fetched. Repo-wide grep before writing returned **zero** prior hits on `NCASP`, `ae_competentAuthority`, `LWEX`, `Atomic Wallet` — net-new confirmed, not assumed.

---

## The finding

### 1. One national regulator is doing essentially all of it

| Competent authority | Member State | Rows | Share |
|---|---|---:|---:|
| CONSOB | IT | **165** | **98.8%** |
| AFM | NL | 1 | 0.6% |
| National Bank of Slovakia (NBS) | SK | 1 | 0.6% |
| **Every other NCA in the EEA** | — | **0** | **0%** |

*(164 rows carry the string `Commissione Nazionale per le Societa e la Borsa (CONSOB)` and one carries the same name with a double space — the same authority, two spellings. Counted as CONSOB.)*

BaFin, AMF, CySEC, CNMV, the Central Bank of Ireland, and every other EEA competent authority contribute **nothing** to the EU's consolidated register of non-compliant crypto-asset service providers. Decision dates run **10 February 2025 → 22 July 2026**, so this is not a young file with a thin tail; it is seventeen months of EU-wide reporting in which two non-Italian entries were made.

### 2. Every one of the 167 rows is a perimeter action. None is a marketing-communications action.

The register's own `ae_infrigment` column reads **`No` on all 167 rows**. `ae_reason` reads `None` on **166 of 167**. Exactly one row carries substantive reason text, and it is the AFM's:

> "MEXC Global provides crypto-asset services in the Netherlands without the required MiCAR license. **MEXC is in breach of section 59 MiCAR.**"
> — AFM, decision date 16/09/2025, comment field pointing to `https://www.afm.nl/en/sector/actueel/2025/sep/pb-mexc`

Article 59 is the authorisation requirement. **Not Article 66 (fair, clear, not misleading), not Article 68 (marketing communications).** The single reasoned row in the EU's consolidated register is an unlicensed-provision case.

### 3. The post-deadline window, measured on the register rather than on a search

**Five rows carry a decision date on or after 1 July 2026:**

| Authority | Entity | Decision date | Infringement field | Reason field |
|---|---|---|---|---|
| CONSOB | Reversal Investment Group | 08/07/2026 | No | None |
| CONSOB | Kortex | 08/07/2026 | No | None |
| CONSOB | Cervo Rendisco | 22/07/2026 | No | None |
| CONSOB | Flandenzo | 22/07/2026 | No | None |
| CONSOB | Corona Fondenza | 22/07/2026 | No | None |

**The post-deadline record is not empty — and it is still not marketing.** Five actions exist, all Italian, all against small unauthorised operators, none with a stated marketing-communications ground. The newest decision date in the whole register is **22 July 2026, twenty-five days before this capture.**

### 4. No tracked firm appears as a respondent — and the one apparent hit is watch (u) firing again

A substring sweep of the ~40-firm Stratum 1–4 cohort against the register's `ae_lei_name`, `ae_commercial_name` and `ae_website` fields returned exactly one candidate: **`HTX`**. It resolves to **`HTXcoin-az`**, CONSOB 04/03/2025, `https://m.htxcoin-az.com` — a lookalike domain, not HTX the Stratum-1 exchange.

**Stated correctly: zero of the tracked firms appear in the EU's non-compliant-entities register as respondents; one appears as an impersonation target.** A name-keyed sweep would have printed the opposite. Watch (u) has now cost a false positive on a third distinct mechanism — brand collision (08-11), document-reference collision (08-15), and today **clone-domain collision**.

---

## What this establishes and what it does not

**ESTABLISHES.**

1. **The day-46 EU-NCA marketing-side enforcement null now survives a test it has never been given.** For six weeks it was derived from searches and index sweeps — instruments the corpus itself has documented as lossy (watch (mm)). It has now been checked against the **EU's own consolidated register of non-compliant CASPs, machine-parsed, 167 rows, at source.** The null holds, and it holds on the strongest instrument available.
2. **The distribution is the finding, not the count.** Any reader who assumes "EU enforcement" means twenty-seven authorities acting in parallel is wrong. **98.8% of the visible record is one NCA.**
3. **The register is structurally incapable of expressing a marketing infringement as currently populated.** 167 of 167 rows say `ae_infrigment: No`; 166 of 167 say `ae_reason: None`. Even if a marketing-side action were taken tomorrow by CONSOB, **this file would not say so** — CONSOB does not populate the reason field at all. That is an instrument property the report must disclose next to the null, or the null will read as stronger than the data can bear.

**DOES NOT ESTABLISH.**

- Nothing about actions taken and not notified to ESMA. The register is fed *by* NCAs; a gap in it is a gap in notification as much as a gap in enforcement, and this file cannot separate the two.
- Nothing about warning lists, which are national instruments that do not flow into this file. The corpus's own AMF, CNMV, BaFin and CONSOB warning-list sweeps (07-08, 07-XX, 08-03, 08-05, 08-06) are a **different** and larger population.
- Nothing about any tracked firm's compliance. **No firm is adjudicated here.** Absence from a non-compliance register is not a finding of compliance.
- Nothing about the five post-deadline CONSOB entities beyond what the register states. Their notice bodies were **not fetched** and are not characterised.

---

## Consequence for Phase 2

The three-part wording adopted 08-06 and anchored 08-07 gains a fourth, quantified leg:

1. **Structural** — ESMA's own sanctioning perimeter excludes CASPs (08-07, primary-anchored).
2. **Prioritisation** — the first post-deadline CSA targeted digital operational resilience, not marketing (08-06).
3. **Forbearance** — the AMF declined to set a shutdown deadline, on the record, named official (08-06).
4. **🆕 Concentration** — **where national action does appear in the EU's consolidated register, 98.8% of it is one authority, and 100% of it is perimeter rather than promotional.** (this file)

**Never print "silence."** Print the mechanism, and now print the distribution.

Pairs directly with `esma-halo-effect-regulatory-status-as-marketing-argument-2025-07.md`: **ESMA told CASPs in July 2025 not to use their regulated status as a marketing argument. Thirteen months later the EU's consolidated register contains no action on that ground, from any authority, including the one that has filed 165 of the 167 rows.** That is the sharpest single pairing in the corpus for Theme 4 and neither half requires alleging a breach by anyone.

---

## Incidental — the register-freshness `[VERIFY]` moves, and not in the page's favour

| Reading | Source | Date asserted |
|---|---|---|
| Page-level stamp, 2026-08-07 | ESMA MiCA page (primary) | 31 July 2026 |
| **Page-level stamp, 2026-08-16 (today)** | **ESMA MiCA page (primary)** | **12 August 2026** |
| Stated cadence, both readings | ESMA MiCA page (primary) | *"weekly intervals"* |

**31 July → 12 August is twelve days.** One observation, two stamps: on this interval **the stated weekly cadence was not met.** Recorded as an observation, not asserted as a pattern — a single gap does not establish one. The 08-07 operational rule stands and is reinforced: **cite the CSV and its own `ae_lastupdate` / `ac_lastupdate` values, never the page stamp.** In this file the newest `ae_lastupdate` is **31/07/2026**, which is *older* than the page's own 12-August stamp — the page claims a freshness its contents do not carry.

---

## Provenance

| Field | Value |
|---|---|
| Publisher | ESMA |
| Document | Interim MiCA Register — non-compliant entities (`NCASP.csv`) |
| Fetched | 2026-08-16, HTTP 200, first-party `esma.europa.eu` |
| Tier | **PRIMARY** |
| `capture_ai_disclosure` | **none — first-party regulator data file, no intermediary, no summarisation step** |
| Parse method | `csv.DictReader`; counts are computed, not eyeballed |
| Quote status | The single AFM reason string is verbatim from the file |
| Not fetched, not guessed | The other four register CSVs (`OTHER`, `ARTZZ`, `EMTWP`, `CASPS`) · the AFM MEXC public-warning page named in the comment field · the five post-deadline CONSOB notice bodies · the Level 2/3 measures table PDF · the 28 Nov 2025 MiCA standards/format statement (`ESMA75-1303207761-6284`, seen on the MiCA page, **not marketing-relevant, deliberately not admitted**) |

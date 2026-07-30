# Regulator register read — CNMV (Spain): public sanctions register, direct read (30 July 2026)

**Source class:** 3 — Regulator filings and statements.
**Regulator:** CNMV (Comisión Nacional del Mercado de Valores, Spain).
**Instrument read:** *Registro público de sanciones impuestas por la CNMV* — the statutory public register of sanctions.
**Primary source URL:** https://www.cnmv.es/portal/Consultas/RegistroSanciones/IniRegSanciones
**Query interface:** https://www.cnmv.es/Portal/Consultas/RegistroSanciones/verRegSanciones.aspx
**Captured:** 2026-07-30. Landing page fetched and read in full.

**Status of this file:** this is a **register-read record**, not an enforcement capture. It exists because the CNMV direct read was carried as an open class-3 target for three consecutive runs (07-27 #2, 07-28, 07-29) without being worked. It is now **discharged**, and the result is a null with two useful structural facts attached.

---

## Result: no in-window Spanish marketing-side enforcement case found

**Nothing net-new enters the corpus from this read.** The day-N "no named marketing-side enforcement case since the 1 July 2026 deadline" count is **unaffected** and **holds at day 29**.

---

## What the register actually is (recorded so the next run does not re-derive it)

From the CNMV's own text on the landing page:

- The register is published under **Article 334 of Ley 6/2023, de 17 de marzo, de los Mercados de Valores y de los Servicios de Inversión**, and Article 94 bis of Ley 35/2003 (collective investment).
- **Very serious and serious infringements** (*infracciones muy graves y graves*) are published through the public sanctions register provided for in **Article 244.1** of that law, read with Article 2(j) of **Real Decreto 815/2023**.
- The published information **also records any contentious-administrative appeals** lodged against the sanction and their outcome.
- **Information is retained in the register for five years.**
- The CNMV may, in appropriate cases, **maintain the anonymity of the sanctioned person** — *"pudiendo, en su caso, mantener el anonimato de la persona sancionada."*

**Two consequences for this report's method, and both cut against over-reading a null:**

1. **The register is a lagging instrument by construction.** It publishes *imposed* sanctions. A *sanctioning file opened* (`expediente sancionador incoado`) is an earlier and separate event that does not appear here until resolved. A marketing-side case could be open in Spain today and be invisible in this register for a long time. **The corpus's silence finding must be stated as "no publicly registered sanction", never as "no enforcement activity."**
2. **Anonymisation is permitted.** Even a resolved marketing-side sanction may appear without the firm named. So this register cannot, on its own, support a claim about *which* firms have or have not been sanctioned.

---

## Precedent note — Spain enforced crypto advertising *before* MiCA, and used a national instrument to do it

Surfaced during this read and recorded because it sharpens a framing the report is going to make:

- The CNMV's executive committee agreed on **31 October 2023** to open its **first sanctioning file (`expediente sancionador`) for possible "serious" infringements in two crypto-asset advertising campaigns**, against **Miolo Desarrollos**. Reported by El Español / Invertia, 2023-11-08.
- The legal basis was **CNMV Circular 1/2022 on crypto-asset advertising** — a *Spanish national* advertising regime — **not MiCA**.

**Why this matters to Chapter 1.** The report's opening register is built on the observation that no named marketing-side enforcement case has followed the MiCA deadline. That framing is only honest if it distinguishes two things:

- **MiCA-era marketing enforcement** — what the corpus is counting, and what remains at zero.
- **National-regime crypto-advertising enforcement** — which **existed before MiCA, and Spain used it.**

An informed reader will know about Circular 1/2022. If the report says "no crypto-advertising enforcement" without qualification, it is wrong, and a Spanish reader will catch it. The claim must be scoped to the MiCA-era marketing-communications regime.

**Dating and sourcing discipline:** the Miolo item is **2023 → out of the corpus window** (pre-December-2024) and is **NOT entered as a corpus record**. It is recorded here as a **framing caveat only**, sourced to secondary press (El Español/Invertia 2023-11-08), and **must not be printed as a corpus finding or as a dated enforcement datum**. `[VERIFY]` against the CNMV's own register or press release before any use beyond the framing caveat above.

---

## Also read and not entered

- **CNMV MiCA Q&A** (*Preguntas y respuestas Reglamento MiCA*), published **15 December 2025**, plus a further criteria document circulating January 2026. These set out authorisation criteria and service-provision guidance ahead of full application from **1 July 2026**, at which point only providers authorised by the CNMV or another European authority may operate in Spain. **Perimeter and authorisation material, not marketing-communications rules.** Not entered — same ruling as the ESMA/AMF transitional-period documents already held.

## Open items

- `[VERIFY]` Run the register's query interface (`verRegSanciones.aspx`) directly with a crypto/CASP filter. This read covered the landing page and its statutory framing; the query form itself was not driven. A future run with browser tooling should execute the query rather than infer from search.
- The CNMV also publishes **`Advertencias de entidades no registradas`** (warnings on unregistered entities) separately from the sanctions register. That is a **different and faster-moving instrument** and has not been swept by this corpus in any jurisdiction. Given that unauthorised-CASP wind-down carries an explicit obligation to *"cease marketing activities and solicitation"* (ESMA/AMF, already held), the warnings lists are a plausible place for the first marketing-adjacent public action to surface. **Recommend adding NCA warning lists as a standing class-3 sweep target.**

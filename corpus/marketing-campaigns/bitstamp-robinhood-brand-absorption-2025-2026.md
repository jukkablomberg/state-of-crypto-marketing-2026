# Bitstamp → "Bitstamp by Robinhood" — brand absorption of a MiCA-licensed Tier-1 tracked firm

**Source class:** 2/4 boundary — firm-owned-channel brand-surface evidence.
**Firm:** Bitstamp — **Stratum 1** (Tier-1 exchange, EU-passported; `tracked-firms.md`: *"Long-running EU-licensed; strong MiCA-relevance"*).
**Captured:** 2026-07-29 (day 28 post-deadline). **Net-new.** Repo-wide greps for `robinhood crypto`, `bitstamp by robinhood`, `brand absorption` find nothing; the corpus's only Robinhood reference is the 2026-06-16 layoff row, filed as **"Crypto-adjacent perimeter."**
**Themes:** **Theme 4** (what happens to an EU marketing surface post-acquisition) · **Theme 1** (whose marketing function is it) · **Theme 5** (a perimeter classification that is wrong).

---

## What was directly verified this run

Fetched `https://blog.bitstamp.net/` on **2026-07-29**. Every item below was read off that page and its metadata:

| evidence | value |
|---|---|
| page title | **"The Bitstamp Blog by Robinhood — Crypto exchange news and insights"** |
| `meta-og:site_name` | **"The Bitstamp Blog by Robinhood"** |
| `meta-twitter:site` | **`@RobinhoodCrypto`** |
| `meta-twitter:creator` | **`@RobinhoodCrypto`** |
| author byline on **every** post | **"Bitstamp by Robinhood"** |
| listed X/Twitter social link | **`https://x.com/RobinhoodCrypto`** (LinkedIn/Facebook/Instagram still resolve to Bitstamp handles) |
| footer nav item | **"The Bitstamp + Robinhood Way"** (`bitstamp.net/bitstamp-way`) |
| copyright | **"All rights reserved © 2026 Bitstamp by Robinhood"** |
| oldest post on page 1 | **2025-07-30**, already titled *"Bitstamp by Robinhood partners with BBVA…"* |

**The regulated entity, from the same page's own legal footer:**

> "Bitstamp Europe S.A., which is authorized by the Commission de Surveillance du Secteur Financier (CSSF) in Luxembourg as a payment institution (licence number Z00000012) and **crypto-asset service provider (licence number N00000003)**"

**So: the MiCA CASP licence sits with Bitstamp Europe S.A., and the consumer-facing brand that licence markets under is now "Bitstamp by Robinhood", pointing at an X account named `@RobinhoodCrypto`.**

---

## Dating — what is solid and what is not

| fact | date | confidence |
|---|---|---|
| Robinhood completes $200M acquisition of Bitstamp | **2025-06-02 / 06-03** | **Solid.** Robinhood's own newsroom (`robinhood.com/us/en/newsroom/robinhood-completes-acquisition-of-bitstamp/`), CNBC 2025-06-02, CoinDesk 2025-06-03, The Block. |
| "Bitstamp by Robinhood" live on the blog | **by 2025-07-30 at the latest** | **Reasonable.** Oldest visible post carrying the name. **Caveat: CMS bylines and titles can be rewritten retroactively.** Not proof the brand was live that day. |
| brand live and complete on the owned channel | **2026-07-29** | **Directly verified this run.** |
| X handle renamed to `@RobinhoodCrypto` | **2026-07-14** | **WEAK — `[VERIFY]`.** Single aggregator source (`ababnews.com`), not primary. The *fact* of the handle is verified from Bitstamp's own metadata; **the date is not.** |
| X account display name **"Robinhood Crypto EU"** | — | **`[VERIFY]`.** Read from a search-result title, not fetched. If it holds, it is the sharpest single datum here. |

**Nothing above is entered as an enforcement or compliance event. It is a brand-surface record.**

---

## Why this matters to the report

### 1. Theme 4 — a third category of absence, and the absence panel now needs all three

Watch **(r)** was opened on 2026-07-28 after Gemini: a firm that **exits** a market produces no marketing signal there for a documented structural reason, and reading that as reticence is an error.

Bitstamp is a **different** object again. It has not exited. It is still EU-licensed, still operating, still publishing. **But it no longer markets under its own name.** Its EU marketing surface has been renamed to its US parent's brand.

The absence panel therefore needs to separate at least three things it currently cannot:

1. **Present and quiet** — reticence. The thing the report actually wants to measure.
2. **Structurally withdrawn** — Gemini (2026-02-05). No EU surface exists to be quiet on.
3. **Brand-absorbed** — Bitstamp. The surface exists, is active, and is no longer searchable under the tracked firm's name.

**Category 3 is the one that silently corrupts the instrument**, because every sweep the corpus runs searches on *"Bitstamp"*. A firm whose marketing now ships as *"Bitstamp by Robinhood"* and speaks from `@RobinhoodCrypto` will read as quiet to a name-keyed instrument no matter how loud it is. This is watch (p)'s defect with a different mechanism: not the wrong surface, **the wrong name on the right surface.**

### 2. Theme 5 — the layoff tracker's Robinhood row is misclassified

`2026-layoff-tracker.csv` records **Robinhood, 2026-06-16, ~290 cut, -10%** as *"Crypto-adjacent perimeter (broker)."*

**Robinhood has owned a Stratum-1 tracked firm since June 2025.** A 10% cut at Robinhood is a cut at the parent of Bitstamp. That does not automatically make it in-cohort — the corpus has no evidence the cuts touched Bitstamp Europe or any marketing function — but **"crypto-adjacent perimeter" is now the wrong label**, and the row's Theme-1 note (management-layer flattening, Tenev declining the AI framing) reads differently once the parent relationship is on the record.

**Action taken:** row **not** rewritten this run — the classification question deserves a deliberate ruling, not a drive-by edit, and no marketing-function evidence exists either way. **Flagged for Phase 2** and carried as watch **(s)**.

### 3. Theme 1 — an unanswerable question the report should ask out loud

Does Bitstamp still have a marketing function, or does Robinhood market Bitstamp? The corpus cannot tell from public sources, and `job-postings/bitstamp.csv` exists but shows no current marketing requisition. **That question — posed, with the brand evidence behind it, and left open — is more honest and more useful than any answer the corpus could currently defend.**

---

## Caveats printed, not smoothed

- **The acquisition is old news; the marketing-surface consequence is the finding.** The report should not present the 2025 acquisition as a discovery.
- **Two dates are aggregator-sourced and flagged `[VERIFY]`** (handle rename; display name). Neither is load-bearing for the finding, which rests on directly-verified owned-channel metadata.
- `bitstamp.net/bitstamp-way` **returned an empty body** when fetched this run (client-rendered). The "Bitstamp + Robinhood Way" page is a likely brand-positioning artefact and **has not been read**. Next run.
- **No claim is made that Bitstamp's EU marketing is non-compliant, reduced, or offshored.** The evidence is a name.

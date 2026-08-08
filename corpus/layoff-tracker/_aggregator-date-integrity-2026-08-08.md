# The aggregator's date column is not the article's date — measured, 2026-08-08

> **THIS FILE IS NOT THE TRACKER. NOTHING HERE IS A CORPUS FACT ABOUT A LAYOFF.**
> It is a verification record for three rows of `_aggregator-crossref-2026-08-07.csv`, and a rule derived from what verifying them found.

**Mandate.** The 2026-08-07 run record's recommendations 1 and 2 named four verification targets in priority order: promote Polygon (2026-01-15) and Ethereum Foundation (2026-06-23) after fetching each primary; then resolve **Coinbase 2026-03-05 (−18%)** and the **FalconX 19-day date conflict**. All four were executed this run. Two promotions landed. **Both verification targets turned out to be aggregator errors, and one of them was very large.**

---

## 1. Coinbase "2026-03-05, −18%" — **FALSE POSITIVE. It is the June 2022 layoff, mis-dated by three years and nine months.**

The 08-07 cross-reference marked this row **"*** HIGHEST-VALUE UNHELD ROW ***"** and warned:

> "A Coinbase contraction TWO MONTHS BEFORE the 05-05 round the corpus treats as Coinbase's 2026 event, and LARGER (18% vs 14%). **If real, the corpus's Theme-5 spine is built on the second cut, not the first.** [VERIFY] at Blockworks."

**Verified at Blockworks. It is not real as a 2026 event.**

The aggregator's `source` column points at Blockworks. The Blockworks article was fetched first-party this run, HTTP 200:

- **URL:** https://blockworks.com/news/coinbase-cut-workforce-ceo-wary-of-potential-recession
- **Headline:** *"Coinbase To Cut 18% of Workforce, CEO Wary of Potential Recession"*
- **Byline:** Shalini Nagarajan
- **Date, on the page: June 14, 2022 08:49 am**
- Hero image path: `/wp-content/uploads/**2022/06**/Coinbase-3.jpg`
- Body: 1,100 employees affected; headcount then "over 4,900"; $40–45M restructuring expense; Coinbase market value "just over $11 billion"; Armstrong quoted saying the firm "over-hired" since 2021 and citing a coming "crypto winter."
- **SEC filing referenced in the article:** `coin-**20220614**.htm`

Every internal date marker — URL slug of the image, the byline date, the SEC accession, the $11B market cap, the Terra collapse reference — places this in **June 2022**. Corroborated independently by the NPR and AOL headlines surfaced in the same search, both of which report the 18% cut and both of which are 2022 items.

### Consequences, stated as rules

1. **The corpus's Theme-5 Coinbase spine is SAFE.** The 2026-05-05 −14% round (Armstrong memo, AI-native pods) remains Coinbase's only 2026 contraction in evidence. **Watch (g)'s newest threat is discharged.** The broader watch (g) — Coinbase n=1 as a basis for generalisation — is untouched and stays open.
2. **The aggregator carries out-of-window rows inside its 2026 table.** Not a mis-typed day. A **three-year-and-nine-month** displacement, presented in a table headed 2026, with a correct link to a correctly-dated article. **The source column is reliable. The date column is not.**
3. **The 35% recall figure must never be printed without this caveat.** The 08-07 measure — corpus 19 of aggregator 54 — used the aggregator's row count as the denominator. **At least one of those 54 is not a 2026 event.** The true denominator is smaller and unknown, so **19/54 = 35% is a FLOOR on the corpus's recall, not an estimate of it.** Phase 2 may state "the corpus holds at least 19 of 54 rows listed by one public aggregator, whose 2026 table is demonstrably contaminated with at least one pre-window event" — and nothing stronger.
4. **The no-bulk-import rule paid for itself in one run.** Had the 08-07 run promoted its own "highest-value" row, this corpus would today be asserting a 2022 layoff as a March 2026 event, at a Tier-1 tracked firm, on the theme the report is built on.

---

## 2. FalconX — **corpus date CORRECT, aggregator wrong by 19 days.**

Conflict as logged 08-07: aggregator **2026-07-15**, corpus **2026-08-03**, both citing Bloomberg, both at −10%.

**Resolved in the corpus's favour.** The Bloomberg article URL surfaced this run carries the date in its own path:

`https://www.bloomberg.com/news/articles/**2026-08-03**/falconx-cuts-staff-on-extended-downturn-in-crypto-markets`
*"FalconX Cuts 10% of Workforce as Crypto Market Downturn Persists"*

Corroborated by Cointelegraph, crypto.news and CoinSpectator items all dated 2026-08-03/04. **The corpus row's 2026-08-03 stands. No change.** (The Bloomberg article itself remains paywalled and **was not fetched**; the date is taken from the URL path as surfaced in search, which is weaker than a fetch and is labelled as such.)

**Second aggregator date error in one run**, in the same direction as the first: the aggregator dates events *earlier* than their sources do.

**NOT ENTERED, recorded only:** search summaries state that roughly half of FalconX's Singapore office was cut "including senior managers and employees in **sales and accounting**." Sales is not marketing, and this reached the corpus as a **search-result summary of an unfetched article**. It does **not** disturb the standing finding. Flagged for capture, not claimed.

---

## 3. Polygon "2026-01-15, −60, −30%" — promoted, with the aggregator's percentage refused

Primary fetched (CoinDesk 2026-01-16). Row entered in `2026-layoff-tracker.csv` dated **2026-01-16** with headcount 60 and **percentage recorded as firm-disputed rather than −30%** — a Polygon Labs spokesperson refuted the 30% figure on the record in the very article the aggregator's chain rests on. **Third aggregator defect: importing a figure that the primary was written to rebut.** Full detail in the tracker row.

## 4. Ethereum Foundation "2026-06-23, −54" — promoted, and it resolves a standing corpus `[VERIFY]`

Primary fetched (CoinDesk 2026-06-23): 54 positions, ~20%. Here the **aggregator's date and headcount were both correct.** Row entered as PERIMETER. Full detail in the tracker row, including a new cohort-definition escalation: the Ethereum Foundation is not in `tracked-firms.md`.

---

## The rule, for every future run

**When promoting from an aggregator, verify the DATE against the linked source before anything else, and treat the aggregator's date as unevidenced until you have.**

Scorecard for the four rows verified this run:

| Row | Aggregator date | Verified date | Aggregator figure | Verified figure |
|---|---|---|---|---|
| Coinbase −18% | 2026-03-05 | **2022-06-14** | −18% | −18% (of a 2022 workforce) |
| FalconX −10% | 2026-07-15 | **2026-08-03** | −10% | −10% |
| Polygon −60 | 2026-01-15 | **2026-01-16** | −30% | **firm-disputed** |
| Ethereum Foundation −54 | 2026-06-23 | 2026-06-23 ✓ | −54 / −20% | 54 / ~20% ✓ |

**Three of four dates wrong. Two of four figures unusable as listed. One of four rows clean.**

### Rows this reflects on, without resolving them

The 08-07 cross-reference flagged **Bybit (−15 at −20%, source column EMPTY)** and **OKX (−10 at −33%)** for "arithmetic smell" — percentages implying organisations of 75 and 30 people at top-tier exchanges. A second explanation is now available and is at least as likely: **they may be correctly-figured regional or historical events carrying wrong dates**, exactly as the Coinbase row was. Neither is entered. Neither is explained. **Recorded as a hypothesis with a named test — fetch each linked source and read its date — not as a finding.**

### And the harder question, left open on purpose

The 08-07 run measured the corpus against the aggregator and found the corpus wanting at 35%. Today the instrument that produced that number was itself measured, and it fails on 3 of 4 dates. **Both instruments are now known to be defective in different ways, and the corpus does not yet know which is worse.** What survives is narrower and duller than either day's headline: *the corpus holds 21 primary-verified rows, every one of which has had its date read at its own source, and it does not know how many 2026 crypto contractions exist.* That is the honest state, and it should be the Phase-2 wording.

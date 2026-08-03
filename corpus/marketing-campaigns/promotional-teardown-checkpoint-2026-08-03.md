# Promotional teardown — day-3 checkpoint, and the surface count keeps growing (Kraken · OKX)

**Class:** firm-side marketing action (successor to `promotional-teardown-checkpoint-2026-08-02.md`)
**Checkpoint date:** **2026-08-03** — day 3 after the 31 July close, day 33 post-MiCA-deadline
**Method:** direct primary fetch of each firm's own live pages on 2026-08-03. Every claim below is verbatim from a page fetched this run.
**Standing caveat, unchanged:** reads are **as served to a non-EEA fetch**. See §4 — this run recovered the first hard evidence about what geo-detection actually does to these pages, and it does not help the firms.

---

## Headline: three days, zero teardowns, and every re-read finds another surface

The 08-02 record documented 3 lapsed campaigns across 5 surfaces. Re-reading two of them on day 3 found **both still live and two more surfaces neither prior checkpoint knew about.**

| firm | surface | first captured | state 2026-08-03 | verdict |
|---|---|---|---|---|
| **Kraken** | `kraken.com/europe-switch` | 08-01 | **LIVE**, byte-comparable copy for a 3rd day | **LAPSED — day 3** |
| **Kraken** | `blog.kraken.com/news/industry-news/europe-mica-switch` | **08-03 — NEW** | **LIVE**, present tense, promo CTAs ×3 | **LAPSED — 3rd Kraken surface** |
| **OKX** | `okx.com/en-eu/learn/okx-europe-deposit-bonus-mica-deadline` | **08-03 — NEW (EEA-locale path)** | **LIVE**, present tense, CTA ×2 | **LAPSED — day 3** |
| **OKX** | `okx.com/en-sg/learn/mica-deposit-bonus-campaign` | 08-03 — **identified, NOT fetched** | unknown | **[VERIFY]** |
| **Bitpanda** | `bitpanda.com/en/campaigns/bya-june-26` | 08-02 | **NOT RE-READ THIS RUN** | carried, unresolved |

**Running surface count for the finding: 7 identified, 6 fetched, 5 confirmed lapsed.**

---

## 1. Kraken — third consecutive day live, and a **third** owned surface

### 1a. `https://www.kraken.com/europe-switch` — fetched 2026-08-03, HTTP 200

Copy is **materially identical to the 08-01 and 08-02 captures**. Nothing has been touched in 72 hours:

- H1: **"Most exchanges aren't licensed after July 1. Kraken is."**
- *"MiCA licensed. MiFID licensed. Operating since 2011. **Switch now and enter our €1M prize draw**."*
- Live CTAs: **"Switch to Kraken"** (→ `kraken.com/sign-up?rfr=pro-web`), **"Enter the €1M draw"** (→ `proapp.kraken.com/9f1e/hg0aq9gh`) — served **twice** on the page
- Standing legend, unchanged: **"Lottery closes July 31. T&Cs apply."**
- Section header still in the imperative: **"Switch to Kraken before July 31. Enter for €1M."**
- `meta-description` / OG / Twitter cards **all still** carry *"Switch now and enter our €1M prize draw… Closes July 31."*

**The two internal inconsistencies logged on 08-02 both persist unchanged on day 3:**
- Step 2 says *"Every euro deposited **from June 22** to July 31"*; FAQ says *"**Between June 22** and July 31, 2026"*.
- Body text claims *"**Forbes best crypto exchange 2025**"*; the badge rail on the same page claims *"**Forbes Most popular crypto exchange 2026**"*.

### 1b. NEW — `https://blog.kraken.com/news/industry-news/europe-mica-switch`

Fetched 2026-08-03, HTTP 200. **A third Kraken-owned surface running the same expired campaign, in the present tense.**

- `meta-article:published_time` **2026-06-19T16:41:32+00:00** · `meta-article:modified_time` **2026-06-19T16:58:32+00:00** — **the post has not been edited since 17 minutes after publication.** Not touched at campaign close.
- Kraken's own category tags on the post: **"Industry News", "Promotions"** — the firm classifies it as promotional inventory, not archive.
- Present-tense promotional copy, day 3 post-close: *"To mark the moment, **we're rewarding traders who make the move**."*
- Three live enrolment CTAs to `kraken.com/europe-switch`: *"Enrol in the prize draw"* ×2, *"Enrol in the €1M prize draw"*.
- TL;DR bullet still reads: *"Make the switch now, and every euro you deposit earns an entry into a **€1M prize draw**."*

### 1c. The three-day date conflict is now **2 surfaces against 1**

The 08-02 record resolved a primary-vs-primary conflict in the stated start date of a €1,000,000 consumer prize draw. Day 3 adds a third data point, and it lands against the landing page:

| Kraken surface | stated promotion start |
|---|---|
| `kraken.com/europe-switch` (Step 2 + FAQ) | **June 22** |
| `support.kraken.com/articles/1m-eur-prize-draw` | **19 June 2026 at 11:00 UTC** |
| **`blog.kraken.com/…/europe-mica-switch` (NEW)** | **"The promotion begins on 19 June 2026 at 11:00 UTC and ends on 31 July 2026 at 13:59 UTC"** |

**Two of Kraken's three owned surfaces say 19 June; the campaign landing page — the one carrying the acquisition CTA — says 22 June.** The outlier is the commercial surface. The corpus asserts no breach and must not. What it records is that the substantive terms of a €1M consumer promotion differ across the firm's own estate, and that the divergent surface is the selling one.

**The blog also states the enrolment condition the landing page omits**, matching the support article: *"in order for your deposits to earn entries, **you must first enrol in the prize draw**."* The landing page's Step 2 says flatly that every euro deposited in the window earns an entry. **Three surfaces, two different materially-conditioned offers.**

### 1d. A compliance-furniture artefact worth recording separately

The Kraken blog post serves, at the very top of the page, the **UK FCA-prescribed risk warning**: *"Don't invest unless you're prepared to lose all the money you invest. This is a high-risk investment and you should not expect to be protected if something goes wrong."* linking to `kraken.com/legal/uk/disclaimer`.

The promotion described on that page is **explicitly EEA-only** — *"This promotion is only open to eligible customers residing in the European Economic Area (EEA)"* — and the UK is not in the EEA.

**A UK financial-promotion banner is being served, site-wide and unconditionally, on an article whose offer is not available to UK consumers.** This is not alleged to be a breach — a blanket UK warning is over-inclusive, not under-inclusive, and over-inclusion is the safe direction. It is recorded because it is the same defect class as everything else in this file: **promotional furniture applied by template rather than by state.** The blanket banner is what a firm ships when the compliance layer is global config and the campaign layer is regional content, and the two do not read each other.

### 1e. A named Kraken quote — deliberately **not** filed as class 4

The blog carries an on-the-record quote from **Andrew Mulvenny, "Kraken Head of Crypto-Asset Service Provider Trading Platform"**:

> "Since receiving authorisation from the Central Bank of Ireland in June 2025, Kraken has operated fully under the MiCA framework, a milestone that reflects our enduring commitment to trust, compliance, and a thriving crypto ecosystem. For our EU customers, that means world-class services backed by the highest regulatory standards."

**This does NOT qualify under `methodology.md` §4** — the role is a trading-platform head, not CMO / VP Marketing / Head of Brand / Head of Growth. It is recorded here, inside the campaign file, as **firm-sourced copy embedded in a promotional artefact**, and it is **not** counted in the class-4 register. Logging the refusal is the point: §4's role gate is only worth having if it is applied when applying it costs the corpus an item.

---

## 2. OKX — a second lapsed surface, on the **EEA locale path**, and a third identified

### 2a. NEW — `https://www.okx.com/en-eu/learn/okx-europe-deposit-bonus-mica-deadline`

Fetched 2026-08-03, HTTP 200. The 08-02 record captured OKX's **`/en-us/`** path. **This is the `/en-eu/` path — the EEA-locale version of the same article — and it is a distinct URL that was not previously in the corpus.**

- **Published on Jun 12, 2026 · Updated on Jun 30, 2026** — updated the day before the deadline, and **not touched since the campaign closed**.
- Present tense, day 3 post-close: *"**From 29 June until 31 July 2026**, anyone who resides in the European Economic Area (EEA), transfers crypto or deposits cash to OKX Europe and opts in **receives an 8% bonus (up to €20,000 in USDC)** on their net deposit, with a minimum of just €10 to qualify."*
- TL;DR block still leads with **"Campaign period: 29 June – 31 July 2026"**.
- Live CTAs served twice: **"Claim your deposit bonus"** → `my.okx.com/ul/LhoH7A`; plus **"Create your OKX account"** → `my.okx.com/ul/rL3Wn5` and three in-table deep links (`ul/L1TecM`, `ul/X2fpJ1`, OKX Card).
- Metadata unchanged: *"Transfer **before the 1 July 2026 MiCA deadline** to a fully regulated exchange."*

**Full MFSA licence stack captured first-party** (Theme-4 value independent of the teardown finding): MiCA CASP — MFSA, issued **27 January 2025**, stated as covering **9 of 10 MiCA services**, passported across **30 EEA states**; MiFID II via **OKX EUROPE MARKETS LTD**, MFSA, **April 2022**; **Payment Institution** licence, MFSA, **February 2026** (OKX Card / OKX Pay). Footer entity statement: *"OKX Europe Limited operating under the trade name OKX is now a crypto-assets trading platform authorised as a Crypto-Asset Services Provider by MFSA pursuant to Article 28 of the Markets in Crypto-Assets Act (Chapter 647 of the Laws of Malta)."*

### 2b. NEW — a third OKX surface identified, **not fetched**

Search surfaced **`https://www.okx.com/en-sg/learn/mica-deposit-bonus-campaign`** — titled *"8% Deposit Bonus on OKX: Get Up to €20,000 in USDC | OKX Singapore"*. **An EEA-only, MiCA-keyed deposit-bonus campaign article sitting on OKX's Singapore locale path.** The page was **not fetched this run and no claim is made about its live state or contents.** `[VERIFY]` — it is the single cheapest high-value fetch for the next run, because if it is live it converts the finding from *"campaigns are not torn down"* to *"regulated regional promotions are syndicated across locales that the promotion excludes"*, which is a materially larger claim.

---

## 3. What the day-3 read does to the finding

**Replication holds and the shape sharpens.** Two firms re-tested at day 3, **2/2 still live**, and each re-read surfaced additional inventory neither prior checkpoint had found. The pattern is not "a page was left up". It is:

> **A campaign is shipped as N surfaces across owned properties — landing page, support article, blog, per-locale learn articles — and the teardown, when it happens at all, is scoped to fewer surfaces than the launch was.**

Every checkpoint that has looked harder has found more inventory. **The corpus does not yet know the denominator for any of these campaigns.** That is now the finding's principal known weakness, and it should be stated in Phase 2 rather than hidden: the report can say *at least N surfaces at firm X were live on day D*, and cannot say *how many surfaces the campaign had*.

---

## 4. The geofence caveat — first hard evidence, and it cuts against the firms

Every teardown record so far has carried the same non-negotiable qualifier: these are **non-EEA fetches**, and a geofenced EEA visitor might be served a closed state. That caveat still stands and is **not** discharged. But this run recovered the first direct evidence about what the geo-layer actually does.

**The OKX `/en-eu/` page detected the fetch's US origin and said so, in a banner served above the campaign content:**

> "**Looks like you're in the United States. Switch to the United States site for products available in your region.** Switch site"

**OKX correctly identified a non-EEA visitor, told that visitor they were in the wrong region — and then served the full EEA-only campaign article, in the present tense, with live CTAs, anyway.** The geo-layer fired and changed nothing about the promotional payload.

What this does and does not establish:

- **Does establish:** on this surface, geo-detection is present, functioning, and **decoupled from promotional state**. The page knows where you are and serves the offer regardless.
- **Does establish:** the "maybe a geofence hides all this from EEA users" defence is weaker than it looked. At least one firm's geo-layer is a *notice*, not a *gate*.
- **Does NOT establish** anything about what an actual EEA IP is served. An EEA visitor might see the same page (most likely, since it is the EEA-locale path) or a closed state. **The caveat stays on the finding.**

**The EEA-egress read remains the single item between this finding and print** — but the bar it must clear has moved. It is no longer "does a geofence exist"; it is "does the geofence do anything to the offer".

---

## Cross-references

- `promotional-teardown-checkpoint-2026-08-02.md` — day 2; 3/3 replication; Bitvavo control; BitMart same-page contradiction.
- `mica-capture-campaign-lapse-checkpoint-2026-08-01.md` — day 1; n=2.
- `mica-competitive-capture-2026-06.md` — the campaigns at launch.
- `../layoff-tracker/2026-layoff-tracker.csv` — BitMart row; the wind-down notice serving a live signup CTA.
- `../regulator-filings/afm-cnmv-post-deadline-index-sweep-2026-08-03.md` — the same day's null: the regulators most likely to act on advertising conduct have not.

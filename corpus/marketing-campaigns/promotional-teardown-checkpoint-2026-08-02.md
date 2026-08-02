# Promotional teardown — the day-2 replication checkpoint (Kraken · OKX · Bitpanda · Bitvavo · BitMart)

**Class:** firm-side marketing action (successor to `mica-capture-campaign-lapse-checkpoint-2026-08-01.md`)
**Checkpoint date:** **2026-08-02** — day 2 after the 31 July close, day 32 post-MiCA-deadline
**Mandate:** the 08-01 run's recommendation #1 — *"replicate the lapse checkpoint on Coinbase, Bitpanda, Bitvavo and Gate; turns n=2 into n=6 and decides whether this is a finding or an anecdote."*
**Method:** direct primary fetch of each firm's own live campaign page on 2026-08-02. No search-engine summaries used as evidence; every claim below is verbatim from a page fetched this run.
**Standing caveat, unchanged and non-negotiable:** all reads are **as served to a non-EEA fetch**. A geofenced EEA visitor may be served a closed state. **This finding must not be printed without that qualifier** until the chrome lane with EEA egress resolves it (08-01 recommendation #2, still open).

---

## Headline: the finding replicated, and then it outgrew its own frame

**3 of 3** deadline-keyed campaigns whose windows closed on 31 July were still publicly live, in the present tense, with working CTAs, on 2026-08-02 — **two days** after close, not one.

And the fourth case found this run is not a campaign at all. **BitMart is serving a live acquisition CTA on the same page that announces it has stopped accepting registrations.** That collapses the framing: this is not a MiCA-campaign teardown problem. It is a **promotional-surface-versus-operational-state** problem, and MiCA capture campaigns were merely where the corpus first noticed it.

| firm | surface | window | state on 2026-08-02 | verdict |
|---|---|---|---|---|
| **Kraken** | `kraken.com/europe-switch` | closes 31 Jul | **LIVE**, present tense, 2 CTAs | **LAPSED — day 2** |
| **Kraken** | `support.kraken.com/articles/1m-eur-prize-draw` | closes 31 Jul | **LIVE**, present tense ("is running") | **LAPSED — 2nd surface, NEW** |
| **OKX** | `okx.com/en-us/learn/okx-europe-deposit-bonus-mica-deadline` | 29 Jun – 31 Jul | **LIVE**, present tense, 2 CTAs | **LAPSED — day 2** |
| **Bitpanda** | `bitpanda.com/en/campaigns/bya-june-26` | "valid until 31st July 23:59" | **LIVE**, present tense, 3 CTAs | **LAPSED — NEW, n→3** |
| **Bitvavo** | `bitvavo.com/en/news/crypto-deposit-promo` | 25 Jun – **30 Sep 2026** | **LIVE, and correctly so** | **CONTROL — cannot lapse** |
| **BitMart** | `bitmart.com/…/orderly-cessation` | registrations closed 26 Jul | **LIVE "Register now" CTA on the closure notice** | **CONTRADICTION ON ONE PAGE** |
| **Coinbase** | — | — | no MiCA capture campaign located | **ABSENCE (see below)** |

---

## 1. Kraken — still live on day 2, and a **second** lapsed surface found

`https://www.kraken.com/europe-switch` — fetched 2026-08-02, HTTP 200. Copy **identical to the 08-01 capture**, nothing changed in 24 hours:

- H1: **"Most exchanges aren't licensed after July 1. Kraken is."**
- *"MiCA licensed. MiFID licensed. Operating since 2011. **Switch now and enter our €1M prize draw**."*
- Live CTAs: **"Switch to Kraken"**, **"Enter the €1M draw"** (→ `proapp.kraken.com/9f1e/hg0aq9gh`)
- Standing legend: **"Lottery closes July 31. T&Cs apply."**
- `meta-description` / OG / Twitter descriptions all still: *"…Switch now and enter our €1M prize draw. Every euro deposited earns one entry. **Closes July 31**."*

### NEW — a second Kraken surface, also lapsed

`https://support.kraken.com/articles/1m-eur-prize-draw` — fetched 2026-08-02, HTTP 200, **"Last updated: July 1, 2026."**

> "Kraken **is running** a deposit prize draw for clients in the European Economic Area (EEA), with a single prize of €1,000,000."

Present tense, day 2 post-close, with full enrolment instructions for three apps (Kraken app / Kraken Pro app / Kraken Pro web) and a live free-entry route via **Sweeppea** (`swpp.me/a/depositsweeps26`). **Two Kraken-owned surfaces, both lapsed.** The 08-01 record treated this as a single-page defect; it is not.

### NEW — the internal date conflict is now **resolved, and it is real**

The 08-01 run flagged a primary-vs-primary date conflict as `[VERIFY]`. **Both sides are now captured in the same run, so it is no longer a verification item — it is a finding.**

| Kraken surface | stated promotion start |
|---|---|
| `kraken.com/europe-switch` — Step 2 | *"Every euro deposited **from June 22** to July 31 earns one entry"* |
| `kraken.com/europe-switch` — FAQ | *"**Between June 22** and July 31, 2026, every euro you deposit…"* |
| `support.kraken.com/articles/1m-eur-prize-draw` | *"The promotion runs from **19 June 2026 at 11:00 UTC** to 31 July 2026 at 13:59 UTC"* |

**A three-day discrepancy in the stated start date of a €1,000,000 consumer prize draw, between two of the firm's own pages, both live simultaneously.** The support article additionally states that entries **only accrue after enrolment** — a material condition that appears on the support page and **not** on the campaign landing page, whose Step 2 says flatly that every euro deposited in the window earns an entry.

The corpus asserts no breach and must not. What it records is that the *substantive terms* of the offer differ across the firm's own estate, which is a different and more serious class of defect than a page left up too long.

**A third inconsistency on the same page, minor but same family:** the body text claims *"Forbes best crypto exchange 2025"*; the badge rail on the same page claims *"Forbes Most popular crypto exchange 2026"*. Two different award claims about the same awarding body on one page.

## 2. OKX — still live on day 2

`https://www.okx.com/en-us/learn/okx-europe-deposit-bonus-mica-deadline` — fetched 2026-08-02, HTTP 200. **Published Jun 12, 2026 · Updated Jul 07, 2026** (unchanged — the page has *not* been touched since the campaign closed).

> *"**From 29 June until 31 July 2026**, anyone who resides in the European Economic Area (EEA), transfers crypto or deposits cash to OKX Europe and opts in **receives an 8% bonus (up to €20,000 in USDC)** on their net deposit, with a minimum of just €10 to qualify."*

Live CTA **"Claim your deposit bonus"** (→ `my.okx.com/ul/LhoH7A`) served twice. Metadata still: *"Transfer **before the 1 July 2026 MiCA deadline**…"*

**Second OKX surface confirmed from its own related-articles rail** (first-party, dated): `okx.com/en-us/learn/mica-deposit-bonus-campaign` — *"50 million up for grabs! Deposit Crypto or Cash on OKX and Get an 8% Bonus (Up to €20,000)"*, **dated Jul 22, 2026**. OKX, like Kraken, runs the lapsed offer on **more than one** owned page.

**Licence stack captured first-party (Theme 4, useful independent of the lapse):** OKX Europe Limited holds **MiCA CASP (MFSA, 27 Jan 2025, 9 of 10 MiCA services)**, **MiFID II (MFSA, April 2022)** and **Payment Institution (MFSA, February 2026)**, all passported across 30 EEA states. The page states the CASP licence covers *"9 of 10 MiCA services"* — a specificity worth quoting, because it is a firm publishing the *extent* of its authorisation rather than the fact of it.

## 3. Bitpanda — **NEW, and it takes the count to 3/3**

`https://www.bitpanda.com/en/campaigns/bya-june-26` — fetched 2026-08-02, HTTP 200.

- H1: **"Get 5% cashback on your crypto transfer"**
- *"Transfer your crypto assets to one of Europe's leading investment platforms, trusted by 7+ million people. **Offer valid until 31st July 23:59**."*
- Live CTAs **"Transfer Now"** / **"Get started now"** (×3, → `account.bitpanda.com/en/register`)
- *"To enter, you must be a fully verified Bitpanda user, accept the Terms, and transfer any amount of crypto to Bitpanda **during the Promotion Period**."*
- OG/Twitter description: **"And win 3 BTC."**

**Same failure mode, third mechanic (cashback + raffle), third NCA-supervised entity.**

**Disclosure quality note — Bitpanda is the panel's best jurisdictional splitter, which makes the lapse more interesting, not less.** The terms block distinguishes by market and by entity:

> *"**AT/EU/CH:** Terms apply. Rewards are granted in **EURCV** and reserved to the first 15,000 new users… Regulated crypto-asset services are provided by **Bitpanda GmbH, authorized by the FMA** in accordance with MiCAR.*
> ***DE:** Terms apply. Rewards are granted in **BTC** and reserved to the first 15,000 new users… Regulated crypto-asset services are provided by **Bitpanda Asset Management GmbH, authorized by the BaFin** in accordance with MiCAR.*
> *You can also participate for free and get 10 entries by submitting a form here."*

Two entities, two NCAs, two reward currencies, a free-entry route, and a risk line (*"Investing in crypto-assets involves risks, up to total loss"*) — **all on the disclosure edge, all correct.** The lifecycle edge is the one left loose. That is precisely the 08-01 finding, replicated at a third firm that is, on every other axis, the most careful of the three.

**A secondary source was falsified in the process.** German trade coverage of Bitpanda's MiCA offer stated transfers counted *"bis zum 12. Juli 2026, 23:59"* and that the offer was capped at *"die ersten 10.000 verifizierten Neukunden."* **Bitpanda's own page says 31 July 23:59 and 15,000.** Both figures in the secondary are wrong. Primary wins; the secondary is not entered. **Third consecutive run in which a search-surfaced summary was contradicted by the primary it summarised.**

## 4. Bitvavo — the **control case**, and it changes what the finding means

`https://bitvavo.com/en/news/crypto-deposit-promo` — fetched 2026-08-02, HTTP 200, dated **Jun 25, 2026**.

Bitvavo's MiCA-adjacent capture campaign runs **25 June 2026 → 30 September 2026**, with reward *"calculated over the full campaign period and paid out in euros on **14 October 2026** before 17:00 CET"*, max €10,000 per user. Structure: **4% APY base for depositing + up to 6% more scaled on trading volume (5× deposit → 5%, 10× → 6%, 20× → 10%)**, opt-in via an in-app **Campaign Hub**, Auto-Earn required.

**Bitvavo is live and correct.** Its window has not closed. It therefore cannot lapse — and that is the point:

> **The firms that lapsed are the firms that keyed their campaign to the deadline *date*. The firm that did not lapse keyed its campaign to a capture *period* that outlasts the deadline by three months.**

This is a genuine control, not a null. It converts a defect observation into a design observation: **a campaign whose end date is the regulatory event inherits the regulatory event's cliff; a campaign whose end date is a commercial horizon does not.** Bitvavo also carries the correct MiCA hedge in the same copy — *"Staking and lending are not regulated under MiCA and the protections afforded to users of regulated services may not apply to you"* — and names its regulator and address (**AFM, Vijzelgracht 50, Amsterdam**) in the footer.

## 5. BitMart — the same failure mode, in its most extreme available form

`https://www.bitmart.com/en-US/support/articles/…/53544595916059`, **"Important Notice Regarding the Orderly Cessation of BitMart Operations", published 2026-07-26 01:40**, fetched 2026-08-02.

The document states:

> *"Beginning **July 26, 2026, at 01:30 (UTC)**, BitMart will gradually stop accepting new user registrations."*

Served **on the same page, below the notice**:

> **"Earn up to $14,000 in rewards — [Register now]"** → `bitmart.com/en-US/register?utm_source=growth-frontend&utm_medium=support-article`

**A UTM-tagged, growth-attributed acquisition CTA, offering a $14,000 reward, embedded in the announcement that registrations are closed and the exchange is winding down.** The contradiction is not across two pages or across two days. It is **within one document**, and the tracking parameters show it is served by a growth system that is not reading the operational state of the business.

This is the cleanest available evidence for the generalised claim, and it is the reason the finding should be re-framed before Phase 2:

> **It is not "MiCA campaigns are not torn down."**
> **It is "promotional surfaces are not wired to the operational state of the business."**
> Four firms. Four mechanics (prize draw / deposit bonus / cashback+raffle / evergreen signup reward). Four supervisory contexts. One failure mode.

## 6. Coinbase — absence, recorded as data

The 08-01 mandate named Coinbase in the replication set. **No Coinbase EU MiCA capture campaign was located this run**, either by search or in any first-party rail encountered. The corpus does **not** record this as "Coinbase tore its campaign down correctly." It records that **no evidence was found that Coinbase ran a deadline-keyed EU capture campaign at all** — which, if it holds under a direct own-channel sweep, is itself a Theme-1 data point: the tracked firm with the highest public posting velocity and the most explicit published operating model (AI-native pods, 2026-05-05) is the one absent from the panel's single largest coordinated acquisition moment. **Do not print either reading until watch (p) has swept Coinbase's own EU channels.** Gate was not reached this run.

---

## What is now printable, and what is not

**Printable (with the non-EEA-fetch qualifier):**
- 3 of 3 deadline-keyed capture campaigns at MiCA-licensed EU firms were serving expired offers in the present tense on day 2 after close, verified by direct first-party fetch.
- Two of the three run the lapsed offer on **more than one** owned surface.
- Kraken's own two surfaces state **different start dates** and **different entry conditions** for the same €1M draw.
- A firm in active wind-down serves a live, growth-tagged acquisition CTA inside its own cessation notice.
- Bitvavo is a clean control: a period-keyed campaign spanning the deadline did not lapse.

**Not printable yet:**
- Any breach assertion. None is made anywhere in this file.
- Any claim about what an EEA-geofenced visitor sees. **Unresolved.**
- Any claim about Coinbase's campaign posture. **Absence unverified against own channels.**
- Any n beyond 4 firms. Gate untested.

**Cheapest next moves:** (1) EEA-egress re-read of all four lapsed surfaces via the chrome lane — this is now the single highest-value open item on the finding, because it is the only thing standing between it and print; (2) Gate + Coinbase own-channel sweep to close the panel; (3) re-check all four on 08-09 to date the teardown, which converts "lapsed" into a measured **time-to-teardown** metric — a number no competing report will have.

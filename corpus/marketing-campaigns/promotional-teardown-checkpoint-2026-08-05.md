# Promotional teardown — day-5 checkpoint: the neglect explanation is dead (Kraken · OKX)

**Class:** cross-cutting — Theme 4 (MiCA readiness / exposure surface) + Theme 1 (gate-stack visibility)
**Captured:** 2026-08-05. Day 5 after both campaigns' stated close (31 July 2026). Day 35 post-deadline.
**Prior checkpoints:** `mica-capture-campaign-lapse-checkpoint-2026-08-01.md` · `promotional-teardown-checkpoint-2026-08-02.md` · `promotional-teardown-checkpoint-2026-08-03.md`
**Caveat carried on every read:** all fetches originate outside the EEA. See §5 — the caveat is now materially weakened by direct evidence, but not discharged.

---

## Headline: the page was edited today, and the expired offer was left in it

Every prior checkpoint had an innocent explanation available: **nobody looked.** The OKX `/en-eu/` article had been recorded as *published 12 Jun, updated 30 Jun, untouched since close* — consistent with simple neglect.

**That explanation is now falsified by the page's own timestamp.**

> `https://www.okx.com/en-eu/learn/okx-europe-deposit-bonus-mica-deadline`
> **"Published on Jun 12, 2026 · Updated on Aug 05, 2026"**

**The page was modified TODAY — five days after the campaign it advertises closed — and it still opens with:**

> **"The EU's MiCA deadline lands on 1 July 2026, and OKX is making it worth your while to move before then."**

Present/future tense, **35 days after the deadline passed**. Below it, unchanged: *"From 29 June until 31 July 2026, anyone who resides in the EEA … **receives** an 8% bonus"* — present tense, 5 days after close — and **three live acquisition CTAs** (`my.okx.com/ul/LhoH7A`, `/ul/rL3Wn5`, `/ul/L1TecM`).

**Someone touched this page today and did not retire the offer.** The finding is no longer *"promotional surfaces are not torn down."* It is:

> **Promotional surfaces are being actively maintained while advertising an expired offer and a deadline that has already passed. The teardown is not being missed; it is not in the workflow.**

That is a governance finding, not a hygiene one, and it is the strongest artefact this corpus holds.

---

## 1. Surface inventory — the denominator problem, partially solved

Watch (c)(iv) recorded that the corpus could not state how many surfaces any of these campaigns had. **Today the language switchers on two OKX surfaces gave the count directly.**

### 1a. OKX — at least **31** identified surfaces for one campaign

| surface family | URL pattern | locales enumerated on-page | count |
|---|---|---|---|
| Learn article A | `okx.com/<locale>/learn/okx-europe-deposit-bonus-mica-deadline` | en-eu, de, es-es, fr-fr, it, nl, pl, pt-pt, ro, nb, fi, sv, cs | **13** |
| Learn article A (extra locales) | `okx.com/en-us/…` (captured 08-02) | en-us | **1** |
| Learn article B | `okx.com/<locale>/learn/mica-deposit-bonus-campaign` | en-sg (fetched today), en-eu (linked today) | **2** |
| Campaign page | `my.okx.com/<locale>/campaigns/switch-to-okx-deposit-bonus` | en-eu, de, es-es, fr-fr, it, nl, pl, pt-pt, ro, nb, fi, sv, zh-hans-eu, cs | **14** |
| Cross-promoting article | `okx.com/<locale>/learn/rewardmaxxing-okx-stack-rewards` (29 Jul; names "The 8% MiCA Deposit Bonus" as currently running) | en-eu, en-sg seen | **1+** |
| **Total identified** | | | **≥31** |

**Fetched and confirmed live at day 5: 4** (`/en-eu/learn/…mica-deadline`, `/en-sg/learn/mica-deposit-bonus-campaign`, `my.okx.com/en-eu/campaigns/switch-to-okx-deposit-bonus`, plus `/en-us/` on 08-02). **The other ~27 are identified from the firm's own language switchers and were NOT fetched.** No claim is made about their state.

**This is the first time the corpus can put a floor under the denominator.** Phase 2 may say: *OKX's MiCA capture campaign shipped across at least 31 identified owned surfaces spanning 15 locales; four were re-read on day 5 and all four were live.* It may **not** say what share was torn down.

### 1b. Kraken — 3 owned surfaces, all still live at day 5

Unchanged from 08-03. `kraken.com/europe-switch` re-fetched today: **byte-comparable copy for a fifth day.**

---

## 2. OKX `/en-sg/` — the Singapore-locale surface, FETCHED (closes the 08-03 `[VERIFY]`)

`https://www.okx.com/en-sg/learn/mica-deposit-bonus-campaign` — fetched 2026-08-05, HTTP 200.

- `meta-og:site_name`: **"OKX Singapore"**. `meta-description`: **"OKX Singapore - Deposit crypto or cash on OKX before 31 July 2026…"**
- **"Published on 16 Jul 2026 · Updated on 22 Jul 2026."**
- Headline: *"50 million up for grabs! Deposit Crypto or Cash on OKX and Get an 8% Bonus (Up to €20,000)"*
- Body, present tense at day 5: *"**Until 31 July 2026**, any OKX user residing in Europe who deposits crypto or cash to OKX and opts in **gets** an 8% bonus"*
- Regulatory copy: *"MiCA's 18-month licensing grace period for EU exchanges ended 1 July 2026; **unlicensed exchanges may face account restrictions or forced offboarding**"*
- **Two live CTAs** ("Claim your deposit bonus" → `my.okx.com/ul/LhoH7A`).

**Verdict: LAPSED — live at day 5, on a Singapore locale path.**

**What this converts.** The 08-03 record said that if this page were live it would move the finding from *"campaigns are not torn down"* to *"regulated regional promotions are syndicated across locales the promotion excludes."* **It is live. The larger claim is now evidenced.** An EEA-only, MiCA-keyed, MFSA-licence-anchored acquisition offer is published under an **OKX Singapore** masthead. MAS is a tracked authority in `methodology.md` §3 and the corpus has never swept it at source — that gap is now materially more relevant.

**Discipline, stated plainly:** the corpus records the artefact. It does **not** assert a MAS breach, a MiCA breach, or any breach. Locale paths are not the same as targeting, and the page carries a jurisdictional disclaimer (*"may cover products that are not available in your region"*).

---

## 3. `my.okx.com/en-eu/campaigns/switch-to-okx-deposit-bonus` — NEW surface, and the sharpest single artefact yet

Fetched 2026-08-05, HTTP 200. **Not in any prior checkpoint.**

**The page announces its own early termination and keeps selling anyway.**

Verbatim, from the page's own terms:

> **"Activity Period Change: This Promotion will end earlier than originally scheduled and will now close at 12:00 GMT+2 on 28 June 2026."**

And in the hero, on the same page, on **5 August 2026 — day 38 after that stated close**:

> **"Get up to 8% back on your deposits. The MiCA deadline is coming."**
> **"Offer valid June 12 to June 28. T&Cs apply."**
> **[Join now]** · **[Deposit Now]** · **[Check My Payouts]**

**"The MiCA deadline is coming"** — future tense — **35 days after the deadline arrived**, on a page that states its own offer closed 38 days ago, under a live enrolment button.

### 3a. A campaign-window conflict inside OKX's own estate

| OKX surface | stated activity period |
|---|---|
| `my.okx.com/en-eu/campaigns/switch-to-okx-deposit-bonus` | **12 June → 28 June 2026** (revised; "ends earlier than originally scheduled") |
| `okx.com/en-eu/learn/okx-europe-deposit-bonus-mica-deadline` | **29 June → 31 July 2026** |
| `okx.com/en-sg/learn/mica-deposit-bonus-campaign` | **until 31 July 2026** |

Also divergent: the campaign page offers a **tiered 5–8% match, cap $500,000 net deposit, max 40,000 USDC**; the learn articles offer a **flat 8%, min €10, max €20,000 USDC**.

**Most likely reading: two sequential campaign phases (June phase, then a 29 Jun–31 Jul phase), not one campaign described inconsistently.** The corpus adopts that reading and **asserts no contradiction**. What it records is narrower and still material:

> Both phases are still live and still selling on 5 August 2026, and a consumer arriving on the firm's own estate today can reach two different, both-expired, materially different offers for what is presented as the same "8% deposit bonus."

### 3b. Disclaimer asymmetry across surfaces of the same campaign — **new, and report-grade**

The `my.okx.com` campaign page carries the MiCA marketing-communications statement, verbatim:

> **"This crypto-asset marketing communication has not been approved by any competent authority in any Member State."**

The two `okx.com/…/learn/…` surfaces — which carry the same offer, the same CTAs, and the same MiCA framing — **do not.** They carry a generic informational/no-investment-advice disclaimer instead.

**This is the cleanest Theme-4 artefact the corpus has.** It is not a compliance judgement; it is an observation about *where the compliance layer was applied*:

> Within a single firm's single campaign, the MiCA marketing-communication statement is attached to the campaign-terms surface and absent from the editorial surfaces that carry the identical offer. **The gate was applied per-template, not per-communication.**

That is precisely the "gate-stack visibility" question Theme 1 is built to answer, evidenced from first-party artefacts, at a Tier-1 firm, with URLs.

**Not asserted:** that the omission is a breach. Whether a `/learn/` article constitutes a marketing communication under MiCA Title II–IV is a legal question the corpus does not answer. The asymmetry itself is the finding.

---

## 4. Kraken — day 5 live, and both internal conflicts hardened

`https://www.kraken.com/europe-switch` — fetched 2026-08-05, HTTP 200. **LIVE, copy byte-comparable for a fifth day.**

Still reads, in the present:

- *"Most exchanges aren't licensed after July 1. Kraken is."*
- *"Switch now and enter our €1M prize draw."* · *"**Lottery closes July 31.**"*
- *"Switch to Kraken **before July 31**. Enter for €1M."* · *"Draw closes July 31, 2026."*
- Live CTAs: `kraken.com/sign-up?rfr=pro-web` · `proapp.kraken.com/9f1e?deep_link_value=userActivationIncentiveDetails/depositsweeps26`

### 4a. The start-date conflict — now **2 v 2**, not 2 v 1

The landing page states the promotion window **twice**, and both times says **June 22**:

- Step 2: *"Every euro deposited **from June 22** to July 31 earns one entry"*
- FAQ: *"**Between June 22** and July 31, 2026, every euro you deposit…"*

Against the blog and support article, both of which say the promotion **begins 19 June 2026 at 11:00 UTC** (`blog.kraken.com/news/industry-news/europe-mica-switch`; `support.kraken.com/articles/1m-eur-prize-draw`).

**Four dated statements of the same promotion's start, across three owned surfaces, carrying two different dates.** The 08-03 read of "2 v 1" understated it. The commercial surface is still the outlier.

### 4b. The Forbes conflict — both claims are now on ONE page

Prior runs logged a "Forbes badge conflict" across surfaces. It is on a single page:

- Body copy: *"Kaiko number one global exchange 2025. **Forbes best crypto exchange 2025.**"*
- Trust-badge strip, same page: Forbes logo, *"**Most popular crypto exchange 2026**"*

**Two different Forbes accolades, two different years, two different superlatives, one landing page.** Neither is sourced or linked on-page. Recorded as an artefact; **no claim** is made that either is inaccurate.

### 4c. Competitor-named SEO title at a tracked firm

`<title>` and canonical og:title: **"MiCA-Licensed Binance Alternative (EU) | Kraken"**. `meta-description`: *"From July 1, EU exchanges need a MiCA licence… €1M draw ends July 31."*

A Tier-1 tracked firm's owned landing page is titled against a **named** Tier-1 tracked competitor, and the description still advertises the closed draw. Theme-3/Theme-4 crossover: this is the capture campaign's positioning stated in the title tag.

---

## 5. The EEA-egress caveat — weakened again, on a second surface

Both `okx.com` surfaces fetched today served the US-origin banner — *"Looks like you're in the United States. Switch to the United States site for products available in your region."* — **and then served the full EEA-only campaign, present tense, with live CTAs, anyway.**

This is now **2 surfaces × 2 days** of direct evidence that OKX's geo-layer **detects, announces, and does not gate the promotional payload.**

**The caveat is not discharged** — an authenticated EEA session may still see a closed state in-app, and all three OKX offers are described as in-app opt-ins. **The bar has moved and should stay moved:** the open question is not *"is there a geofence"* but *"does the geofence do anything to the offer."* On the evidence so far, on the web surfaces, it does not.

---

## 6. Running tallies

- **Surfaces identified across the finding: ≥34** (OKX ≥31 + Kraken 3), up from 7 on 08-03.
- **Fetched: 9.** **Confirmed lapsed and live at day 5: 7** (Kraken ×3 — landing re-read today, blog + support carried from 08-03; OKX ×4).
- **Bitpanda `bitpanda.com/en/campaigns/bya-june-26`: NOT re-read for a third consecutive run.** Carried, unresolved.
- **Firms: 3 identified (Kraken, OKX, Bitpanda); 2 re-verified today.**

---

## 7. What Phase 2 can and cannot say

**Can say, with URLs and timestamps:**
- Two Tier-1 MiCA-licensed exchanges ran MiCA-deadline capture campaigns that closed 31 July 2026 and were **still live and still selling on 5 August 2026**, across at least seven owned surfaces.
- **One of those surfaces carries an edit timestamp of the day it was read, with the expired offer intact** — so the persistence is not attributable to neglect.
- One campaign's terms page **states its own early closure** and serves an enrolment CTA 38 days later.
- An EEA-only MiCA promotion is published under an **OKX Singapore** masthead.
- Within one campaign, the MiCA marketing-communication statement appears on the terms surface and is absent from the editorial surfaces carrying the same offer.
- A €1M consumer promotion states two different start dates across the firm's own estate, with the divergent value on the selling surface.

**Cannot say:**
- What share of any campaign's surfaces was torn down (denominator has a floor now, not a value).
- What an authenticated EEA visitor sees.
- That any of this breaches MiCA, MAS rules, or any other rule. **The corpus records artefacts. It does not adjudicate.**

---

## Not reached / not guessed

- The ~27 identified-but-unfetched OKX locale surfaces.
- `bitpanda.com/en/campaigns/bya-june-26` — third run carried.
- `okx.com/en-eu/learn/mica-deposit-bonus-campaign` — linked from the `/en-eu/` article today, **identified, not fetched**.
- `okx.com/en-eu/learn/rewardmaxxing-okx-stack-rewards` (29 Jul) — identified; names the 8% MiCA Deposit Bonus as currently running; **not fetched**.
- Kraken support article + blog — not re-fetched today; 08-03 reads stand and the landing page corroborates the conflict.
- Gate, Coinbase, Bybit, Crypto.com, Gemini, Sui, all of Strata 2 and 4 — **own-channel sweep still unrun (watch (p)).**
- Any authenticated or EEA-egress read. **No proxy or VPN was used and none is claimed.**

# CANONICAL — THE AGENCY STACK

**Built 2026-09-10 (Tier 0). Source: `projects/northpoint/research/legacy/agency-panel-trend-data-asof-2026-06-15.json`.**
Panel span **2026-05-18 → 2026-06-15**, 9 capture dates, 18 agencies, **162 dated entries**.
88 `recentClientsNamed` strings resolve to **58 real entities + 21 composites + 9 aliases** (reconciles exactly).

> 🔴 **WHY THIS FILE EXISTS.** The corpus's agency chapter was built from **the 2026-06-15 entry only — the last of
> nine.** Eight of nine dated entries per agency were never read. That single extraction choice produced every
> agency finding the report currently prints, and **most of them are wrong.**

---

## 🔴 THE FALSIFICATION — read this before using any agency claim in the draft

The report states there is **exactly one** tracked-firm agency overlap (Sui). The full panel says:

**Eleven clients are claimed by two or more agencies. Seven of them are tracked-cohort firms.**

| tracked firm | agencies claiming it | n |
|---|---|---|
| **KuCoin** | MarketAcross · Blockwiz · RZLT | **3** |
| Sui | Coinbound · RZLT | 2 |
| OKX | Coinbound · NinjaPromo | 2 |
| Binance | NinjaPromo · MarketAcross | 2 |
| HTX | NinjaPromo · MarketAcross | 2 |
| Crypto.com | NinjaPromo · MarketAcross | 2 |
| Bybit | MarketAcross · Blockwiz | 2 |

Untracked overlaps: Tron (3), eToro (2), Polkadot (2), Polymath (2).

**Every one of these live claims is now false and must be corrected:**

| claim in `findings/03-agency-stack.md` | truth from the full panel |
|---|---|
| "exactly 1 overlap (Sui)" | **7 tracked-firm overlaps.** Sui is not even the largest |
| "the maximum is two, at Sui alone" | **Maximum is three, at KuCoin**, from three separate agencies |
| "KuCoin is claimed by Blockwiz alone" | False — MarketAcross and RZLT also claim it |
| "HTX appears in no agency's claim list" | False — NinjaPromo **and** MarketAcross, 05-18 → 06-01 |
| "Crypto.com appears in no agency's claim list" | False — NinjaPromo + MarketAcross |
| "14 of 18 agencies claim no tracked firm" | **12 of 18** |
| tracked firms named by any agency: 8 | **10** (adds HTX, Crypto.com) |
| claiming agencies: 4 | **6** (adds NinjaPromo, RZLT) |

🔴 **Two annotations in `tracked-firms.md` were WITHDRAWN as unsupported and were correct all along:**
KuCoin's *"Three-agency overlap: RZLT + Blockwiz + MarketAcross"* and HTX's *"NinjaPromo agency relationship."*
**They were withdrawn against a truncated dataset.** Restore both.

⚠ `[VERIFY]` **Huobi and HTX are the same company** (Huobi rebranded to HTX). Blockwiz claims "Huobi"; NinjaPromo
and MarketAcross claim "HTX". Merging makes HTX a **three-agency** overlap and the tracked total **8**. Left
unmerged because the panel keeps them as distinct strings and the corpus states no alias rule. **Decide before
print.**

**The reader-facing finding this unlocks:** multi-agency engagement without an internal owning seat is not a
one-firm curiosity — **seven of ten tracked firms named by any agency are claimed by two or more.** That is the
governance-gap thesis with a denominator behind it for the first time.

---

## TABLE 1 — THE AGENCY PANEL

HQ and focus from the panel's own `notableEvent` text plus the `comp-tag` lines in
`competitor-intelligence-report-asof-2026-06-15.html` (same panel, same as-of).
**Nothing here is inferred from an agency's name.** UNKNOWN means the corpus does not state it.

| agency | HQ | focus & positioning | named clients | threat | health trend (9 entries) |
|---|---|---|---|---|---|
| **Coinbound** | NYC | Influencer + Web3; infra/L1-L2 positioning; own Web3 ad platform | 11 | high ×9 | 7 flat, label → **growing** from 05-26 |
| **MarketAcross** | Israel | Crypto PR retainer since 2012; tier-1 guaranteed coverage; institutional editorial reach | 10 | medium ×9 | 7,7,7,7,6,6,6,6,6 |
| **NinjaPromo** | London / Dubai | **Subscription full-stack — "Replace Your Entire Marketing Team for $4K/Mo"** | 7 | medium ×9 | step down at 05-25 |
| **Single Grain** | UNKNOWN | SaaS + Web3; AEO/GEO/LLMO; Eric Siu; 3.2× ROI claim | 7 | medium ×8, high 05-27 | label → growing from 05-27 |
| **Blockwiz** | Canada | Influencer + analytics | 6 | low ×8 | 6,6,6,6,5,5,5,5,5 |
| **TokenMinds** | Singapore (+ Bangkok) | Integrated Web3 + AI; token-launch / tokenomics advisory | 5 | low ×6 → medium ×3 | mild decay |
| **RZLT** | UNKNOWN (35+ across 10 countries) | AI-native Web3, GEO; 100+ protocols | 4 | high ×9 | 7,8,8,8,8,8,8,7,7 |
| **Outset PR** | UNKNOWN | Crypto-PR boutique, analytics-centric; 5-category Clutch shortlist | 4 | mixed | 8×7 → **6,6** |
| **Bond Finance** | UNKNOWN | Precision/defensibility over hype; institutional Web3; 230+ projects | 4 | low → medium → **high ×2 (only rising threat in the panel)** | 8,8,8,8,7,7,7,8,8 |
| **Lunar Strategy** | Lisbon | Founder-led organic + TradFi thesis; Lunar3 Capital VC pivot; Espressio AI | 3 | medium ×9 | mild decay |
| **ICODA** | UNKNOWN | AI-SEO / AEO-GEO; **Anthropic Claude Partner (05-07)**; iGaming + L1 | 3 | high ×8 | 6×8 → 9 → 7,7 |
| **Serotonin** | NYC | Marketing-as-infrastructure + advisory | 3 | medium ×7 → low | 7,7,7,7,8,8,8,**5,5 — sharpest drop in the panel** |
| **Crowdcreate** | UNKNOWN | IR + fundraising marketing ($250M raised, 800+ projects); Forbes #1 | 3 | low ×8 | 6,6,6,6,5,5,5,6,6 |
| **GuerrillaBuzz** | UNKNOWN | Grassroots PR + tier-1 coverage | 1 | low ×8 | 7,7,7,7,5,5,6,5,5 |
| **Blue Manakin** | Madrid (+ Brazil/Mexico/Argentina/Uruguay) | LATAM / Spanish-language specialist; **"genuine Latin American DNA"; no MiCA positioning despite Madrid HQ** | 0 | low ×9 | 6,6,6,6,5,5,5,5,5 |
| **X10** | London + Dubai | Influencer + Leadgram retargeting | 0 | low ×9 | 6,6,6,6,5,5,5,5,5 |
| **Flexe.io** | Dubai (Asia/YouTube concentration) | Influencer roster / KOL marketplace, 500–700+ clients | 0 | medium ×6 → low ×3 | 7,7,7,7,5,5,5,5,5 |
| **Majinx** | UAE | Bear-market PR specialist; UAE VC niche; 100+ outlet distribution | 0 | low ×9 | 5 flat ×9 |

**Capture gap — HQ unstated for 7 of 18:** ICODA, Crowdcreate, GuerrillaBuzz, RZLT, Single Grain, Outset PR, Bond
Finance. Focus is stated for all 18.

**Four agencies name no real client at all** (Blue Manakin, X10, Flexe, Majinx) — their entire client evidence is
composites like "500+ clients" and "UAE-focused VCs".

---

## TABLE 2 — CLIENT → AGENCY (58 real entities)

Tracked-cohort firms named by an agency — **10 of 27**:

| client | agencies | n | first seen | last seen |
|---|---|---|---|---|
| KuCoin | MarketAcross, Blockwiz, RZLT | 3 | 05-18 | 06-15 |
| Sui | Coinbound, RZLT | 2 | 05-18 | 06-15 |
| OKX | Coinbound, NinjaPromo | 2 | 05-18 | 06-15 |
| Binance | NinjaPromo, MarketAcross | 2 | 05-18 | 06-15 |
| HTX | NinjaPromo, MarketAcross | 2 | 05-18 | **06-01** |
| Crypto.com | NinjaPromo, MarketAcross | 2 | 05-18 | **06-01** |
| Bybit | MarketAcross, Blockwiz | 2 | 05-18 | 06-15 |
| MetaMask | Coinbound | 1 | 05-18 | 06-15 |
| Polygon | MarketAcross | 1 | 05-18 | 06-15 |
| Solana | MarketAcross | 1 | 05-18 | 06-15 |

⚠ **HTX and Crypto.com both drop out of the claim lists after 06-01** while others persist to 06-15. Recorded as
observed; **a claim disappearing is not a relationship ending** — agencies rotate case studies. Do not print as
a churn finding without a second source.

Non-tracked named clients (48): Tron·3, eToro·2, Polkadot·2, Polymath·2, then single-agency — Gala, Immutable,
Nexo, Cosmos, Litecoin, Polymarket, Cardano, MindAI, BitSpinCasino, Bitget, TON, BingX, Filecoin, UXLINK, MovitOn,
536 Lottery, CryptoBlades, Khan Bank, Bit Digital, Mojito, Franklin, Anker, TP-Link, Cloudbet, MEXC, Huobi,
AdaSwap, Paxful, NEAR Protocol, Internet Computer/Dfinity, Bittrex, Blockgeeks, SmartRent, **Amazon, Crunchbase,
Uber** (Single Grain's non-crypto book), Nav Markets, StealthEX, ChangeNOW, Step App, TrippyLabs, Orange,
Mario Nawfal, Suede Labs.

**21 composites excluded from every count** — "100+ blockchain clients", "230+ projects — undisclosed",
"undisclosed L1s", "500+ clients", "UAE-focused VCs", "global crypto VCs", "YouTube/KOL network — undisclosed",
"iGaming operators", "DeFi protocols", "NFT projects", "early-stage tokens", "SaaS clients", and others.
**9 aliases folded:** TRON→Tron · Near→NEAR Protocol · Dfinity ×3→Internet Computer · Bybit (historical)→Bybit ·
Bit Digital (board seat/board)→Bit Digital · Mojito (spinout)→Mojito.

---

## What the panel CANNOT tell us

- **Whether a claim is a live engagement.** These are agency-side *claims* on their own marketing surfaces. The
  corpus already forbids upgrading "claim" to "retainer" — that rule stands and now matters more, not less.
- **Scope, fee, duration or which agency does what** for a firm with three of them.
- **Agencies the panel cannot see at all.** Two are already documented: **Serviceplan** (Bitpanda's mainstream
  agency, 5 football clubs + TV/OOH) and **Holographik** (Sui's brand system). Neither is in the 18. **The panel is
  a crypto-native-agency panel, not a crypto-marketing-agency panel** — state that limit wherever the table appears.
- **Anything after 2026-06-15.** The panel is a five-month time series that stops there.

---

## ADDENDUM 2026-09-15 — the 18 agencies, public facts as read on 15 September 2026

Own site, LinkedIn About page, Clutch, Crunchbase, DesignRush; headcount is the agency's own statement first, directory brackets labelled. **No agency publishes revenue.** "Claims, of the 27" = which of the report's 27 companies the agency named as a client on its own site that day (logo walls count, as in the panel). Compared with the 18 May–15 June panel capture: OKX claimed by 4 (Coinbound, Blockwiz, Lunar Strategy, X10), KuCoin by 4 (MarketAcross, Blockwiz, RZLT, Crowdcreate), HTX by 3 (NinjaPromo, Blockwiz, ICODA), Sui by 3 (Coinbound, MarketAcross, RZLT), Polygon 2, Optimism 2. Exhibit 4 in the report keeps the dated panel; Chapter 3 states the September re-read in one sentence.

| Agency | HQ | Founded | Headcount | Ownership, funding | Claims, of the 27 | Services, pricing |
|---|---|---|---|---|---|---|
| Coinbound | New York | 2018 | “45+” (own site); Clutch 50–249 | Founder Ty Smith; part of holding company Nowbound; acquired Coinscribble | OKX, Sui, MetaMask | Influencer, PR, social, paid, fractional CMO. Quote only; Clutch min. $10k |
| MarketAcross | Tel Aviv | 2013/14 | ≈37 (directory); Crunchbase 11–50 | Founders Elad Mor, Nadav Dakner (also Chainwire); makes venture investments | Binance, Bybit, KuCoin, Crypto.com, Sui, Solana, Polygon, Ava Labs, ConsenSys (logo wall) | Blockchain PR, comms, SEO, events. “Results-based retainer”; no price |
| NinjaPromo | London / New York (+10 offices) | 2017 | “300+ specialists” (own site); Crunchbase 101–250 | Founders Paul Lipen, Slava Kasperovich; ≈$0.4m seed (Heartwood) | HTX | Subscription marketing. Published: $4,000–$12,800/mo tiers; enterprise to $100k/mo |
| Single Grain | Los Angeles | 2009 (Eric Siu owner since 2014) | Clutch 10–49 | Eric Siu; “7-figure agency” (own words) | — | SEO, paid media, CRO, “AI growth”. Quote only; Clutch min. $10k |
| Blockwiz | Toronto | 2019 | “70” (own Medium page); “75 full-time” (directory) | Founder Dev Sharma | KuCoin, Bybit, OKX (as OKEx), HTX (as Huobi) — third-party listing; own site unreachable | Influencer, community, paid, content. No price |
| TokenMinds | Singapore | 2016/17 | “30+” (own site) | Founders Rob Eijgenraam, Anchor Chan | — | Web3 + AI development, tokenisation, marketing/PR. No price |
| RZLT | Zagreb (listings also say London) | 2018 | “35+ across 10 countries” (own site); Clutch 10–49 | Founder Luka Ciganek | Sui, Optimism, KuCoin | “AI-native” GTM, social, paid, community, DevRel. Clutch min. $5k, $50–99/h |
| Outset PR | registered St Vincent & the Grenadines | 2022 | ≈30 named on own site; Crunchbase 11–50 | Founder Mike Ermolaev (ex-ChangeNOW) | — | Data-driven crypto PR. Projects under $10k (directory) |
| Bond Finance | Poole, UK | 2017 | “14+” (own site); team page lists 7 | Founder Toby Cutler | — | Web3 GTM, community, investor attraction. Clutch min. $5k, $50–99/h |
| Lunar Strategy | Lisbon | 2019 | “30+” (own site); LinkedIn 41 | Founders Tim and Jack Haldorsson; acquired by Turtle (DeFi), Jul 2026 | OKX | GTM, social, community, KOL, PR, events. Budget tiers from $15–25k |
| ICODA | Wrocław / Bellevue, WA (Global Digital Consulting LLC) | 2017 | LinkedIn 35; Clutch 10–49 | CEO Vlad Pivnev | HTX (as Huobi Global) | Full-stack crypto, iGaming, AI marketing; listings; market making. Clutch min. $10k, $25–49/h |
| Serotonin | Remote, US (Serotonin Inc.) | 2020 | “global team of 90 across 15 countries” (LinkedIn); “100” (CEO, Apr 2025) | Founder/CEO Amanda Cassatt; spun out Mojito ($20m raised); makes investments | Aptos, Arbitrum, Optimism, Polygon | GTM platform: marketing, strategy, recruiting, legal. Directory min. $10–25k, $250/h |
| Crowdcreate | Irvine, CA (Crowdcreate LLC) | 2014 | LinkedIn 28; Clutch 10–49 | Founders Jeffrey Maganis, Ivan Kan | KuCoin | Growth, SEO, influencer, investor outreach, PR. No price |
| GuerrillaBuzz | Tel Aviv | 2017 | LinkedIn 7; Crunchbase 1–10 — “boutique on purpose” | Founders Asaf Fybish, Yuval Halevi | — | Blockchain PR, SEO, Reddit, AI-search optimisation. No price |
| Blue Manakin | Madrid (entity registered in Mexico) | 2021 | 9 named on own site; LinkedIn 5 | Founders Luca Zollino, Oliver Cuello Núñez | — | Spanish/LatAm crypto marketing, community, listings. No price |
| X10 Agency | not stated on own site (directories: Albuquerque) | 2016 (directories) | “20+” (directories); no LinkedIn page | CEO Sergey Baloyan | OKX (NFT marketplace) | KOL, community, PR, Asia packages, listings, market making. Directory min. $1–10k |
| Flexe.io | Dubai (IFZA) | 2018 | “up to 50” (own site); LinkedIn 14 | Founder Alexander Tikhonov | — | KOL/YouTube/TikTok, PR, paid, listings. Published: campaigns from $4,000 to $300,000 |
| Majinx | Kyiv / Austin / Murcia | 2021 | “45” (CEO, Oct 2023); LinkedIn 4 | Founder Ruslan Lynnyk; now Majinx Capital (fund) + Majinx Labs (agency; site down 15 Sep 2026) | — | Fundraising + marketing for early-stage web3. No price |

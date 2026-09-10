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

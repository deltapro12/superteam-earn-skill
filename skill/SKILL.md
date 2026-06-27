---
name: superteam-earn
description: Discover and complete Solana ecosystem bounties on Superteam Earn with zero upfront capital when possible. Covers listing discovery, capital-gated filtering, human and agent submission flows, Phantom wallet payouts, and off-ramp to fiat (US ACH via Coinbase/Kraken, LATAM via Binance P2P). Use when the user wants to earn USDC/USDG from bounties, scan Superteam listings, or set up crypto payout without Stripe.
user-invocable: true
---

# Superteam Earn Skill

Helps founders and agents **earn on-chain** from Superteam Earn bounties — without confusing capital-gated competitions with zero-cost dev/content work.

## When to use

- User wants to **earn crypto** from Solana bounties
- User has **no seed capital** (filter out buy-in competitions)
- User needs **Phantom + Superteam** setup for payout
- User in **Ecuador/LATAM** needs USDC → bank dollars
- Agent should **scan listings** or **submit** via Superteam agent API

## Default decisions (2026)

1. **Primary platform:** [Superteam Earn](https://superteam.fun/earn/) — USDC/USDG/SOL to wallet
2. **Avoid for no-capital users:** Indexify Stack Wars and similar (require USDC buy-in)
3. **Best zero-capital categories:** Dev demos, agent skills, research/docs, content
4. **Wallet:** Phantom (Solana) — empty wallet OK for signup; payout address required to win
5. **US off-ramp:** Coinbase/Kraken ACH → US bank
6. **LATAM off-ramp:** Binance P2P → local bank (Ecuador uses USD natively)

## Operating procedure

### 1. Scan live bounties

```bash
python scripts/scan_superteam_all.py
python scripts/fetch_superteam_listing.py <slug>
```

Read: [discover-bounties.md](discover-bounties.md)

### 2. Filter for zero capital

Reject listings that require token buy-in, stack deposits, or KYC-heavy fiat rails the user cannot complete.

Read: [zero-capital-filter.md](zero-capital-filter.md)

### 3. Execute work + submit

- **Human-only:** Superteam profile + Phantom + submission link
- **Agent-eligible:** Register agent, submit, human claims with `claimCode`

Read: [submit-and-claim.md](submit-and-claim.md), [agent-api.md](agent-api.md)

### 4. Receive payout

Winners paid on-chain. For fiat: Phantom → exchange P2P → bank.

Read: [wallet-payout-usa.md](wallet-payout-usa.md) or [wallet-payout-latam.md](wallet-payout-latam.md)

## Progressive disclosure

| File | Read when |
|------|-----------|
| [discover-bounties.md](discover-bounties.md) | Finding open bounties, API endpoints |
| [zero-capital-filter.md](zero-capital-filter.md) | User has no money to deposit |
| [submit-and-claim.md](submit-and-claim.md) | Preparing Superteam submission |
| [agent-api.md](agent-api.md) | Autonomous agent register/submit/claim |
| [wallet-payout-usa.md](wallet-payout-usa.md) | US bank withdrawal (ACH) |
| [wallet-payout-latam.md](wallet-payout-latam.md) | Ecuador/LATAM bank withdrawal |

## Commands

| Command | Action |
|---------|--------|
| `/scan-bounties` | Run listing scanner, summarize actionable |
| `/filter-zero-capital` | Remove buy-in bounties from results |

## Anti-patterns

- Do not recommend Algora/Stripe when user needs direct wallet payout
- Do not recommend Indexify Stack Wars when user has $0 USDC
- Do not share wallet seed phrases or private keys
- Confirm P2P bank deposit before releasing USDC on Binance
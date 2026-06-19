# Zero-capital bounty filter

Use when the user **cannot deposit USDC/SOL** upfront.

## Include (no buy-in)

| Signal in description | Example |
|-----------------------|---------|
| GitHub repo / PR submission | Solana AI Kit skills bounty |
| Code sample / technical demo | Solana subscriptions demo |
| Written analysis / report | Business challenge bounties |
| Twitter thread / video | Content bounties (needs X account, not money) |
| Agent skill `SKILL.md` | Ship skills to solana-ai-kit |

## Exclude (capital required)

| Signal | Why |
|--------|-----|
| "minimum $X USDC deposited/held" | Indexify Stack Wars |
| "buy-in" / "min buy-in" | Trading competitions |
| Hardware / PCB fabrication | Parts cost money |
| Paid API keys required with no free tier | Hidden capital |

## Known capital-gated (2026)

- `build-a-stack-on-indexify-app-for-pnl-competition` — min **$10 USDC** in stack
- Most DeFi "trade and win" formats

## Prioritization for broke builders

1. **Agent skills** — $400 top-10 × 10 winners (pool $3,000 USDG)
2. **Technical demos** — large pools, code-only
3. **Small USDC content** — $120–200 threads if user has X
4. **Algora/GitHub** — only if payout rail works (often Stripe-blocked)

## Decision tree

```
User has $0?
  ├─ Yes → filter zero-capital list → prefer code/skills/content
  └─ No  → may include Indexify if user accepts trading risk
```
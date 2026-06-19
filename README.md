# Superteam Earn Skill

Agent skill for **discovering, evaluating, and submitting** Solana ecosystem bounties on [Superteam Earn](https://superteam.fun/earn/) — with emphasis on **zero-upfront-capital** opportunities and **direct wallet payouts** (USDC/USDG/SOL).

Built for the [Solana AI Kit skills bounty](https://superteam.fun/earn/listing/skills).

## Problem

Solana builders want to earn from open bounties but face:

- Scattered listings across sponsors and categories
- Capital-gated competitions (e.g. trading stacks requiring USDC buy-in)
- Unclear payout paths (Stripe vs on-chain vs regional off-ramp)
- Agent workflows split between human signup and agent submission APIs

This skill gives coding agents a **repeatable playbook** plus **working scanner scripts**.

## What it does

| Module | Purpose |
|--------|---------|
| `discover-bounties.md` | Scan live listings, filter by type/reward/competition |
| `zero-capital-filter.md` | Exclude buy-in bounties; prioritize code/content/skills |
| `submit-and-claim.md` | Human + agent submission flows on Superteam Earn |
| `wallet-payout-latam.md` | Phantom → Binance P2P → bank (Ecuador USD, general LATAM) |
| `agent-api.md` | Superteam agent registration, listings API, claim codes |

## Install

```bash
git clone https://github.com/deltapro12/superteam-earn-skill
cd superteam-earn-skill
./install.sh
```

Copies `skill/` to `~/.claude/skills/superteam-earn/` (or `$CLAUDE_SKILLS_DIR`).

### Quick scan (no install)

```bash
python scripts/scan_superteam_all.py
python scripts/fetch_superteam_listing.py <slug>
```

## Structure

```
skill/
  SKILL.md                 # Entry point (progressive disclosure)
  discover-bounties.md
  zero-capital-filter.md
  submit-and-claim.md
  wallet-payout-latam.md
  agent-api.md
scripts/
  scan_superteam_all.py
  fetch_superteam_listing.py
commands/
  scan-bounties.md
install.sh
```

## Closest competing skills

- [ColosseumOrg/colosseum-copilot](https://github.com/ColosseumOrg/colosseum-copilot) — startup/GTM, not bounty ops
- [sendaifun/solana-new](https://github.com/sendaifun/solana-new) — new project launch, not Earn workflow

**Gap filled:** operational bounty hunting + payout setup for builders with no seed capital.

## License

MIT
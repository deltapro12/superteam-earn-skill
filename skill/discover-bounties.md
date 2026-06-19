# Discover Superteam Earn bounties

## Public listings API

```
GET https://earn.superteam.fun/api/listings
```

Returns open bounties, projects, hackathons with fields:

| Field | Meaning |
|-------|---------|
| `type` | `bounty`, `project`, `hackathon` |
| `rewardAmount` | Total pool |
| `token` | `USDC`, `USDG`, `SOL`, etc. |
| `slug` | URL slug for detail page |
| `agentAccess` | `HUMAN_ONLY`, `AGENT_ALLOWED`, `AGENT_ONLY` |
| `status` | `OPEN` |
| `_count.Submission` | Current competition size |

## Detail page (full requirements)

Listing pages embed JSON in `__NEXT_DATA__`. Fetch with:

```bash
python scripts/fetch_superteam_listing.py <slug>
```

Key fields in `listing.description` (HTML): scope, judging, eligibility questions, deadlines.

## Scanner script

`scripts/scan_superteam_all.py` prints:

- All open bounties sorted by reward
- **Actionable** subset: reward $50–$3000, submissions ≤ 15
- **Smallest** bounties ≤ $200

## High-value listing types (2026)

| Slug pattern | Typical capital | Skill |
|--------------|-----------------|-------|
| `skills` | $0 | Agent skill repos for Solana AI Kit |
| `technical-demo-*` | $0 | Code samples + repo |
| `business-challenge-*` | $0 | Research / analysis |
| `publish-*` / `create-a-video-*` | $0 | Content (needs X/video) |
| `build-a-stack-on-indexify*` | **$10+ USDC** | Trading — capital required |

## URLs

- Browse: https://superteam.fun/earn/all?tab=bounties
- Agents: https://superteam.fun/earn/agents
- Agent docs: https://superteam.fun/skill.md
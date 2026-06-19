# Submit and claim on Superteam Earn

## Human submission flow

1. Create profile: https://superteam.fun/earn/ (connect Phantom)
2. Open listing → read `description` via `fetch_superteam_listing.py`
3. Complete work (repo, PR, content, etc.)
4. **Submit Now** before deadline
5. Fill eligibility questions (listing-specific)
6. **Submission Link:** public GitHub repo or PR URL

### Example: Solana AI Kit skills bounty

- **Listing:** https://superteam.fun/earn/listing/skills
- **Deadline:** 2026-07-01
- **Rewards:** top 10 — $400 (1st–5th), $200 (6th–10th) USDG
- **Deliverable:** public GitHub repo with `skill/SKILL.md`, README, MIT license
- **Eligibility questions:**
  1. New idea or contribution to existing repo?
  2. Closest competing skill?
  3. Links proving founder-market fit

## Agent submission flow

For `AGENT_ALLOWED` / `AGENT_ONLY` listings:

1. `POST https://superteam.fun/api/agents` → `apiKey`, `claimCode`
2. `GET /api/agents/listings/live` with Bearer token
3. `POST /api/agents/submissions/create` with `link`, `otherInfo`
4. Human visits `https://superteam.fun/earn/claim/<claimCode>`
5. Human completes talent profile → payout eligibility

Full spec: https://superteam.fun/skill.md

## After winning

- Payout to Phantom (USDC/USDG/SOL)
- Verify on https://solscan.io
- Off-ramp: see [wallet-payout-latam.md](wallet-payout-latam.md)

## Checklist before submit

- [ ] Public repo link works
- [ ] README explains problem + install
- [ ] MIT license present
- [ ] Meets all eligibility answers
- [ ] Submitted before deadline (UTC)
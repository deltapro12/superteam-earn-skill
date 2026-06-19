# /scan-bounties

Run the Superteam Earn listing scanner and summarize actionable zero-capital bounties.

## Steps

1. Execute `python scripts/scan_superteam_all.py` from skill root
2. Apply rules from `zero-capital-filter.md`
3. For top 3 picks, run `python scripts/fetch_superteam_listing.py <slug>`
4. Report: title, reward, token, submissions, deadline, capital required (yes/no), URL

## Output format

```
# Superteam scan — <date>
## Zero-capital picks
1. ...
2. ...
## Avoid (capital required)
- ...
```
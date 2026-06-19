#!/usr/bin/env python3
"""Scan all open Superteam bounties."""
import json
import urllib.request

API = "https://earn.superteam.fun/api/listings"
req = urllib.request.Request(API, headers={"User-Agent": "scan/1.0", "Accept": "application/json"})
items = json.load(urllib.request.urlopen(req, timeout=60))

bounties = []
for item in items:
    if item.get("type") != "bounty" or item.get("status") != "OPEN":
        continue
    sponsor = item.get("sponsor") or {}
    bounties.append({
        "title": item.get("title"),
        "reward": item.get("rewardAmount") or 0,
        "token": item.get("token", ""),
        "slug": item.get("slug", ""),
        "agent": item.get("agentAccess", ""),
        "deadline": (item.get("deadline") or "")[:10],
        "submissions": item.get("_count", {}).get("Submission", 0),
        "sponsor": sponsor.get("name", ""),
        "id": item.get("id"),
    })

bounties.sort(key=lambda x: (-x["reward"], x["submissions"]))
print(f"All OPEN bounties: {len(bounties)}\n")

# Small/medium actionable (50-3000, low subs)
print("ACTIONABLE (reward $50-$3000, subs <= 15):\n")
actionable = [b for b in bounties if 50 <= b["reward"] <= 3000 and b["submissions"] <= 15]
actionable.sort(key=lambda x: (x["submissions"], -x["reward"]))
for r in actionable:
    print(f"  ${r['reward']:>5} {r['token']:4} | {r['agent']:12} | subs:{r['submissions']:2} | due:{r['deadline']}")
    print(f"  {r['title']}")
    print(f"  https://superteam.fun/earn/listing/{r['slug']}\n")

print("\nSMALLEST (reward <= $200):\n")
small = [b for b in bounties if b["reward"] <= 200]
small.sort(key=lambda x: (x["submissions"], -x["reward"]))
for r in small[:15]:
    print(f"  ${r['reward']:>5} {r['token']:4} | subs:{r['submissions']:2} | {r['title'][:65]}")
    print(f"  https://superteam.fun/earn/listing/{r['slug']}")
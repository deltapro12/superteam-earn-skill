#!/usr/bin/env python3
import json
import re
import sys
import urllib.request

slug = sys.argv[1] if len(sys.argv) > 1 else "build-a-stack-on-indexify-app-for-pnl-competition"
url = f"https://superteam.fun/earn/listing/{slug}"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.DOTALL)
if not m:
    print("No __NEXT_DATA__ found")
    sys.exit(1)
data = json.loads(m.group(1))
props = data.get("props", {}).get("pageProps", {})
print(json.dumps(props, indent=2, ensure_ascii=False))
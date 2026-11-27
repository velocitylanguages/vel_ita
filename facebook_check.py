"""Read-only Facebook page diagnostics.

Prints page identity, recent posts, and basic counts. Never prints tokens.
"""

from __future__ import annotations

import json
import os
import sys

import requests

sys.stdout.reconfigure(encoding="utf-8")
GRAPH = "https://graph.facebook.com/v21.0"
token = (
    os.getenv("FACEBOOK_ACCESS_TOKEN")
    or os.getenv("FB_PAGE_ACCESS_TOKEN")
    or os.getenv("FB_ACCESS_TOKEN")
    or os.getenv("META_ACCESS_TOKEN")
    or ""
).strip()
page_id = (os.getenv("FACEBOOK_PAGE_ID") or os.getenv("FB_PAGE_ID") or "").strip()
ig_token = (os.getenv("INSTAGRAM_ACCESS_TOKEN") or os.getenv("IG_ACCESS_TOKEN") or "").strip()
ig_id = (os.getenv("INSTAGRAM_ACCOUNT_ID") or os.getenv("IG_USER_ID") or "").strip()

if not token:
    print("NO FACEBOOK TOKEN")
    raise SystemExit(1)

print("token_present", bool(token), "page_id_present", bool(page_id))


def get(path: str, params: dict | None = None) -> dict:
    p = {"access_token": token}
    if params:
        p.update(params)
    r = requests.get(f"{GRAPH}/{path}", params=p, timeout=30)
    try:
        data = r.json()
    except Exception:
        data = {"status": r.status_code, "body": r.text[:300]}
    return {"status": r.status_code, "data": data}


me = get("me", {"fields": "id,name"})
print("ME", json.dumps(me, ensure_ascii=False))

accounts = get("me/accounts", {"fields": "id,name,link,fan_count,followers_count", "limit": 100})
print("ACCOUNTS", json.dumps(accounts, ensure_ascii=False))

if page_id:
    page = get(page_id, {"fields": "id,name,link,fan_count,followers_count,verification_status,category"})
    print("PAGE", json.dumps(page, ensure_ascii=False))
    posts = get(
        f"{page_id}/published_posts",
        {
            "fields": "id,message,created_time,permalink_url,shares,likes.summary(true),comments.summary(true)",
            "limit": 10,
        },
    )
    print("POSTS", json.dumps(posts, ensure_ascii=False))

if ig_token and ig_id:
    r = requests.get(
        f"{GRAPH}/{ig_id}",
        params={"fields": "id,username,followers_count,media_count", "access_token": ig_token},
        timeout=30,
    )
    try:
        print("INSTAGRAM", json.dumps({"status": r.status_code, "data": r.json()}, ensure_ascii=False))
    except Exception:
        print("INSTAGRAM", r.status_code, r.text[:200])

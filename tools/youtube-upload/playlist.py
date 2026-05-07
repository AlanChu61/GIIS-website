#!/usr/bin/env python3
"""Manage GIIS YouTube playlists via the YouTube Data API.

Subcommands:
    list                              — list all playlists on the channel
    show     <name|id>                — list videos in one playlist
    create   <name> [--privacy ...]   — create a new playlist
    add      <playlist> <video_id>+   — add one or more videos
    remove   <playlist> <video_id>+   — remove videos
    reorder  <playlist>               — sort items by their video title (alphabetical)
    delete   <playlist>               — delete a playlist (asks confirmation)
    ensure   <name>                   — create if missing, return its ID

In every command, <playlist> can be either the playlist's display name or its
ID (PL... form). Names are case-insensitive.

Quota costs (relevant for batch use):
    playlists.list           1 unit
    playlists.insert         50 units
    playlistItems.insert     50 units / video
    playlistItems.delete     50 units / video
    playlists.delete         50 units
"""
from __future__ import annotations
import argparse, sys
from pathlib import Path

# Reuse the auth flow from upload_video.py so we share the same token.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from upload_video import get_creds   # noqa: E402

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def _yt():
    return build("youtube", "v3", credentials=get_creds())

def _all_playlists(yt):
    """Yield every playlist on the authenticated user's channel."""
    page = None
    while True:
        req = yt.playlists().list(
            part="snippet,status,contentDetails",
            mine=True, maxResults=50, pageToken=page,
        )
        resp = req.execute()
        for it in resp.get("items", []):
            yield it
        page = resp.get("nextPageToken")
        if not page: break

def _resolve(yt, key: str) -> tuple[str, str] | None:
    """Resolve a playlist display name OR ID to (id, title). Case-insensitive."""
    if key.startswith("PL") and len(key) > 12:
        # Looks like an ID — fetch directly.
        try:
            r = yt.playlists().list(part="snippet", id=key).execute()
            items = r.get("items", [])
            if items:
                return items[0]["id"], items[0]["snippet"]["title"]
        except HttpError:
            pass
    key_lo = key.lower()
    for p in _all_playlists(yt):
        if p["snippet"]["title"].lower() == key_lo:
            return p["id"], p["snippet"]["title"]
    return None

# ─────── subcommands ───────

def cmd_list(args):
    yt = _yt()
    found = False
    for p in _all_playlists(yt):
        found = True
        s = p["snippet"]; c = p["contentDetails"]; st = p["status"]
        print(f"{p['id']}  [{st['privacyStatus']:>8}]  {c['itemCount']:>3} videos   {s['title']}")
    if not found:
        print("(no playlists yet)")

def cmd_show(args):
    yt = _yt()
    r = _resolve(yt, args.playlist)
    if not r: sys.exit(f"no such playlist: {args.playlist}")
    pid, title = r
    print(f"# {title}  ({pid})")
    page = None; idx = 1
    while True:
        resp = yt.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=pid, maxResults=50, pageToken=page,
        ).execute()
        for it in resp.get("items", []):
            sn = it["snippet"]; cd = it["contentDetails"]
            print(f"  {idx:>2}. {cd['videoId']}   {sn['title']}")
            idx += 1
        page = resp.get("nextPageToken")
        if not page: break

def cmd_create(args):
    yt = _yt()
    body = {
        "snippet": {
            "title": args.name,
            "description": args.description or "",
            "defaultLanguage": "en",
        },
        "status": {"privacyStatus": args.privacy},
    }
    resp = yt.playlists().insert(part="snippet,status", body=body).execute()
    print(f"created  {resp['id']}  {resp['snippet']['title']}  ({resp['status']['privacyStatus']})")
    print(f"URL  https://www.youtube.com/playlist?list={resp['id']}")
    return resp["id"]

def cmd_ensure(args):
    """Idempotent: print the playlist's ID, creating it if missing."""
    yt = _yt()
    r = _resolve(yt, args.name)
    if r:
        print(r[0])
        return
    body = {"snippet": {"title": args.name, "defaultLanguage": "en"},
            "status": {"privacyStatus": args.privacy}}
    resp = yt.playlists().insert(part="snippet,status", body=body).execute()
    print(resp["id"])

def cmd_add(args):
    yt = _yt()
    r = _resolve(yt, args.playlist)
    if not r: sys.exit(f"no such playlist: {args.playlist}")
    pid, title = r
    for vid in args.video_ids:
        body = {"snippet": {"playlistId": pid,
                             "resourceId": {"kind": "youtube#video", "videoId": vid}}}
        try:
            resp = yt.playlistItems().insert(part="snippet", body=body).execute()
            print(f"added  {vid}  →  {title}  (item {resp['id']})")
        except HttpError as e:
            print(f"  fail   {vid}: {e._get_reason()}")

def cmd_remove(args):
    yt = _yt()
    r = _resolve(yt, args.playlist)
    if not r: sys.exit(f"no such playlist: {args.playlist}")
    pid, title = r
    # Build map of videoId → playlistItem ID
    page = None; mapping = {}
    while True:
        resp = yt.playlistItems().list(
            part="contentDetails", playlistId=pid, maxResults=50, pageToken=page).execute()
        for it in resp.get("items", []):
            mapping[it["contentDetails"]["videoId"]] = it["id"]
        page = resp.get("nextPageToken")
        if not page: break
    for vid in args.video_ids:
        item_id = mapping.get(vid)
        if not item_id:
            print(f"  skip   {vid} (not in playlist)")
            continue
        yt.playlistItems().delete(id=item_id).execute()
        print(f"removed {vid}  from  {title}")

def cmd_reorder(args):
    """Sort playlist items by their video title (alphabetical)."""
    yt = _yt()
    r = _resolve(yt, args.playlist)
    if not r: sys.exit(f"no such playlist: {args.playlist}")
    pid, title = r
    page = None; items = []
    while True:
        resp = yt.playlistItems().list(
            part="snippet", playlistId=pid, maxResults=50, pageToken=page).execute()
        items += resp.get("items", [])
        page = resp.get("nextPageToken")
        if not page: break
    items.sort(key=lambda it: it["snippet"]["title"])
    for pos, it in enumerate(items):
        body = {"id": it["id"],
                "snippet": {"playlistId": pid,
                             "position": pos,
                             "resourceId": it["snippet"]["resourceId"]}}
        yt.playlistItems().update(part="snippet", body=body).execute()
        print(f"  {pos:>2}. {it['snippet']['title']}")

def cmd_delete(args):
    yt = _yt()
    r = _resolve(yt, args.playlist)
    if not r: sys.exit(f"no such playlist: {args.playlist}")
    pid, title = r
    if not args.yes:
        ans = input(f"delete playlist '{title}' ({pid})? [y/N] ").strip().lower()
        if ans != "y":
            print("cancelled"); return
    yt.playlists().delete(id=pid).execute()
    print(f"deleted {title}")

# ─────── arg parsing ───────

def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list", help="list all playlists on the channel").set_defaults(func=cmd_list)

    sp = sub.add_parser("show", help="list videos in one playlist")
    sp.add_argument("playlist"); sp.set_defaults(func=cmd_show)

    sp = sub.add_parser("create", help="create a new playlist")
    sp.add_argument("name")
    sp.add_argument("--description", default="")
    sp.add_argument("--privacy", default="public", choices=["public","unlisted","private"])
    sp.set_defaults(func=cmd_create)

    sp = sub.add_parser("ensure", help="create if missing, print its ID")
    sp.add_argument("name")
    sp.add_argument("--privacy", default="public", choices=["public","unlisted","private"])
    sp.set_defaults(func=cmd_ensure)

    sp = sub.add_parser("add", help="add videos to a playlist")
    sp.add_argument("playlist"); sp.add_argument("video_ids", nargs="+")
    sp.set_defaults(func=cmd_add)

    sp = sub.add_parser("remove", help="remove videos from a playlist")
    sp.add_argument("playlist"); sp.add_argument("video_ids", nargs="+")
    sp.set_defaults(func=cmd_remove)

    sp = sub.add_parser("reorder", help="alphabetical reorder of playlist items")
    sp.add_argument("playlist"); sp.set_defaults(func=cmd_reorder)

    sp = sub.add_parser("delete", help="delete a playlist")
    sp.add_argument("playlist"); sp.add_argument("--yes", action="store_true")
    sp.set_defaults(func=cmd_delete)

    args = p.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()

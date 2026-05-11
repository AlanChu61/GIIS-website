#!/usr/bin/env bash
#
# Daily YouTube upload runner. Called by launchd (see com.giis.youtube-daily.plist)
# at 09:00 Pacific each day — after YouTube Data API quota resets at midnight PT.
#
# Logs to ~/Library/Logs/giis-youtube-daily.log so you can `tail` it and see what
# ran. Exits non-zero on upload failure (launchd will surface this in Console.app).
#
# Manual invocation:
#   bash tools/youtube-upload/daily.sh
#
set -euo pipefail

# Run from the repo root so relative paths work regardless of cwd.
REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_ROOT"

LOG="${HOME}/Library/Logs/giis-youtube-daily.log"
mkdir -p "$(dirname "$LOG")"

{
  echo
  echo "════════════════════════════════════════════════════════════════════"
  echo "GIIS YouTube daily run — $(date -Iseconds)"
  echo "════════════════════════════════════════════════════════════════════"
  python3 tools/youtube-upload/yt_queue.py status
  echo
  python3 tools/youtube-upload/yt_queue.py upload --max 4 --privacy unlisted
} 2>&1 | tee -a "$LOG"

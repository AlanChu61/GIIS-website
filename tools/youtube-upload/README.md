# tools/youtube-upload — quickstart

Upload a finished lesson MP4 to the GIIS YouTube channel.

```bash
python3 tools/youtube-upload/upload_lesson.py teaching-videos/algebra-i-module-4-sample/
```

**First time using this?** Read `setup.md` — there's a one-time Google Cloud setup (~15 min). After that, every upload is one command.

## What's in here

| File | Purpose |
|---|---|
| `setup.md` | One-time setup walkthrough: YouTube channel + Google Cloud + OAuth |
| `SKILL.md` | What Claude reads to know when/how to use this tool |
| `upload_lesson.py` | Upload a whole lesson folder. Auto-builds title/description/chapters from `script.json`, attaches captions + thumbnail, and **adds the video to the course playlist** (creates the playlist if missing). Privacy defaults to `unlisted`. |
| `upload_video.py` | Low-level: upload any MP4 with explicit title/description flags. Used by `upload_lesson.py` under the hood. |
| `playlist.py` | Manage playlists — list / show / create / add / remove / reorder / delete. |
| `client_secret.json` | Your Google OAuth credentials. **Never commit.** Already in `.gitignore`. |
| `token.json` | Saved auth token after first interactive login. **Never commit.** |

## Common commands

### Uploading

```bash
# Upload one lesson (default unlisted; auto-adds to "Algebra I" playlist)
python3 tools/youtube-upload/upload_lesson.py teaching-videos/algebra-i-module-1-variables/

# Make it public from the start
python3 tools/youtube-upload/upload_lesson.py teaching-videos/algebra-i-module-1-variables/ --privacy public

# Override the playlist (default = script.json's `course` field)
python3 tools/youtube-upload/upload_lesson.py teaching-videos/foo/ --playlist "Algebra I — Sample Lessons"

# Don't add to any playlist
python3 tools/youtube-upload/upload_lesson.py teaching-videos/foo/ --no-playlist

# Upload all 3 sample lessons (each goes into its course's playlist)
for d in teaching-videos/algebra-i-module-{1-variables,7-functions,14-quadratics}/; do
  python3 tools/youtube-upload/upload_lesson.py "$d"
done
```

### Playlist management

```bash
# List all playlists on the channel
python3 tools/youtube-upload/playlist.py list

# List the videos in one playlist (by name OR ID)
python3 tools/youtube-upload/playlist.py show "Algebra I"

# Create a playlist explicitly (uploads auto-create too)
python3 tools/youtube-upload/playlist.py create "Algebra I — Full Course" \
    --description "Lecture videos for the 14-module Algebra I curriculum." \
    --privacy public

# Add specific videos by ID
python3 tools/youtube-upload/playlist.py add "Algebra I" O7VGTGNhBGA dQw4w9WgXcQ

# Reorder a playlist alphabetically by video title
python3 tools/youtube-upload/playlist.py reorder "Algebra I"

# Delete a playlist (asks for confirmation)
python3 tools/youtube-upload/playlist.py delete "Test Playlist"
```

## Quota

YouTube Data API gives 10,000 units/day free. Each lesson upload ≈ 2,050 units → ~4-5 lessons/day. For batch days, request a quota increase in Google Cloud Console.

## Privacy strategy (recommended)

1. Upload everything as `unlisted` first.
2. Watch the YouTube version once to verify chapters, captions, and thumbnail render correctly.
3. Flip the privacy to `public` in YouTube Studio when you're confident.

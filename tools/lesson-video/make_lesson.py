#!/usr/bin/env python3
"""One-shot pipeline: synth Aria narration with edge-tts, then merge to MP4.

Run this on YOUR own Mac (Bing speech endpoint must be reachable):

    pip install edge-tts imageio-ffmpeg
    python3 tools/lesson-video/make_lesson.py teaching-videos/<lesson-folder>/

That's it — produces `<lesson-folder>.mp4` next to the script.json.

What it does
------------
1. Reads `script.json` for voice, rate, and section list.
2. Synthesizes one MP3 per section via edge-tts (skips sections whose MP3
   already exists — re-runs are cheap; delete an MP3 to regenerate it).
3. Calls merge_lesson.py to convert MP3→WAV, build the SRT, mix in
   intro/outro music, and render the final MP4 (1920x1080 H.264 + AAC
   + burned-in subtitles).

Why this exists
---------------
Claude's sandbox can't reach the Microsoft TTS endpoint, so the synth step
has to happen on a machine with internet access — that's your Mac. The merge
step COULD run in the sandbox too, but doing both here means you get the
finished MP4 in one command without round-tripping through chat.

For partial work (e.g. "I tweaked slides, just re-stitch") use merge_lesson.py
directly; that one Claude can run from sandbox.
"""
from __future__ import annotations
import argparse, asyncio, json, os, subprocess, sys
from pathlib import Path

DEFAULT_VOICE = "en-US-AriaNeural"
DEFAULT_RATE  = "-3%"

def need(pkg: str, import_name: str | None = None):
    try:
        __import__(import_name or pkg.replace("-", "_"))
    except ImportError:
        sys.exit(f"error: missing dependency '{pkg}'.\n  fix:  pip install {pkg}")

async def synth(folder: Path) -> int:
    """Generate MP3s for every section that doesn't already have one. Returns
    the number of NEW files written."""
    import edge_tts
    script = json.loads((folder / "script.json").read_text())
    voice = script.get("voice", DEFAULT_VOICE)
    rate  = script.get("voice_rate", DEFAULT_RATE)
    audio = folder / "audio"
    audio.mkdir(exist_ok=True)
    print(f"[synth] voice={voice}  rate={rate}  sections={len(script['sections'])}")

    fresh = 0
    for s in script["sections"]:
        mp3 = audio / f"{s['id']}.mp3"
        # Stale wav (zero-byte from a failed previous run) — clean up.
        wav = audio / f"{s['id']}.wav"
        if wav.exists() and wav.stat().st_size == 0:
            wav.unlink()
        if mp3.exists() and mp3.stat().st_size > 0:
            print(f"  [skip] {mp3.name}  (exists, delete to regen)")
            continue
        print(f"  [tts]  {mp3.name}")
        comm = edge_tts.Communicate(s["text"], voice, rate=rate)
        await comm.save(str(mp3))
        fresh += 1
    print(f"[synth] {fresh} new file(s); {len(script['sections']) - fresh} cached")
    return fresh

def merge(folder: Path, output: str | None) -> None:
    here = Path(__file__).resolve().parent
    cmd = [sys.executable, str(here / "merge_lesson.py"), str(folder)]
    if output:
        cmd += ["--output", output]
    print(f"[merge] {' '.join(cmd)}")
    r = subprocess.run(cmd)
    if r.returncode != 0:
        sys.exit(r.returncode)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", help="lesson folder with script.json + slides/")
    ap.add_argument("--output", default=None, help="output mp4 filename")
    ap.add_argument("--no-synth", action="store_true",
                    help="skip TTS, only merge (use existing audio/*.mp3)")
    args = ap.parse_args()

    folder = Path(args.folder).resolve()
    if not folder.is_dir():
        sys.exit(f"not a folder: {folder}")
    if not (folder / "script.json").exists():
        sys.exit(f"missing {folder}/script.json")

    if not args.no_synth:
        need("edge-tts", "edge_tts")
        asyncio.run(synth(folder))
    need("imageio-ffmpeg", "imageio_ffmpeg")
    merge(folder, args.output)

if __name__ == "__main__":
    main()

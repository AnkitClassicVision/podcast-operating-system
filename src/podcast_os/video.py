from __future__ import annotations

from pathlib import Path
import json
import shutil
import subprocess

FFMPEG_REQUIRED = ["ffmpeg", "ffprobe"]

def check_ffmpeg() -> dict[str, str]:
    result = {}
    for binary in FFMPEG_REQUIRED:
        path = shutil.which(binary)
        if not path:
            raise RuntimeError(f"{binary} is not installed or not on PATH")
        version = subprocess.run([binary, "-version"], capture_output=True, text=True, check=True).stdout.splitlines()[0]
        result[binary] = version
    return result

def probe_media(path: str | Path) -> dict:
    command = ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", str(path)]
    out = subprocess.run(command, capture_output=True, text=True, check=True).stdout
    return json.loads(out)

def ffmpeg_plan() -> list[dict[str, str]]:
    return [
        {"step": "probe", "command": "ffprobe -show_format -show_streams raw/input.mp4"},
        {"step": "normalize_audio", "command": "ffmpeg -i raw/input.mp4 -af loudnorm=I=-16:TP=-1.5:LRA=11 exports/audio-normalized.wav"},
        {"step": "side_by_side", "command": "ffmpeg -i host.mp4 -i guest.mp4 -filter_complex '[0:v]scale=960:1080:force_original_aspect_ratio=decrease,pad=960:1080:(ow-iw)/2:(oh-ih)/2[left];[1:v]scale=960:1080:force_original_aspect_ratio=decrease,pad=960:1080:(ow-iw)/2:(oh-ih)/2[right];[left][right]hstack=inputs=2[v]' -map '[v]' -an exports/interview-layout.mp4"},
        {"step": "add_intro_outro", "command": "ffmpeg concat workflow: intro + episode + outro, re-encoded to a consistent 1080p/aac output"},
        {"step": "social_clip", "command": "ffmpeg -ss START -i exports/full-episode.mp4 -t DURATION -c:v libx264 -preset fast -crf 23 -c:a aac exports/clip.mp4"},
        {"step": "thumbnail", "command": "ffmpeg -ss 00:03:00 -i exports/full-episode.mp4 -frames:v 1 exports/thumbnail.jpg"},
    ]

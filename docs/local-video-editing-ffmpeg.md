# Local Video Editing with FFmpeg

This workflow keeps editing local by default.

## Required local tools

- `ffmpeg`
- `ffprobe`
- Optional: `whisper` or another transcript tool
- Optional: Remotion if you render branded clips with React templates

Verify:

```bash
python -m podcast_os check-ffmpeg
```

## Standard local workflow

1. Probe media.
2. Extract or normalize audio.
3. Mix separate host/guest audio if needed.
4. Build side-by-side interview layout if separate video tracks exist.
5. Add intro and outro.
6. Export full video.
7. Export podcast MP3.
8. Extract thumbnails.
9. Extract social clips.
10. Compress social-ready assets.

## Default audio target

- Integrated loudness: `-16 LUFS`
- True peak: `-1.5 dBTP`
- Loudness range: `11`

## Default video target

- 1920x1080
- 30fps
- H.264 video
- AAC audio

## Example commands

Probe:

```bash
ffprobe -v quiet -print_format json -show_format -show_streams raw/input.mp4
```

Normalize audio:

```bash
ffmpeg -y -i raw/input.mp4 -vn -af loudnorm=I=-16:TP=-1.5:LRA=11 exports/audio-normalized.wav
```

Trim a clip:

```bash
ffmpeg -y -ss 00:15:30 -i exports/full-episode.mp4 -t 60 -c:v libx264 -preset fast -crf 23 -c:a aac exports/clip-01.mp4
```

Thumbnail:

```bash
ffmpeg -y -ss 00:03:00 -i exports/full-episode.mp4 -frames:v 1 exports/thumbnail.jpg
```

---
name: local-video-editing-ffmpeg
description: Use for local podcast audio/video processing with FFmpeg and ffprobe.
---

# Local Video Editing with FFmpeg

Required tools:

- ffmpeg
- ffprobe

Preferred workflow:

1. Probe input.
2. Normalize audio to -16 LUFS.
3. Mix tracks if separate host/guest audio exists.
4. Assemble intro + episode + outro.
5. Export MP4 and MP3.
6. Extract clips and thumbnails.
7. Verify outputs with ffprobe.

Do not modify raw media in place. Write to `exports/`.

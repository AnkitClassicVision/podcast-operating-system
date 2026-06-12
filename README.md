# Podcast Operating System

A public, tool-swappable production harness for running a podcast from sourcing to recording, local video editing, content creation, promotion, publishing, and analytics.

This repo is **tool-opinionated but not tool-locked**:

- The workflow spine is stable.
- Prompts, recipes, and connectors are swappable.
- Local video editing uses FFmpeg-first commands by default.
- Social and publishing actions default to local export or dry run.
- No private guests, transcripts, media, account IDs, API keys, or proprietary internal process notes are included.

## What you get

- A robust end-to-end podcast process.
- JSON schemas for episodes, guests, content packs, assets, and social posts.
- Prompt packs you can replace without changing code.
- Recipes for editing, show notes, clips, and promotion.
- Connector interfaces for CMS, storage, recording, editing, publishing, social, and analytics tools.
- Local FFmpeg video/audio workflow for intro/outro, audio normalization, side-by-side interview layout, thumbnails, audiograms, and social clips.
- Synthetic examples and tests.
- A private-data scanner for public-release hygiene.

## Quick start

```bash
git clone https://github.com/AnkitClassicVision/podcast-operating-system.git
cd podcast-operating-system
python3 -m venv .venv
source .venv/bin/activate
pip install -e . pytest
python -m podcast_os check-ffmpeg
python -m podcast_os validate-episode examples/sample_episode.json
python -m podcast_os generate-content-pack examples/sample_episode.json --out /tmp/content-pack.md
python -m podcast_os export-social examples/sample_episode.json --out /tmp/social-posts.json
python scripts/scan_private_data.py .
pytest
```

## Configure your stack

Copy the example config:

```bash
cp podcast.config.example.json podcast.config.json
```

Then choose your connectors and prompt pack:

```json
{
  "workflow": {
    "cms": "local_json",
    "recording": "manual_upload",
    "editing": "local_ffmpeg",
    "publishing": "manual_export",
    "social": "manual_csv"
  },
  "prompt_pack": "default"
}
```

You can later replace any layer:

- `editing`: `local_ffmpeg`, `descript_export`, `premiere_manual`, `final_cut_manual`, `remotion`
- `social`: `manual_csv`, `zernio`, `buffer`, `late`, `hootsuite`
- `cms`: `local_json`, `notion`, `airtable`, `google_sheets`
- `publishing`: `manual_export`, `youtube`, `rss`, `spotify_for_podcasters`

## Workflow spine

1. Source topic or guest.
2. Research guest/topic.
3. Build episode brief.
4. Record episode.
5. Ingest raw assets and transcript.
6. Edit audio/video locally or through a tool connector.
7. Generate show notes, clips, newsletter blurbs, and social posts.
8. Publish or export publishing assets.
9. Promote episode.
10. Track analytics and archive reusable assets.

## Safety model

Default behavior is safe:

- No live publishing unless an adapter explicitly supports it.
- Dry-run/manual export is the default connector behavior.
- `.env` is ignored.
- `episodes/`, `raw/`, `exports/`, `media/`, and `private/` are ignored by default.
- Example data is synthetic.
- `scripts/scan_private_data.py` blocks obvious secrets, emails, phone numbers, private keys, and private-data filenames.

## Public-release rule

Do not flip a private podcast repo public. Create a clean public repo with fresh history, synthetic examples, and generic connector stubs. Keep your real workflow repo private.

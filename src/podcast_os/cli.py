from __future__ import annotations

import argparse
import json
from pathlib import Path

from .content import generate_content_pack, generate_social_posts
from .models import Episode, validate_episode_dict
from .safety import scan_path
from .video import check_ffmpeg, ffmpeg_plan


def cmd_validate_episode(args):
    data = json.loads(Path(args.episode).read_text(encoding="utf-8"))
    validate_episode_dict(data)
    print(f"OK: {args.episode}")


def cmd_generate_content_pack(args):
    episode = Episode.from_file(args.episode)
    content = generate_content_pack(episode)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(content, encoding="utf-8")
    print(args.out)


def cmd_export_social(args):
    episode = Episode.from_file(args.episode)
    posts = generate_social_posts(episode)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(posts, indent=2) + "\n", encoding="utf-8")
    print(args.out)


def cmd_check_ffmpeg(args):
    versions = check_ffmpeg()
    print(json.dumps(versions, indent=2))


def cmd_local_video_plan(args):
    print(json.dumps(ffmpeg_plan(), indent=2))


def cmd_scan(args):
    findings = scan_path(args.path)
    if findings:
        print(json.dumps(findings, indent=2))
        raise SystemExit(1)
    print("OK: no private-data patterns detected")


def build_parser():
    parser = argparse.ArgumentParser(prog="podcast-os")
    sub = parser.add_subparsers(required=True)

    p = sub.add_parser("validate-episode")
    p.add_argument("episode")
    p.set_defaults(func=cmd_validate_episode)

    p = sub.add_parser("generate-content-pack")
    p.add_argument("episode")
    p.add_argument("--out", required=True)
    p.set_defaults(func=cmd_generate_content_pack)

    p = sub.add_parser("export-social")
    p.add_argument("episode")
    p.add_argument("--out", required=True)
    p.set_defaults(func=cmd_export_social)

    p = sub.add_parser("check-ffmpeg")
    p.set_defaults(func=cmd_check_ffmpeg)

    p = sub.add_parser("local-video-plan")
    p.set_defaults(func=cmd_local_video_plan)

    p = sub.add_parser("scan-private-data")
    p.add_argument("path", nargs="?", default=".")
    p.set_defaults(func=cmd_scan)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)

if __name__ == "__main__":
    main()

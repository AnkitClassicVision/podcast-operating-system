#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from podcast_os.video import check_ffmpeg

print(json.dumps(check_ffmpeg(), indent=2))

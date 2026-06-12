#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from podcast_os.safety import scan_path

path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
findings = scan_path(path)
if findings:
    print(json.dumps(findings, indent=2))
    raise SystemExit(1)
print("OK: no private-data patterns detected")

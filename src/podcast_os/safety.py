from __future__ import annotations

from pathlib import Path
import re

EXCLUDED_DIRS = {".git", ".venv", "venv", "__pycache__", ".pytest_cache", "dist", "build"}
BINARY_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".mp4", ".mov", ".mp3", ".wav", ".pdf", ".docx"}
PRIVATE_PATH_HINTS = ["/private/", "/raw/", "/recordings/", "/transcripts/", "/logs/", "/episodes/"]

PATTERNS = {
    "private_key": re.compile(r"-----BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
    # Do not let whitespace cross line boundaries, or blank .env.example keys can
    # accidentally consume the next variable name.
    "api_key_assignment": re.compile(r"(?i)(api[_-]?key|token|secret|password)[ \t]*[:=][ \t]*['\"]?[A-Za-z0-9_\-]{16,}"),
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@(?!example\.com\b|example\.org\b|example\.net\b)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "phone": re.compile(r"\b(?:\+?1[-.\s]?)?\(?[2-9]\d{2}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"),
    "bearer": re.compile(r"(?i)bearer\s+[A-Za-z0-9._\-]{20,}"),
}

def iter_text_files(root: str | Path):
    root = Path(root)
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in BINARY_EXTENSIONS:
            continue
        yield path

def scan_path(root: str | Path) -> list[dict[str, str]]:
    root = Path(root).resolve()
    findings: list[dict[str, str]] = []
    for path in iter_text_files(root):
        rel = "/" + str(path.relative_to(root)).replace("\\", "/")
        if any(hint in rel for hint in PRIVATE_PATH_HINTS):
            findings.append({"file": rel.lstrip("/"), "kind": "private_path_hint"})
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for kind, pattern in PATTERNS.items():
            if pattern.search(text):
                findings.append({"file": rel.lstrip("/"), "kind": kind})
    return findings

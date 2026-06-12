from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
import json

REQUIRED_EPISODE_FIELDS = ["id", "title", "format", "status", "guest", "assets", "channels"]

@dataclass
class Guest:
    name: str
    role: str = "guest"
    company: str = "Example Co"
    bio: str = "Short synthetic bio."

@dataclass
class Episode:
    id: str
    title: str
    format: str
    status: str
    guest: dict[str, Any]
    assets: dict[str, Any] = field(default_factory=dict)
    channels: list[str] = field(default_factory=list)
    topic: str = ""
    summary: str = ""

    @classmethod
    def from_file(cls, path: str | Path) -> "Episode":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        validate_episode_dict(data)
        return cls(**{k: data.get(k) for k in cls.__dataclass_fields__.keys()})

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "format": self.format,
            "status": self.status,
            "guest": self.guest,
            "assets": self.assets,
            "channels": self.channels,
            "topic": self.topic,
            "summary": self.summary,
        }

def validate_episode_dict(data: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_EPISODE_FIELDS if field not in data]
    if missing:
        raise ValueError(f"Missing required episode fields: {', '.join(missing)}")
    if not isinstance(data["guest"], dict):
        raise ValueError("episode.guest must be an object")
    if not isinstance(data["assets"], dict):
        raise ValueError("episode.assets must be an object")
    if not isinstance(data["channels"], list):
        raise ValueError("episode.channels must be a list")

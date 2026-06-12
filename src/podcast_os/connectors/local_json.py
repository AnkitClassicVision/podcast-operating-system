from __future__ import annotations

from pathlib import Path
from .base import ConnectorResult, DryRunConnector

class LocalJsonConnector(DryRunConnector):
    name = "local_json"

    def __init__(self, root: str = "examples"):
        self.root = Path(root)

    def validate_config(self) -> ConnectorResult:
        if not self.root.exists():
            return ConnectorResult(False, f"root does not exist: {self.root}")
        return ConnectorResult(True, f"root exists: {self.root}")

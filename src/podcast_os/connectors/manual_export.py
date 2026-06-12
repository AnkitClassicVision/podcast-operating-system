from __future__ import annotations

from pathlib import Path
from .base import ConnectorResult, DryRunConnector

class ManualExportConnector(DryRunConnector):
    name = "manual_export"

    def __init__(self, export_dir: str = "exports"):
        self.export_dir = Path(export_dir)

    def dry_run(self) -> ConnectorResult:
        return ConnectorResult(True, f"would export files to {self.export_dir}")

    def execute(self, *, confirm: bool = False) -> ConnectorResult:
        if not confirm:
            return ConnectorResult(False, "manual export blocked without confirmation")
        self.export_dir.mkdir(parents=True, exist_ok=True)
        return ConnectorResult(True, f"created export directory: {self.export_dir}")

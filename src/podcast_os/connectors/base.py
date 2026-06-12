from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Any

@dataclass
class ConnectorResult:
    ok: bool
    message: str
    data: dict[str, Any] | None = None

class Connector(Protocol):
    name: str
    mode: str

    def validate_config(self) -> ConnectorResult: ...
    def pull_inputs(self) -> ConnectorResult: ...
    def generate_preview(self) -> ConnectorResult: ...
    def dry_run(self) -> ConnectorResult: ...
    def execute(self, *, confirm: bool = False) -> ConnectorResult: ...

class DryRunConnector:
    name = "dry_run"
    mode = "local"

    def validate_config(self) -> ConnectorResult:
        return ConnectorResult(True, "config valid")

    def pull_inputs(self) -> ConnectorResult:
        return ConnectorResult(True, "inputs pulled", {})

    def generate_preview(self) -> ConnectorResult:
        return ConnectorResult(True, "preview generated", {})

    def dry_run(self) -> ConnectorResult:
        return ConnectorResult(True, "dry run complete", {})

    def execute(self, *, confirm: bool = False) -> ConnectorResult:
        if not confirm:
            return ConnectorResult(False, "live execution blocked: pass confirm=True")
        return ConnectorResult(True, "execution complete", {})

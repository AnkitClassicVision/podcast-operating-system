# Connector Contracts

Every connector should implement the same lifecycle:

1. `validate_config()`
2. `pull_inputs()`
3. `generate_preview()`
4. `dry_run()`
5. `execute(confirm=True)`

## Rules

- Dry run is the default.
- Live execution must require explicit confirmation.
- Connectors should never print secrets.
- Connectors should report what they would read/write.
- Multi-account connectors must require an explicit account/profile selection.

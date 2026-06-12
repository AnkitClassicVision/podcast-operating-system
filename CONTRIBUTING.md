# Contributing

Contributions should preserve the pluggable architecture:

- Add connector adapters under `src/podcast_os/connectors/`.
- Add prompt variants under `prompt_packs/`.
- Add recipe variants under `recipes/`.
- Keep examples synthetic.
- Do not add private workflow data.

Before opening a PR:

```bash
python scripts/scan_private_data.py .
pytest
```

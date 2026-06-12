# Public Release Safety

Use a clean public repo with fresh history. Do not flip a private podcast operations repo public.

## Before publishing

- Remove real episodes.
- Remove raw recordings and transcripts.
- Replace real guests with synthetic examples.
- Remove tool account IDs.
- Remove `.env` and config files.
- Remove private prompts or strategy notes.
- Run `python scripts/scan_private_data.py .`.
- Run tests.

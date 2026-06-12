# Security Policy

This repository is designed to be public-safe. Keep real podcast operations in a private repo or private workspace.

## Never commit

- `.env` files
- API keys or OAuth tokens
- Recording links
- Calendar links
- Raw transcripts
- Raw recordings
- Guest personal contact details
- Private media folders
- Account IDs or database IDs
- Internal strategy notes

## Public-release checklist

Run before every release:

```bash
python scripts/scan_private_data.py .
pytest
```

If the scanner flags a file, either remove it, replace it with synthetic data, or move it to a private workspace.

## Connector safety

Connectors must default to dry-run or local export. Any live publishing or external write must require an explicit flag and clearly name the destination.

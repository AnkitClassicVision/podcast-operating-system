from pathlib import Path
from podcast_os.safety import scan_path


def test_repo_scanner_clean_on_repo():
    findings = scan_path(Path.cwd())
    assert findings == []


def test_scanner_detects_secret(tmp_path):
    p = tmp_path / "bad.txt"
    p.write_text("API" + "_KEY=" + "abc12345678901234567890")
    findings = scan_path(tmp_path)
    assert findings

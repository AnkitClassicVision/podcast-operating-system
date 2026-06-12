from pathlib import Path
from podcast_os.cli import main


def test_cli_generate_content_pack(tmp_path):
    out = tmp_path / "pack.md"
    main(["generate-content-pack", "examples/sample_episode.json", "--out", str(out)])
    assert out.exists()
    assert "How operators build" in out.read_text()

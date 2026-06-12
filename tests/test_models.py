import json
from pathlib import Path

from podcast_os.models import Episode, validate_episode_dict


def test_sample_episode_valid():
    path = Path("examples/sample_episode.json")
    episode = Episode.from_file(path)
    assert episode.id == "example-001"
    assert "youtube" in episode.channels


def test_missing_required_field_fails():
    data = json.loads(Path("examples/sample_episode.json").read_text())
    data.pop("guest")
    try:
        validate_episode_dict(data)
    except ValueError as exc:
        assert "guest" in str(exc)
    else:
        raise AssertionError("expected validation error")

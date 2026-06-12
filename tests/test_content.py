from podcast_os.models import Episode
from podcast_os.content import generate_content_pack, generate_social_posts


def test_content_pack_contains_title():
    episode = Episode.from_file("examples/sample_episode.json")
    pack = generate_content_pack(episode)
    assert episode.title in pack
    assert "Promotion assets" in pack


def test_social_posts_generated():
    episode = Episode.from_file("examples/sample_episode.json")
    posts = generate_social_posts(episode)
    assert len(posts) >= 3
    assert all("copy" in post for post in posts)

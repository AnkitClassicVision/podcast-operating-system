from __future__ import annotations

from .models import Episode

CONTENT_PACK_TEMPLATE = """# {title}

## One-line promise
{promise}

## Guest
- Name: {guest_name}
- Role: {guest_role}
- Company: {guest_company}

## Episode summary
{summary}

## Show notes
- Problem: What made this topic worth recording?
- Moment: What story or example makes it concrete?
- Lesson: What can a listener use this week?
- CTA: Where should a listener go next?

## Clip candidates
1. Strong standalone quote
2. Specific tactical lesson
3. Emotional or surprising moment

## Promotion assets
- Release email
- LinkedIn post
- Short-form video caption
- Newsletter blurb
- Guest-share guide
"""

SOCIAL_POSTS = [
    {
        "platform": "linkedin",
        "type": "launch_post",
        "copy": "New episode: {title}. We talked about {topic}. The useful takeaway: {promise}",
    },
    {
        "platform": "youtube_shorts",
        "type": "clip_caption",
        "copy": "A sharp moment from {title}: {promise}",
    },
    {
        "platform": "newsletter",
        "type": "blurb",
        "copy": "This week on the podcast: {title}. If you care about {topic}, start here.",
    },
]

def episode_promise(episode: Episode) -> str:
    if episode.summary:
        return episode.summary.split(".")[0].strip() + "."
    if episode.topic:
        return f"A practical conversation about {episode.topic}."
    return "A practical conversation with one reusable lesson."

def generate_content_pack(episode: Episode) -> str:
    guest = episode.guest or {}
    return CONTENT_PACK_TEMPLATE.format(
        title=episode.title,
        promise=episode_promise(episode),
        guest_name=guest.get("name", "Example Guest"),
        guest_role=guest.get("role", "guest"),
        guest_company=guest.get("company", "Example Co"),
        summary=episode.summary or "Add a 3-5 sentence summary after editing.",
    )

def generate_social_posts(episode: Episode) -> list[dict[str, str]]:
    promise = episode_promise(episode)
    topic = episode.topic or "the episode topic"
    return [
        {**post, "copy": post["copy"].format(title=episode.title, topic=topic, promise=promise)}
        for post in SOCIAL_POSTS
    ]

from podcast_os.video import ffmpeg_plan


def test_ffmpeg_plan_has_expected_steps():
    steps = [item["step"] for item in ffmpeg_plan()]
    assert "normalize_audio" in steps
    assert "social_clip" in steps

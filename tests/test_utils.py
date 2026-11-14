"""Unit tests for URL parsing and timestamp utilities."""

import pytest
from src.core.exceptions import InvalidYouTubeURLException
from src.core.utils import (
    build_youtube_timestamp_url,
    extract_video_id,
    format_timestamp,
    parse_timestamp,
)


def test_extract_video_id_standard_url():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    assert extract_video_id(url) == "dQw4w9WgXcQ"


def test_extract_video_id_with_extra_params():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=42s&feature=shared"
    assert extract_video_id(url) == "dQw4w9WgXcQ"


def test_extract_video_id_short_url():
    url = "https://youtu.be/dQw4w9WgXcQ"
    assert extract_video_id(url) == "dQw4w9WgXcQ"


def test_extract_video_id_embed_url():
    url = "https://www.youtube.com/embed/dQw4w9WgXcQ"
    assert extract_video_id(url) == "dQw4w9WgXcQ"


def test_extract_video_id_shorts_url():
    url = "https://www.youtube.com/shorts/dQw4w9WgXcQ"
    assert extract_video_id(url) == "dQw4w9WgXcQ"


def test_extract_video_id_live_url():
    url = "https://www.youtube.com/live/dQw4w9WgXcQ"
    assert extract_video_id(url) == "dQw4w9WgXcQ"


def test_extract_video_id_direct_id():
    raw_id = "dQw4w9WgXcQ"
    assert extract_video_id(raw_id) == "dQw4w9WgXcQ"


def test_extract_video_id_invalid_url():
    with pytest.raises(InvalidYouTubeURLException):
        extract_video_id("https://vimeo.com/12345678")

    with pytest.raises(InvalidYouTubeURLException):
        extract_video_id("")

    with pytest.raises(InvalidYouTubeURLException):
        extract_video_id("not-a-valid-id")


def test_format_timestamp():
    assert format_timestamp(0) == "00:00"
    assert format_timestamp(45) == "00:45"
    assert format_timestamp(65.4) == "01:05"
    assert format_timestamp(125) == "02:05"
    assert format_timestamp(3600) == "01:00:00"
    assert format_timestamp(3665.9) == "01:01:05"


def test_parse_timestamp():
    assert parse_timestamp("45") == 45.0
    assert parse_timestamp("01:05") == 65.0
    assert parse_timestamp("01:01:05") == 3665.0

    with pytest.raises(ValueError):
        parse_timestamp("invalid:time:format:extra")


def test_build_youtube_timestamp_url():
    url = build_youtube_timestamp_url("dQw4w9WgXcQ", 125.8)
    assert url == "https://youtu.be/dQw4w9WgXcQ?t=125"


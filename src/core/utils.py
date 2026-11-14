"""Core utility functions for YouTube URL parsing and timestamp conversions."""

import math
import re
from src.core.exceptions import InvalidYouTubeURLException

# Canonical YouTube video ID is 11 characters (alphanumeric, -, _)
YOUTUBE_ID_PATTERN = re.compile(r"^[a-zA-Z0-9_-]{11}$")

# Comprehensive regex to extract YouTube video ID from various URL formats
YOUTUBE_URL_REGEX = re.compile(
    r"(?:https?:\/\/)?(?:www\.|m\.)?(?:youtube\.com\/(?:watch\?(?:.*&)?v=|embed\/|v\/|shorts\/|live\/)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
)


def extract_video_id(url_or_id: str) -> str:
    """Extracts the 11-character YouTube video ID from a URL or raw ID.

    Args:
        url_or_id: YouTube URL (desktop, mobile, short, embed, shorts) or direct ID.

    Returns:
        Canonical 11-character video ID string.

    Raises:
        InvalidYouTubeURLException: If no valid video ID could be parsed.
    """
    if not url_or_id or not isinstance(url_or_id, str):
        raise InvalidYouTubeURLException("Empty or non-string YouTube URL provided.")

    cleaned = url_or_id.strip()

    # Direct video ID passed
    if YOUTUBE_ID_PATTERN.match(cleaned):
        return cleaned

    # Match against URL regex
    match = YOUTUBE_URL_REGEX.search(cleaned)
    if match:
        video_id = match.group(1)
        if YOUTUBE_ID_PATTERN.match(video_id):
            return video_id

    raise InvalidYouTubeURLException(
        f"Unable to extract a valid YouTube video ID from: '{url_or_id}'"
    )


def format_timestamp(seconds: float) -> str:
    """Formats seconds into human-readable [HH:]MM:SS string.

    Examples:
        75.0 -> "01:15"
        3665.0 -> "01:01:05"
        5.2 -> "00:05"
    """
    total_sec = max(0, int(math.floor(seconds)))
    hours = total_sec // 3600
    minutes = (total_sec % 3600) // 60
    secs = total_sec % 60

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def parse_timestamp(timestamp_str: str) -> float:
    """Parses [HH:]MM:SS or integer second strings into total seconds as float.

    Examples:
        "01:15" -> 75.0
        "01:01:05" -> 3665.0
        "45" -> 45.0

    Raises:
        ValueError: If format is invalid.
    """
    if not timestamp_str or not isinstance(timestamp_str, str):
        raise ValueError("Invalid timestamp string")

    parts = timestamp_str.strip().split(":")
    try:
        if len(parts) == 1:
            return float(parts[0])
        elif len(parts) == 2:
            minutes, seconds = float(parts[0]), float(parts[1])
            return minutes * 60 + seconds
        elif len(parts) == 3:
            hours, minutes, seconds = float(parts[0]), float(parts[1]), float(parts[2])
            return hours * 3600 + minutes * 60 + seconds
        else:
            raise ValueError(f"Too many segments in timestamp: {timestamp_str}")
    except ValueError as e:
        raise ValueError(f"Could not parse timestamp '{timestamp_str}': {e}") from e


def build_youtube_timestamp_url(video_id: str, seconds: float) -> str:
    """Constructs a direct jump link to the specific timestamp of a YouTube video."""
    canonical_id = extract_video_id(video_id)
    sec_int = max(0, int(math.floor(seconds)))
    return f"https://youtu.be/{canonical_id}?t={sec_int}"


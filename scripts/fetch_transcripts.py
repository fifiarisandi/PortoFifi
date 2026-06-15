#!/usr/bin/env python3
"""Fetch YouTube video transcripts and save them as organized markdown files."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, quote, urlparse
from urllib.request import urlopen

from youtube_transcript_api import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
    YouTubeTranscriptApi,
)

VIDEOS = {
    "matt-diggity": [
        "https://www.youtube.com/watch?v=Ryr15qNIdrw",
        "https://www.youtube.com/watch?v=MWCAVBXhcbU",
    ],
    "nathan-gotch": [
        "https://www.youtube.com/watch?v=WAXmw1ImBj4",
        "https://www.youtube.com/watch?v=QqLhztKZeqU",
    ],
    "semrush": [
        "https://www.youtube.com/watch?v=4qCfvoQi758",
        "https://www.youtube.com/watch?v=a4jmsmdtvfo",
    ],
    "ahrefs": [
        "https://www.youtube.com/watch?v=5OccF4g0UKI",
        "https://www.youtube.com/watch?v=ke-53zivOaw",
    ],
    "wpbeginner": [
        "https://www.youtube.com/watch?v=cxa0dlnElc8",
        "https://www.youtube.com/watch?v=dLXZ3FKWBeE",
    ],
    "edward-sturm": [
        "https://www.youtube.com/watch?v=vJZH0V0sJtM",
        "https://www.youtube.com/watch?v=ckSHSIPNDb8",
        "https://www.youtube.com/watch?v=t8CoElpldtk",
    ],
    "hubspot-marketing": [
        "https://www.youtube.com/watch?v=XQL6zV8aRFk",
        "https://www.youtube.com/watch?v=kuhhJ4PA8gk",
        "https://www.youtube.com/watch?v=5Mlx-2kbAXs",
    ],
}

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "research" / "youtube-transcripts"


def extract_video_id(url: str) -> str:
    """Extract a YouTube video ID from a URL, ignoring extra query params."""
    parsed = urlparse(url)

    if parsed.hostname in {"youtu.be", "www.youtu.be"}:
        video_id = parsed.path.lstrip("/").split("/")[0]
    elif parsed.hostname in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
        if parsed.path == "/watch":
            video_id = parse_qs(parsed.query).get("v", [""])[0]
        elif parsed.path.startswith("/embed/"):
            video_id = parsed.path.split("/")[2]
        elif parsed.path.startswith("/shorts/"):
            video_id = parsed.path.split("/")[2]
        else:
            video_id = ""
    else:
        video_id = ""

    video_id = video_id.split("&")[0].strip()
    if not video_id:
        raise ValueError(f"Could not extract video ID from URL: {url}")
    return video_id


def fetch_video_title(video_id: str, url: str) -> tuple[str, bool]:
    """Try to fetch the video title via pytube or oEmbed; fall back to the video ID."""
    try:
        from pytube import YouTube

        title = YouTube(url).title
        if title:
            return title.strip(), True
    except Exception:
        pass

    try:
        oembed_url = (
            "https://www.youtube.com/oembed"
            f"?url={quote(url, safe='')}&format=json"
        )
        with urlopen(oembed_url, timeout=15) as response:
            title = json.load(response).get("title", "").strip()
        if title:
            return title, True
    except Exception:
        pass

    return video_id, False


def format_transcript(segments) -> str:
    """Join transcript segments into readable paragraphs."""
    text = " ".join(segment.text.strip() for segment in segments)
    text = re.sub(r"\s+", " ", text).strip()

    # Break into paragraphs every ~4 sentences for readability.
    sentences = re.split(r"(?<=[.!?])\s+", text)
    paragraphs: list[str] = []
    chunk: list[str] = []

    for sentence in sentences:
        if not sentence:
            continue
        chunk.append(sentence)
        if len(chunk) >= 4:
            paragraphs.append(" ".join(chunk))
            chunk = []

    if chunk:
        paragraphs.append(" ".join(chunk))

    return "\n\n".join(paragraphs)


def build_markdown(
    title: str,
    channel: str,
    video_id: str,
    transcript_text: str,
    title_is_placeholder: bool,
) -> str:
    title_line = f"# {title}"
    if title_is_placeholder:
        title_line += "\n<!-- Title unavailable; using video ID as placeholder -->"

    return (
        f"{title_line}\n"
        f"**Channel:** {channel}\n"
        f"**URL:** https://www.youtube.com/watch?v={video_id}\n\n"
        f"## Transcript\n\n"
        f"{transcript_text}\n"
    )


def transcript_exists(channel: str, video_id: str) -> bool:
    """Return True if a transcript file for this video already exists."""
    channel_dir = OUTPUT_DIR / channel
    if not channel_dir.exists():
        return False

    video_id_path = channel_dir / f"{video_id}.md"
    if video_id_path.exists():
        return True

    url_marker = f"watch?v={video_id}"
    return any(
        url_marker in path.read_text(encoding="utf-8")
        for path in channel_dir.glob("*.md")
    )


def save_transcript(
    channel: str,
    video_id: str,
    url: str,
) -> None:
    channel_dir = OUTPUT_DIR / channel
    channel_dir.mkdir(parents=True, exist_ok=True)

    transcript = YouTubeTranscriptApi().fetch(video_id)
    title, title_found = fetch_video_title(video_id, url)
    markdown = build_markdown(
        title=title,
        channel=channel,
        video_id=video_id,
        transcript_text=format_transcript(transcript),
        title_is_placeholder=not title_found,
    )

    output_path = channel_dir / f"{video_id}.md"
    output_path.write_text(markdown, encoding="utf-8")
    print(f"Saved: {output_path}")


def main() -> int:
    saved = 0
    skipped = 0
    failed: list[str] = []

    for channel, urls in VIDEOS.items():
        for url in urls:
            try:
                video_id = extract_video_id(url)
            except ValueError as exc:
                print(f"WARNING: {exc}", file=sys.stderr)
                failed.append(url)
                continue

            if transcript_exists(channel, video_id):
                print(f"Skipping (already exists): {channel}/{video_id}")
                skipped += 1
                continue

            try:
                save_transcript(channel, video_id, url)
                saved += 1
            except (TranscriptsDisabled, NoTranscriptFound) as exc:
                print(
                    f"WARNING: Transcript unavailable for video {video_id}: {exc}",
                    file=sys.stderr,
                )
                failed.append(video_id)
            except VideoUnavailable as exc:
                print(
                    f"WARNING: Video unavailable for video {video_id}: {exc}",
                    file=sys.stderr,
                )
                failed.append(video_id)
            except Exception as exc:
                print(
                    f"WARNING: Failed to process video {video_id}: {exc}",
                    file=sys.stderr,
                )
                failed.append(video_id)

    print()
    print("Summary")
    print(f"  Successfully saved: {saved}")
    print(f"  Skipped (already exists): {skipped}")
    print(f"  Failed: {len(failed)}")
    if failed:
        print(f"  Failed video IDs/URLs: {', '.join(failed)}")

    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())

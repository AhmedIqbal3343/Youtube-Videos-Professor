import re

def extract_video_id(url: str) -> str:
    """
    Extract YouTube video ID from URL
    """
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url)
    if not match:
        raise ValueError("Invalid YouTube URL")
    return match.group(1)

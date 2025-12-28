from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
import re

def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if not match:
        raise ValueError("Invalid YouTube URL")
    return match.group(1)

def load_youtube_docs(url):
    video_id = extract_video_id(url)
    transcript = YouTubeTranscriptApi.fetch(video_id)

    full_text = " ".join([t["text"] for t in transcript])

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_text(full_text)

    return [Document(page_content=chunk) for chunk in chunks]

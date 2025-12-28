import os
from langchain_openai import ChatOpenAI

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in environment")

llm = ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    openai_api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    temperature=0.2
)

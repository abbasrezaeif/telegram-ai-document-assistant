import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:3b"


def summarize_text(text: str, language: str = "Persian") -> str:
    if not text:
        return ""

    max_chars = 12000
    trimmed_text = text[:max_chars]

    prompt = f"""
You are an AI document assistant.

Summarize the following document in {language}.

Return the result with this structure:

## خلاصه کلی
A clear short summary.

## نکات کلیدی
- Key point 1
- Key point 2
- Key point 3

## موضوعات مهم
- Topic 1
- Topic 2

## نتیجه‌گیری
Final conclusion.

Document:
{trimmed_text}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
        },
        timeout=300,
    )

    response.raise_for_status()

    data = response.json()
    return data.get("response", "").strip()
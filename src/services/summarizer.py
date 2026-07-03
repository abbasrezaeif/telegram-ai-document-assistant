import requests

from src.services.chunker import split_text


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:3b"


def summarize_chunk(chunk: str, language: str = "Persian") -> str:
    prompt = f"""
You are an expert document summarizer.

Summarize this text in {language}.
Keep it short and useful.
Use bullet points.

Text:
{chunk}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": 350
            },
        },
        timeout=600,
    )

    response.raise_for_status()
    return response.json().get("response", "").strip()


def summarize_text(text: str, language: str = "Persian") -> str:
    chunks = split_text(text)

    summaries = []
    total = len(chunks)

    for index, chunk in enumerate(chunks, start=1):
        print(f"Summarizing chunk {index}/{total}")
        summaries.append(summarize_chunk(chunk, language))

    merged_summary = "\n\n".join(summaries)

    final_prompt = f"""
You are an expert AI assistant.

Merge these partial summaries into one final Persian summary.
Keep it concise.

Structure:
## خلاصه کلی
## نکات کلیدی
## نتیجه‌گیری

Partial summaries:
{merged_summary}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": final_prompt,
            "stream": False,
            "options": {
                "num_predict": 500
            },
        },
        timeout=600,
    )

    response.raise_for_status()
    return response.json().get("response", "").strip()
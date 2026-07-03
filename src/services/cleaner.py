import re


def clean_text(text: str) -> str:
    if not text:
        return ""

    text = text.replace("\u200c", " ")
    text = text.replace("\ufeff", "")
    text = text.replace("‏", "")
    text = text.replace("‎", "")

    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)

    lines = text.splitlines()
    cleaned_lines = []

    for line in lines:
        line = line.strip()

        if not line:
            cleaned_lines.append("")
            continue

        if re.fullmatch(r"[-–—_ ]+", line):
            continue

        if re.fullmatch(r"\d+", line):
            continue

        if line.lower().startswith("--- ocr page"):
            continue

        if line.lower().startswith("--- page"):
            continue

        cleaned_lines.append(line)

    cleaned_text = "\n".join(cleaned_lines)
    cleaned_text = re.sub(r"\n{3,}", "\n\n", cleaned_text)

    return cleaned_text.strip()
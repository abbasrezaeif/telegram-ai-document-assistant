from pathlib import Path

import pytesseract
from pdf2image import convert_from_path


def ocr_pdf(file_path: str, language: str = "fas+eng") -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    pages = convert_from_path(str(path), dpi=300)

    text_parts = []

    for page_number, page_image in enumerate(pages, start=1):
        page_text = pytesseract.image_to_string(
            page_image,
            lang=language,
        )

        text_parts.append(f"\n--- OCR Page {page_number} ---\n")
        text_parts.append(page_text)

    return "\n".join(text_parts).strip()
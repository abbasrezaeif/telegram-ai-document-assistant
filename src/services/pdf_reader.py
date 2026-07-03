from pathlib import Path
import pdfplumber


def extract_text_from_pdf(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    text_parts = []

    with pdfplumber.open(path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text() or ""
            text_parts.append(f"\n--- Page {page_number} ---\n")
            text_parts.append(page_text)

    return "\n".join(text_parts).strip()


def save_extracted_text(document_id: int, text: str) -> Path:
    output_dir = Path("data/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"document_{document_id}_text.txt"
    output_path.write_text(text, encoding="utf-8")

    return output_path
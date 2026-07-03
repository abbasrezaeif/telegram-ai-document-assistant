from telegram import Update
from telegram.ext import ContextTypes

from src.database.db import save_document
from src.services.downloader import save_pdf
from src.services.pdf_reader import extract_text_from_pdf, save_extracted_text
from src.services.ocr import ocr_pdf
from src.services.cleaner import clean_text
from src.services.summarizer import summarize_text


def should_use_ocr(text: str) -> bool:
    if not text:
        return True

    if len(text.strip()) < 500:
        return True

    strange_chars = ["ﻧ", "ﺎ", "ﯽ", "ﺪ", "ﻣ", "ﺷ", "ﺘ", "ﺑ", "ﺮ"]
    strange_count = sum(text.count(char) for char in strange_chars)

    if strange_count > 20:
        return True

    return False


async def handle_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document = update.message.document

    if not document:
        await update.message.reply_text("❌ Please send a PDF file.")
        return

    await update.message.reply_text("📄 PDF received.\nDownloading...")

    path = await save_pdf(document)

    user_id = update.effective_user.id
    document_id = save_document(
        user_id=user_id,
        file_name=path.name,
        file_path=str(path),
    )

    await update.message.reply_text(
        f"✅ Saved successfully!\n\n"
        f"File: {path.name}\n"
        f"Document ID: {document_id}\n\n"
        f"🔍 Extracting text..."
    )

    extracted_text = extract_text_from_pdf(str(path))
    extraction_method = "pdfplumber"

    if should_use_ocr(extracted_text):
        await update.message.reply_text(
            "⚠️ Selectable text looks empty or corrupted.\n"
            "Running OCR..."
        )

        extracted_text = ocr_pdf(str(path), language="fas+eng")
        extraction_method = "ocr"

    cleaned_text = clean_text(extracted_text)
    text_output_path = save_extracted_text(document_id, cleaned_text)

    if not cleaned_text:
        await update.message.reply_text(
            "❌ Could not extract readable text from this PDF."
        )
        return

    await update.message.reply_text(
        f"✅ Text extracted and cleaned successfully!\n\n"
        f"Method: {extraction_method}\n"
        f"Raw characters: {len(extracted_text)}\n"
        f"Clean characters: {len(cleaned_text)}\n"
        f"Saved as: {text_output_path.name}\n\n"
        f"🧠 Summarizing with Local AI..."
    )

    summary = summarize_text(cleaned_text, language="Persian")

    if len(summary) > 3500:
        summary = summary[:3500] + "\n\n..."

    await update.message.reply_text(
        f"✅ Summary ready!\n\n{summary}"
    )

    print(f"Saved PDF: {path}")
    print(f"Saved to database with document_id: {document_id}")
    print(f"Extraction method: {extraction_method}")
    print(f"Extracted and cleaned text saved to: {text_output_path}")
    print("Summary sent to user")
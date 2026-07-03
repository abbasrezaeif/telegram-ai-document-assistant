from telegram import Update
from telegram.ext import ContextTypes

from src.database.db import save_document
from src.services.downloader import save_pdf
from src.services.pdf_reader import extract_text_from_pdf, save_extracted_text


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
    text_output_path = save_extracted_text(document_id, extracted_text)

    if extracted_text:
        preview = extracted_text[:1000]
        await update.message.reply_text(
            f"✅ Text extracted successfully!\n\n"
            f"Characters: {len(extracted_text)}\n"
            f"Saved as: {text_output_path.name}\n\n"
            f"Preview:\n{preview}"
        )
    else:
        await update.message.reply_text(
            "⚠️ No selectable text found in this PDF.\n"
            "This file may need OCR in the next step."
        )

    print(f"Saved PDF: {path}")
    print(f"Saved to database with document_id: {document_id}")
    print(f"Extracted text saved to: {text_output_path}")
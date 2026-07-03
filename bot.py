from dotenv import load_dotenv
import os
from pathlib import Path

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

DOWNLOAD_DIR = Path("data/downloads")
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to DocPilot AI!\n\n"
        "Send me a PDF document and I'll summarize it using Local AI."
    )


async def handle_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document = update.message.document

    if not document:
        await update.message.reply_text("Please send a PDF file.")
        return

    file_name = document.file_name or "document.pdf"

    if not file_name.lower().endswith(".pdf"):
        await update.message.reply_text("❌ Please send a valid PDF file.")
        return

    await update.message.reply_text("📄 PDF received. Downloading...")

    telegram_file = await document.get_file()

    save_path = DOWNLOAD_DIR / file_name
    await telegram_file.download_to_drive(custom_path=str(save_path))

    await update.message.reply_text(
        f"✅ PDF saved successfully!\n\n"
        f"File name: {file_name}"
    )

    print(f"Saved PDF: {save_path}")


def main():
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is missing. Check your .env file.")

    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .connect_timeout(30)
        .read_timeout(30)
        .write_timeout(30)
        .pool_timeout(30)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.PDF, handle_pdf))

    print("✅ DocPilot AI is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
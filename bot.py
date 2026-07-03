from dotenv import load_dotenv
import os

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from src.database.db import init_db
from src.handlers.start import start
from src.handlers.pdf import handle_pdf


load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


def main():
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is missing. Check your .env file.")

    init_db()

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
from dotenv import load_dotenv
import os

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to DocPilot AI!\n\n"
        "Send me a PDF document and I'll summarize it using Local AI."
    )


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

    print("✅ DocPilot AI is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
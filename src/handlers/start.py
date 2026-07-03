from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to DocPilot AI!\n\n"
        "Send me a PDF document and I'll summarize it using Local AI."
    )
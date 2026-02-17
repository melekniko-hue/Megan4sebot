import os
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def sorgu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Kullanım: /sorgu kullaniciadi")
        return

    username = context.args[0]
    await update.message.reply_text("Aranıyor...")

    result = subprocess.getoutput(f"sherlock {username} --print-found")

    if len(result) > 4000:
        result = result[:4000]

    await update.message.reply_text(result)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("sorgu", sorgu))
app.run_polling()

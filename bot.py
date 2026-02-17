import os
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sherlock bot hazır 🔍")

async def sherlock_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Kullanım: /sherlock kullaniciadi")
        return

    username = context.args[0]
    await update.message.reply_text(f"{username} aranıyor... 🔎")

    try:
        result = subprocess.run(
            ["sherlock", username, "--print-found"],
            capture_output=True,
            text=True,
            timeout=60
        )

        output = result.stdout

        if len(output) > 4000:
            output = output[:4000] + "\n\nÇok uzun olduğu için kısaltıldı."

        await update.message.reply_text(output)

    except Exception as e:
        await update.message.reply_text(f"Hata oluştu: {e}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sherlock", sherlock_search))

app.run_polling()

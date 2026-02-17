import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Kategori bot hazır 🔎\n\n"
        "Komutlar:\n"
        "/instagram kullaniciadi\n"
        "/x kullaniciadi\n"
        "/telegram kullaniciadi"
    )

def check_username(url):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return "✅ Kullanıcı bulundu"
        elif r.status_code == 404:
            return "❌ Kullanıcı bulunamadı"
        else:
            return f"⚠️ Durum kodu: {r.status_code}"
    except:
        return "⚠️ Bağlantı hatası"

async def instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Kullanım: /instagram kullaniciadi")
        return
    username = context.args[0]
    result = check_username(f"https://www.instagram.com/{username}/")
    await update.message.reply_text(f"Instagram sonucu:\n{result}")

async def x(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Kullanım: /x kullaniciadi")
        return
    username = context.args[0]
    result = check_username(f"https://x.com/{username}")
    await update.message.reply_text(f"X sonucu:\n{result}")

async def telegram_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Kullanım: /telegram kullaniciadi")
        return
    username = context.args[0]
    result = check_username(f"https://t.me/{username}")
    await update.message.reply_text(f"Telegram sonucu:\n{result}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("instagram", instagram))
app.add_handler(CommandHandler("x", x))
app.add_handler(CommandHandler("telegram", telegram_check))

app.run_polling()

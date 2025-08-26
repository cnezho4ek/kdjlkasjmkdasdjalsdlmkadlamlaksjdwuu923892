import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = os.environ.get("TOKEN")  # будем использовать переменные окружения

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Скоро отвечу прямо сюда или в лс. Если не отвечаю в течении 20-30 минут, попробуй дургие способы связи со мной: https://neopryaten.online\n\nHey! I’ll reply here or in DMs soon. If I don’t respond within 20–30 minutes, try other ways to contact me: https://neopryaten.online")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()

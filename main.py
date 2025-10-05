import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Токен берём из переменной Railway (Variables -> BOT_TOKEN)
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📊 График", url="https://docs.google.com/spreadsheets/d/1EXAMPLE")],
        [InlineKeyboardButton("⏰ Часы", url="https://docs.google.com/spreadsheets/d/2EXAMPLE")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "✅ Бот запущен!\nНе забудьте записывать свои часы:",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()

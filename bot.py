import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

CHANNEL = "https://t.me/hosseinii12car"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚘 به کانال خرید و فروش خودرو خوش آمدید!\n\n"
        "خودروهای داخلی و خارجی\n"
        "حواله و خودروهای صفر و کم‌کارکرد\n\n"
        "برای مشاهده آگهی‌ها وارد کانال شوید:\n"
        f"{https://t.me/hosseinii12car}"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()

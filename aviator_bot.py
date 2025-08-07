
import logging
import random
from datetime import datetime, timedelta
import pytz
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8065175698:AAGPoXJTSAkhmtMYEYcPPZpEDYD855ncYo4"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome! Send /signal anytime to get latest Aviator signals.")

def generate_signal():
    now = datetime.now(pytz.timezone("Asia/Kolkata"))
    signals = []
    for i in [3, 5, 8, 12, 16]:  # delay in minutes
        future_time = now + timedelta(minutes=i)
        time_str = future_time.strftime("%I:%M %p")
        x_value = round(random.uniform(2.1, 3.5), 2)
        signals.append(f"🎯 {time_str} ➤ Cashout at {x_value}x")
    return now.strftime("%d-%b-%Y %I:%M %p"), signals

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    signal_time, signals = generate_signal()
    text = f"""🚨 Aviator Signals 🚨

🕒 Iss message ka time: {signal_time}

🛫 Next 5 Game Predictions:

{chr(10).join(signals)}

💡 Bet only on mentioned times. Play responsibly.
#AviatorBaba"""
    await update.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

app.run_polling()

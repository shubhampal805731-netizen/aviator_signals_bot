import os
from telegram.ext import Updater, CommandHandler
from datetime import datetime, timedelta
import pytz
import random

# Token from environment
BOT_TOKEN = os.environ["BOT_TOKEN"]

def generate_signal():
    return round(random.uniform(2.1, 3.5), 2)

def start(update, context):
    now = datetime.now(pytz.timezone("Asia/Kolkata"))
    message_time = now.strftime("%d-%b-%Y %I:%M %p")

    response = f"🚨 Aviator Signals 🚨\n\n🕒 Iss message ka time: {message_time}\n\n🛫 Next 5 Game Predictions:\n\n"
    
    signal_times = []
    game_start_time = now + timedelta(minutes=3)
    gaps = [2, 3, 4, 4]  # time gaps between signals

    for gap in gaps:
        signal_times.append(game_start_time.strftime("%I:%M %p"))
        game_start_time += timedelta(minutes=gap)

    for i, time_str in enumerate(signal_times):
        response += f"🎯 {time_str} ➤ Cashout at {generate_signal()}x\n"

    response += "\n💡 Bet only on mentioned times. Play responsibly.\n#AviatorBaba"
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

print("✅ Bot is running...")
updater.start_polling()
updater.idle()

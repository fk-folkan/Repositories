import telebot
import os

TOKEN = os.getenv("TOKEN")
MY_ID = os.getenv("MY_ID")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 البوت شغال الآن على سيرفر Railway!")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"وصلت رسالتك: {message.text}")

if MY_ID:
    try:
        bot.send_message(MY_ID, "✅ تم تشغيل البوت بنجاح على السيرفر!")
    except Exception as e:
        print(f"Error: {e}")

print("Bot is running...")
bot.infinity_polling(none_stop=True)

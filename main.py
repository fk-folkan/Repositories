import telebot
import os

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🔥 البوت شغال على السيرفر")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, message.text)

print("Bot is running...")
bot.infinity_polling(none_stop=True)

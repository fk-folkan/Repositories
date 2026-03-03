import telebot
from telebot import types
import os

# جلب التوكن من إعدادات السيرفر
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # إنشاء أزرار عصرية تحت الرسالة
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("✨ خدماتنا", callback_data='services')
    btn2 = types.InlineKeyboardButton("📊 الإحصائيات", callback_data='stats')
    btn3 = types.InlineKeyboardButton("📞 الدعم الفني", callback_data='support')
    markup.add(btn1, btn2, btn3)
    
    welcome_text = (
        f"<b>أهلاً بك يا {message.from_user.first_name} في بوتك المطور 🚀</b>\n\n"
        "هذا البوت يعمل بنظام الاستجابة السريعة.\n"
        "يرجى اختيار قسم من الأقسام أدناه:"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='HTML', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "services":
        bot.answer_callback_query(call.id, "جاري فتح الخدمات...")
        bot.edit_message_text("🛠 <b>قائمة الخدمات:</b>\n1- زيادة متابعين\n2- رشق لايكات", 
                             call.message.chat.id, call.message.message_id, parse_mode='HTML')

print("Bot is running...")
bot.infinity_polling()

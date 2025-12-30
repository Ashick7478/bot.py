import telebot

TOKEN = "8385496169:AAF6ZWtHjGgy3q1YN2Eq3WPByxTUAZ1sB0s"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "👋 Bot is alive!\n\nআপনি এখন Driver Location Bot-এ আছেন।"
    )

bot.infinity_polling()

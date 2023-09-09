import telebot
bot = telebot.TeleBot("6492917074:AAH3f6MPYHEM-z7yN4PoS-kbTGE77YgSWXs")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты напили /start')

bot.polling(none_stop=True)
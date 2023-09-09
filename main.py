import telebot
from dotenv import dotenv_values

secrets = dotenv_values(".env")

bot = telebot.TeleBot(secrets['BOT_TOKEN'])

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты напили /start')

bot.polling(none_stop=True)
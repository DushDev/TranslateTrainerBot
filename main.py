import telebot
from dotenv import dotenv_values
from translateApi import translate
from notionApi import get_list_of_words, write_row, get_words_for_learning
from check_language import check_text_language
from pprint import pprint



secrets = dotenv_values(".env")
bot = telebot.TeleBot(secrets['BOT_TOKEN'])

def check_user(msg) -> bool:
    res = int(msg.from_user.id) == int(secrets['USER_ID']) or int(msg.from_user.id) == int(secrets['USER2_ID'])
    return res 

@bot.message_handler(commands=['start'])
def start_message(message):
    if not check_user(message): return 
    bot.send_message(message.chat.id, 'Вітаю. Пишіть будь який текст для перекладу з української на англійську і навпаки.')

@bot.message_handler(commands=['list'])
def list_message(message):
    if not check_user(message): return
    bot.reply_to(message, get_list_of_words())

@bot.message_handler(commands=['learn'])
def list_message(message):
    if not check_user(message): return
    bot.reply_to(message, get_words_for_learning(), parse_mode='MarkdownV2')
    

@bot.message_handler(content_types=['text'])
def translates(message: telebot.types.Message):
    if not check_user(message): return
    # if text begin from / print it
    if message.text.startswith('/'):
        return
    try:
        res = translate(message.text) 
        
        button_notion = telebot.types.InlineKeyboardButton('Add to Notion', callback_data=f'add_to_notion|||{message.text}|||{res}')

        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(button_notion)
        bot.reply_to(message, res, reply_markup=keyboard)
    except Exception as e:
        bot.reply_to(message, 'ERROR: ' + str(e))

@bot.callback_query_handler(func=lambda call: call.data.startswith('add_to_notion'))
def add_word(call: telebot.types.CallbackQuery):
    if not check_user(call.message): return
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text, reply_markup=None)
    data = call.data.split('|||')
    eng = ''
    ukr = ''
    if(check_text_language(data[1])=='en'):
        eng = data[1]
        ukr = data[2]
    else:
        eng = data[2]
        ukr = data[1]
    write_row(eng, ukr)

bot.polling(none_stop=True)
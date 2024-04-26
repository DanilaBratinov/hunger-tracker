import telebot
import pendulum
from telebot import types

import main

token = '6077672902:AAEUUetlpTzk50lu3d5v4AHdfTMuOgJwO8U'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    
    item1 = types.KeyboardButton('14-10')
    item2 = types.KeyboardButton('16-8')
    item3 = types.KeyboardButton('18-6')
    item4 = types.KeyboardButton('20-4')

    markup.add(item1, item2, item3, item4)
    
    chatID = message.chat.id
    bot.send_message(chatID, "Выберите интервал голодания", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_message(message):
    match message.text:
       case '14-10':
            bot.send_message(message.chat.id, f"{main.get_progress_view(14, 14, 11)}")
            
@bot.message_handler(commands=['startgolod'])
def start_golod(message):

    bot.send_message(message.chat.id, "Трекер голодания звпущен!\nУзнать текущее состояние голодания можно командой '/how'")

bot.infinity_polling()
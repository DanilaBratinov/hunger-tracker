import telebot
import redis
import datetime
from telebot import types

import main

token = '6077672902:AAEUUetlpTzk50lu3d5v4AHdfTMuOgJwO8U'
bot = telebot.TeleBot(token)

r = redis.Redis(host='91.217.77.53', port='6379')


@bot.message_handler(commands=['start'])
def start_message(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Начать голодание')

    markup.add(item1)
    
    chatID = message.chat.id
    bot.send_message(chatID, "Выберите интервал голодания", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_message(message):
    match message.text:
       case 'Начать голодание':

            dt = datetime.datetime.now()
            time = dt.strftime('%d.%m.%Y %H:%M')

            r.mset({f"{message.from_user.id}":f"{time}"})
            bot.send_message(message.chat.id, "Трекер голодания звпущен!\nУзнать текущее состояние голодания можно командой '/how'")

bot.infinity_polling()
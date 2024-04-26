import telebot
import redis
from datetime import datetime
from telebot import types

token = '6077672902:AAEUUetlpTzk50lu3d5v4AHdfTMuOgJwO8U'
bot = telebot.TeleBot(token)

r = redis.Redis(host='91.217.77.53', port='6379')

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Начать голодание')
    item2 = types.KeyboardButton('Посмотреть результат')

    markup.add(item1, item2)
    
    chatID = message.chat.id
    bot.send_message(chatID, "Выберите интервал голодания", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_message(message):
    match message.text:
        case 'Начать голодание':
            time = datetime.now().strftime('%d.%m.%Y %H:%M')

            r.mset({f"{message.from_user.id}":f"{time}"})
            bot.send_message(message.chat.id, "Трекер голодания звпущен!\nУзнать текущее состояние голодания можно командой '/how'")

        case 'Посмотреть результат':
            date_str1 = {datetime.now().strftime('%d.%m.%Y %H:%M')}
            date_str2 = f"{r.get(f'{message.from_user.id}').decode('utf-8')}"

            date1 = datetime.strptime(date_str1, '%d.%m.%Y %H:%M')
            date2 = datetime.strptime(date_str2, '%d.%m.%Y %H:%M')

            diff = date1 - date2

            hours = diff.seconds // 3600
            minutes = (diff.seconds % 3600) //60
            seconds = diff.seconds % 60

            bot.send_message(message.chat.id, f"Вы голодаете {hours} часов, {minutes} минут и {seconds} секунд")

bot.infinity_polling()
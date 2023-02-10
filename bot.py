import random
import telebot
from telebot import types

bot = telebot.TeleBot('5600847297:AAEqsun3bZq0LHLskWhmdmgpfFxw-jdAT60')

soft_flowers = ["https://flover.studio/tproduct/1-691865201921-avtorskii-buket-2",
"https://flover.studio/tproduct/1-435082614401-avtorskii-buket-4", "https://flover.studio/tproduct/1-136745445341-avtorskii-buket-8",
           "https://flover.studio/tproduct/1-356047785651-avtorskii-buket-10"]

bright_flowers = ["https://flover.studio/tproduct/1-793990755131-avtorskii-buket-11", "https://flover.studio/tproduct/1-251828660121-avtorskii-buket-7",
                  "https://flover.studio/tproduct/1-582377032931-avtorskii-buket-3" ]

wedding = ["https://flover.studio/wedding/tproduct/505738211-612972092581-buket-5", "https://flover.studio/wedding/tproduct/505738211-633296362561-buket-8",
"https://flover.studio/wedding/tproduct/505738211-536563838991-buket-110", "https://flover.studio/wedding/tproduct/505738211-323139605571-buket-20",
"https://flover.studio/wedding/tproduct/505738211-781537132011-buket-14"]

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Авторские букеты")
    btn2 = types.KeyboardButton("Свадебные букеты")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я помогу тебе подобрать букет. Выбери услугу".format(
                         message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Авторские букеты":
        bot.send_message(message.chat.id, text="Сейчас подберем тебе авторский букет!)")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.InlineKeyboardButton("Нежные оттенки")
        btn5 = types.InlineKeyboardButton("Яркие цвета")
        markup.add(btn4, btn5)
        bot.send_message(message.chat.id, text="Какой оттенок предпочитаешь?".format(message.from_user),
                         reply_markup=markup)
    elif message.text == "Свадебные букеты":
        w = random.randint(0, len(wedding)-1)
        bot.send_message(message.chat.id, text=wedding[w])
    elif message.text == "Нежные оттенки":
        a = random.randint(0, len(soft_flowers)-1)
        bot.send_message(message.chat.id, text=soft_flowers[a])
    elif message.text == "Яркие цвета":
        b = random.randint(0, len(bright_flowers) - 1)
        bot.send_message(message.chat.id, text=bright_flowers[b])
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)

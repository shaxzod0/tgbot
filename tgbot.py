import index
from telebot import types
import telebot

bot = telebot.TeleBot(index.API_TOKEN)

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_address = types.KeyboardButton('Menu', request_location=True)
btn_payment = types.KeyboardButton('Способ оплаты')
btn_store = types.KeyboardButton('Карзинка')
btn_salad = types.KeyboardButton('Салады')
btn_barbeque = types.KeyboardButton('Шашлыки')
btn_fish = types.KeyboardButton('Рыба')
btn_soup = types.KeyboardButton('Супы')
btn_bear = types.KeyboardButton('Пива')
markup_menu.add(btn_address, btn_payment, btn_barbeque,btn_bear,btn_fish,btn_fish,btn_salad,btn_soup,btn_store) 
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,'Hello asalka', reply_markup=markup_menu)

@bot.message_handler(func=lambda message: True) 
def echo_all(message):
    bot.reply_to(message,message.text, reply_markup=markup_menu)

bot.polling()
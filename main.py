import telebot
from telebot import types
from googletrans import Translator
from langdetect  import detect

bot = telebot.TeleBot('6112929182:AAGsju_kijZ-Vmeg7y6-k4Z9k1Rt-1dZsgE')
translator = Translator()

@bot.message_handler(commands=['start'])
def rhe(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('перейти',url='https://t.me/+NXOSq2yDSvYyMjNi'))
    bot.send_message(message.chat.id,'для начало подпишитесь на канал и введите код',reply_markup=markup)

@bot.message_handler()
def translate_message(message):
     src = detect(message.text)

     dest = 'en'

     translated_text = translator.translate(message.text, src=src, dest=dest).text

     bot.send_message(message.chat.id,translated_text)

@bot.message_handler()
def uiv(message):
    if message.text.lower() == '1423':
        bot.send_message(message.chat.id,'введите текст для перевода')








bot.polling()
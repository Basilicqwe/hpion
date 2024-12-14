import telebot
from config import *
from telebot import types

bot = telebot.TeleBot(token)

info=[]

@bot.message_handler(func=lambda message: True)
def getmessage(message):
    info.append(message.chat.id)
    info.append(message.chat.type)
    info.append(message.chat.title)
    info.append(message.from_user.username)
    info.append(message.from_user.first_name)
    info.append(message.from_user.last_name)
    info.append(message.text)
    print (info)
bot.infinity_polling()
    
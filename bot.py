import sqlite3
import telebot
from config1 import *
from telebot import types
from logic import *
import datetime

bot = telebot.TeleBot(token)



def convert_seconds(seconds):
    # Определяем количество секунд в различных временных единицах
    seconds_in_minute = 60
    seconds_in_hour = 3600
    seconds_in_day = 86400
    seconds_in_month = 2592000  # Приблизительное значение для месяца (30 дней)
    seconds_in_year = 31536000   # Приблизительное значение для года (365 дней)

    years = seconds // seconds_in_year
    seconds %= seconds_in_year

    months = seconds // seconds_in_month
    seconds %= seconds_in_month

    days = seconds // seconds_in_day
    seconds %= seconds_in_day

    hours = seconds // seconds_in_hour
    seconds %= seconds_in_hour

    minutes = seconds // seconds_in_minute
    seconds %= seconds_in_minute

    return years, months, days, hours, minutes, seconds
# 2094384000+10368000+1641600+message.date
info=[]

@bot.message_handler(commands=['start'])
def user(message):
    bot.send_message(message.chat.id, 'Здравствуйте! я-бот, который будет отправлять вам все сообщения из нужного вам чата, но для этого мне нужен ваш chat.id(уже есть)))) и права администратора в группе. Как только у меня будут все необходимые данные, вы сразу начнёте получать все сообщения!')
    global userid
    userid = message.chat.id

@bot.message_handler(func=lambda message: True)
def getmessage(message):
    info=[]
    info.append(message.chat.id)
    info.append(datetime.datetime.now())
    info.append(message.location)
    info.append(message.chat.type)
    info.append(message.chat.title)
    info.append(message.from_user.username)
    info.append(message.from_user.first_name)
    info.append(message.from_user.last_name)
    info.append(message.text)
    print (info)

    db.new_info(tuple(info))

    bot.send_message(userid,f"{info}")
    b=input('Вы хотите ответить?\n')
    if b=='да':
        while True:
            d=input("вводите\n")
            if d=="всё":
                break
            else:
                bot.send_message(message.chat.id, d)
    else:
        pass

    # f = open('xyzz.txt','w') 
    # f.write(str(info))
    # f.close() 

    # bot.send_message(5361711060,f"{info}")


db=DB_Manager("data.db")
db.create_tables()

bot.infinity_polling()       
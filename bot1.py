import telebot
from config import token

bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda message: True)
def start_message(message):
    print(message)
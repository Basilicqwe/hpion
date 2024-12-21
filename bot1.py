import telebot
from config import token

bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda message: True)
def handle_message(message, сommands=['Коля']):
    print(message.text, message.chat.id)
    bot.send_message(message.chat.id, input())
    global i
    i=message.chat.id
    f = open('xyzz.txt','w') 
    f.write(str(i))
    f.close() 
bot.infinity_polling()
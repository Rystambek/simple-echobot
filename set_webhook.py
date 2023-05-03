from telegram import Bot
import os

TOKEN = '6004154698:AAEo2pZT8WqoCqRGAXZchoYMtdgozcq3Kbc'

bot = Bot(TOKEN)

url = 'https://echobotrustambek.pythonanywhere.com/bot'

# print(bot.set_webhook(url))
print(bot.get_webhook_info())
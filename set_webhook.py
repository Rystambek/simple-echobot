from telegram import Bot
import os

TOKEN = '6162217632:AAEnncQeDNHOnSCAlMw0PTxbkJpAQQdL2X4'

bot = Bot(TOKEN)

url = 'https://echobotrustambek.pythonanywhere.com/bot'

# print(bot.set_webhook(url))
print(bot.get_webhook_info())
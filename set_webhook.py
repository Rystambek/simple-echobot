from telegram import Bot
import os

TOKEN = '5790746885:AAFJusXWRH3yN5CJ9hjKcmHyrzmHVv5A_vY'

bot = Bot(TOKEN)

url = 'https://echobotrustambek.pythonanywhere.com/bot'

print(bot.set_webhook(url))
# print(bot.delete_webhook())
print(bot.get_webhook_info())
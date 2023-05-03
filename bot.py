from telegram.ext import Updater, CommandHandler,Filters
import os

from main import start,msg

TOKEN = os.environ.get('TOKEN')

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.dispatcher.add_handler(CommandHandler('start', start))
    dp.dispatcher.add_handler(Filters.update,msg)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

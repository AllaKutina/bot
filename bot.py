from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import ephem

from datetime import datetime, date

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = "Ну привет"
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def get_constellation(bot, update):
    user_text = update.message.text
    planet = user_text.split(' ')[1]
    today = date.today()
    now = '{}/{}/{}'.format(today.year, today.month, today.day)

    planet = getattr(ephem, planet.capitalize(), None)

    if planet:
        planet = planet(now)
        const = ephem.constellation(planet)
        result = ','.join(const)
        update.message.reply_text(result)
    else:
        update.message.reply_text('Я не знаю такой планеты')

def main():
    mybot = Updater('953569815:AAGuhJ4QyUdlc_75KLLMnrbieJ157TQtCCk', request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation))
    dp.add_handler(MessageHandler(Filters.text, get_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()
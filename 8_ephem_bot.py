"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters






def greet_user(update, context):
    text = 'Привет! Я бот, который разбирается в астрологии. Введи команду\n\n/planet "Название планеты на английском"'
    update.message.reply_text(text)




def planet_def(update, context):
    user_text = update.message.text.split()
    planet_name = user_text[1].capitalize()
    try:
        planet = getattr(ephem, planet_name)()
        planet.compute()
        constellation = ephem.constellation(planet)
        update.message.reply_text(f"Сегодня планета {planet_name} находится в созвездии {constellation[1]}")
    except AttributeError:
        update.message.reply_text(f"Я не знаю такой планеты: {planet_name}. Попробуйте ввести другую планету.")
        

        


def main():
    mybot = Updater("6544532825:AAG7TV26jeGrOeJydax8lxSOJfoB_9UIqVM", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_def))
    
    



    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

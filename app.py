import pandas as pd
import telebot
import webbrowser
from datetime import datetime
import os

FILENAME = "/data/todo.json" if "AMVERA" in os.environ else "todo.json"
bot = telebot.TeleBot('6600850602:AAGPhNvuwEbtw5UVsR0XozxwqRJCrxYJsnE')


@bot.message_handler(commands=['workers'])  # обработка команд
def start_message(message):
    """Функция для вывода информации о смене"""
    list_excel = pd.read_excel('change.xlsx')
    format_str = str(list_excel)
    delete_str = format_str.replace("Columns:", "").replace("Empty DataFrame", "").replace("[", "").replace("]",
                                                                                                            "").replace(
        "Index:", "")

    bot.send_message(message.chat.id,
                     "На смене ЖК Внуково и ЖК Новое Внуково:\n Сегодня" + delete_str.replace("00:00:00", ""))


@bot.message_handler(commands=['info'])  # обработка команд
def site(message):
    webbrowser.open(
        'https://docs.google.com/spreadsheets/d/1CZACkNb4rPtAyMfdkYNEU25QiwwUihB51IdrHJV4Wy4/edit#gid=441057524&range=B1')


@bot.message_handler(commands=['start'])  # обработка команд
def start_message(message):

    date = datetime.now()
    a = str(date)
    index_date = a[10:16]
    list_excel = pd.read_excel('change.xlsx')
    format_str = str(list_excel)
    delete_str = (format_str.replace("Columns:", "").replace
                  ("Empty DataFrame", "").replace("[", "").replace
                  ("]", "").replace("Index:", ""))
    print(delete_str)

    bot.send_message(message.chat.id, f'📅 Сегодня на смене {delete_str.replace("00:00:00", "")}\n'
                                      f'Время:{index_date}. '
                                      f' Добро пожаловать, ты находишься'
                                      f' в боте, который предоставляет информацию о количестве смен'
                                      f' и дежурных сотрудниках в ЖК Внуково и ЖК Новое Внуково и дополнительные возможности.\n\n'
                                      f'Нажмите /help - для получения справки по работе с ботом.')


@bot.message_handler(commands=['help'])  # обработка команд
def help(message):
    bot.send_message(message.chat.id,
                     """Информационный бот ЖК Внуково и ЖК Новое Внуково.
Ты можешь пользоваться данным ботом с помощью команд.
Выполните команду /start - для начала работы с ботом.

Другие команды:

✈ /sanpin - для получения информации о санитарных нормах обслуживания жителей.

✈ /phones - телефоны аварийный служб.

✈ /temp - температурный график работы тепловый сетей.

✈ /eng - информация об инженерном составе ЖК Внуково и ЖК Новое Внуково.

✈ «Кто на смене?» - для получения информации кто находится на на смене. """, parse_mode='html')


@bot.message_handler()
def info(message):
    list_excel = pd.read_excel('change.xlsx')
    format_str = str(list_excel)
    delete_str = (format_str.replace("Columns:", "").replace
                  ("Empty DataFrame", "").replace("[", "").replace
                  ("]", "").replace("Index:", ""))

    if message.text.lower() == 'кто на смене?' and 'КТО НА СМЕНЕ?' and 'Кто на смене?' or 'Доброе утро! Кто сегодня на смене?':
        bot.send_message(message.chat.id,
                         f'На смене сегодня {delete_str.replace("00:00:00", "")}\n')

    elif message.text.lower() == 'Доброе утро! Кто из мастеров сегодня на смене?':
        bot.send_message(message.chat.id,
                         f'На смене сегодня, {delete_str}', )

    else:
        bot.send_message(message.chat.id,
                         f'Неверная команда, пожалуйста проверьте, набранную вами команду')


bot.polling(none_stop=True)  # программа будет постоянно выполняться и не завершится

import telebot
import webbrowser

bot = telebot.TeleBot('6600850602:AAGPhNvuwEbtw5UVsR0XozxwqRJCrxYJsnE')


@bot.message_handler(commands=['site'])  # обработка команд
def site(message):
    webbrowser.open('https://hh.ru/applicant/resumes/view?resume=561759baff0982dd8c0039ed1f4c716f486278')


@bot.message_handler(commands=['start', 'hello'])  # обработка команд
def main(message):
    bot.send_message(message.chat.id, f'Добро пожаловать, {message.from_user.first_name}')


@bot.message_handler(commands=['help'])  # обработка команд
def main(message):
    bot.send_message(message.chat.id, '<b>Информация для пользования ботом</b>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Добро пожаловать, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID:{message.from_user.id}')
    elif message.text.lower() == 'салям':
        bot.send_message(message.chat.id, f'Исэнмесез, {message.from_user.first_name} хален ничек? ')
    elif message.text.lower() == 'яхшы':
        bot.send_message(message.chat.id, f'Кутагымны кашы, {message.from_user.first_name}')


    else:
        bot.send_message(message.chat.id, f'Неверная команда')


bot.polling(none_stop=True)  # программа будет постоянно выполняться и не завершится

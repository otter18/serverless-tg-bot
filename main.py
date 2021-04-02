#  Copyright (c) ChernV (@otter18), 2021.

import os
import random
import telebot

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))


# ---------------- dialog params ----------------
dialog = {
    'hello': {
        'in': ['/hello', 'привет', 'hello', 'hi', 'privet', 'hey'],
        'out': ['Приветствую', 'Здравствуйте', 'Привет!']
    },
    'how r u': {
        'in': ['/howru', 'как дела', 'как ты', 'how are you', 'дела', 'how is it going'],
        'out': ['Хорошо', 'Отлично', 'Good. And how are u?']
    },
    'name': {
        'in': ['/name', 'зовут', 'name', 'имя'],
        'out': [
            'Я telegram-template-bot',
            'Я бот шаблон, но ты можешь звать меня в свой проект',
            'Это секрет. Используй команду /help, чтобы узнать'
        ]
    }
}


# --------------------- bot ---------------------
@bot.message_handler(commands=['help', 'start'])
def say_welcome(message):
    bot.send_message(message.chat.id,
                     'Hi, there! I am hosted by Yandex.Cloud Functions.\n'
                     'For more info click [here](https://github.com/otter18/serverless-tg-bot)',
                     parse_mode='markdown')


@bot.message_handler(func=lambda message: True)
def echo(message):
    for t, resp in dialog.items():
        if sum([e in message.text.lower() for e in resp['in']]):
            bot.send_message(message.chat.id, random.choice(resp['out']))
            return

    bot.send_message(message.chat.id, 'Seems wrong. Use /help to discover more')


# ---------------- local testing ----------------
if __name__ == '__main__':
    bot.infinity_polling()

import telebot
from main import bot


def handler(event, _):
    message = telebot.types.Update.de_json(event['data'])
    bot.process_new_updates([message])
    return {
        'statusCode': 200,
        'body': '!',
    }

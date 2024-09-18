import logging
import telebot
from telebot import types
from Variables import CHAT_ID, CHAT_ID2
import configparser

config = configparser.ConfigParser()
config.read('DATA.ini', encoding='utf-8')
TELEGRAM_BOT_TOKEN = config['TELEGRAM']['TELEGRAM_BOT_TOKEN']

CHAT_ID = '783897764'
CHAT_ID2 = '783897764'
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
# Конфигурация логгера
logging.basicConfig(filename='LOGS.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')


def send_message(formatted_message):
    logging.info(formatted_message)
    bot.send_message(CHAT_ID, formatted_message)
    if CHAT_ID2!= CHAT_ID:
        bot.send_message(CHAT_ID2, formatted_message)

def log_and_print(*messages):
    formatted_message = ' '.join(map(str, messages))
    if 'ошибка' in formatted_message or 'Ошибка' in formatted_message or 'Error' in formatted_message:
        logging.error(formatted_message)
        bot.send_message(CHAT_ID, formatted_message)
        if CHAT_ID2!= CHAT_ID:
            bot.send_message(CHAT_ID2, formatted_message)
    if 'Конец' in formatted_message:
        send_message(formatted_message)
    if 'Запуск' in formatted_message:
        send_message(formatted_message)
    if 'Всего успешно обработано файлов GPT:' in formatted_message:
        print(formatted_message)
        send_message(formatted_message)
    if "Первый найден" in formatted_message:
        send_message(formatted_message)
    if "Второй найден" in formatted_message:
        send_message(formatted_message)
    if "Пауза" in formatted_message:
        send_message(formatted_message)
    if "Снятие с паузы" in formatted_message:
        send_message(formatted_message)
    if "Завершение работы" in formatted_message:
        send_message(formatted_message)
    else:
        logging.info(formatted_message)
        print(formatted_message)

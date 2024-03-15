import logging

# Конфигурация логгера
logging.basicConfig(filename='LOGS.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

def log_and_print(*messages):
    formatted_message = ' '.join(map(str, messages))
    logging.info(formatted_message)  # Запись в файл журнала
    print(formatted_message)  # Вывод на консоль

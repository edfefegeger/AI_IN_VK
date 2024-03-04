def log_and_print(*messages):
    formatted_message = ' '.join(map(str, messages))
    print(formatted_message)
    with open("LOGS.log", 'a', encoding='utf-8') as f:
        f.write(formatted_message + '\n')
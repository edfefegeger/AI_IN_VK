import keyboard
from logger import log_and_print
Not_paused = False
paused = False
def toggle_pause():
    global paused
    paused = True
    global Not_paused
    Not_paused = False
    log_and_print("Нажато '-'")
def toggle_pause2():
    global paused
    paused = False
    global Not_paused
    Not_paused = True
    log_and_print("Нажато '+'")


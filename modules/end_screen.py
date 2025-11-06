import os
import keyboard
from .print_field import *
from .start_game import *

def end_screen(field, snake_body, prize_pos, last_key, score, message):
    """Екран закінчення"""    
    os.system('cls||clear')
    print_field(field, snake_body, prize_pos, last_key, score, message)
    print("\nНатисни G, щоб почати заново або ESC, щоб вийти.")
    keyboard.on_press_key("g", lambda _: start_game(), suppress=True)
    keyboard.wait("esc")
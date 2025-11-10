import os
import keyboard
from .print_field import *
from .start_game import *

def end_screen(field, snake_body, prize_pos, last_key, score, message):
    """Екран закінчення"""    
    os.system('cls||clear')
    print_field(field, snake_body, prize_pos, last_key, score, message)
    print("\nНатисни [G], щоб почати заново або [ESC], щоб вийти.")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'g':
                keyboard.unhook_all()                
                return start_game()
            elif event.name == "esc":            
                keyboard.unhook_all()
                return
        
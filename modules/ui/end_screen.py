import os
import keyboard
from modules.print_field import *

def end_screen(field, snake_body, prize_pos, last_key, score, message):
    """Екран закінчення"""    
    os.system('cls||clear')
    print_field(field, snake_body, prize_pos, last_key, score, message)
    print("\nНатисніть: [G] - щоб почати заново, [R] - для повернення в меню \n\n[ESC] - щоб вийти.")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'g':
                keyboard.unhook_all()  
                from .start_game import start_game              
                return start_game()
            elif event.name == "r":            
                keyboard.unhook_all()
                from .menu import menu
                return menu()
            elif event.name == "esc":            
                keyboard.unhook_all()
                return    
        
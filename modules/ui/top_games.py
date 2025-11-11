import keyboard
import os
from modules.utils import load_log_json

def top_games():
    """інтерфейс, де видно топ забігів"""
    os.system("cls||clear")
    
    print("-----ТОП РЕЗУЛЬТАТІВ-----")
    log = load_log_json()
    for record in log:
        print(record)
    
    print(f"\nНатисніть: [R] - щоб повернутись")  
    while True:        
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'r':
                keyboard.unhook_all()
                from modules.ui import menu
                return menu()
            
    
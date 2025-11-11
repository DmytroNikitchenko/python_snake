import keyboard
import os

def menu():
    """головне меню гри"""
    os.system("cls||clear")
    print(f"-----SNAKE-----")  
    print(f"Натисніть: \n[1] - щоб грати \n[2] - щоб відкрити магазин \n[3] - щоб подивитися топ результатів \n\n[ESC] - для виходу")  
    while True:        
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == '1':
                keyboard.unhook_all()
                from .start_game import start_game
                return start_game()
            elif event.name == '2':
                keyboard.unhook_all()
                from .color_shop import color_shop
                return color_shop()
            elif event.name == '3':
                keyboard.unhook_all()    
                from .top_games import top_games            
                return top_games()
            elif event.name == 'esc':
                return
import os
import keyboard
from .select_difficulty import *
from .color_shop import *

def start_game():  
    keyboard.unhook_all()
    os.system('cls||clear')
    time_interval = select_difficulty()
    width = int(input("Введіть ширину поля (не менше 3): "))
    heigth = int(input("Введіть висоту поля (не менше 3): "))
    
    print(f"Обрана складність: {time_interval}, поле розміром {width}x{heigth}\nНатисніть [1] щоб грати, натисність [2] щоб змінити параметри, або [3] щоб відкрити магазин")
    
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == '1':
                break
            elif event.name == '2':
                keyboard.unhook_all()
                return start_game()
            elif event.name == '3':
                color_shop()
                return start_game()

            
        
    from run import main
    return main(width, heigth, time_interval)  
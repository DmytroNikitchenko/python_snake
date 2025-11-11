# налаштування кольору
import os
import keyboard
from blessed import Terminal
import time
from modules.utils import *
from modules.game_logic import *

term = Terminal()

player = Snake()

COLOR_SHOP = {
    "green": 0,
    "yellow": 50,
    "magenta": 100,
    "cyan": 150,
    "white": 200,
    "red": 75,           
    "blue": 90,          
    "gray": 40,          
    "orange": 120,       
    "brown": 60,         
    "teal_gray": 130,    
    "indigo": 160,       
    "pink_red": 180,     
    "steel_blue": 110,   
    "olive": 70,         
    "beige": 140         
}

def color_shop():
    """інтерфейс магазину кольорів"""  

    os.system("cls||clear")
    print("---МАГАЗИН КОЛЬОРІВ---")   
    print("Натисніть: \n[1] - для відкриття покупки \n[2] - для перегляду свого гардеробу \n[3] - для виходу")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == '1':
                keyboard.unhook_all()
                return buy_color()
            elif event.name == '2': 
                keyboard.unhook_all()   
                return select_color()      
            elif event.name == '3':
                keyboard.unhook_all()
                from .menu import menu
                return menu()
    
def buy_color():
    """функція для відкриття інтерфейсу для покупки кольору"""  
    while True:
        os.system('cls||clear')
        
        print("-----МАГАЗИН КОЛЬОРІВ-----")
        
        for color, price in COLOR_SHOP.items():
            if color not in player.get_owned_colors():
                print(f"{color}: {price}")
        print(f"\nВаш рахунок: {player.get_money()}")
        
        selected = input("Оберіть колір для покупки (напишіть назву), або введіть [q] для повернення: ")
        if selected == "q":            
            return color_shop()
        elif selected not in COLOR_SHOP.keys():
            print("Введіть коректний колір!")
            time.sleep(1)
            os.system('cls||clear') 
            return color_shop()
        if player.get_money() < COLOR_SHOP[selected]:
            print("Недостатньо коштів!")
            time.sleep(1)
            os.system('cls||clear') 
            return color_shop()
        player.set_player_money(-COLOR_SHOP[selected])
        player.add_owned_color(selected)
        print("Успішна покупка!")
        time.sleep(1.5)
        return color_shop()
    
def select_color():     
    """функція для відкриття інтерфейсу для вибору кольору"""  
    
    while True:
        os.system("cls||clear")
        print("-----ГАРДЕРОБ-----")
        for color in player.get_owned_colors():
            print(color)
            markers = []
            if color == player.get_body_color():
                markers.append("[тіло] ")
            if color == player.get_head_color():
                markers.append("[голова] ")
            if markers:            
                print(term.move_up(1) + term.move_right(len(color) + 1) + "".join(markers))
                
        selected = input("Оберіть колір для вибору (напишіть назву), або введіть [q] для повернення: ")
        
        if selected == "q":            
            return color_shop()
        elif selected not in player.get_owned_colors():
            print("Введіть коректний колір!")
            time.sleep(1)
            os.system('cls||clear') 
            return color_shop()        
        
        print(f"Обрано колір: {selected}")
        
        while True:
            os.system('cls||clear')
            
            print("-----ГАРДЕРОБ-----")            
            print(f"Оберіть для якої частини змійки встановити колір [{selected}]: \n[1] - для голови \n[2] - для тіла \n[3] - для всього \n\n[R] - для повернення")
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == '1':
                    keyboard.unhook_all()
                    player.set_head_color(selected)                    
                    print(f"Колір [{selected}] встановлено для голови")                    
                    time.sleep(1.5)
                    return select_color()
                elif event.name == '2': 
                    keyboard.unhook_all()
                    player.set_body_color(selected)                    
                    print(f"Колір [{selected}] встановлено для тіла")
                    time.sleep(1.5)
                    return select_color()     
                elif event.name == '3':
                    keyboard.unhook_all()
                    player.set_head_color(selected)
                    player.set_body_color(selected)
                    print(f"Колір [{selected}] встановлено для всього")
                    time.sleep(1.5)
                    return select_color()    
                elif event.name == 'r':
                    keyboard.unhook_all()   
                    from .menu import menu
                    return menu()
# налаштування кольору
import os
import keyboard
from blessed import Terminal
import time
from .utils import *
from .game_logic import *

term = Terminal()

#player = Snake()

COLOR_SHOP = {
    "green": 0,
    "yellow": 50,
    "magenta": 100,
    "cyan": 150,
    "white": 200
}

def color_shop():
    os.system("cls||clear")
    print("---МАГАЗИН КОЛЬОРІВ---")   
    print("Натисніть [1] для відкриття покупки, або [2] для перегляду свого гардеробу")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == '1':
                buy_color()
            elif event.name == '2':    
                select_color()      
    
def buy_color():
    player = load_player_data()
    for color, price in COLOR_SHOP.items():
        if color not in player["owned_color"]:
            print(f"{color}: {price}")
    print(f"Ваш рахунок: {player["money"]}")
         
    while True:
        selected = input("Оберіть колір для покупки (напишіть назву), або введіть [q] для повернення: ")
        if selected == "q":            
            return color_shop()
        elif selected not in COLOR_SHOP.keys():
            print("Введіть коректний колір!")
            time.sleep(1)
            os.system('cls||clear') 
            return color_shop()
        if player["money"] < COLOR_SHOP[selected]:
            print("Недостатньо коштів!")
            time.sleep(1)
            os.system('cls||clear') 
            return color_shop()
        player["money"] -= COLOR_SHOP[selected]
        player["owned_color"].append(selected)
        save_player_data(player)
        print("Успішна покупка!")
        time.sleep(1.5)
        return color_shop()
    
def select_color():
    player = load_player_data()
    for color in player["owned_color"]:
        print(color)
        markers = []
        if "term."+color == player["snake_color"]:
            markers.append("[тіло] ")
        if "term."+color == player["head_color"]:
            markers.append("[голова] ")
        if markers:            
            print(term.move_up(1) + term.move_right(len(color) + 1) + "".join(markers))

    while True:
        selected = input("Оберіть колір для вибору (напишіть назву), або введіть [q] для повернення: ")
        if selected == "q":            
            return color_shop()
        elif selected not in player["owned_color"]:
            print("Введіть коректний колір!")
            time.sleep(1)
            os.system('cls||clear') 
            return color_shop()        
        player["money"] -= COLOR_SHOP[selected]
        player["owned_color"].append(selected)
        save_player_data(player)
        print("Успішна покупка!")
        time.sleep(1.5)
        return color_shop()
    


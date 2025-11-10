# налаштування кольору
import os
import keyboard
from blessed import Terminal
import time
from .utils import *
from .game_logic import *

term = Terminal()

player = Snake()

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
    for color, price in COLOR_SHOP.items():
        if color not in player.get_owned_colors():
            print(f"{color}: {price}")
    print(f"Ваш рахунок: {player.get_money()}")
         
    while True:
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
    for color in player.get_owned_colors():
        print(color)
        markers = []
        if "term."+color == player.get_body_color():
            markers.append("[тіло] ")
        if "term."+color == player.get_head_color():
            markers.append("[голова] ")
        if markers:            
            print(term.move_up(1) + term.move_right(len(color) + 1) + "".join(markers))

    while True:
        selected = input("Оберіть колір для вибору (напишіть назву), або введіть [q] для повернення: ")
        if selected == "q":            
            return color_shop()
        elif selected not in player.get_owned_colors():
            print("Введіть коректний колір!")
            time.sleep(1)
            os.system('cls||clear') 
            return color_shop()        
        player.set_player_money(-COLOR_SHOP[selected]) 
        player.add_owned_color(selected)
        print("Успішна покупка!")
        time.sleep(1.5)
        return color_shop()
    


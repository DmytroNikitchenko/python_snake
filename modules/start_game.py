import os
from .select_difficulty import *    

def start_game():
    os.system('cls||clear')
    time_interval = select_difficulty()
    width = int(input("Введіть ширину поля (не менше 3): "))
    heigth = int(input("Введіть висоту поля (не менше 3): "))
    
    from run import main
    return main(width, heigth, time_interval)  
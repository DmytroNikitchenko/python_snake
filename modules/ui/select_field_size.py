import os
import time

def select_field_size(width=10, height=10):
    os.system("cls||clear")
    print("-----НАЛАШТУВАННЯ РОЗМІРОСТІ ПОЛЯ-----")
    
    try:
        width = float(input("Введіть ширину поля (не менше 3): "))
        match width:
            case (w) if (w%1 is 0) | (w>=3):
                pass                   
            case _:
                print("Введіть коректне значення ширини!")
                time.sleep(1.5)
                return select_field_size() 
    except ValueError:
        print("Введіть коректне значення ширини!")
        time.sleep(1.5)
        return select_field_size()

    try:
        height = float(input("Введіть висоту поля (не менше 3): "))
        match height:        
            case (h) if (h%1 is 0) | (h>=3):            
                pass
            case _:
                print("Введіть коректне значення висоти!")
                time.sleep(1.5)
                return select_field_size()
    except ValueError:
        print("Введіть коректне значення ширини!")
        time.sleep(1.5)
        return select_field_size()   
        
    return int(width), int(height)
            
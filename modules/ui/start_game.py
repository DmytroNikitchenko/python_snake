import os
import keyboard

def start_game():
    """налаштування складності гри"""       
    os.system('cls||clear')
    print("-----НАЛАШТУВАННЯ ГРИ-----")
    keyboard.unhook_all()
    from .select_time_interval import select_time_interval
    time_interval = select_time_interval()
    
    from .select_field_size import select_field_size
    width, height = select_field_size()
    
    
    print(f"Обрана складність: {time_interval}, поле розміром {width}x{height}\nНатисніть [1] щоб грати, натисність [2] щоб змінити параметри")  
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == '1':
                keyboard.unhook_all()
                break
            elif event.name == '2':
                keyboard.unhook_all()
                return start_game()    
                    
    from run import main   
    return main(width, height, time_interval)
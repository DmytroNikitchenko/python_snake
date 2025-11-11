import os

def select_time_interval():
    """налаштування інтервалу"""
    difficulties = {"1":"легко \t(0.5с)", "2":"середньо \t(0.35с)", "3":"важко \t(0.20с)", "4":"налаштувати самому"}
    
    for mode_num in difficulties:
        print(f"{mode_num}: {difficulties[mode_num]}")
    selected = input("Оберіть складність: ")
    match selected:
        case "1" | "легко" | "0.5с" | "0.5":
            return 0.5
        case "2" | "середньо" | "0.35с" | "0.35":
            return 0.35
        case "3" | "важко" | "0.20с" | "0.25": 
            return 0.2
        case "4" | "налаштувати самому":
            time_interval = (input("Введіть інтервал переміщень змійки в секундах (наприклад 0.25): "))
            try:
                if float(time_interval)<=0:
                    raise Exception
                return float(time_interval.replace(",","."))                     
            except:
                os.system('cls||clear')
                print("-----НАЛАШТУВАННЯ ГРИ-----")
                print("Оберіть коректну складність:")
                return select_time_interval()
        case _:
            os.system('cls||clear')
            print("-----НАЛАШТУВАННЯ ГРИ-----")
            print("Оберіть складність з перелічених:")
            return select_time_interval()
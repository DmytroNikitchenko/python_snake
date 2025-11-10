import keyboard
import time
import random
from modules import *

#  глобальні змінні
score = 0        # рахунок гравця
game_over = False

last_key = "d"   # напрямок глобальний
        
# рух гравця
def move_player(player_pos, direction, field, snake_body):
    """Рухає гравця і перевіряє межі поля"""
    global game_over # Потрібно, щоб завершити гру при зіткненні
    y, x = player_pos
    new_head = [y, x]

    if direction == "w":
        new_head[0] -= 1
    elif direction == "s":
        new_head[0] += 1
    elif direction == "a":
        new_head[1] -= 1
    elif direction == "d":
        new_head[1] += 1

    # Перевірка на стіну
    if field[new_head[0]][new_head[1]] == "█":
        game_over = True
        return player_pos # Повертаємо стару позицію, щоб гравець не зайшов у стіну
    
    if new_head in snake_body:
        game_over = True
        return player_pos
    
    snake_body.insert(0, new_head)    
    
    return new_head

def on_key_press(event):
    """Обробник натискання клавіш. Змінює напрямок руху."""
    global last_key, game_over
    key = event.name
    
    if key == "w" and last_key != "s":
        last_key = "w"
    elif key == "s" and last_key != "w":
        last_key = "s"
    elif key == "a" and last_key != "d":
        last_key = "a"
    elif key == "d" and last_key != "a":
        last_key = "d"
    elif key == "q":
        game_over = True

# основна функція 
def main(width, height, time_interval):
    global score, game_over, last_key    
    field = create_field(width, height)
    
    snake_body = [[(height//2)-1, (width//2)-1]]
    player_pos = snake_body[0]
    
    prize_pos = [random.randint(1, height - 2), random.randint(1, width - 2)]
    while prize_pos in snake_body: # Перевірка, чи приз не з'явився на будь-якій частині тіла
        prize_pos = [random.randint(1, height - 2), random.randint(1, width - 2)]
            
    is_win = False #  true/false для визначення перемоги

    def new_prize():
        nonlocal prize_pos        
        prize_pos = [random.randint(1, height - 2), random.randint(1, width - 2)]
        while prize_pos in snake_body: # Перевірка, чи приз не з'явився на будь-якій частині тіла
            prize_pos = [random.randint(1, height - 2), random.randint(1, width - 2)]

    keyboard.on_press(on_key_press, suppress=True)
    with term.fullscreen():
        while not game_over:
            # відображення 
            message = ""
            if 0 < score < 100:
                message = "Ранг: 🟢 Початківець"
            elif 100 <= score < 200:
                message = "Ранг: 🟠 Досвідчений"
            elif score >= 200:
                message = "Ранг: 🏆 Майстер"
            
            print_field(field, snake_body, prize_pos, last_key, score, message)
            
            #  затримка 
            time.sleep(time_interval)

            # оновлення  
            player_pos = move_player(player_pos, last_key, field, snake_body)

            if game_over: # якщо move_player завершив гру - виходимо з циклу
                break

            if player_pos == prize_pos:
                score += 10
                new_prize()
            else:
                if len(snake_body)>1:                
                    snake_body.pop()

            if score >= ((width-2) * (height-2))*10:
                is_win = True
                game_over = True # завершуємо гру перемогою
        final_message = ""
        if is_win:
            final_message = "🎊 ПЕРЕМОГА! 🎊"
        else:
            final_message = "💥 ПРОГРАШ 💥"       
        
        save_result_to_file(score, width, height, time_interval)
        keyboard.unhook_all()
    end_screen(field, snake_body, prize_pos, last_key, score, message + "\n" + final_message)

# запуск
if __name__ == "__main__":
    start_game()   
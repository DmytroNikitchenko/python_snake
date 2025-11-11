from blessed import Terminal
from .game_logic import *
term = Terminal()

COLOR_MAP = {
    "green": term.green,
    "yellow": term.yellow,
    "magenta": term.magenta,
    "cyan": term.cyan,
    "white": term.white
}

PRIZE_COLOR = term.red
WALL_COLOR = term.black


def print_field(field, snake_body, prize_pos, last_key, score, message="", is_mega_food = False):
    """Виводить поле на екран"""    
    player = Snake()
    SNAKE_COLOR = COLOR_MAP[f"{player.get_body_color()}"]
    HEAD_COLOR = COLOR_MAP[f"{player.get_head_color()}"]    

    display_field = [list(row) for row in field]
         
    for y, row in enumerate(display_field):
        for x, char in enumerate(row):
            if char == "█":
                display_field[y][x] = WALL_COLOR("█")
         
    py, px = snake_body[0]
    
    match last_key:
        case "w":
            display_field[py][px] = HEAD_COLOR("↑")
        case "a":
            display_field[py][px] = HEAD_COLOR("←")
        case "s":
            display_field[py][px] = HEAD_COLOR("↓")
        case "d":
            display_field[py][px] = HEAD_COLOR("→")
               
    ry, rx = prize_pos
    
    if is_mega_food:
        display_field[ry][rx] = term.green("*")
    else:
        display_field[ry][rx] = PRIZE_COLOR("*")
    
    for part_y, part_x in snake_body[1:]: # з другого елемента
        display_field[part_y][part_x] = SNAKE_COLOR + ("O")
        
    
    print(term.home, end="")

    output = []
    
    for row in display_field:
        output.append("".join(row))
    
    print() 
    print('\n'.join(output)) # друк поля 
    
    
    print(f"Score: {score}\n")
    if message:
        print(term.clear_eol, end="")  # очищує поточний рядок
        print(message)
"""обробник термінальної графіки"""

from typing import List, Tuple
from blessed import Terminal
from .entities.snake import Snake
from .entities.food import Food
from .entities.mega_apple import MegaApple
from .field import Field


class Renderer:
    """обробник термінальної графіки"""

    COLOR_MAP = {
        "green": None,  # встановлення в ініт
        "yellow": None,
        "magenta": None,
        "cyan": None,
        "white": None,
        "red": None,
        "blue": None,
        "gray": None,
        "orange": None,
        "brown": None,
        "teal_gray": None,
        "indigo": None,
        "pink_red": None,
        "steel_blue": None,
        "olive": None,
        "beige": None
    }

    def __init__(self):
        """ініт"""
        self.term = Terminal()

        self.COLOR_MAP = {
            "green": self.term.green,
            "yellow": self.term.yellow,
            "magenta": self.term.magenta,
            "cyan": self.term.cyan,
            "white": self.term.white,
            "red": self.term.red,
            "blue": self.term.blue,
            "gray": self.term.gray,
            "orange": self.term.color(208),
            "brown": self.term.color(94),
            "teal_gray": self.term.color(37),
            "indigo": self.term.color(54),
            "pink_red": self.term.color(197),
            "steel_blue": self.term.color(67),
            "olive": self.term.color(100),
            "beige": self.term.color(181)
        }

    def render_field(
        self,
        field: Field,
        snake: Snake,
        food: Food,
        score: int,
        message: str = "",
        head_color: str = "green",
        body_color: str = "green"
    ):        
        snake_color = self.COLOR_MAP.get(body_color, self.term.green)
        head_col = self.COLOR_MAP.get(head_color, self.term.green)

        # колір яблука
        if isinstance(food, MegaApple):
            food_color = self.term.green
        else:
            food_color = self.term.red

        # створення поля
        display_field = []
        for y in range(field.height):
            row = []
            for x in range(field.width):
                pos = (y, x)
                
                char = field.get_cell_char(pos)
                                
                if char == "O":
                    row.append(self.term.bold_cyan(char))
                elif char == "#":
                    row.append(self.term.black(char))
                else:
                    row.append(char)
            display_field.append(row)

        # голова змійки
        head_y, head_x = snake.head
        display_field[head_y][head_x] = head_col(snake.render_char())

        # тіло змійки
        for body_y, body_x in snake.get_body_segments():
            display_field[body_y][body_x] = snake_color("O")

        # відображеня яблук
        food_y, food_x = food.position
        display_field[food_y][food_x] = food_color(food.render_char())

        # Print to terminal
        print(self.term.home, end="")
        print()
        for row in display_field:
            print("".join(row))

        print(f"Score: {score}\n")
        if message:
            print(self.term.clear_eol, end="")
            print(message)

    def clear_screen(self):
        """Clear the terminal screen."""
        print(self.term.clear())

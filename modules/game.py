"""головний клас гри"""

import time
import random
import keyboard
from typing import Optional
from .field import Field
from .entities.snake import Snake
from .entities.apple import Apple
from .entities.mega_apple import MegaApple
from .entities.food import Food
from .renderer import Renderer
from .player import Player
from .data_manager import DataManager


class Game:
    """головний клас гри"""

    def __init__(self, width: int, height: int, time_interval: float, obstacle_count: int = 0, game_mode: str = "classic"):
        """ініт"""
        self.width = width
        self.height = height
        self.time_interval = time_interval
        self.obstacle_count = obstacle_count
        self.game_mode = game_mode

        self.field = Field(width, height, game_mode)
        self.renderer = Renderer()
        self.player = Player()

        self.snake: Optional[Snake] = None
        self.food: Optional[Food] = None

        self.score = 0
        self.game_over = False
        self.is_win = False
        self.count_of_eaten = 0

    def setup_game(self):
        """ініт сутностей і станів"""
        # ресет значень
        self.score = 0
        self.game_over = False
        self.is_win = False
        self.count_of_eaten = 0

        # змійка в центрі поля
        initial_pos = ((self.height // 2) - 1, (self.width // 2) - 1)
        self.snake = Snake(initial_pos, initial_direction="d")

        # додавання перешод, не зачіпаючи гравця
        if self.obstacle_count > 0:
            self.field.add_random_obstacles(self.obstacle_count, [initial_pos])

        # спавн стартового яблука
        self.spawn_food()

    def spawn_food(self):
        """спавн яблука (10% шанс на мега яблуко)."""
        occupied = self.snake.body if self.snake else []
        position = self.field.get_random_empty_position(occupied)

        # 10% шанс на мега яблуко
        if random.random() < 0.10:
            self.food = MegaApple(position)
        else:
            self.food = Apple(position)

    def handle_input(self, key: str):
        """обробка інпутів"""
        key_map = {
            "ц": "w",
            "і": "s",
            "ф": "a",
            "в": "d",
            "й": "q"
        }
        key = key_map.get(key, key)

        # екстренний вихід
        if key == "q":
            self.game_over = True
            return

        # апдейт напряму
        if key in ["w", "s", "a", "d"]:
            self.snake.direction = key

    def check_collisions(self) -> bool:
        """перевірка на зіткнення"""
        head = self.snake.head

        # перевірка на зіткнення зі стіною
        if self.field.is_wall(head):
            self.game_over = True
            return False

        # перевірка на зіткнення з собою
        if self.snake.check_self_collision():
            self.game_over = True
            return False

        # перевірка на їжу
        if head == self.food.position:
            self.score += self.food.score_value
            self.snake.grow(self.food.growth_value)
            self.count_of_eaten += 1
            self.spawn_food()

        # перевірка на перемогу
        max_score = ((self.width - 2) * (self.height - 2)) * 10 - 10
        if self.score >= max_score:
            self.is_win = True
            self.game_over = True
            return False

        return True

    def update(self):
        """оновлення гри (1 тік)"""
        if not self.game_over:
            self.snake.move()

            # керування телепортацією
            if self.game_mode == "teleport" and self.field.is_teleport_hole(self.snake.head):
                exit_pos = self.field.get_teleport_exit(self.snake.head)
                if exit_pos:
                    # телепорт голови змійки на точку виходу
                    self.snake._body[0] = exit_pos
                    self.snake._position = exit_pos

            self.check_collisions()

    def render(self):
        """малювання поля відповідно до поточних налаштувань"""
        # оновлення даних про гравця
        self.player.refresh()

        message = Player.get_rank_message(self.score)
        self.renderer.render_field(
            self.field,
            self.snake,
            self.food,
            self.score,
            message,
            self.player.get_head_color(),
            self.player.get_body_color()
        )

    def run(self) -> dict:
        """головна функція гри"""
        self.setup_game()

        # обробник натискань
        def on_key_press(event):
            self.handle_input(event.name)

        keyboard.on_press(on_key_press, suppress=True)

        # головний цикл гри
        with self.renderer.term.fullscreen():
            while not self.game_over:
                self.render()
                time.sleep(self.time_interval)
                self.update()

        # кінець захоплення клавіатури
        keyboard.unhook_all()

        # збереження результатів
        DataManager.save_game_log(self.score, self.width, self.height, self.time_interval)
        self.player.set_player_money(self.score / 5)

        # повернення результату гри
        return {
            "score": self.score,
            "is_win": self.is_win,
            "count_of_eaten": self.count_of_eaten,
            "money_earned": self.score / 5
        }

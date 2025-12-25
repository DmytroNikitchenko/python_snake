"""управління всіма екранами UI"""

import os
import time
import keyboard
from typing import Tuple, Optional
from blessed import Terminal
from .game import Game
from .player import Player
from .data_manager import DataManager


class UIManager:
    """управління всіма екранами UI"""

    COLOR_SHOP = {
        "green": 0,
        "yellow": 50,
        "magenta": 100,
        "cyan": 150,
        "white": 200,
        "red": 75,
        "blue": 90,
        "gray": 40,
        "orange": 120,
        "brown": 60,
        "teal_gray": 130,
        "indigo": 160,
        "pink_red": 180,
        "steel_blue": 110,
        "olive": 70,
        "beige": 140
    }

    def __init__(self):
        """ініціалізація"""
        self.term = Terminal()
        self.player = Player()

    def start(self):
        """стартова точка гри"""
        self.show_menu()

    def clear_screen(self):
        """очистка терміналу"""
        os.system("cls||clear")

    def show_menu(self):
        """відображення головного меню"""
        self.clear_screen()
        print("-----SNAKE-----")
        print("Натисніть: \n[1] - щоб грати \n[2] - щоб відкрити магазин \n[3] - щоб подивитися топ результатів \n\n[ESC] - для виходу")

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                keyboard.unhook_all()
                if event.name == '1':
                    self.show_start_game()
                    return
                elif event.name == '2':
                    self.show_color_shop()
                    return
                elif event.name == '3':
                    self.show_top_games()
                    return
                elif event.name == 'esc':
                    return

    def show_start_game(self):
        """екран налаштувань гри"""
        self.clear_screen()
        print("-----НАЛАШТУВАННЯ ГРИ-----")

        game_mode = self.select_game_mode()
        time_interval = self.select_time_interval()
        width, height = self.select_field_size()
        obstacle_count = self.select_obstacle_count(width, height)

        mode_text = "Телепорти" if game_mode == "teleport" else "Класичний"
        self.clear_screen()
        print(f"Режим: {mode_text}, Складність: {time_interval}, поле {width}x{height}, перешкод: {obstacle_count}\nНатисніть [1] щоб грати, [2] щоб змінити параметри")

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                keyboard.unhook_all()
                if event.name == '1':
                    result = self.run_game(width, height, time_interval, obstacle_count, game_mode)
                    
                    self.player.refresh()
                    
                    self.show_end_screen(result)
                    return
                elif event.name == '2':
                    self.show_start_game()
                    return

    def select_game_mode(self) -> str:
        """обирання складності гри"""
        self.clear_screen()
        print("-----ВИБІР РЕЖИМУ ГРИ-----")
        print("[1] - Класичний режим (стандартні стіни)")
        print("[2] - Режим телепортів (стіни з отворами-порталами)")

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                keyboard.unhook_all()
                if event.name == '1':
                    return "classic"
                elif event.name == '2':
                    return "teleport"

    def select_time_interval(self) -> float:
        """встановлення інтервалу між тіками"""
        self.clear_screen()
        print("---Налаштування складності---")
        difficulties = {
            "1": "легко \t(0.5с)",
            "2": "середньо \t(0.35с)",
            "3": "важко \t(0.20с)",
            "4": "налаштувати самому"
        }

        for mode_num in difficulties:
            print(f"{mode_num}: {difficulties[mode_num]}")

        selected = input("Оберіть складність: ")

        if selected in ["1", "легко", "0.5с", "0.5"]:
            return 0.5
        elif selected in ["2", "середньо", "0.35с", "0.35"]:
            return 0.35
        elif selected in ["3", "важко", "0.20с", "0.25"]:
            return 0.2
        elif selected in ["4", "налаштувати самому"]:
            time_interval = input("Введіть інтервал переміщень змійки в секундах (наприклад 0.25): ")
            try:
                interval = float(time_interval.replace(",", "."))
                if interval <= 0:
                    raise ValueError
                return interval
            except:
                self.clear_screen()
                print("-----НАЛАШТУВАННЯ ГРИ-----")
                print("Оберіть коректну складність:")
                return self.select_time_interval()
        else:
            self.clear_screen()
            print("-----НАЛАШТУВАННЯ ГРИ-----")
            print("Оберіть складність з перелічених:")
            return self.select_time_interval()

    def select_field_size(self) -> Tuple[int, int]:
        """встановлення розміру поля"""
        self.clear_screen()
        print("-----НАЛАШТУВАННЯ РОЗМІРОСТІ ПОЛЯ-----")

        try:
            width = float(input("Введіть ширину поля (не менше 3): "))
            if width % 1 == 0 and width >= 3:
                width = int(width)
            else:
                print("Введіть коректне значення ширини!")
                time.sleep(1.5)
                return self.select_field_size()
        except:
            print("Введіть коректне значення ширини!")
            time.sleep(1.5)
            return self.select_field_size()

        try:
            height = float(input("Введіть висоту поля (не менше 3): "))
            if height % 1 == 0 and height >= 3:
                height = int(height)
            else:
                print("Введіть коректне значення висоти!")
                time.sleep(1.5)
                return self.select_field_size()
        except:
            print("Введіть коректне значення висоти!")
            time.sleep(1.5)
            return self.select_field_size()

        return width, height

    def select_obstacle_count(self, width: int, height: int) -> int:
        """встановлення кількості рандомних перешкод"""
        self.clear_screen()
        print("-----НАЛАШТУВАННЯ ПЕРЕШКОД-----")

        # Calculate max obstacles (10% of playable area)
        playable_area = (width - 2) * (height - 2)
        max_obstacles = int(playable_area * 0.1)

        print(f"Поле {width}x{height} має {playable_area} вільних клітинок")
        print(f"Максимум перешкод: {max_obstacles} (10% площі)")

        try:
            obstacle_count = int(input(f"Введіть кількість перешкод (0-{max_obstacles}): "))
            if 0 <= obstacle_count <= max_obstacles:
                return obstacle_count
            else:
                print(f"Введіть значення від 0 до {max_obstacles}!")
                time.sleep(1.5)
                return self.select_obstacle_count(width, height)
        except:
            print("Введіть коректне число!")
            time.sleep(1.5)
            return self.select_obstacle_count(width, height)

    def run_game(self, width: int, height: int, time_interval: float, obstacle_count: int = 0, game_mode: str = "classic") -> dict:
        """створення гри та її запуск"""
        game = Game(width, height, time_interval, obstacle_count, game_mode)
        return game.run()

    def show_end_screen(self, result: dict):
        """відображення екрану в кінці гри"""
        self.clear_screen()

        if result["is_win"]:
            final_message = "🎊 ПЕРЕМОГА! 🎊"
        else:
            final_message = "💥 ПРОГРАШ 💥"

        print(f"Score: {result['score']}")
        print(f"Яблук з'їдено: {result['count_of_eaten']}")
        print(f"Монеток зароблено: {result['money_earned']}")
        print(final_message)
        print("\nНатисніть: [G] - щоб почати заново, [R] - для повернення в меню \n\n[ESC] - щоб вийти.")

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                keyboard.unhook_all()
                if event.name == 'g':
                    self.show_start_game()
                    return
                elif event.name == "r":
                    self.show_menu()
                    return
                elif event.name == "esc":
                    return

    def show_color_shop(self):
        """UI магазину кольорів"""
        self.clear_screen()
        print("---МАГАЗИН КОЛЬОРІВ---")
        print("Натисніть: \n[1] - для відкриття покупки \n[2] - для перегляду свого гардеробу \n[3] - для виходу")

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                keyboard.unhook_all()
                if event.name == '1':
                    self.show_buy_color()
                    return
                elif event.name == '2':
                    self.show_select_color()
                    return
                elif event.name == '3':
                    self.show_menu()
                    return

    def show_buy_color(self):
        """дисплей покупки в магазині"""
        self.clear_screen()
        print("-----МАГАЗИН КОЛЬОРІВ-----")

        for color, price in self.COLOR_SHOP.items():
            if color not in self.player.get_owned_colors():
                print(f"{color}: {price}")

        print(f"\nВаш рахунок: {self.player.get_money()}")

        selected = input("Оберіть колір для покупки (напишіть назву), або введіть [q] для повернення: ")

        if selected == "q":
            self.show_color_shop()
            return
        elif selected not in self.COLOR_SHOP.keys():
            print("Введіть коректний колір!")
            time.sleep(1)
            self.show_color_shop()
            return

        if self.player.get_money() < self.COLOR_SHOP[selected]:
            print("Недостатньо коштів!")
            time.sleep(1)
            self.show_color_shop()
            return

        self.player.set_player_money(-self.COLOR_SHOP[selected])
        self.player.add_owned_color(selected)
        print("Успішна покупка!")
        time.sleep(1.5)
        self.show_color_shop()

    def show_select_color(self):
        """гардероб"""
        self.clear_screen()
        print("-----ГАРДЕРОБ-----")

        for color in self.player.get_owned_colors():
            print(color)
            markers = []
            if color == self.player.get_body_color():
                markers.append("[тіло] ")
            if color == self.player.get_head_color():
                markers.append("[голова] ")
            if markers:
                print(self.term.move_up(1) + self.term.move_right(len(color) + 1) + "".join(markers))

        selected = input("Оберіть колір для вибору (напишіть назву), або введіть [q] для повернення: ")

        if selected == "q":
            self.show_color_shop()
            return
        elif selected not in self.player.get_owned_colors():
            print("Введіть коректний колір!")
            time.sleep(1)
            self.show_color_shop()
            return

        print(f"Обрано колір: {selected}")
        self.show_apply_color(selected)

    def show_apply_color(self, color: str):
        """дисплей примінення кольору"""
        self.clear_screen()
        print("-----ГАРДЕРОБ-----")
        print(f"Оберіть для якої частини змійки встановити колір [{color}]: \n[1] - для голови \n[2] - для тіла \n[3] - для всього \n\n[R] - для повернення")

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                keyboard.unhook_all()
                if event.name == '1':
                    self.player.set_head_color(color)
                    print(f"Колір [{color}] встановлено для голови")
                    time.sleep(1.5)
                    self.show_select_color()
                    return
                elif event.name == '2':
                    self.player.set_body_color(color)
                    print(f"Колір [{color}] встановлено для тіла")
                    time.sleep(1.5)
                    self.show_select_color()
                    return
                elif event.name == '3':
                    self.player.set_head_color(color)
                    self.player.set_body_color(color)
                    print(f"Колір [{color}] встановлено для всього")
                    time.sleep(1.5)
                    self.show_select_color()
                    return
                elif event.name == 'r':
                    self.show_menu()
                    return

    def show_top_games(self):
        """дисплей топу забігів"""
        self.clear_screen()
        print("-----ТОП РЕЗУЛЬТАТІВ-----")
        
        log = DataManager.load_game_log()
        
        if not log:
            print("\nСписок ігор порожній.")
        else:
            header = f"{'#':<4} {'РАХУНОК':<10} {'ПОЛЕ':<10} {'ШВИДК.':<10} {'ДАТА':<20}"
            print(header)
            print() # Отступ

            for i, record in enumerate(log):
                rank = i + 1
                
                score = str(record.get("result", 0))
                size = f"{record.get('field_width', '?')}x{record.get('field_height', '?')}"
                speed = f"{record.get('time_interval', '?')}с"
                date = record.get("start_time", "N/A")

                row_str = f"{rank:<4} {score:<10} {size:<10} {speed:<10} {date:<20}"

                if rank == 1:
                    print(self.term.bold_yellow(f"🏆 {row_str}"))
                elif rank == 2:
                    print(self.term.bold_white(f"🥈 {row_str}"))
                elif rank == 3:
                    print(self.term.bold_red(f"🥉 {row_str}"))
                else:
                    print(f"   {row_str}")

        print(f"\n\n[R] - щоб повернутись")

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                keyboard.unhook_all()
                if event.name == 'r':
                    self.show_menu()
                    return

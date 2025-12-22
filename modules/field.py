"""клас для керування полем"""

import random
from typing import List, Tuple, Optional, Dict
from .entities.wall import Wall


class Field:
    """менеджер поля"""

    def __init__(self, width: int = 10, height: int = 10, game_mode: str = "classic"):
        """ініт"""
        self._width = width
        self._height = height
        self._game_mode = game_mode
        self._teleport_holes: Dict[Tuple[int, int], Tuple[int, int]] = {}
        self._walls = self._create_walls()

    @property
    def width(self) -> int:
        """отримання ширини"""
        return self._width

    @property
    def height(self) -> int:
        """отримання висоти"""
        return self._height

    @property
    def walls(self) -> List[Wall]:
        """отримання структури поля"""
        return self._walls

    def _create_walls(self) -> List[Wall]:
        """створення стін"""
        walls = []

        if self._game_mode == "teleport":
            # розрахунок центру для подальшого нанесення порталів
            center_y = self._height // 2
            center_x = self._width // 2

            # створення точок телепортації
            # верхній портао -> нижній
            top_hole = (0, center_x)
            bottom_hole = (self._height - 1, center_x)
            self._teleport_holes[top_hole] = (bottom_hole[0] - 1, bottom_hole[1])
            self._teleport_holes[bottom_hole] = (top_hole[0] + 1, top_hole[1])

            # лівий портал -> правий
            left_hole = (center_y, 0)
            right_hole = (center_y, self._width - 1)
            self._teleport_holes[left_hole] = (right_hole[0], right_hole[1] - 1)
            self._teleport_holes[right_hole] = (left_hole[0], left_hole[1] + 1)

            # створення стін з отворами під портали
            for y in range(self._height):
                for x in range(self._width):
                    if y == 0 or y == self._height - 1 or x == 0 or x == self._width - 1:
                        # пропуск якщо портал
                        if (y, x) not in self._teleport_holes:
                            walls.append(Wall((y, x)))
        else:
            # в класичному моді гри - всі стінки стандартні
            for y in range(self._height):
                for x in range(self._width):
                    if y == 0 or y == self._height - 1 or x == 0 or x == self._width - 1:
                        walls.append(Wall((y, x)))

        return walls

    def is_wall(self, position: Tuple[int, int]) -> bool:
        """перевірка на стіну"""
        return any(wall.position == position for wall in self._walls)

    def is_valid_position(self, position: Tuple[int, int]) -> bool:
        """перевірка на коректність позиції"""
        y, x = position
        if y < 0 or y >= self._height or x < 0 or x >= self._width:
            return False
        return not self.is_wall(position)

    def get_random_empty_position(self, occupied: List[Tuple[int, int]]) -> Tuple[int, int]:
        """отримання випаднової вільної позиції"""
        while True:
            y = random.randint(1, self._height - 2)
            x = random.randint(1, self._width - 2)
            position = (y, x)
            if position not in occupied and not self.is_wall(position):
                return position

    def _is_field_reachable(self, start_pos: Tuple[int, int]) -> bool:
        """перевірка на те, щоб не було недосяжних частин поля"""
        visited = set()
        stack = [start_pos]
        empty_cells = set()

        # кількість вільних слотів поля
        for y in range(1, self._height - 1):
            for x in range(1, self._width - 1):
                pos = (y, x)
                if not self.is_wall(pos):
                    empty_cells.add(pos)

        # проходження з початкової позиції
        while stack:
            current = stack.pop()
            if current in visited:
                continue

            visited.add(current)

            # перевірка 4х напрямів
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_pos = (current[0] + dy, current[1] + dx)
                if (next_pos not in visited and
                    next_pos in empty_cells and
                    not self.is_wall(next_pos)):
                    stack.append(next_pos)

        # повертаємо "досяжність" всіх клітинок
        return len(visited) == len(empty_cells)

    def add_random_obstacles(self, count: int, excluded_positions: List[Tuple[int, int]]):
        """додавання випадкової перешкоди на поле"""
        attempts = 0
        max_attempts = count * 10  # ліміт спроб, для уникнення циклу

        for i in range(count):
            placed = False

            while not placed and attempts < max_attempts:
                attempts += 1

                # знаходження вільної позиції
                position = self.get_random_empty_position(excluded_positions)

                # додати перешколу (тестово)
                self._walls.append(Wall(position))

                # перевірка, чи доступне після цього все поле
                if self._is_field_reachable(excluded_positions[0]):
                    excluded_positions.append(position)
                    placed = True
                else:
                    # якщо створює непрохідність - ремув
                    self._walls.pop()

            if not placed:
                # припинити, якщо не вдалося розмістити
                break

    def is_teleport_hole(self, position: Tuple[int, int]) -> bool:
        """перевірка на портал"""
        return position in self._teleport_holes

    def get_teleport_exit(self, position: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        """отримати координати виходу портала"""
        return self._teleport_holes.get(position)

    def get_cell_char(self, position: Tuple[int, int]) -> str:
        """отримання символу, по позиції"""
        if self.is_teleport_hole(position):
            return "O"
        if self.is_wall(position):
            return "#" #█
        return " "

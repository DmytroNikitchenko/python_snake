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
        
        self._walls: Dict[Tuple[int, int], Wall] = {} 
        self._create_walls()

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def walls(self) -> List[Wall]:
        """повертає список об'єктів стін (для сумісності)"""
        return list(self._walls.values())

    def _create_walls(self) -> None:
        """створення стін та наповнення словника"""        
        if self._game_mode == "teleport":
            self._setup_teleports()

        for y in range(self._height):
            for x in range(self._width):
                if y == 0 or y == self._height - 1 or x == 0 or x == self._width - 1:
                    if (y, x) not in self._teleport_holes:
                        self._add_wall((y, x))

    def _setup_teleports(self):
        """налаштування порталів для режиму teleport"""
        center_y = self._height // 2
        center_x = self._width // 2

        # верхній -> нижній
        top_hole = (0, center_x)
        bottom_hole = (self._height - 1, center_x)
        self._teleport_holes[top_hole] = (bottom_hole[0] - 1, bottom_hole[1])
        self._teleport_holes[bottom_hole] = (top_hole[0] + 1, top_hole[1])

        # лівий -> правий
        left_hole = (center_y, 0)
        right_hole = (center_y, self._width - 1)
        self._teleport_holes[left_hole] = (right_hole[0], right_hole[1] - 1)
        self._teleport_holes[right_hole] = (left_hole[0], left_hole[1] + 1)

    def _add_wall(self, position: Tuple[int, int]):
        """метод додавання стіни"""
        self._walls[position] = Wall(position)

    def is_wall(self, position: Tuple[int, int]) -> bool:
        """перевірка на стіну (тепер O(1))"""
        return position in self._walls

    def is_valid_position(self, position: Tuple[int, int]) -> bool:
        """перевірка на коректність позиції"""
        y, x = position
        if y < 0 or y >= self._height or x < 0 or x >= self._width:
            return False
        return not self.is_wall(position)

    def get_random_empty_position(self, occupied: List[Tuple[int, int]]) -> Tuple[int, int]:
        """отримання випадкової вільної позиції"""
        while True:
            y = random.randint(1, self._height - 2)
            x = random.randint(1, self._width - 2)
            position = (y, x)
            if position not in occupied and not self.is_wall(position):
                return position

    def _is_field_reachable(self, start_pos: Tuple[int, int]) -> bool:
        """перевірка досяжності"""
        visited = set()
        stack = [start_pos]
        
        empty_cells_count = 0
        for y in range(1, self._height - 1):
            for x in range(1, self._width - 1):
                if not self.is_wall((y, x)):
                    empty_cells_count += 1

        visited_count = 0
        
        while stack:
            current = stack.pop()
            if current in visited:
                continue

            visited.add(current)
            visited_count += 1

            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_pos = (current[0] + dy, current[1] + dx)
                
                # перевірка тільки координат
                if (next_pos not in visited and
                    0 < next_pos[0] < self._height - 1 and 
                    0 < next_pos[1] < self._width - 1 and
                    not self.is_wall(next_pos)):
                    stack.append(next_pos)

        return visited_count == empty_cells_count

    def add_random_obstacles(self, count: int, excluded_positions: List[Tuple[int, int]]):
        """додавання випадкової перешкоди"""
        attempts = 0
        max_attempts = count * 10
        
        added_walls = 0
        
        while added_walls < count and attempts < max_attempts:
            attempts += 1
            position = self.get_random_empty_position(excluded_positions)

            # додаємо стіну 
            self._add_wall(position)

            # перевіряємо прохідність
            if self._is_field_reachable(excluded_positions[0]):
                excluded_positions.append(position)
                added_walls += 1
            else:
                # якщо заблокували прохід - видаляємо зі словника
                del self._walls[position]

    def is_teleport_hole(self, position: Tuple[int, int]) -> bool:
        return position in self._teleport_holes

    def get_teleport_exit(self, position: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        return self._teleport_holes.get(position)

    def get_cell_char(self, position: Tuple[int, int]) -> str:
        """отримання символу"""
        if self.is_teleport_hole(position):
            return "O"
        
        if position in self._walls:
            return self._walls[position].render_char()
            
        return " "
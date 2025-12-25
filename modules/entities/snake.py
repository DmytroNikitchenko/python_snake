"""сутність змійки"""

from typing import List, Tuple
from .base_entity import BaseEntity


class Snake(BaseEntity):
    """сутність змійки"""

    DIRECTION_VECTORS = {
        "w": (-1, 0),  # верх
        "s": (1, 0),   # них
        "a": (0, -1),  # ліво
        "d": (0, 1)    # право
    }

    DIRECTION_ARROWS = {
        "w": "↑",
        "s": "↓",
        "a": "←",
        "d": "→"
    }
    
    OPPOSITE_DIRECTIONS = {
        "w": "s",
        "s": "w",
        "a": "d",
        "d": "a"
    }

    def __init__(self, initial_position: Tuple[int, int], initial_direction: str = "d"):
        """ініт"""
        super().__init__(initial_position)
        self._body = [initial_position]
        self._direction = initial_direction
        self._pending_growth = 0

    @property
    def body(self) -> List[Tuple[int, int]]:
        """отримати частину саме тіла змійки"""
        return self._body

    @property
    def direction(self) -> str:
        """отримання направлення"""
        return self._direction

    @direction.setter
    def direction(self, new_direction: str):
        """встановити нове направлення"""
        if new_direction not in self.DIRECTION_VECTORS:
            return

        if len(self._body) > 1:
            if new_direction == self.OPPOSITE_DIRECTIONS.get(self._direction):
                return

        self._direction = new_direction

    @property
    def head(self) -> Tuple[int, int]:
        """отримання позиції голови"""
        return self._body[0]

    def move(self) -> Tuple[int, int]:
        """переміщення по поточному напряму"""
        dy, dx = self.DIRECTION_VECTORS[self._direction]
        new_head = (self.head[0] + dy, self.head[1] + dx)

        # додавання нової голови до тіла
        self._body.insert(0, new_head)
        self._position = new_head

        # зростання
        if self._pending_growth > 0:
            self._pending_growth -= 1
        else:
            # видалення хвосту, якщо не зростає
            if len(self._body) > 1:
                self._body.pop()

        return new_head

    def teleport_head(self, position: Tuple[int, int]):
        """телепортація голови у нову позицію"""
        # змінюємо координати голови (перший елемент списку)
        self._body[0] = position
        # оновлюємо базову позицію сутності
        self._position = position

    def grow(self, amount: int = 1):
        """додавання зростання для змійки"""
        self._pending_growth += amount

    def check_self_collision(self) -> bool:
        """перевірка на входження голови у тіло"""
        return self.head in self._body[1:]

    def render_char(self) -> str:
        """отримання стрілки напряму змійки"""
        return self.DIRECTION_ARROWS.get(self._direction, "→")

    def get_body_segments(self) -> List[Tuple[int, int]]:
        """отримати тіло змійки"""
        return self._body[1:]

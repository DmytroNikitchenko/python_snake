"""базовий клас сутності для всієї гри"""

from abc import ABC, abstractmethod
from typing import Tuple


class BaseEntity(ABC):
    """абстрактний клас для всії сутностей"""

    def __init__(self, position: Tuple[int, int]):
        """ініт"""
        self._position = position

    @property
    def position(self) -> Tuple[int, int]:
        """отримання координат"""
        return self._position

    @position.setter
    def position(self, pos: Tuple[int, int]):
        """встановлення координат"""
        self._position = pos

    @property
    def y(self) -> int:
        """отримати "y" координату"""
        return self._position[0]

    @property
    def x(self) -> int:
        """отримати "х" координату."""
        return self._position[1]

    @abstractmethod
    def render_char(self) -> str:
        """повернути символ цієї сутності"""
        pass

    def __eq__(self, other):
        """перевірити відношення на основі позиції"""
        if isinstance(other, BaseEntity):
            return self.position == other.position
        return False

"""абстрактиний клас їжі"""

from abc import abstractmethod
from typing import Tuple
from .base_entity import BaseEntity


class Food(BaseEntity):
    """абстрактиний клас їжі"""

    def __init__(self, position: Tuple[int, int], score_value: int, growth_value: int):
        """ініт"""
        super().__init__(position)
        self._score_value = score_value
        self._growth_value = growth_value

    @property
    def score_value(self) -> int:
        """отримання очок з іжі"""
        return self._score_value

    @property
    def growth_value(self) -> int:
        """отримання зростання з їжі"""
        return self._growth_value

    @abstractmethod
    def render_char(self) -> str:
        """повернути символ їжі"""
        pass

"""Mega apple food entity."""

from typing import Tuple
from .food import Food


class MegaApple(Food):
    """мега яблуко дає 30 points і 3 росту"""

    def __init__(self, position: Tuple[int, int]):
        """ініт"""
        super().__init__(position, score_value=30, growth_value=3)

    def render_char(self) -> str:
        """повертає символ "мега" яблука"""
        return "*"

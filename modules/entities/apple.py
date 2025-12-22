"""яблуко"""

from typing import Tuple
from .food import Food


class Apple(Food):
    """звичайне яблуко дає 10 очків та 1 зростання"""

    def __init__(self, position: Tuple[int, int]):
        """ініт"""
        super().__init__(position, score_value=10, growth_value=1)

    def render_char(self) -> str:
        """повертає символ яблука"""
        return "*"

"""Wall entity class."""

from typing import Tuple
from .base_entity import BaseEntity


class Wall(BaseEntity):
    """клас головної перешкоди гри"""

    def __init__(self, position: Tuple[int, int]):
        """ініт"""
        super().__init__(position)

    def render_char(self) -> str:
        """повернення символу стіни"""
        return "#"

"""Entity classes for the Snake game."""

from .base_entity import BaseEntity
from .wall import Wall
from .food import Food
from .apple import Apple
from .mega_apple import MegaApple
from .snake import Snake

__all__ = [
    'BaseEntity',
    'Wall',
    'Food',
    'Apple',
    'MegaApple',
    'Snake'
]

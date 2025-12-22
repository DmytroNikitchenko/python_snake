"""імпорти для гри"""

# класи сутностей
from .entities.base_entity import BaseEntity
from .entities.snake import Snake
from .entities.wall import Wall
from .entities.food import Food
from .entities.apple import Apple
from .entities.mega_apple import MegaApple

# логічні класи
from .field import Field
from .game import Game
from .player import Player
from .renderer import Renderer
from .data_manager import DataManager
from .ui_manager import UIManager

__all__ = [
    # сутності
    'BaseEntity',
    'Snake',
    'Wall',
    'Food',
    'Apple',
    'MegaApple',
    # логіка
    'Field',
    'Game',
    'Player',
    'Renderer',
    'DataManager',
    'UIManager'
]
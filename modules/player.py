"""клас профілю гравця"""

from typing import List
from .data_manager import DataManager


class Player:
    """керує даними профілю гравця"""

    def __init__(self):
        """ініт"""
        self._data = DataManager.load_player_data()

    def refresh(self):
        """оновлює дані про гравця, отримуючі останні з сейву"""
        self._data = DataManager.load_player_data()

    def get_head_color(self) -> str:
        return self._data["head_color"]

    def get_body_color(self) -> str:
        return self._data["snake_color"]

    def get_owned_colors(self) -> List[str]:
        return self._data["owned_color"]

    def get_money(self) -> float:
        return self._data["money"]

    def set_head_color(self, color: str):
        self._data["head_color"] = color
        DataManager.save_player_data(self._data)

    def set_body_color(self, color: str):
        self._data["snake_color"] = color
        DataManager.save_player_data(self._data)

    def set_player_money(self, delta: float):
        self._data["money"] += delta
        DataManager.save_player_data(self._data)

    def add_owned_color(self, color: str):
        if color not in self._data["owned_color"]:
            self._data["owned_color"].append(color)
            DataManager.save_player_data(self._data)

    @staticmethod
    def get_rank_message(score: int) -> str:
        if 0 < score < 100:
            return "Ранг: 🟢 Початківець"
        elif 100 <= score < 200:
            return "Ранг: 🟠 Досвідчений"
        elif score >= 200:
            return "Ранг: 🏆 Майстер"
        return ""

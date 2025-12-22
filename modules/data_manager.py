"""менеджер операцій з даними"""

import os
import json
import datetime
from typing import Dict, List, Any


class DataManager:
    """контролює дані"""

    PLAYER_FILE = "player.json"
    LOG_FILE = "log.json"
    DEFAULT_PLAYER = {
        "money": 0,
        "snake_color": "green",
        "head_color": "green",
        "owned_color": ["green"]
    }

    @classmethod
    def load_player_data(cls) -> Dict[str, Any]:
        """завантажує інфо про гравця з json"""
        if not os.path.exists(cls.PLAYER_FILE) or os.path.getsize(cls.PLAYER_FILE) == 0:
            player = cls.DEFAULT_PLAYER.copy()
            with open(cls.PLAYER_FILE, "w") as f:
                json.dump(player, f, indent=4)
            return player
        else:
            with open(cls.PLAYER_FILE, "r") as f:
                player = json.load(f)
            return player

    @classmethod
    def save_player_data(cls, player: Dict[str, Any]):
        """збереження інфо про гравця в json"""
        with open(cls.PLAYER_FILE, "w") as f:
            json.dump(player, f, indent=4)

    @classmethod
    def load_game_log(cls) -> List[Dict[str, Any]]:
        """
        завантаження логу гри з json файлу, відсортованих по результату (спадання)
        """
        if os.path.exists(cls.LOG_FILE):
            with open(cls.LOG_FILE, "r") as f:
                try:
                    data = json.load(f)
                except Exception:
                    data = []
        else:
            data = []

        data.sort(key=lambda x: x["result"], reverse=True)
        return data

    @classmethod
    def save_game_log(cls, result: int, width: int, height: int, time_interval: float):
        """завантаження логу гри в json файл"""
        record = {
            "result": result,
            "time_interval": time_interval,
            "field_width": width,
            "field_height": height,
            "start_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        if os.path.exists(cls.LOG_FILE):
            with open(cls.LOG_FILE, "r") as f:
                try:
                    data = json.load(f)
                except Exception:
                    data = []
        else:
            data = []

        data.append(record)

        with open(cls.LOG_FILE, "w") as f:
            json.dump(data, f, indent=4)

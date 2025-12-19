import os
import json

def save_player_data(player):
    """збереження даних про гравця та його налаштування"""    
    with open("player.json", "w") as f:
        json.dump(player, f, indent=4)  
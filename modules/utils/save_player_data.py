import os
import json

def save_player_data(player):
    if not os.path.exists("player.json") or os.path.getsize("player.json") == 0:
        player = {"money":0, "snake_color":"green", "head_color":"green", "owned_color":["green"]}
        with open("player.json", "w") as f:
            json.dump(player, f, indent=4)
    with open("player.json", "w") as f:
        json.dump(player, f, indent=4)
        

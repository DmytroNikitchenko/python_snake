import os
import json

def load_player_data():
    if not os.path.exists("player.json") or os.path.getsize("player.json") == 0:
        player = {"money":0, "snake_color":"term.green", "head_color":"term.green", "owned_color":["green"]}
        with open("player.json", "w") as f:
            json.dump(player, f, indent=4)
        return player
    else:
        with open("player.json", "r") as f:
            player = json.load(f)    
        return player
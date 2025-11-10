from modules.utils import *

class Snake():
    def __init__(self):
        self._player = load_player_data()        
             
    def get_head_color(self):
        return self._player["head_color"]
    
    def get_body_color(self):
        return self._player["snake_color"]
    
    def get_owned_colors(self):
        return self._player["owned_color"]
    
    def set_head_color(self, color):
        self._player["head_color"] = color
        save_player_data()
        
    def set_body_color(self, color):
        self._player["snake_color"] = color
        save_player_data()
        
    def set_player_money(self, delta):
        self._player["money"] += delta
        save_player_data()
        
    def add_owned_color(self, color):
        self._player["owned_color"].append(color)
        save_player_data()


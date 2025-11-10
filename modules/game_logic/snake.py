from modules.utils import *

class Snake():
    def __init__(self):
        self._player = load_player_data()        
             
    def get_head_color(self):
        return self._player["head_color"].replace("term.", "")
    
    def get_body_color(self):
        return self._player["snake_color"].replace("term.", "")
    
    def get_owned_colors(self):
        return self._player["owned_color"]
    
    def get_money(self):
        return self._player["money"]  
    
    def set_head_color(self, color):
        self._player["head_color"] = color
        save_player_data(self._player)       
        
    def set_body_color(self, color):
        self._player["snake_color"] = color
        save_player_data(self._player)
        
    def set_player_money(self, delta):
        self._player["money"] += delta
        save_player_data(self._player)
        
    def add_owned_color(self, color):
        self._player["owned_color"].append(color)
        save_player_data(self._player)
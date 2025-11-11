import json
import os

def load_log_json():
    """завантаження даних про всі забіги, відсортовані від першого місця по балах"""
    filename = "log.json"
        
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                data = json.load(f)
            except Exception:
                data = []
    else:
        data = []
        
    data.sort(key=lambda x: x["result"], reverse=True)
        
    return data
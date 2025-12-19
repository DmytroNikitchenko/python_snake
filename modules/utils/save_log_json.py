# збереження результату в файл
import json
import os
import datetime
def save_log_json(result, width, height, time_interval):
    """збереження даних про забіг"""
    record = {
        "result": result,
        "time_interval": time_interval,
        "field_width": width,
        "field_height": height,
        "start_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    
    filename = "log.json"
    
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                data = json.load(f)
            except Exception:
                data = []
    else:
        data = []
    
    data.append(record)
    
    with open("log.json", "w") as f1:
        json.dump(data, f1, indent=4)

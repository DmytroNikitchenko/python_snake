# збереження результату в файл

import datetime
def save_result_to_file(result, width, height):
    with open("results.txt", "a") as f1:
        f1.write(f"Забіг в {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} має результат: {result},\t при полі розміром {width}x{height}\n")
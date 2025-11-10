# збереження результату в файл

import datetime
def save_result_to_file(result, width, height, time_interval):
    with open("results.txt", "a") as f1:
        f1.write(f"Забіг в {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} має результат: {result},\t при полі розміром {width}x{height}\t та швидкості {time_interval}\n")
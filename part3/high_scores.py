import os
import csv

if __name__ == "__main__":
    base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp09/practice_files"
    scores = {}
    with open(os.path.join(base_path, "scores.csv"), "r") as file_handler_input:
        csv_file_reader = csv.reader(file_handler_input)
        for name, score in csv_file_reader:
            try:
                if scores[name] < score:
                    scores[name] = score
            except KeyError:
                scores[name] = score

    for key, value in sorted(scores.items()):
        print(key, value)
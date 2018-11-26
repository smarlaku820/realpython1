import csv
import os

if __name__ == "__main__":
    base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp09/practice_files"
    with open(os.path.join(base_path, 'wonka.csv'), "r") as file_handle:
        csv_handler = csv.reader(file_handle)
        for row in csv_handler:
            print(row)

    with open(os.path.join(base_path, 'wonka.csv'), "r") as file_handle:
        csv_handler = csv.reader(file_handle)
        # by passing the header
        print(next(csv_handler))
        for first_name, last_name, reward in csv_handler:
            print("{} {} got: {}".format(first_name, last_name, reward))

    with open(os.path.join(base_path, 'tabbed wonka.csv'), "r") as file_handle:
        csv_handler = csv.reader(file_handle, delimiter="\t")
        # by passing the header
        print(next(csv_handler))
        for row in csv_handler:
            print(row)
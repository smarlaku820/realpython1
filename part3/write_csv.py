import os
import csv

if __name__ == "__main__":
    base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp09/practice_files"
    with open(os.path.join(base_path, "movies.csv"), "w") as file_handle:
        csv_file_writer = csv.writer(file_handle)
        csv_file_writer.writerow(["Movies", "Rating"])
        csv_file_writer.writerow(["Inception", "7"])
        csv_file_writer.writerow(["Monty Python's Silver Amulat", "3"])
        csv_file_writer.writerow(["AutoBiography of a Yogi", "3"])

    my_ratings = [['Movies', 'Rating'],
                  ['Django Unchained', '2'],['Titanic','2'],['Avatar','7']]

    with open(os.path.join(base_path, "movies_extended.csv"), "w") as file_handle:
        csv_file_writer = csv.writer(file_handle)
        csv_file_writer.writerows(my_ratings)
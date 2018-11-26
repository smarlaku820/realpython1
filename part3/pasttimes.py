import os
import csv

if __name__ == "__main__":
    base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp09/practice_files"
    with open(os.path.join(base_path, 'pastimes.csv'), "r") as file_handle:
        csv_file_handler = csv.reader(file_handle)
        print(next(csv_file_handler))
        for person, pastime in csv_file_handler:
            if pastime.lower().find("fighting") != -1:
                print(person, pastime)

    with open(os.path.join(base_path, 'pastimes.csv'), "r") as file_handle:
        csv_file_handler = csv.reader(file_handle)
        print(next(csv_file_handler))
        for person, pastime in csv_file_handler:
            if pastime.lower().find("fighting") != -1:
                print(person, pastime, "Combat")
            else:
                print(person, pastime, "Other")

    with open(os.path.join(base_path, 'pastimes.csv'), "r") as file_handle_read, open(os.path.join(base_path, 'categorized pastimes.csv'), "w") as file_handle_write:
        csv_file_rhandler = csv.reader(file_handle_read)
        csv_file_whandler = csv.writer(file_handle_write)
        print(next(csv_file_rhandler))
        write_rows = [["Name", "Favorite pastime", "Type of Pastime"]]
        for person, pastime in csv_file_rhandler:
            if pastime.lower().find("fighting") != -1:
                write_rows.append([person, pastime, "Combat"])
            else:
                write_rows.append([person, pastime, "Other"])
        csv_file_whandler.writerows(write_rows)
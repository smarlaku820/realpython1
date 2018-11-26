import os
import glob

if __name__ == "__main__":
    base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp09/practice_files/little pics"
    for current_folder, sub_folders, file_list in os.walk(base_path):
        for file in file_list:
            full_path = os.path.join(current_folder, file)
            fileName, extension = os.path.splitext(full_path)
            if extension == '.jpg' and os.path.getsize(full_path) < 2000:
                print("Removing the  file {}".format(full_path))
                os.remove(full_path)


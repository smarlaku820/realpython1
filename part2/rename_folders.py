import os

base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp09/practice_files/images"
file_list = os.listdir(base_path)

for file in file_list:
    full_name = os.path.join(base_path, file)
    if os.path.isdir(full_name):
        new_folder_name = os.path.join(base_path, file + "_folder")
        print(new_folder_name)
        os.rename(full_name, new_folder_name)
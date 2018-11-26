import os
import time

base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp09/practice_files/images"

print("To list all the files in the base path")
for current_folder, sub_folders, file_list in os.walk(base_path):
    for file in file_list:
        print(os.path.join(current_folder, file))
        print(os.path.getsize(os.path.join(current_folder, file)))
        print("created time %s" % time.ctime(os.path.getctime(os.path.join(current_folder, file))))


print("To list all the sub-folders in the base path")
for current_folder, sub_folders, file_list in os.walk(base_path):
    for sub in sub_folders:
        print(os.path.join(current_folder, sub))
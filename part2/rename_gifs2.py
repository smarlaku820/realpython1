import glob
import os

base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp09/practice_files/images"
possible_files = os.path.join(base_path, "*.gif")

for file_name in glob.glob(possible_files):
    print("Converting {} to JPG. . .".format(file_name))
    full_file_name = os.path.join(base_path, file_name)
    new_file_name = os.path.join(base_path, file_name[0:len(file_name) - 4] + ".jpg")
    os.rename(full_file_name, new_file_name)
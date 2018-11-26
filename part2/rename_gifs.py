import os

base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp09/practice_files/images"
file_list = os.listdir(base_path)

for file_name in file_list:
    if file_name.lower().endswith('.jpg'):
        print("Converting {} to GIF...".format(file_name))
        old_file_name = os.path.join(base_path, file_name)
        new_file_name = os.path.join(base_path, file_name[0:len(file_name)-4]+".gif")
        os.rename(old_file_name, new_file_name)

print("list of GIF's available are as follows:")
for file_name in os.listdir(base_path):
    if file_name.lower().endswith('.gif'):
        print(file_name)
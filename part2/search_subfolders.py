import os
import glob


base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp09/practice_files/images"
possible_paths = os.path.join(base_path, '*/*png')

for file in glob.glob(possible_paths):
    print(file)
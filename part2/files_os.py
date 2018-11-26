import os

my_path = "C:/Users/zc11/PycharmProjects/realpython1"
input_file_name = os.path.join(my_path, "part1/election.py")

with open(input_file_name, "r") as my_input_file:
    for line in my_input_file.readlines():
        print(line, end="")
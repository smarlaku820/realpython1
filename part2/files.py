my_input_file = open("poem.txt", "r")

for line in my_input_file.readlines():
    print(line, end="")

my_input_file.close()
with open("poem.txt", "r") as input_file:
    for line in input_file.readlines():
        print(line, end="")
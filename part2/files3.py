with open("poem.txt", "r") as inp, open("output.txt", "w") as oup:
    for line in inp.readlines():
        oup.writelines(line)

with open("output.txt", "a") as file:
    file.writelines(["\nthis is a new line that i have added."])
from random import randint

if __name__ == "__main__":
    flips = 0
    trails = 10000
    for _ in range(0, trails):
        x = randint(0, 1)
        flips += 1
        while randint(0, 1) == x:
            flips += 1
        flips += 1
    print("Average no of coin flips is {}".format(flips/trails))
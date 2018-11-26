from random import randint


def tossdie():
    return randint(1, 6)


if __name__ == "__main__":
    tosses = []
    for _ in range(0, 10000):
        tosses.append(tossdie())
    print("Average Number Resulting From the Tosses is {}".format(round(sum(tosses)/len(tosses))))

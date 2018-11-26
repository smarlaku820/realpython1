from random import random


def flip(p):
    return 'H' if random() < p else 'T'


if __name__ == "__main__":
    flips = 0
    trials = 10000
    for _ in range(0, trials):
        x = flip(0.2)
        flips += 1
        while flip(0.2) == x:
            flips += 1
        flips += 1
    print("A biased coin is tossed. It has only 20% of chances of showing a HEAD when the coin is flipped.")
    print("Average of no of coin flips would be {}".format(flips/trials))
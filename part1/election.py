from random import random


def elect(p):
    return 'A' if random() < p else 'B'


if __name__ == "__main__":
    a_wins = 0
    b_wins = 0
    results = []
    for _ in range(0, 10000):
        results.append(elect(0.87))
        results.append(elect(0.65))
        results.append(elect(0.17))
        if results.count('A') > results.count('B'):
            a_wins += 1
        else:
            b_wins += 1
        results.clear()
    print("The Probability that A wins the election is {}".format(a_wins/10000))
    print("The Probability that B wins the election is {}".format(b_wins/10000))
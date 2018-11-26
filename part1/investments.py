def invest(amount, rate, time):
    print("principal amount: ${}".format(amount))
    print("annual rate of return: {}".format(rate))
    for _ in range(1, time+1):
        amount = amount + rate*amount
        print("year {}: ${}".format(_, amount))


if __name__ == "__main__":
    invest(100, .05, 8)
    invest(2000, .025, 5)
def factors(x):
    for _ in range(1, x+1):
        if x%_ == 0:
            print("{} is a divisor of {}".format(_, x))


if __name__ == "__main__":
    tries = 0
    while tries < 3:
        tries += 1
        try:
            n = int(input("Enter a positive integer:"))
            if n <= 0:
                continue
            else:
                factors(n)
                break;
        except ValueError:
            print("please, enter a positive integer. stop playing ..")
    else:
        print("Better Luck Next Time Sir!")
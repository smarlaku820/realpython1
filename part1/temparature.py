def c2f(c):
    print("{} degrees C = {} degrees F".format(c, c*(9/5) + 32))


def f2c(f):
    print("{} degrees F = {} degress C".format(f, (f-32)*5/9))


if __name__ == "__main__":
    f2c(72)
    c2f(37)
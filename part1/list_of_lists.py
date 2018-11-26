def enrollment_stats(univ):
    e = []
    t = []
    for _ in range(len(univ)):
        e.append(univ[_][1])
        t.append(univ[_][2])
    return e, t


def mean_func(l):
    totals = 0
    for _ in l:
        totals += _
    return totals/len(l)


def median_func(l):
    l.sort()
    if len(l) % 2 != 0:
        return l[len(l)//2]
    else:
        return l[len(l)//2 + 1]


if __name__ == "__main__":
    universities = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500]
    ]
    x, y = enrollment_stats(universities)
    print("*****" * 5)
    print("Total students:  {}".format(sum(x)))
    print("Total tution:  $ {}".format(sum(y)))
    print("\nStudent mean:    {}".format(int(mean_func(x))))
    print("Student median:  {}".format(median_func(x)))
    print("\nTution mean:   $ {}".format(int(mean_func(y))))
    print("Tution median: $ {}".format(median_func(y)))
    print("*****"*5)
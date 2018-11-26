def multiples(x):
    mul = []
    for _ in range(1, 101):
        if _%x == 0:
            mul.append(_)
    return mul


if __name__ == "__main__":
    cats = dict()
    for _ in range(1, 101):
        cats['cat# '+str(_)] = 0
    for var in range(1, 101):
        positions = multiples(var)
        for x in positions:
            pos = 'cat# '+str(x)
            if cats[pos] == 0:
                cats[pos] = 1
            else:
                cats[pos] = 0
    print("The following are the cats with hats on :")
    for _ in range(1, 101):
        if cats['cat# '+str(_)] == 1:
            print('cat# '+str(_))
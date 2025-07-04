def difference(*args):
    list_1 = []
    a = 0
    for arg in args:
        if arg + arg != 0:
            for arg in args:
                arg = float(arg)
                list_1.append(arg)
            a = max(list_1) - min(list_1)
            if a % 1 == 0:
                a = int(a)
            else:
                a = round(a, 2)
        else:
            a = 0
    return a
print(difference(10.2, -2.2, 0, 1.1, 0.5))
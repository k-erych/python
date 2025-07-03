def difference(*args):
    list_1 = []
    for arg in args:
        arg = float(arg)
        list_1.append(arg)
    a = max(list_1) - min(list_1)
    if a % 1 == 0:
        a = int(a)
    return a
print(difference(5, 6, 2, 9, 5.2))
def add_one(some_list):
    c = str()
    for i in some_list:
        b = str(i)
        c = str(c + b)
    d = int(c)
    e = d + 1
    str_1 = str(e)
    list_1 = list(str_1)
    print(list_1)
list_1 = list([2, 7, 9])
add_one(list_1)


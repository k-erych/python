def find_unique_value(some_list):
    b = int()
    for i in range(0, 100):
        a = some_list.count(i)
        if a == 1:
            b = i
            break
        else:
            continue
    print(b)
list_1 = [1, 1, 1, 3, 3, 4, 5, 4]
find_unique_value(list_1)


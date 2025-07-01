def find_unique_value(some_list):
    b = int()
    for i in some_list:
        a = some_list.count(i)
        if a == 1:
            if str(i).count(".") == 1:
                b = float(i)
            else:
                b = int(i)
            break
        else:
            continue
    return b
list_1 = [1, 1, 1, 3, 3, 4, 5, 4]
b = find_unique_value(list_1)
print(b)

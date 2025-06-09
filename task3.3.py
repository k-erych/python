list1 = [-3, 2, 4, 876, 568]
if len(list1) == 0:
    print(list1)
elif len(list1) == 1:
    list2 = [list1, []]
    print(list2)
elif len(list1) % 2 == 0:
    n = int(len(list1) / 2)
    list01 = list1[0:n]
    list02 = list1[n:]
    list03 = [list01, list02]
    print(list03)
else:
    n = int(len(list1)) // 2
    list01 = list1[0:n+1]
    list02 = list1[n+1:]
    list03 = [list01, list02]
    print(list03)
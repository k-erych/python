my_list = [0, 1, 0, 3, 12, 0, 5]

i = 0
while i < len(my_list):
    if my_list[i] == 0:
        my_list.pop(i)
        my_list.append(0)
    else:
        i += 1
print(my_list)

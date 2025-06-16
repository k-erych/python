my_list = [0, 1, 0, 3, 12, 0, 5]

x = my_list.count(0)
while 0 in my_list:
    my_list.remove(0)
for _ in range(x):
    my_list.append(0)

print(my_list)


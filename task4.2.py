list1 = [1, 4, 6, 3, 1, 2, 7]
x = len(list1)
if x == 0:
    result = 0
else:
    sum_even = 0
    for i in range(0, x, 2):
        sum_even = sum_even + list1[i]
    result = sum_even * list1[-1]
print(result)


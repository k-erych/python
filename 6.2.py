set_1 = {0, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19 }
set_2 = {2, 3, 4}
num_1 = int(input("Введіть число в діапазоні від 0 до 8640000: ")) # {}
day = num_1 // (24 * 60 * 60)
remainder = num_1 % (24 * 60 * 60)
hour = remainder // 3600
mi = (remainder % 3600) // 60
sec = remainder % 60
if day in set_1 or day % 10 in set_1:
    print(f'{day} днів, {hour}:{mi}:{sec}')
elif day == 1 or day % 10 == 1:
    print(f'{day} день, {hour}:{mi}:{sec}')
elif day in set_2 or day % 10 in set_2:
    print(f'{day} дні, {hour}:{mi}:{sec}')







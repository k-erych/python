import string
str_1 = str(string.ascii_letters)
res = str(input("Введіть через дефіс дві літери: "))
let_1 = res[0]
let_2 = res[2]
ind_1 = (string.ascii_letters.index(let_1))
ind_2 = (string.ascii_letters.index(let_2))
if ind_1 < ind_2:
    print(str_1[ind_1:ind_2+1])
elif ind_1 > ind_2:
    str_2 = str_1[ind_1:len(str_1)]
    str_3 = str_1[0:ind_2+1]
    str_4 = str_2 + str_3
    print(str_4)
else:
    print(let_1)
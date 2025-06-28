def second_index(text, some_str):
    a = (text.index(some_str))
    b = len(text)
    new_str = text[a+1:b]
    old_str = text[0:a+1]
    if some_str in new_str:
        ind_1 = new_str.index(some_str)
        ind_true = int(ind_1 + len(old_str))
        print(ind_true)
    else:
        print("None")
text_1 = str(input("Введіть тест: "))
some_str_1 = str(input("Введіть символ, другий індекс якого ви хочете дізнатися: "))
second_index(text_1, some_str_1)
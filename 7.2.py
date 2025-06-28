def correct_sentence(str_1):
    if str_1[-1] != ".":
        str_1 = str_1 + "."
    if not str_1[0].isupper():
        a = str_1[0]
        str_1 = str_1.replace(str_1[0], str_1[0].capitalize())
    print(str_1)
sent = str(input("Введіть речення: "))
correct_sentence(sent)

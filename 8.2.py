import string
str_1 = str(input("Введіть рядок на перевірку: "))
def is_palindrome(text):
    a = text
    for i in string.punctuation:
        a = a.replace(i, "")
    while True:
        a = a.replace(" ", "")
        if " " not in a:
            break
    a = a.lower()
    b = len(a)
    k = False
    for c in range(0, b):
        if a[c] == a[-c - 1]:
            k = True
    print(k)

is_palindrome(str_1)
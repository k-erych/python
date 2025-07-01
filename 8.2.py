import string
str_1 = str(input("Введіть рядок на перевірку: "))
def is_palindrome(text):
    a = text
    for i in string.punctuation:
        a = a.replace(i, "")
    a = a.replace(" ", "")
    a = a.lower()

    b = len(a)
    for c in range(b // 2):
        if a[c] != a[-(c + 1)]:
            return False
    return True


k = is_palindrome(str_1)
print(k)
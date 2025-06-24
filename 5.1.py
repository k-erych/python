import keyword
import string
str_1 = str(input("Напишіть рядок: "))
words = str_1.split("_")
str_2 = str_1.replace("_", "")

if any(x.isupper() for x in str_1):
    print("False")
elif str_1[0].isdigit():
    print("False")
elif any(c in string.punctuation for c in str_2):
    print("False")
elif any(word in keyword.kwlist for word in words):
    print("False")
else:
    print("True")




import keyword
import string
str_1 = str(input("Напишіть рядок: "))
words = str_1.split("_")
if any(x.isupper() for x in str_1):
    print("False")
elif str_1[0].isdigit():
    print("False")
elif str_1 in keyword.kwlist:
    print("False")
elif any(c in string.punctuation for c in str_1.replace("_", "")):
    print("False")
elif set(str_1) <= {"_"} and str_1 != "_":
    print("False")
else:
    print("True")




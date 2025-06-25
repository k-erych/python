import string

str1 = str(input("Введіть рядок: "))
str2 = str1.title()
str3 = str2
for char in string.punctuation:
    str3 = str3.replace(char, "").replace(" ", "")
str4 = "#" + str3
str5 = str4[:140]
print(str5)

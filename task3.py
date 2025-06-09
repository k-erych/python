digit1 = float(input("Оберіть число номер 1: "))
oper = str(input("Оберіть арифмитичну дію з запропонованих: + , - , * , /: "))
digit2 = float(input("Оберіть число номер 2: "))
if oper == "/" and digit2 == 0:
    print("Неможливо виконати операцію (ділення на 0)")
elif oper == "*":
    print(digit1 * digit2)
elif oper == "/":
    print(digit1 / digit2)
elif oper == "+":
    print(digit1 + digit2)
else:
    print(digit1 - digit2)
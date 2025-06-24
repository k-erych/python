wish = 1
while wish == 1:
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
    res = input("Ви хочете продовжити? ")
    res_1 = res.upper()
    if res_1 != "YES" and res_1 != "Y":
        print("Роботу завершено")
        break
    else:
        continue
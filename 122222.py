number = int(input("Напишіть 5-х значне число: "))

digit1 = number % 10
digit2 = (number % 100) // 10
digit3 = (number % 1000) // 100
digit4 = (number % 10000) // 1000
digit5 = number // 10000

print(digit1) , print(digit2)



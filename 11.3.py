def is_even(number):
    str_1 = str(number)
    if str_1[-1] in {"0", "2", "4", "6", "8"}:
        return True
    else:
        return False
print(is_even(12345698))
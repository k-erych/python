from inspect import isgenerator
def generate_cube_numbers(end):
    if end < 8:
        return
    else:
        for i in range(2, end + 1):
            cube = i * i * i
            if cube <= end:
                yield cube
            else:
                return
print(list(generate_cube_numbers(80)))

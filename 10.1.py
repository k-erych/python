def pow(x):
     return x ** 2

def some_gen(begin, stop, func):
    current = begin
    for _ in range(stop):
        yield current
        current = func(current)
    return current
for val in some_gen(2, 6, pow):
   print(val)
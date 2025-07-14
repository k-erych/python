from inspect import isgenerator
def prime_generator(end):
    if end >= 2:
        yield 2
    if end >= 3:
        yield 3
    if end >= 5:
        yield 5
    for i in range(6, end + 1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            yield i
gen = prime_generator(2)
print(isgenerator(gen))
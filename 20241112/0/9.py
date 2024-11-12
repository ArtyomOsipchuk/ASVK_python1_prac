from math import inf

def divisor(a, b):
    c = a / b
    return -c

def div(a, b):
    if abs(b) <= 1:
        return ZeroDivisionError(f"Маловато будет, {b} - это же почти наверняка ноль!?!")
    c = a / b
    return -c

def proxy(fun, *args):
    try:
        return fun(*args)
    except ZeroDivisionError:
        return inf

for i in range(-2, 3):
    print(proxy(divisor, 100, i))

for i in range(-2, 3):
    print(proxy(div, 100, i))

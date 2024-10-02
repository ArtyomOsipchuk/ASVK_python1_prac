from math import *


def Calc(s, t, u):
    x1 = lambda x: eval(s)
    x2 = lambda x: eval(t)
    x3 = lambda x, y: eval(u)
    return lambda x: x3(x1(x), x2(x))


a, b, c = eval(input())
f = Calc(a, b, c)
print(f(eval(input())))

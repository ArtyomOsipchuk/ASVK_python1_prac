from fractions import Fraction as frac
from decimal import Decimal as dec

def esum(N, one):
    cnt = one
    res = one
    for i in range(1, N):
        cnt *= i
        res += one / cnt
    return res


print(esum(100, 1))
print(esum(100, 1.0))
print(esum(100, frac("1")))
print(esum(100, dec("1")))

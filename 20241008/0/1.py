from fractions import Fraction as frac
from decimal import Decimal as dec

def multiplier(x, y, Type):
    return Type(x) * Type(y)

print(f'{multiplier("1.1", "1.2", float)=}')
print(multiplier("1.2", "2.2", float))
print(f'{multiplier("1.1", "1.2", frac)=}')
print(multiplier("1.2", "2.2", frac))
print(f'{multiplier("1.1", "1.2", dec)=}')
print(multiplier("1.2", "2.2", dec))

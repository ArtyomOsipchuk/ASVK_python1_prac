from fractions import Fraction as frac
import decimal

print(decimal.getcontext())
decimal.getcontext().prec = 10
print(decimal.Decimal(1) / 3)

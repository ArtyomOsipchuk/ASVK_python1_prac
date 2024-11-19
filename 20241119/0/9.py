from string import ascii_letters
class Trad:
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)

t = Trad()
print(dir(t))
print(t.q)

class Slotter:
    __slots__ = tuple(ascii_letters)
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)

s = Slotter()
print(dir(s))
print(s.T)

import sys
print(sys.getsizeof(Trad))
print(sys.getsizeof(Slotter))
print(sys.getsizeof(t))
print(sys.getsizeof(s))

from pympler.asizeof import asizeof
print(asizeof(Trad))
print(asizeof(Slotter))
print(asizeof(t))
print(asizeof(s))

t = [Trad() for i in range(1000)]
s = [Slotter() for i in range(1000)]
print(asizeof(t))
print(asizeof(s))

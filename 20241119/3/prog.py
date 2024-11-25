class Vowel:
    __slots__ = tuple("aouiey")
    answer = 42

    @property
    def full(self):
        for i in sorted(self.__slots__):
            try:
                getattr(self, i)
            except AttributeError:
                return False
        return True

    @full.setter
    def full(self, val):
        pass

    def __init__(self, *args, **kwargs):
        for i, j in kwargs.items():
            setattr(self, i, j)

    def __str__(self):
        s = []
        for i in sorted(self.__slots__):
            try:
                s.append(f"{i}: {getattr(self, i)}")
            except AttributeError:
                continue
        return ", ".join(s)

import sys

exec(sys.stdin.read())

import collections

class DivStr(collections.UserString):
    def __init__(self, data=""):
        self.data = data

    def __floordiv__(self, n):
        le = len(self.data)
        for i in range(0, le - le % n, le // n):
            yield self.data[i: i + le // n]

    def __mod__(self, n):
        return DivStr(self.data[-1 * (len(self.data) % n):])

a = DivStr("XcDfQWEasdERTdfgRTY")
print(* a // 4)
print(a % 4)
print(* a % 10 // 3)
print(a.lower() % 3)
print(* a[1:7] // 3)
print(a % 5 + DivStr() + a % 6)

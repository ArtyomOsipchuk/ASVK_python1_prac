import collections

class DivStr(collections.UserString):
    def __init__(self, data=""):
        self.data = data

    def __floordiv__(self, n):
        le = len(self.data)
        for i in range(0, le - le % n, le // n):
            yield self.data[i: i + le // n]

    def __mod__(self, n):
        if len(self.data) % n == 0:
            return DivStr()
        return DivStr(self.data[-1 * (len(self.data) % n):])

import sys
exec(sys.stdin.read())

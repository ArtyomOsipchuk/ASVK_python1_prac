class Num:
    def __get__(self, obj, val):
        if not hasattr(obj, "real"):
            obj.real = 0
        return obj.real

    def __set__(self, obj, val):
        if hasattr(val, "real"):
            obj.real = val.real
        elif hasattr(val, "__len__"):
            obj.real = len(val)
        else:
            obj.real = 0

    def __delete__(self, obj):
        obj.real = 0

import sys

exec(sys.stdin.read())

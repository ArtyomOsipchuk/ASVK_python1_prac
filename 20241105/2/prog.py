class Triangle:
    def __init__(self, t1, t2, t3):
        self.t1 = tuple(t1)
        self.t2 = tuple(t2)
        self.t3 = tuple(t3)

    def __bool__(self):
        return bool(abs(self))

    def __abs__(self):
        S = round(0.5 * abs((self.t1[0] - self.t3[0]) * (self.t2[1] - self.t3[1]) - (self.t2[0] - self.t3[0]) * (self.t1[1] - self.t3[1])), 3)
        if not S:
            return 0
        return S

    def __lt__(self, obj):
        return abs(self) < abs(obj)
    
    def _dir(self, dot, t1, t2):
        return (t1[0] - dot[0]) * (t2[1] - dot[1]) - (t1[1] - dot[1]) * (t2[0] - dot[0])

    def _in_angle(self, dot):
        d1 = self._dir(dot, self.t1, self.t2)
        d2 = self._dir(dot, self.t2, self.t3)
        d3 = self._dir(dot, self.t3, self.t1)
        return not ((d1 < 0 or d2 < 0 or d3 < 0) and (d1 > 0 or d2 > 0 or d3 > 0))

    def __contains__(self, obj):
        if not obj:
            return True
        return self._in_angle(obj.t1) and self._in_angle(obj.t2) and self._in_angle(obj.t3)

    def __and__(self, obj):
        if not self or not obj:
            return False
        if self._in_angle(obj.t1) or self._in_angle(obj.t2) or self._in_angle(obj.t3) or obj._in_angle(self.t1) or obj._in_angle(self.t2) or obj._in_angle(self.t3):
            return True
        return False

import sys

exec(sys.stdin.read())

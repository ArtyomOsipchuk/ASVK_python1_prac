class Num:
	_real = 0

        @property
        def real(self):
            return self._real

        @real.setter
        def real(self, val):
            if hasattr(val, "real"):
                self._real = val.real
            if hasattr(val, "len"):
                self._real = len(val)
            return 0

        @real.deleter
        def real(self):
            self._real = 0


class C:
  num = Num()
print(C().num)
c, d = C(), C()
c.num = d.num = 2
print(c.num, d.num)
print(c.num+d.num)
c.num = "qwerqwerqwer"
print(c.num, d.num)
print(c.num+d.num)
d.num = range(10, 1000, 7)
print(c.num, d.num)
print(c.num+d.num)

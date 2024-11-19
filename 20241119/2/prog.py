class Num:
    n = 0

    def __get__(self, obj, val):
        return self.n
    
    def __set__(self, obj, val):
        try:
            self.n = val.real
        except:
            self.n = val.__len__()


class C:
  num = Num()
print(C().num)
c, d = C(), C()
c.num = d.num = 2
print(c.num+d.num)
c.num = "qwerqwerqwer"
print(c.num, d.num)
print(c.num+d.num)
d.num = range(10, 1000, 7)
print(c.num+d.num)

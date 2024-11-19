class slo:
    __slots__ = "a", "b", "c"
    ro = 100500

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

c = slo(5, 7, 8)
print(c.a)
print(c.ro)
dir(slo)
print(c.__slots__)
#print(c.__dict__)
#c.ro = 123

class dump(tuple):
    pass



class C(metaclass=dump):
    def __init__(self, val):
        self.val = val

    def add(self, other, another=None):
        return self.val + other + (another or self.val)

c = C(10)
print(c.add(9))
print(c.add(9, another=10))

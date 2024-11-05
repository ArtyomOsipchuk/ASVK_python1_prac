class Rectangle:
    rectcnt = 0
    def __init__(self, x1, x2, y1, y2):
        self.__class__.rectcnt += 1
        setattr(self, f"rect_{self.rectcnt}", self.rectcnt)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def __del__(self):
        self.__class__.rectcnt -= 1
        print(self.rectcnt)

    def __bool__(self):
        return bool(abs(self))

    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1})"
    
    def __abs__(self):
        return abs(self.x1 - self.x2) * abs(self.y1 - self.y2)

    def __lt__(self, obj):
        return abs(self) < abs(obj)

    def __eq__(self, obj):
        return abs(self) == abs(obj)

    def __mul__(self, n):
        x1 = self.x1 * n
        x2 = self.x2 * n
        y1 = self.y1 * n
        y2 = self.y2 * n
        return self.__class__(x1, x2, y1, y2)

    __rmul__ = __mul__

    def __getitem__(self, pos):
        return ((self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1))[pos]

r = Rectangle(1, 2, 3, 4)
rr = Rectangle(2, 0, 3, 4)
rrr = Rectangle(4, 3, 2, 1)
print(r)
print(5 * r * 5)
print(r[0])

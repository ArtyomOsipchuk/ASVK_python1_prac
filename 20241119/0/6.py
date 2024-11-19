class Counter:
    def __init__(self):
        self.c = 0

    def __get__(self, obj, cls):
        return self.c

    def __set__(self, obj, val):
        self.c = val

    def __delete__(self, obj):
        print(f"Deleted counter :0")


class C:
    counter = Counter()
    def __init__(self):
        self.counter += 1
    def __del__(self):
        self.counter -= 1
c = C()
print(c.counter)
d = C()
print(d.counter)
del c
print(d.counter)
del d.counter
print(d.counter)

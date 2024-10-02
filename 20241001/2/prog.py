def subd(a, b):
    if isinstance(a, type(b)):
        if isinstance(a, (list, tuple)):
            return type(a)([i for i in a if i not in b])
        return type(a)(a.__sub__(b))


a, b = eval(input())
print(subd(a, b))

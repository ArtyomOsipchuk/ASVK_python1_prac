class Dumper():
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print(args, kwargs, end=" → ")
        res = self.function(*args, **kwargs)
        print(res)
        return res

class IsType:
    def __init__(self, typ):
        self.typ = typ

    def __call__(self, fun):
        def decor(*args):
            if not all(isinstance(i, self.typ) for i in args):
                raise TypeError
            return fun(*args)
        return decor

@IsType(int)
def simplefun(N):
    return N*2+1

print(simplefun(4))


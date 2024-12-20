def genf(f):
    def newfun(*args):
        print(">", *args)
        res = f(*args)
        print("<", res)
        return res
    return newfun

def isint(fun):
    def wrapper(*args):
        res = fun(*args)
        if not isinstance(res, int):
            raise TypeError
        return res
    return wrapper

@isint
@genf
def fun(a,b):
    return a*2+b

print(fun(2,3))
print(fun("a","b"))


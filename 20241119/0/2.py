def multicall(times):
    def decorator(fun):
        def newfun(*args):
            return [fun(*args) for i in range(times)]
        return newfun
    return decorator

def isint(typ):
    def decor(fun):
        def wrapper(*args):
            res = fun(*args)
            if not all(isinstance(i, typ) for i in args):
                raise TypeError
            return res
        return wrapper
    return decor

@isint(int)
@multicall(5)
def simplefun(N):
    return N*2+1

print(*simplefun(4))

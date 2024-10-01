def MINF(*args):
    def g(x):
        return min([f(x) for f in args])
    return g

fun = MINF(lambda x: x + 1, lambda x: abs(x))
print(fun(-100))
print(fun(100))

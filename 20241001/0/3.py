def S(f, g):
    def fun(x):
        return f(x) + g(x)
    return fun

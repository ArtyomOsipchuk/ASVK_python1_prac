print(globals())
globals()['a'] = 42
print(globals())
print(a)

def fun(a):
    c = a + 1
    print(locals())
    d = c

fun(123)

print(eval("a + b + abs(c)", {"a": 1, "b": 2, "c": -3}))
print(eval("a + b + abs(c)", None, {"a": 1, "b": 2, "c": -3})) #None = global

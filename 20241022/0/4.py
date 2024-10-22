def f(x):
    yield ">"
    yield from x
    yield "<"
    return len(x)

def run(gen):
    s = yield from gen
    print(f"/{s}/")


'''
g = f("abc")
print(list(g))
g = f("abc")
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''
g = f("qwerty")
st = run(g)
for i in st:
    print(i)

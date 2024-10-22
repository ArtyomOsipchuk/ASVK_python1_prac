def travel(n):
    yield from ["по кочкам"] * n
    return "и в яму."

def travelwrap(n):
    yield (yield from travel(n))


g = travelwrap(5)
for i in g:
    print(i)

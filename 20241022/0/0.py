from itertools import count

def f():
    s = 0
    for i in count(1):    
        s += 1 / (i * i)
        yield s

func = f()
for i, j in zip(func, range(1, 11)):
    print(i, j)

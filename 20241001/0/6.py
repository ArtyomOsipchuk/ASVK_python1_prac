def rbin(n, x=[1]):
    if len(x) == n:
        print(*x, sep="")
    else:
        rbin(n, x + [1])
        rbin(n, x + [0])

rbin(3)

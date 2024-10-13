s, w, A, *inp = eval(input())

Ak, Bk = [], []
for i in range(len(inp)):
    if i < A + 1:
        Ak.append(inp[i])
    elif i == A + 1:
        B = inp[i]
    else:
        Bk.append(inp[i])

Amn = lambda x: sum([(x ** i) * Ak[-(i + 1)] for i in range(A + 1)])
Bmn = lambda x: sum([(x ** i) * Bk[-(i + 1)] for i in range(B + 1)])

if Bmn(s) == 0:
    print(False)
else:
    print((Amn(s) / Bmn(s)) == w)

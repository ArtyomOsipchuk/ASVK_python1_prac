a = [list(eval(input()))]
le = len(a[0])
for i in range(le * 2 - 1):
    a.append(list(eval(input())))
res = [[0 for i in range(le)] for i in range(le)]
for j in range(le):
    for k in range(le):
        res[k][j] = sum([a[j][m] * a[le + m][k] for m in range(le)])
for j in range(le):
    for k in range(le - 1):
        print(res[k][j], end=",")
    print(res[k + 1][j])

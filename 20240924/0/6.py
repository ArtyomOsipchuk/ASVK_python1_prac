a = eval(input())
print(a)
print(all([len(i) == len(a) for i in a]))

for i in range(len(a)):
    for j in range(len(a[0])):
        a[i][j], a[j][i] = a[j][i], a[i][j]


for i in range(len(a)):
    print(a[i])

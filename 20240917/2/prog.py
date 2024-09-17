a = eval(input())
s = 0
while a > 0:
    s += a
    if s > 21:
        print(s)
        break
    a = eval(input())
else:
    print(a)

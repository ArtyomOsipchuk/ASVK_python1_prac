from math import *

s = input().split()
W, H, A, B = [int(i) for i in s[:-1]]
f = lambda x: eval(s[-1])

def scale(a, b, A, B, x):
    return (B - A) * (x - a) / (b - a) + A

def show(screen):
    print("\n".join(["".join(s) for s in screen]))

screen = [[" "] * W for i in range(H)]

mma = f(A)
mmi = f(A)
for i in range(A, B + 1):
    mma = max(mma, f(i))
    mmi = min(mmi, f(i))

for i in range(0, W):
    if (i + 1 == W):
        x = scale(0, W - 1, A, B, i)
        y = -f(x)
        shift = scale(mmi, mma, 0, H - 1, y)
        if shift > H - 1:
            shift = H - 1
        elif shift < 0:
            shift = 0
        screen[round(shift)][i] = "*"
        break
    x1 = scale(0, W - 1, A, B, i)
    x2 = scale(0, W - 1, A, B, i + 1)
    y1 = -f(x1)
    y2 = -f(x2)
    shift1 = scale(mmi, mma, 0, H - 1, y1)
    shift2 = scale(mmi, mma, 0, H - 1, y2)
    screen[round(shift1)][i] = "*"
    screen[round(shift2)][i + 1] = "*"
    mi, ma = i, i + 1
    if (shift1 > shift2):
        shift1, shift2 = shift2, shift1
        mi, ma = i + 1, i
    for j in range(round(shift1) + 1, round(shift2)):
        screen[j][mi + (ma - mi) // 2] = "*"

show(screen)

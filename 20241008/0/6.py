from math import *

def scale(a, b, A, B, x):
    return (B - A) * (x - a) / (b - a) + A

W = 60
H = 20
screen = [[" "] * W for i in range(H)]

def show(screen):
    print("\n".join(["".join(s) for s in screen]))


A, B = -4, 4
for i in range(W):
    x = scale(0, W - 1, A, B, i)
    y = -sin(x)
    shift = scale(-1, 1, 0, H - 1, y)
    screen[round(shift)][i] = "*" 

show(screen)

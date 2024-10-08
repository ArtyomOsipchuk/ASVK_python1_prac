from math import *

def scale(a, b, A, B, x):
    x = (B - A) / (b - a) * x + A
    return x


W = 20
H = 20
A, B = -4, 4
for i in range(H):
    x = scale(0, H - 1, A, B, i)
    y = sin(x)
    shift = round((y + 1) / 2 * W)
    print("_" * shift, "*")

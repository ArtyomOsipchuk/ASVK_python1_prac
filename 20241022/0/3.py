def walk2d(x=0, y=0):
    while True:
        dx, dy = yield x, y
        x += dx
        y += dy

g = walk2d()
next(g)
for dx, dy in zip(range(1, 10), range(-10, -20, -1)):
    print(g.send((dx, dy)))

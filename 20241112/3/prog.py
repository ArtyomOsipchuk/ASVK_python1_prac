class Undead(Exception):
    pass

class Skeleton(Undead):
    pass

class Zombie(Undead):
    pass

class Ghoul(Undead):
    pass

def necro(a):
    if a % 3 == 0:
        raise Skeleton("Skeleton")
    if a % 3 == 1:
        raise Zombie("Zombie")
    if a % 3 == 2:
        raise Ghoul("Generic Undead")

x, y = eval(input())
for i in range(x, y):
    try:
        necro(i)
    except Undead as e:
        print(e)

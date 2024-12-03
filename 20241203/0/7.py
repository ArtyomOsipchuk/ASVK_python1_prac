a = input()
a.split()
while c := input():
    match c.split():
        case [a[0], *tail] if "yes" in c:
            print("1", c)
        case a[1]:
            print("2", c)
        case [a[2], *center, a[1]]:
            print("3", c)

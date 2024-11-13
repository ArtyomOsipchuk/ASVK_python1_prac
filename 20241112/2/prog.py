class InvalidInput(Exception):
    pass

class BadTriangle(Exception):
    pass


def triangleSquare():
    inStr = input()
    coords = eval(inStr)
    if len(coords) != 3:
        raise InvalidInput()
    for i in coords:
        if type(i) != tuple:
            raise InvalidInput()
    x1, y1 = coords[0]
    x2, y2 = coords[1]
    x3, y3 = coords[2]
    S = 0.5 * abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3))
    if not S: 
        raise BadTriangle()
    return S

S = 0
while True:
    try:
        S = triangleSquare()
    except BadTriangle:
        print("Not a triangle")
    except Exception:
        print("Invalid input")
    else:
        print(S)
        break


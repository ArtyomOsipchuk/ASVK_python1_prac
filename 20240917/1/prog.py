n = eval(input())
if (n % 25 == 0):
    if (n % 2 == 0):
        print("A + B -", end=" ")
    else:
        print("A - B +", end=" ")
else:
    print("A - B -", end=" ")
if (n % 8 == 0):
    print("C +")
else:
    print("C -")

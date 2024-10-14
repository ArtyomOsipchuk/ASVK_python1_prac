s = input()
s = input()
h = 0
w = len(s) - 2
types = []
while s != '#' * len(s):
    types.append(s[1])
    h += 1
    s = input()
gas = types.count(".") * w
water = types.count("~") * w
print("#" * (h + 2))
for i in range(0, w * h, h):
    if i + h <= gas:
        print(f"#{'.' * h}#")
    else:
        print(f"#{'~' * h}#")
print("#" * (h + 2))
if gas >= water:
    print(f"{'.' * 20} {gas}/{w * h}")
    print(f"{'~' * round(20 * water / gas)}{' ' * (20 - round(20 * water / gas))} {' ' * (len(str(gas)) - len(str(water)))}{water}/{w * h}")
if water > gas :
    print(f"{'.' * round(20 * gas / water)}{' ' * (20 - round(20 * gas / water))} {' ' * (len(str(water)) - len(str(gas)))}{gas}/{w * h}")
    print(f"{'~' * 20} {water}/{w * h}")

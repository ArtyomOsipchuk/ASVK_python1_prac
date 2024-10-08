length = 0
for i in range(12, 24):
    length = max(len(bin(i) + hex(i)), length)

for i in range(12, 24):
    print(f"{bin(i)} = {' '*(length - len(bin(i) + hex(i)))}{hex(i)}")

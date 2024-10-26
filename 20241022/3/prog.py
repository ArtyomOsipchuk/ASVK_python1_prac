from itertools import product

print(*sorted(filter(lambda x: x.count("TOR") == 2, ["".join(p) for p in product("TOR", repeat=int(input()))])))

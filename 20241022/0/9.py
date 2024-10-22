from itertools import *

for i, j in product("ABCDEFGH", range(1, 9)):
    print(f"{i}{j}", end='\t')

import sys
from random import randrange

N = int(sys.argv[1])

for i in range(N):
    print([randrange(10) for i in range(N)])

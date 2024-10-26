from itertools import islice

def slide(seq, n):
    for i in range(len(seq)):
        for j in islice(seq, i, i + n):
            yield j

import sys
exec(sys.stdin.read())

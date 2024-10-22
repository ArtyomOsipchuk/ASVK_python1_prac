from itertools import *

print(list(filterfalse(lambda x: x % 7, range(11, 66))))

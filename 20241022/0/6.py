from itertools import *

s = 0
print(list(islice(dropwhile(lambda x: x <= 1.6, (s := s + 1 / (i * i) for i in count(1))), 10)))

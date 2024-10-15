from collections import Counter

t1 = input()
t2 = input()
print(not (Counter(t1) - Counter(t2)))

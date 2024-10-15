s = input().lower()
res = set()
for i in range(len(s) - 1):
    a, b = s[i], s[i + 1]
    if a.isalpha() and b.isalpha():
        res.add(a + b)
print(len(res))

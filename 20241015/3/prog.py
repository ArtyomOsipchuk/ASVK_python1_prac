from collections import Counter, defaultdict


w = int(input())
text = []
while (s := input()):
    for i in s.split():
        if "'s" in i:
            i = i[:-2]
        a = ""
        for j in i.lower():
            if j.isalpha():
                a += j
        if len(a) == w:
            text.append(a)
cc = Counter(text)
if cc:
    mx = cc.most_common()[0][1]
    print(*sorted([i[0] for i in Counter(text).most_common() if i[1] == mx]))

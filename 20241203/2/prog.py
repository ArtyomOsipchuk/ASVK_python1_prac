from collections import defaultdict
import math
import sys

p = defaultdict(int)
labels = {}
coms = []
i = 0
s = sys.stdin.read()
for com in s.split('\n'):
    if ":" in com:
        com = com.split(":")
        labels[com[0].strip()] = i - 1
        coms.append(com[1].strip())
    else:
      coms.append(com.strip())
    i += 1
j = 0
while j < i:
    com = coms[j]
    match com.split():
        case ["stop"]:
            break
        case ["store", num, r1]:
            try:
              num = float(num)
              p[r1] = num
            except Exception:
              p[r1] = 0
        case [op, r1, r2, r3]:
            try:
                match op:
                    case "div":
                        p[r3] = p[r1] / p[r2]
                    case "add":
                        p[r3] = p[r1] + p[r2]
                    case "sub":
                        p[r3] = p[r1] - p[r2]
                    case "mul":
                        p[r3] = p[r1] * p[r2]
            except Exception:
                p[r3] = math.inf
            try:
                match op:
                    case "ifeq":
                        if p[r1] == p[r2]:
                            j = labels[r3]
                    case "ifne":
                        if p[r1] != p[r2]:
                            j = labels[r3]
                    case "ifgt":
                        if p[r1] > p[r2]:
                          j = labels[r3]
                    case "ifge":
                        if p[r1] >= p[r2]:
                            j = labels[r3]
                    case "iflt":
                        if p[r1] < p[r2]:
                            j = labels[r3]
                    case "ifle":
                        if p[r1] <= p[r2]:
                            j = labels[r3]
            except Exception:
                break
        case ["out", r1]:
            print(p[r1])
    j += 1

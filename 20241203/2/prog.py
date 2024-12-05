from itertools import defaultdict
import math

p = defaultdict(int)
labels = {}
coms = []
i = 0
while com := input():
    if ":" in com:
        com = com.split(":")
    labels[com[0]] = i
    coms.append(com[1])
    i += 1
j = 0
while j < i:
    com = coms[j]
    match com.split():
        #print(com)
        case ["stop"]:
            return 0
        case ["store", float(num), r1]:
            p[r1] = num
        case ["store", num, r1]:
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
        case [CMP, r1, r2, r3]:
            match CMP:
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
        case ["out", r1]:
            print(p[r1])

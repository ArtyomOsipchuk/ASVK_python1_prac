from math import *

f_cnt = 1
s_cnt = 1
d = dict()
while "quit" not in (func := input()):
    s_cnt += 1
    func = func.split()
    if func[0][0] == ':':
        f_cnt += 1
        d[func[0][1:]] = eval(f"lambda {', '.join(func[1:-1])}: {func[-1]}")
    else:
        print(eval(f"d[func[0]]({', '.join(func[1:])})"))
eval("print(" + func[5:] + f".format({f_cnt}, {s_cnt}))")

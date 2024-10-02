def Pareto(*args):
    res = []
    for i in args[0]:
        not_dominated = 1
        for j in args[0]:
            if i is not j:
                if (i[0] <= j[0] and i[1] <= j[1]):
                    if (i[0] < j[0] or i[1] < j[1]):
                        not_dominated = 0
                        break
        if not_dominated:
            res.append(i)
    return tuple(i for i in res)


print(Pareto(eval(input())))

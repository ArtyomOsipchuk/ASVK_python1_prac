n = eval(input())
i, j = 0, 0
while i < 3:
    while j < 3:
        six = (n + i) * (n + j)
        summ = 0
        while six > 0:
            summ += six % 10
            six //= 10
        if (summ == 6):
            print(n + i, "*", n + j, "= :=)", end=" ")
        else:
            print(n + i, "*", n + j, "=", (n + i) * (n + j), end=" ")
        j += 1;
    j = 0;
    i += 1;
    print()


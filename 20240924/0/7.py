a, b = eval(input())
print([i for i in range(a // 2 * 2 + 1, b, 2) if '3' not in str(i)])

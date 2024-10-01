dwuc = lambda a, b: lambda x: a*x + b

res = dwuc(1, 3)
print(res(7))
print(res.__closure__[0].cell_contents)
print(res.__closure__[1].cell_contents)

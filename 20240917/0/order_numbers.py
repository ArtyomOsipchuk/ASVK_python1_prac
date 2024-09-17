order, result = 1, 0;
a = eval(input())
while a:
    if order == a:
        result += 1
    order += 1
    a = eval(input())
print(result)

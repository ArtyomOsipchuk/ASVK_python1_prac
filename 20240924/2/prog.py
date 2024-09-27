def bubble(arr, key):
    for j in range(len(arr) - 1, 0, -1):
        for i in range(j):
            if key(arr[i]) > key(arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print(arr)


bubble(list(eval(input())), lambda x: x**2 % 100)

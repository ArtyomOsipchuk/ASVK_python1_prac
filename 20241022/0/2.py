def gen():
    print("::")
    res = yield "Start"
    print(">")
    while res := (yield f"/{res}/"):
        print(">>")
    yield "Finish"
    print("<")


g = gen()
print(next(g))
for i in range(5, -1, -1):
    print(g.send(i))

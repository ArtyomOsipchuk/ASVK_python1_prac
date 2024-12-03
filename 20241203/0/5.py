t = "wqtqwtqwt awtg g3ag 3t 2"
match t.split():
    case []:
        print("empty")
    case ["qwe"]:
        print("No doubt qwe")
    case [str(x)]:
        print("1 str", x)
    case [x]:
        print("it's list of one", x)
    case [_, *tail]:
        print("list", tail)

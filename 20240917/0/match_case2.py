match input():
    case "1":
        print("один")
    case "2":
        print("два")
    case "3":
        print("три")
    case var if int(var) % 2 != 0:
        print(var, "-- это много")
    case _:
        print("чётное")

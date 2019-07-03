for a in range(int(input())):
    x = input()
    y = input()
    check = True
    for i in range(len(x)):
        if x[i] != y[i] and x[i] != "?" and y[i] != "?":
            check = False
            break

    if check:
        print("Yes")
    else:
        print("No")
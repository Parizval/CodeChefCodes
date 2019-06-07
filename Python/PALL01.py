for a in range(int(input())):
    val = input()
    if val == val[::-1]:
        print("wins")
    else:
        print("losses")
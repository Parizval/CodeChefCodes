for a in range(int(input())):
    string = input()
    Up = 0 ; down = 0 ; n = len(string)
    for i in range(1,n):
        if string[i] != string[i-1]:
            if string[i-1] == "U":
                Up += 1
            else:
                down += 1
    if string[n-1] == "U":
        up += 1
    else:
        down += 1
    print(min(Up,down))
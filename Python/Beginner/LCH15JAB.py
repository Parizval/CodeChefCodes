for a in range(int(input())):
    check = False;
    string = input()
    for i in string:
        b = string.count(i)
        if b == len(string) - b :
            check = True
            break
    if check:
        print("YES")
    else:
        print("NO")
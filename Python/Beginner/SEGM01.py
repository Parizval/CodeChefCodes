for a in range(int(input())):
    string = input()
    one = 0 ; zero = 0 ; n = len(string)
    for i in range(1,n):
        if string[i] != string[i-1]:
            if string[i-1] == "1":
                one += 1
            else:
                zero += 1
    if string[n-1] == "1":
        one += 1
    else:
        zero += 1
    if one == 1 :
        print("YES")
    else:
        print("NO")
for a in range(int(input())):
    val = list(map(int,input().split()))
    val.sort()
    if val[0] == val[1] and val[2] == val[3]:
        print("YES")
    else:
        print("NO")
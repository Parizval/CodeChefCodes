for a in range(int(input())):
    n = int(input())
    val = list(map(str,input().split()))
    check = True
    for i in range(1,n):
        if val[i] == "cookie" and val[i-1] == "cookie":
            check = False
            break
    if val[n-1] == "cookie":
        check = False
    if check:
        print("YES")
    else:
        print("NO")
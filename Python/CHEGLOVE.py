for a in range(int(input())):
    n = int(input())
    L = list(map(int,input().split()))
    G = list(map(int, input().split()))
    up = 0 ; down = 0 ;
    for i in range(n):
        if L[i] <= G[i]:
            up += 1
        if L[i] <= G[n-1-i]:
            down += 1
    if up == n and down == n :
        print("both")
    elif up == n :
        print("front")
    elif down == n :
        print("back")
    else:
        print("none")
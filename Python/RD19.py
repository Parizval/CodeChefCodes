from math import gcd
for a in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))
    check = False
    b = val[0]
    for i in range(1,n):
        if gcd(b,val[i]) == 1 :
            check = True
            break
    if check:print(0)
    else:print(-1)
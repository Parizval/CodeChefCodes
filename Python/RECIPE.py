from math import gcd
for a in range(int(input())):
    val = list(map(int,input().split()))
    k = val[1]
    n = val[0]
    for i in range(2,n+1):
        k = gcd(k,val[i])
    ans = ""
    for j in range(1,n+1):
        ans += str(val[j]//k) + " "
    print(ans)
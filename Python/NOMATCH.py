for a in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))
    val.sort()
    ans = 0 
    for i in range(n//2):
        ans += abs(val[n-i-1] - val[i])
    print(ans)
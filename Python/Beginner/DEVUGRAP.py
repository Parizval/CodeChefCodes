for a in range(int(input())):
    n,k = map(int,input().split())
    val = list(map(int,input().split()))
    ans = 0
    for i in val:
        n = i // k
        ans += min(i-n*k,(n+1)*k-i)
    print(ans)
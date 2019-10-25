for a in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))
    ans = 1
    for i in range(1,n):
        if i < 5:
            if val[i] < min(val[:i]):
                ans += 1
        else:
            if val[i] < min(val[i-5:i]):
                ans += 1
    print(ans)
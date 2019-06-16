for a in range(int(input())):
    N,K = map(int,input().split())
    val = list(map(int,input().split()))
    ans = 0
    for i in range(K):
        ans += val[i]
    count = ans
    for j in range(K,N):
        count += val[j] - val[j-K]
        if count > ans:
            ans = count
    print(ans)



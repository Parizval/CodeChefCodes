for a in range(int(input())):
    N, K = map(int,input().split())
    stairs = list(map(int,input().split()))
    ans = 0 ; lower = 0
    for i in range(N):
        diff = stairs[i] - lower
        if diff > K :
            if diff % K == 0 :
                ans += diff// K - 1
            else:
                ans += diff // K
        lower = stairs[i]
    print(ans)
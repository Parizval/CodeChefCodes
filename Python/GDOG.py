for a in range(int(input())):
    N,K = map(int,input().split())
    ans = 0
    for i in range(1,K+1):
        b = N % i
        if b > ans:
            ans =  b
    print(ans)
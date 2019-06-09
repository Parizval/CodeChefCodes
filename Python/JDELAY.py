for t in range(int(input())):
    n = int(input())
    ans = 0 
    for i in range(n):
        s,j = map(int,input().split())
        if j - s > 5 : 
            ans += 1 
    print(ans)
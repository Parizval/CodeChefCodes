for a in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))
    ans = 0 
    even = 0 
    for i in range(n-1,-1,-1):
        if val[i] % 2 == 0 : 
            ans += n-1 - i - even
            even += 1
    print(ans)
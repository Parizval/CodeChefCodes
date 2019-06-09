for a in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))
    ans = min(val) * (n-1)
    print(ans)
for a in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))
    val.sort()
    diff = []
    for i in range(n-1):
        diff.append(val[i+1]-val[i])
    ans = min(diff)
    print(ans)
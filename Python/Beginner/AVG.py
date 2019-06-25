for a in range(int(input())):
    n,k,v = map(int,input().split())
    sq = list(map(int,input().split()))
    total = v*(n+k) - sum(sq)
    if total % k == 0 and total / k > 0 : 
        print(int(total / k))
    else:
        print(-1)
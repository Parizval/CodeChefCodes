for a in range(int(input())):
    n,a,b = map(int,input().split())
    val = list(map(int,input().split()))
    pa = val.count(a)
    pb = val.count(b)
    ans = pa*pb
    ans = ans/(n*n)
    print(ans)
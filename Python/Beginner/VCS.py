for a in range(int(input())):
    N,M,K = map(int,input().split())
    one = set(map(int,input().split()))
    two = set(map(int,input().split()))
    total = set(range(1,N+1))
    a1 = one.intersection(two)
    a2 = total - one.union(two)
    print(len(a1),len(a2))

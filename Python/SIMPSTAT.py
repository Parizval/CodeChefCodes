for a in range(int(input())):
    n,k = map(int,input().split())
    values = list(map(int,input().split()))
    values.sort()
    total = 0 
    for i in range(k,n-k):
        total += values[i]
    total = total/(n-2*k)
    print(total)
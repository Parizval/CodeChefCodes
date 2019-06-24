for a in range(int(input())):
    d,n = map(int,input().split())
    for i in range(d):
        total = (n*(n+1))/2
        n = total
    print(int(total))
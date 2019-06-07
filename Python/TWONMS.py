for t in range(int(input())):
    a,b,n = map(int,input().split())
    if n % 2 == 0 : 
        high = max(a,b)
        low = min(a,b)
        print(high//low)
    else:
        high = max(a*2,b)
        low = min(a*2,b)
        print(high//low)
        
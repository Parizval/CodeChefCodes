for a in range(int(input())):
    a,b,n = map(int,input().split())
    if n % 2 == 0 : 
        a = abs(a)
        b = abs(b)
        if a > b : 
            print(1)
        elif b > a : 
            print(2)
        else:
            print(0)
    else:
        if a > b : 
            print(1)
        elif b > a : 
            print(2)
        else:
            print(0)
    
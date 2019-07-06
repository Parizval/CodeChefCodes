for a in range(int(input())):
    n,b,m = map(int,input().split())
    value = 0 
    while True:
        if n % 2 == 0 : 
            value += (n //2) * m 
            n = n - n //2 
            m *= 2 
            if n != 0 : 
                value += b
            else:
                break
        else:
            value += ((n+1)//2 )* m 
            n = n - (n+1)//2
            m *= 2 
            if n != 0 : 
                value += b 
            else:
                break
    print(value)    
for a in range(int(input())):
    n = int(input())
    d1 = 0 ; c1 = 1000;d2 = 0 ; c2 = 1000 ;d3 = 0 ; c3 = 1000;
    for b in range(n):
        c,l,x = map(int,input().split())
        if l == 1 and x >= d1:
            if x == x1:
                c1 = min(c,c1)
            else:
                c1 = c
            d1 = x
        elif l == 2 and x >= d2 :
            if x == d2 :
                c2 = min(c,c2)
            else:
                c2 = c
            d2 = x
        else:
            if x == d3 :
                c3 = min(c,c3)
            else:
                c3 = c
            d3 = x
    print(d1,c1)
    print(d2,c2)
    print(d3,c3)



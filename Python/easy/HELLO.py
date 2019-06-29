for a in range(int(input())):
    d,u,n = map(float,input().split())
    ans = 0 ; value = 0 ; cheap = d * u; n = int(n)
    for i in range(n):
        m , r , c = map(float,input().split())
        value = u * r + c / m
        if value < cheap:
            ans = i + 1
            cheap = value
    print(ans)
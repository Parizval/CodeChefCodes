n,k = map(int,input().split())
value = list(0 for i in range(n))
ans = 0
for a in range(k):
    b = input()
    if b == "CLOSEALL":
        value = list(0 for i in range(n))
        ans = 0
        print(ans)
    else:
        d,e = b.split()
        e = int(e)
        if value[e-1] == 1 :
            value[e-1] = 0
            ans += -1
        else:
            value[e-1] = 1
            ans += 1
        print(ans)
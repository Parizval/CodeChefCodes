for a in range(int(input())):
    b = int(input())
    d = 0 
    if b > 2048 :
        d += b//2048
        b = b % 2048
        c = str(bin(b))
        ans = d + c.count("1")
        print(ans)
    else:
        c = str(bin(b))
        print(c.count("1"))
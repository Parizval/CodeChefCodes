for a in range(int(input())):
    q,p = map(int,input().split())
    ans = 0 
    if q > 1000 :
        ans = float(q*p*0.9)
        print("%.6f"%(ans))
    else:
        ans = float(q*p)
        print("%.6f"%(ans))
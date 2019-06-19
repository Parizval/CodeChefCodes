for a in range(int(input())):
    S,SG,FG,D,T = map(int,input().split())
    ans = S + ((D*180000)/(T*1000))
    if abs(SG-ans) < abs(FG-ans):print("SEBI")
    elif abs(SG-ans) > abs(FG-ans):print("FATHER")
    else:print("DRAW")
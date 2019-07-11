for a in range(int(input())):
    x , y , k , n = map(int,input().split())
    requirment = x - y ; check = False
    for i in range(n):
        p,c = map(int,input().split())
        if p >= requirment and c <= k : check = True
    if check:print("LuckyChef")
    else: print("UnluckyChef")



for a in range(int(input())):
    n,p = map(int,input().split())
    val = list(map(int,input().split()))
    cakewalk = 0 
    hard = 0 
    for i in val : 
        if i >= p //2 : 
            cakewalk +=  1
        elif i <= p // 10 : 
            hard += 1 
        if cakewalk > 1 and hard > 3 : 
            break
    if cakewalk == 1 and hard == 2 : 
        print("yes")
    else:
        print("no")
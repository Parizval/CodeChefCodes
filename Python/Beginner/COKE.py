for a in range(int(input())):
    n,m,k,l,r = map(int,input().split())
    cost =[];temp = [] ; ans = - 1 
    for b in range(n):
        c,d = map(int,input().split())
        cost.append(d)
        temp.append(c)
    net = 0 ; check = False
    for i in range(n):
        if temp[i] > k + 1 : 
            net = max(temp[i]-m,k)
        
        elif temp[i] < k - 1 : 
            net = min(temp[i]+m,k)
        else : net = k 
        
        if net >= l and net <= r : check = True
        
        if ans == - 1 and check == True: ans = cost[i]
        elif check == True and cost[i] < ans : ans = cost[i]
        
        check = False
    print(ans)
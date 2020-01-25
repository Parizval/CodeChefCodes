for a in range(int(input())):
    n = int(input())
    profit = 0
    temp = 0 
    for b in range(n):
        s,p,v = map(int,input().split())
        temp = p//(s+1)
        temp = temp*v  
        if temp >  profit : 
            profit = temp 
    print(profit)
        
            
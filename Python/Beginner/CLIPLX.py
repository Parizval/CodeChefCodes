for a in range(int(input())):
    x,y = map(int,input().split())
    if x > y : 
        ans = x - y 
    else:
        ans = 0 
    print(ans)
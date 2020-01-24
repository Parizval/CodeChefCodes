for a in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    
    zero = array.count(0)
    two = array.count(2)
    
    ans = zero*(zero-1) + two*(two-1)
    ans = int(ans/2)
    
    print(ans)
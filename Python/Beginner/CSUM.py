for a in range(int(input())):
    n,k = map(int,input().split())
    val = list(map(int,input().split()))
    start = 0 ; 
    end = n -1 ; 
    val.sort()
    ans = False
    while(start < end):
        s = val[start] + val[end]
        if s == k : 
            ans = True
            break
        elif s > k : 
            end += - 1 
        else : 
            start += 1 
    if ans:
        print("Yes")
    else:
        print("No")
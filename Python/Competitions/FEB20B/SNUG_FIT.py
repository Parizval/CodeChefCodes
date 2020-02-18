for a in range(int(input())):
    n = int(input())
    w1 = list(map(int,input().split()))
    w2 = list(map(int,input().split()))
    
    w1.sort()
    w2.sort()
    ans = 0 
    for  i in range(n):
        ans += min(w1[i],w2[i])
    print(ans)
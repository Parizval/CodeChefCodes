for a in range(int(input())):
    n = int(input())
    c = list(map(int,input().split()))
    c.sort()
    diff = 0 
    for i in range(n-1):
        if i == 0 :
            diff = c[1] - c[0]
        if c[i+1] - c[i] == 0 : 
            diff = 0 
            break
        if c[i+1] - c[i] < diff : 
            diff = c[i+1] - c[i]
    print(diff)
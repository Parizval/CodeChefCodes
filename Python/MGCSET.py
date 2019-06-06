for a in range(int(input())):
    n,m = map(int,input().split())
    val = list(map(int,input().split()))
    counter = 0 
    for i in val : 
        if i % m == 0 : 
            counter += 1
    ans = 2**counter - 1 
    print(ans)
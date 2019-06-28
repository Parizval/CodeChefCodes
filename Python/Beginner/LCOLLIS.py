for a in range(int(input())):
    n,m = map(int,input().split())
    value = [0 for b in range(m)]
    for c in range(n):
        string = input()
        for i in range(m):
            if string[i] == "1": value[i] += 1
    ans = 0 ;
    for j in value:
        ans += (j*(j-1))//2
    print(ans)
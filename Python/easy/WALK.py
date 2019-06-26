for a in range(int(input())):
    n = int(input())
    value = list(map(int,input().split()))
    ans = n ; check = n ;
    for i in range(n):
        if check < value[i]:
            check = value[i]
            ans = value[i] + i
        check += -1
    print(ans)
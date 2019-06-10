for _ in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))
    ans = sum(val)
    if ans % 2 == 1 : 
        print("YES")
    else:
        print("NO")	
for a in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))
    k = int(input())
    find = val[k-1]
    val.sort()
    pos = 0 
    for i in range(n) : 
        if val[i] == find:
            pos = i + 1 
            break
    print(pos)
    
for a in range(int(input())):
    ans = []
    n,m = map(int,input().split())
    total = list(map(int,input().split()))
    val = list(map(int,input().split()))
    for i in total : 
        if i not in val : ans.append(str(i))
    for j in val : 
        ans.append(str(j))
    print(" ".join(ans))
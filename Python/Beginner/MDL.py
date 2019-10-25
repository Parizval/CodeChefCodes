for a in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))
    highest = max(val)
    lowest = min(val)
    ans = []
    for i in val:
        if i == lowest:
            ans.append(str(lowest))
        if i == highest:
            ans.append(str(highest))
    print(" ".join(ans))
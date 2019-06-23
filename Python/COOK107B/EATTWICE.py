for a in range(int(input())):
    n,m = map(int,input().split())
    taste = [0 for c in range(m)]
    for i in range(n):
        x,y = map(int,input().split())
        if y > taste[x-1]:
            taste[x-1] = y
    taste.sort()
    print(taste[-1]+taste[-2])
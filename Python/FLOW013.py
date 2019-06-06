for i in range(int(input())):
    angle = list(map(int,input().split()))
    if sum(angle) == 180 : 
        print("YES")
    else:
        print("NO")
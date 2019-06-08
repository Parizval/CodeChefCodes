for a in range(int(input())):
    m,n = map(int,input().split())
    rx , ry = map(int,input().split())
    seq = int(input())
    value = input()
    x, y = 0 , 0 
    for i in value:
        if i == "U":
            y += 1 
        elif i == "D":
            y -= 1 
        elif i == "R":
            x += 1 
        else:
            x -= 1 
    if x == rx and y == ry:
        print("Case {}: REACHED".format(a+1))
    elif x < 0 or y < 0 or x > m or y > n : 
        print("Case {}: DANGER".format(a+1))
    else:
        print("Case {}: SOMEWHERE".format(a+1))
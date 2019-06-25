for a in range(int(input())):
    X1,X2,X3,V1,V2 = map(int,input().split())
    one = X3 - X1
    two = X2 - X3
    time1 = one/V1
    time2 = two/V2
    if time1 > time2:
        print("Kefa")
    elif time1 < time2:
        print("Chef")
    else:
        print("Draw")
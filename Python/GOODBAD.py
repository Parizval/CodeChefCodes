for a in range(int(input())):
    n,k = map(int,input().split())
    val = input()
    up = 0 
    down = 0 
    for i in val : 
        if ord(i) >= 65 and ord(i) <= 90 : 
            up += 1 
        else:
            down += 1 
    if down > k and up <= k : 
        print("chef")
    elif down <= k and up > k : 
        print("brother")
    elif down  <= k and up <= k : 
        print("both")
    else:
        print("none")
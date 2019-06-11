for a in range(int(input())):
    time = []
    prob = 0 
    for b in range(10):
        val = list(map(int,input().split()))
        time.append(val)
    for i in range(10):
        for j in range(10):
            if time[i][j] <= 30 : 
                prob += 1
    if prob >= 60 : 
        print("yes")
    else:
        print("no")
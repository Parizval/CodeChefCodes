for a in range(int(input())):
    d = int(input())
    prob = [0 for i in range(32)]
    for b in range(d):
        x,y = map(int,input().split())
        prob[x] = y
    for c in range(1,32):
        prob[c] = prob[c] + prob[c-1]
    for e in range(int(input())):
        dead,req = map(int,input().split())
        if prob[dead] >= req:
            print("Go Camp")
        else:
            print("Go Sleep")
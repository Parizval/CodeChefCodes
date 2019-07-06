# cook your dish here
# cook your dish here
for _ in range(int(input())):
    t1 = int(input())
    tl = list(map(int,input().split()))
    
    d1 = int(input())
    dl = list(map(int,input().split()))
    
    ts = int(input())
    tls = list(map(int,input().split()))
    
    ds = int(input())
    dls = list(map(int,input().split()))
    check = True
    for i in tls:
        if i not in tl:
            check = False
    if check:
        for j in dls:
            if j not in dl:
                check = False
    if check:
        print("yes")
    else:
        print("no")	
for a in range(int(input())):
    val = int(input())
    check = False
    for i in range(2,val//2 + 1):
        if val % i == 0 : 
            check = True
            break
    if check:
        print("no")
    else:
        print("yes")
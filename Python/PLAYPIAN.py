for a in range(int(input())):
    st = input()
    checker = True
    for i in range(0,len(st),2):
        if st[i:i+2] == "AA" or st[i:i+2] == "BB":
            checker = False
            break
    if checker:
        print("yes")
    else:
        print("no")
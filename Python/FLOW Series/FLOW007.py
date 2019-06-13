for a in range(int(input())):
    b = input()
    value = '' ;
    check = False
    start = len(b) - 1 
    for i in range(start,-1,-1):
        if b[i] == '0' and check == False:
            continue
        else:
            value += b[i]
            check = True
    print(value)
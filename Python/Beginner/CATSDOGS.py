for a in range(int(input())):
    C,D,L = map(int,input().split())
    check = True
    if L % 4 != 0 :
        check = False
    else:
        animals = L //4
        upperlimit = D + C
        remainder = C - 2*D
        if remainder < 0 :
            remainder = 0
        lowerlimit = D + remainder
        if animals < lowerlimit or animals > upperlimit:
            check = False
    if check:
        print("yes")
    else:
        print("no")
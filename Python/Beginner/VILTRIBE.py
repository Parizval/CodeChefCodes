for a in range(int(input())):
    A = 0; B = 0 ;dots = 0 ;start = "";
    string = input()
    check = False
    for i in string:
        if check:
            if i == "A":
                start = i
                A += 1
            elif i == "B":
                start = i
                B += 1
        else:
            if i == ".":
                dots += 1
            elif i == "A":
                if i ==  start:
                    A += dots
                dots = 0
                start = i
                A += 1
            else:
                if i ==  start:
                    B += dots
                dots = 0
                start = i
                B += 1
    print(A,B)
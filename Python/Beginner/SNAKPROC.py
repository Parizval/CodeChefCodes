for a in range(int(input())):
    counter = 0 ; check = True
    n = int(input())
    string = input()
    for i in string:
        if i == "H":
            counter += 1
        elif i == "T":
            counter += -1
        if counter > 1 or counter < 0 :
            check = False
            break
    if check == True and counter == 0 :
        print("Valid")
    else:
        print("Invalid")
for a in range(int(input())):
    string = input()
    values = string.split()
    
    check = False
    for i in values:
        if i == "not":
            check = True
    if check:
        print("Real Fancy")
    else:
        print("regularly fancy")
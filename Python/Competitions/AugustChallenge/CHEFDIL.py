for a in range(int(input())):
    string = input()
    one = 0 ; 
    for i in string:
        if i == "1": one += 1 
    if one % 2 == 0 : print("LOSE") 
    else : print("WIN")
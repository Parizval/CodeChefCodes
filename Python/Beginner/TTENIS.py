for a in range(int(input())):
    A = 0 
    B = 0 
    val = input()
    for i in range(len(val)) : 
        if val[i] == "1":
            A += 1
        else:
            B +=  1
        if A == 11 and B < 10 : 
            print("WIN")
            break
        elif B == 11 and A < 10 : 
            print("LOSE")
            break
        elif A == 10 and B == 10:
            for j in range(i+1,len(val)):
                if val[j] == "1":
                    A += 1 
                else:
                    B += 1
                if A - B == 2 :
                    print("WIN")
                    break
                elif B - A == 2 : 
                    print("LOSE")
                    break
            break
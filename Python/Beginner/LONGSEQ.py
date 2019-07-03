for a in range(int(input())):
    val = input()
    zero = 0 
    one = 0 
    for i in val : 
        if i == "1":
            one += 1
    zero = len(val) - one 
    if zero == 1 or one == 1 : 
        print("Yes")
    else:
        print("No")
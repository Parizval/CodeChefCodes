for a in range(int(input())):
    n = int(input())
    one = 0 ; two = 0 ; three = 0 ; four = 0 ; five = 0 ;
    for i in range(n):
        j = input()
        if j == "cakewalk":
            one = 1
        elif j == "simple":
            two = 1
        elif j == "easy":
            three = 1
        elif j == "easy-medium" or j == "medium":
            four = 1
        elif j == "medium-hard" or j == "hard":
            five = 1
    if one == 1 and two == 1 and three == 1 and four == 1 and five == 1 :
        print("Yes")
    else:
        print("No")
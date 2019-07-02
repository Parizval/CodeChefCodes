for a in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))
    if len(set(val)) == n : 
        two = list(val)
        two.sort()
        check = False
        for i in range(n):
            if two[i] != val[i]:
                check = True
            if val[i] > n : 
                check = False
                break
        if check : 
            print("yes")
        else:
            print("no")
    else:
        print("no")
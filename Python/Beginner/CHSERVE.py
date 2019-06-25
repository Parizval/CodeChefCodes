for a in range(int(input())):
    p1,p2,k = map(int,input().split())
    sum = p1 + p2
    if sum % k == 0 :
        b = int(sum / k )
        if b % 2 == 0 :
            print("CHEF")
        else:
            print("COOK")
    else:
        b = sum // k 
        if b % 2 == 0 :
            print("CHEF")
        else:
            print("COOK")
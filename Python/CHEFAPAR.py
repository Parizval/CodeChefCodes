for a in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))
    bill = 0 
    for i in val : 
        if i == 0 :
            bill += 1100
        else:
            if bill > 0 : 
                bill += 100
                
    print(bill)
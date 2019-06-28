for a in range(int(input())):
    n , k = map(int,input().split())
    bill = 0 ; time = 0 ; lower = 0 ;
    for c in range(n):
        x,y = map(int,input().split())
        time += x
        if time <= k :
            continue
        elif time > k and lower < k :
            bill += (time - k )*y
        else:
            bill += x*y
        lower = time
    print(bill)
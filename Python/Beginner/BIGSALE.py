for a in range(int(input())):
    ans = 0 ; total = 0 ;
    for b in range(int(input())):
        price,quantity,discount = map(int,input().split())
        diff = (price * discount*discount)/10000
        ans += quantity*diff
    print("{:.6f}".format(ans))
for a in range(int(input())):
    guests = 0 
    n = int(input())
    val = list(map(int,input().split()))
    val.sort()
    for i in range(n):
        if guests >= val[i] : guests += 1 
    print(guests)
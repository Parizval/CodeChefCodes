for a in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))
    if n == 1 :
        print(1)
    else:
        presum = val[0]
        total = sum(val)
        ans = presum + total
        b = 0
        index = 1
        for i in range(1,n):
            presum += val[i]
            total -= val[i-1]
            b = presum + total
            if b < ans:
                ans = b
                index = i + 1
        print(index)



for a in range(int(input())):
    n,k = map(int,input().split())
    array = list(map(int,input().split()))
    total = 0 
    for i in array:
        if i % k != 0 :      
            total += i
    print(total%k)
for a in range(int(input())):
    N,X = map(int,input().split())
    val = list(map(int,input().split()))
    amount = sum(val)
    if amount % X == 0 : 
        print(amount//X)
    else:
        if (amount - min(val))//X == amount // X : 
            print(-1)
        else:
            print(amount//X)
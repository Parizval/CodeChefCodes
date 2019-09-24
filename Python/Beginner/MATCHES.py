for a in range(int(input())):
    p,q = map(int,input().split())
    total = p + q 
    val = [6,2,5,5,4,5,6,3,7,6]
    ans = 0 ; 
    for i in str(total):
        ans += val[int(i)] 
    print(ans)
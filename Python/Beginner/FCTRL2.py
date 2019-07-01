for i in range(int(input())):
    value = int(input())
    ans = 1 
    for b in range(1,value+1):
        ans *= b 
    print(ans)
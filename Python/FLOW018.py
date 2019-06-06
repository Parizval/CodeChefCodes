for a in range(int(input())):
    b = int(input())
    ans = 1 
    for i in range(1,b+1):
        ans *= i
    print(ans)
for a in range(int(input())):
    n = int(input())
    value = list(map(int,input().split()))
    ans = 0 ; twos = 0 ; other = 0 ;
    for i in value:
        if i == 2 :
            twos += 1
        elif i > 2 :
            other += 1
    ans = twos*other + (other*(other-1))//2
    print(ans)
        
for a in range(int(input())):
    N,U,D = map(int,input().split())
    value = list(map(int,input().split()))
    pos = value[0]
    ans = 1 ; parachute = True;
    for i in range(1,N):
        if value[i] - pos > U :
            break
        if pos - value[i] > D :
            if parachute:
                parachute = False
            else:
                break
        pos= value[i]
        ans += 1
    print(ans)
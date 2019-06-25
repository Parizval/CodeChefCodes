for a in range(int(input())):
    N,M = map(int,input().split())
    if (N*M) % 2 == 0 :
        print("YES")
    else:
        print("NO")
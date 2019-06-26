for a in range(int(input())):
    N, K = map(int,input().split())
    value = list(map(int,input().split()))
    total = sum(value)
    if total % 2 == 0 and K == 1 :
        print("odd")
    else:
        print("even")
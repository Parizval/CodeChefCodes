for a in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))
    b = set(val)
    if len(val) > len(b):
        print("Yes")
    else:
        print("No")
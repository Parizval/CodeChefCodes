for a in range(int(input())):
    n = int(input())
    value = list(map(int,input().split()))
    value.sort()
    print(value[0]+value[1])
for a in range(int(input())):
    n,m = map(int,input().split())
    one = set(map(int,input().split()))
    two = set(map(int,input().split()))
    print(len(one.intersection(two)))
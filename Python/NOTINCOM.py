for a in range(int(input())):
    n,m = map(int,input().split())
    alice = list(map(int,input().split()))
    bertha = list(map(int,input().split()))
    value = 0 
    for i in range(n):
        if alice[i] in bertha : 
            value += 1 
    print(value)
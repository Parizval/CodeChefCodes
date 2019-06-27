for a in range(int(input())):
    n = int(input())
    correct = list(map(int,input().split()))
    chef = list(map(int,input().split()))
    prize = list(map(int,input().split()))
    count = 0
    for i in range(n):
        if correct[i] == chef[i]:
            count += 1
    ans = 0
    upper = 0
    if count == n :
        print(prize[n-1])
    else:
        for j in range(count+1):
            if upper < prize[j]:
                upper = prize[j]
        print(upper)
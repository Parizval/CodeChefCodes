from collections import Counter
for a  in range(int(input())):
    n = int(input())
    
    array = list(map(int,input().split()))
    
    frequency = Counter(array)
    num = []
    for k, v in frequency.items():
        if v > 3 : 
            num.append(k)
            num.append(k)
        elif v > 1 : 
            num.append(k)
    if len(num) < 2 : 
        print(-1)
    else: 
        num.sort()
        print(num[-1]*num[-2])
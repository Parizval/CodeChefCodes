for a in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))
    average = sum(val) / n  
    
    if 2 not in val and 5 in val and average >= 4 : 
        print("Yes")
    else:
        print("No")
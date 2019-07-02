for a in range(int(input())):
    s1 = set(map(str,input().split()))
    s2 = set(map(str,input().split()))
    ans = len(s1.intersection(s2))
    if ans > 0 : print("Yes") 
    else:print("No")
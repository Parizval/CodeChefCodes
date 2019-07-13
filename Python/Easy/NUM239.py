for a in range(int(input())):
    counter  = 0 
    L,R = map(int,input().split())
    for i in range(L,R+1):
        if i % 10 == 2 or i % 10 == 3 or i % 10 == 9 : counter += 1 
    print(counter)
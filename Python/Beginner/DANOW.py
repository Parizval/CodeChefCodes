num,query = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i in range(query):
    one,two = map(int,input().split()) 
    total = 0 ; 
    for j in range(one-1,two):
        total += A[j]*B[j];
    print(total)
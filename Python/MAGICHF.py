test = int(input())
for i in range(test):
    num, pos, query = map(int,input().split())
    for j in range(query):
        left , right = map(int,input().split()) ; 
        if left == pos : 
            pos = right 
        elif right == pos : 
            pos = left
            
    print(pos)
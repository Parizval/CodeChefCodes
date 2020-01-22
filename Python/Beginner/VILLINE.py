n = int(input())
m,c = map(int,input().split())
pos = 0 ; neg = 0 ; 
temp = 0 
for i in range(n):
    x,y,p = map(int,input().split())
    temp = y - m*x -c  
    if  temp > 0 : 
        pos += p 
    else:
        neg += p 
print(max(pos,neg))
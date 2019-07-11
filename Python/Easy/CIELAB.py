a,b = map(int,input().split())
n = a -b 
if n % 10 >= 8 : 
    n += -2 
else:
    n += 1 
print(n)
n,k = map(int,input().split())
count = 0 
for i in range(n):
    v = int(input())
    if v % k == 0 :
        count += 1 
print(count)
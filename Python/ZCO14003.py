n = int(input())
val = []
for a in range(n):
    b = int(input())
    val.append(b)
val.sort()
ans = [] 
for i in range(n):
    ans.append(val[i]*(n-i))
print(max(ans))
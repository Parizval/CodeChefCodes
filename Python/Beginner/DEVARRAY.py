N,Q = map(int,input().split())
A = list(map(int,input().split()))
upper = -1
lower = 9999999999
for i in A:
    if i > upper:
        upper = i
    elif i < lower:
        lower = i
for i in range(Q):
    q = int(input())
    if q <= upper and q >= lower:print("Yes")
    else:print("No")
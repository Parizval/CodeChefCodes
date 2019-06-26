A,B, C = map(int,input().split())
one = set();two = set();three = set();
for i in range(A):
    one.add(int(input()))
for j in range(B):
    two.add(int(input()))
for k in range(C):
    three.add(int(input()))
ans = set()
ans = set(one.intersection(two))
ans.update(two.intersection(three))
ans.update(three.intersection(one))
print(len(ans))
D = sorted(ans)
for i in D :
    print(i)
from math import gcd
for a in range(int(input())):
  n = int(input())
  val = list(map(int,input().split()))
  ans = 0 
  for i in range(n):
    ans = gcd(ans,val[i])
  print(ans)
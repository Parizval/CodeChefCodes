from math import gcd
for a in range(int(input())):
  b ,c = map(int,input().split())
  ans = 2*gcd(b,c)
  print(ans)	
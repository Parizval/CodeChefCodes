from math import gcd
for a in range(int(input())):
  b,l = map(int,input().split())
  div = gcd(b,l)
  div = div **2
  ans = (l*b)//div
  print(ans)
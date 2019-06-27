for a in range(int(input())):
  n = int(input())
  one = list(map(int,input().split()))
  two = list(map(int,input().split()))
  b = 0 
  c = 0 
  d = 0 
  e = 0 
  for i in range(n):
    if i % 2 == 0 : 
      c += two[i]
      e += one[i]
    else:
      b += one[i]
      d += two[i]
  print(min(b+c,e+d))
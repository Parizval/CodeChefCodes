for a in range(int(input())):
  n,m,k = map(int,input().split())
  value = abs(n-m)
  if value - k <= 0 : 
    print(0)
  else:
    print(value-k)
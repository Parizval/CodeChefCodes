for a in range(int(input())):
  n,m = map(int,input().split())
  remain = n % m 
  if remain % 2 == 0 : 
    print("EVEN")
  else:
    print("ODD")
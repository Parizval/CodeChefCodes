for a in range(int(input())):
  n = int(input())
  val = list(map(int,input().split()))
  ans = 0 ; mul = 0 ; 
  for i in range(n):
    for j in range(i+1,n):
      mul = val[i]*val[j]
      digit = [int(d) for d in str(mul)]
      total = sum(digit)
      if total > ans : ans = total 
  print(ans)
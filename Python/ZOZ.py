for a in range(int(input())):
  n,k = map(int,input().split())
  val = list(map(int,input().split()))
  total = sum(val)
  ans = 0 
  for i in val : 
    if i + k > total - i : 
      ans += 1 
  print(ans)	
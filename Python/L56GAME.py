for a in range(int(input())):
  n = int(input())
  val = list(map(int,input().split()))
  odd = 0 
  even = 0
  ans = 0 
  for i in val : 
    if i % 2 == 0 : 
      even += 1 
    else:
      odd += 1
  ans += odd % 2 
  even += odd // 2 
  if even > 0 : 
    ans += 1
  print(ans)
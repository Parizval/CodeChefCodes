for a in range(int(input())):
  n,k = map(int,input().split())
  val = list(map(int,input().split()))
  counter = len(val)- val.count(1)
  if counter <= k :
    print("YES")
  else:
    print("NO")
for a in range(int(input())):
  n = int(input())
  val = list(map(int,input().split()))
  if n % 2 == 1 and val[0] == 1 :
    check = True
    for i in range(1,n//2+1):
      if val[i] - val[i-1] != 1 :
        check = False
        break
    for j in range(n//2+1,n):
      if val[j] - val[j-1] != -1 : 
        check = False
        break
    if check:
      print("yes")
    else:
      print("no")
  else:
    print("no")
for a in range(int(input())):
  st = input()
  val = st[0]
  tr = 0 
  for i in range(1,len(st)):
    if st[i] != val:
      tr += 1 
      val = st[i]
  if st[-1] != st[0]:
    tr += 1 
  if tr <= 2 : 
    print("uniform")
  else:
    print("non-uniform")

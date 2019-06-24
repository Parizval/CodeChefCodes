count = 0
for a in range(int(input())):
  x1,y1,x2,y2,x3,y3 = map(int,input().split())
  d1 = (x2 - x1)**2 + (y2 - y1)**2
  d2 = (x3 - x2)**2 + (y3 - y2)**2
  d3 = (x3 - x1)**2 + (y3 - y1)**2
  hypo = max(d1,d2,d3)
  total = d1+d2+d3 - 2*hypo
  if total == 0 :
    count += 1
print(count)
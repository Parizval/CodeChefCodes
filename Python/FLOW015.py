days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
for a in range(int(input())):
  y = int(input())
  if y > 2001 : 
    y = y - 2001 
    y = y + y//4 + y//400 - y//100
    y = y % 7 
  else:
    y = 2001 - 1 - y 
    y = -(y+y//4 + y //400 + 2 - y//100)%7
  print(days[y])  
val = ["chef","che","hef","ch","ef","he"]
counter = 0 
for a in range(int(input())):
  string = input()
  for i in val: 
    if i in string : 
      counter += 1 
      break 
print(counter)
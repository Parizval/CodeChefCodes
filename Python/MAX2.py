n = int(input())
value = input()
counter = 0 
for i in range(n-1,-1,-1):
    if value[i] == '1':
        break
    counter += 1 
if counter == n : 
    print(0)
else:
    print(counter)
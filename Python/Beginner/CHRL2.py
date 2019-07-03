one = 0; two = 0; three = 0; count = 0
string = input()
for i in string:
    if i == "C":
        one += 1
    if one > 0 and i == "H":
        two +=1
        one += -1
    if two > 0  and i == "E":
        three +=1
        two += -1
    if three > 0 and i == "F":
        count += 1
        three += -1

print(count)
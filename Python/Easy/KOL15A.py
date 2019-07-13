nums = ["1","2","3","4","5","6","7","8","9"]
for a in range(int(input())):
    sum = 0 
    string = input()
    for i in string:
        if i in nums:
            sum += int(i)
    print(sum)
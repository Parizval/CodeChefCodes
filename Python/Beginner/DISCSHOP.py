def number(arr):
    num = 0 
    for i in arr : 
        num = num*10 + i
    return num

for a in range(int(input())):
    n = int(input())
    if n < 10 : 
        print(n)
        continue
    digit = [int(i) for i in str(n)]
    numbers =  []
    for j in range(len(digit)):
        extra = []
        extra = digit[:j]+digit[j+1:]
        numbers.append(number(extra))
    
    print(min(numbers))
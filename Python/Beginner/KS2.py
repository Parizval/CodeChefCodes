# cook your dish here
for a in range(int(input())):
    n = int(input())
    total = sum([int(i) for i in str(n)])
    if total% 10 == 0 : 
        print(str(n)+'0')
    else:
        add = 10 - (total%10)
        print(str(n)+str(add))
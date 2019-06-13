# cook your dish here
for a in range(int(input())):
    total = 0 
    sal = int(input())
    if sal >= 1500:
        total = 1.98*sal + 500 
        print(total)
    else:
        total = 2* sal 
        print(total)
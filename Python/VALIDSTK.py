t = int(input())
for i in range(t):
    operation = input()
    string = list(map(int,input().split()))
    num = 0
    for j in string:
        if j == 1:
            num += 1
        elif j == 0:
            num = num - 1
        if num < 0:
            print('Invalid')
            break
    if num >= 0 :
        print('Valid')

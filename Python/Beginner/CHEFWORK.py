n = int(input())
c = list(map(int,input().split()))
t = list(map(int,input().split()))
one = - 1 ; two = - 1 ; three = -1
for i in range(n):
    if t[i] == 1:
        if one == -1 or one > c[i]:
            one = c[i]
    elif t[i] == 2 :
        if two == -1 or two > c[i]:
            two = c[i]

    elif t[i] == 3 :
        if three == -1 or three > c[i]  :
            three = c[i]

if one >= 0  and two >= 0 and three >= 0 :
    print(min(one+two,three))
elif one >= 0 and two >= 0 and three < 0 :
    print(one + two)
elif (one < 0 or two < 0 )and three >= 0 :
    print(three)
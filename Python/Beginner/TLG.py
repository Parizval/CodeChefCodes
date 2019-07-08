one = 0  ; two = 0 ; ans = 0
for a in range(int(input())):
    x,y = map(int,input().split())
    one += x ; two += y ;
    if one - two > diff:
        diff = one - two
        ans = 1
    elif two - one > diff:
        diff = two - one
        ans = 2
print(ans,diff)
n = int(input())
values = list(map(int,input().split()))
l = 0
ul = 0 
for i in values:
    if i % 2 == 0 : 
        l += 1 
    else:
        ul += 1
if l > ul : 
    print("READY FOR BATTLE")
else:
    print("NOT READY")
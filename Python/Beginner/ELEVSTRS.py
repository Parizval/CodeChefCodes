import math
for a in range(int(input())):
    n,b,c = map(int,input().split())
    ele = (2*n)/c
    stair = (math.sqrt(2)*n)/b
    if ele > stair:
        print("Stairs")
    else:
        print("Elevator")
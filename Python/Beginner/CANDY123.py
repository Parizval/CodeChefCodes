import math
for a in range(int(input())):
    b,c = map(int,input().split())
    one = int(math.sqrt(b))
    two = int((-1 + math.sqrt(1+4*c))/2)
    if one > two :
        print("Limak")
    else:
        print("Bob")
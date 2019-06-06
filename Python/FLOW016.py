import math
for a in range(int(input())):
    one,two = map(int,input().split())
    first = math.gcd(one,two)
    second = int(one*two/first)
    print("{} {}".format(first,second))
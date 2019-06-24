from math import gcd
for a in range(int(input())):
    one,two = map(int,input().split())
    print(gcd(one,two))
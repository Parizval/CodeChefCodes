from math import sqrt
for a in range(int(input())):
    n = int(input())
    counter = 0 
    val = 0 
    while True:
        if n == 0 : 
            break
        else:
            val  = int(sqrt(n))
            counter += 1
            n = n - val**2
    print(counter)
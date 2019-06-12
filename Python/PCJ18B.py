for a in range(int(input())):
    n = int(input())
    val = 0 
    for i in range(n,0,-2):
        val += i*i
    print(val)
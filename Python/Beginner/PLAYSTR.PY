for a in range(int(input())):
    n = int(input())
    b = input()
    c = input()
    first = 0 ; second = 0 
    for p in range(n):
        if b[p] == "1": first += 1 
        if c[p] == "1" : second += 1
    if first == second : print("YES")
    else : print("NO")
for a in range(int(input())):
    n = int(input())
    first = [] ; last = [] ; 
    for j in range(n):
        b = input()
        p,q = b.split()
        first.append(p)
        last.append(q)
    for i in range(n):
        if first.count(first[i]) > 1 : 
            print(first[i],last[i])
        else:
            print(first[i])
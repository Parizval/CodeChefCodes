for a in range(int(input())):
    n = int(input())
    pairs = []
    for i in range(n):
        b = int(input())
        pairs.append(b)
    for j in pairs:
        if pairs.count(j) % 2 != 0 :
            print(j)
            break
for a in range(int(input())):
    n = int(input())
    two = set()
    for b in range(n):
        c = input()
        d = set(c)
        if b == 0:
            two = set(c)
        else:
            two = two.intersection(d)
    print(len(two))	
for a in range(int(input())):
    count = 0
    one = list(input())
    two = list(input())
    for b in two:
        if b in one : count += 1
    print(count)
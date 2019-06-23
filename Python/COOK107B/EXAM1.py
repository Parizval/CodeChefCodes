for a in range(int(input())):
    n = int(input())
    val = input()
    chef = input()
    ans = 0 ; penalty = False
    for i in range(n):
        if penalty:
            penalty = False
            continue
        if chef[i] == val[i]:
            ans += 1
        if chef[i] != val[i] and chef[i] != "N":
            penalty = True
    print(ans)
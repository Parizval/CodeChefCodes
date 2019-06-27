for a in range(int(input())):
    n = int(input())
    string = input()
    counter = [0,0,0]; ans = 0 ;
    for i in string:
        if i == "R":
            counter[0] += 1
        elif i == "G":
            counter[1] += 1
        else:
            counter[2] += 1
    ans = n - max(counter)
    print(ans)
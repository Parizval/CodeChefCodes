for a in range(int(input())):
    row = []
    b = input()
    c = input()
    d = input()
    row.append(list(b))
    row.append(list(c))
    row.append(list(d))
    ans = False
    for b in range(2):
        for c in range(2):
            if row[b][c] == 'l':
                if row[b+1][c] == 'l' and row[b+1][c+1] == 'l':
                    ans = True
                    break;
    if ans == False:
        print("no")
    else:
        print("yes")
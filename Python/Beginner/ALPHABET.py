a = input()
values = list(a)
for b in range(int(input())):
    v = input()
    check = True
    for i in v:
        if i not in values:
            check = False
            break
    if check:
        print("Yes")
    else:
        print("No")
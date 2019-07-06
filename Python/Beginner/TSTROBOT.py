for a in range(int(input())):
    b,pos = map(int,input().split())
    string = input()
    value = 1 
    visit = []
    visit.append(pos)
    for i in string:
        if i == "R":
            pos += 1 
            if pos not in visit:
                value += 1
                visit.append(pos)
        else:
            pos -= 1 
            if pos not in visit:
                value += 1
                visit.append(pos)
    print(value)
# cook your dish here
for i in range(int(input())):
    val = list(map(str,input().split()))
    if len(val) == 1 :
        val[0] = val[0].lower()
        val[0] = val[0].capitalize()
        print(val[0])
    elif len(val) == 2 :
        f = val[0][0]
        f = f.upper()
        val[1] = val[1].lower()
        val[1] = val[1].capitalize()
        print(f+". "+val[1])
    elif len(val) == 3 :
        f = val[0][0]
        f = f.upper()
        g = val[1][0]
        g = g.upper()
        val[2] = val[2].lower()
        val[2] = val[2].capitalize()
        print(f+". "+g+". "+val[2])
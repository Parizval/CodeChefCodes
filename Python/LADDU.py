for t in range(int(input())):
    n = input()
    a,b = n.split()
    score = 0 
    for c in range(int(a)):
        val = input()
        if val == "TOP_CONTRIBUTOR":
            score += 300
        elif val == "CONTEST_HOSTED":
            score += 50 
        else:
            d,e = val.split()
            if d == "CONTEST_WON":
                if int(e) > 20 : 
                    score += 300
                else:
                    score += 320 - int(e)
            elif d == "BUG_FOUND":
                score += int(e)
    if b == "INDIAN":
        print(score//200)
    else:
        print(score//400)
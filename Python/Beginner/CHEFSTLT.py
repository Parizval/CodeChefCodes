for a in range(int(input())):
    s1 = input()
    s2 = input()
    lower = 0 ; upper = 0 ;
    for i in range(len(s1)):
        if s1[i] != s2[i] and s1[i] != "?" and s2[i] != "?":
            lower += 1
            upper += 1
        elif s1[i] == s2[i] and s2[i] == "?":
            upper += 1
        elif s1[i] != s2[i] and (s1[i] == "?" or s2[i] == "?"):
            upper += 1
    print(lower,upper)
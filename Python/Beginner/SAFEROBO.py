for a in range(int(input())):
    string = input()
    a = 0 ; b = 0 
    s,p = map(int,input().split())
    for i in range(len(string)):
        if string[i] == 'A':
            a = i 
        if  string[i] == 'B':
            b = i 
            break
    #print(b-a,s+p)
    if  (b-a)%(s+p) == 0 :  
        print("unsafe")
    else:
        print("safe")
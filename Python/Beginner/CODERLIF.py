for _ in range(int(input())):
    val = list(map(int,input().split()))
    counter = 0 
    check = True
    for i in val:
        if i == 1:
            counter += 1 
        elif i == 0:
            counter = 0
            
        if counter > 5 :
            check = False
            break
    if check:
        print("#allcodersarefun")
    else:
        print("#coderlifematters")
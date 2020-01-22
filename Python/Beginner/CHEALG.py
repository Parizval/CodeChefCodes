for  a in range(int(input())):
    string = input()
    num = 0 ;  char  = string[0]
    count = 0
        
    for i in range(len(string)):
        if i == 0 :  
            num += 1    
            char  = string[0]
            count += 1 
            continue
        
        if  string[i] != char:
            #print(char,count)    
            char = string[i]
            num +=  len(str(count)) + 1 
            count = 1 
        else:
            count += 1 
            
    num += len(str(count))
    if num < len(string):
        print("YES")
    else:
        print("NO")
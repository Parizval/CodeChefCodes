ans = ["Beginner","Junior Developer","Middle Developer","Senior Developer","Hacker","Jeff Dean"]
for a in range(int(input())):
    val = list(map(int,input().split()))
    counter = 0 
    for i in val : 
        if i == 1 : 
            counter += 1
            
    print(ans[counter])
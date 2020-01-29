import itertools
def findsubsets(s, n): 
    return [set(i) for i in itertools.combinations(s, n)] 
for a  in range(int(input())):
    elements = set(map(int,input().split()))
    check = False
    for i in range(1,5,1):
        array = findsubsets(elements,i)
        for i in array:
            if sum(i) == 0 : 
                # print(i)
                check = True
                break
            
        if check:
            break
    if check:
        print("Yes")
    else:
        print("No")
from itertools import permutations
total = 0 
for a in range(int(input())):
    data = [0 for i in range(16)]
    
    #movie_map =  {'A':0,'B':4,'C':8,'D':12}
    index_map = {12:0,3:1,6:2,9:3}

    indexes = [i for  i in  range(4)]
    comb = permutations(indexes)
    
    data = {}
    data['A'] = [0,0,0,0]
    data['B'] = [0,0,0,0]
    data['C'] = [0,0,0,0]
    data['D'] = [0,0,0,0]

    for i in  range(int(input())):
        movie,time  = input().split()
        data[movie][index_map[int(time)]] += 1
    
    
    #print(data)
    counter = 0
    profit = - 400  
    for i in list(comb):
        ans =  []
        for  j in range(4):
            charac = chr(i[j]+65)
            ans.append(data[charac][j])
        ans.sort(reverse=True)
        temp = 0 
        price = 100 
        for j in range(4):
            if  ans[j] == 0  :  
                temp -= 100 
            else:
                temp += ans[j]*price
                price -= 25 
        
        if  temp >= profit:
            profit = temp 
    
    print(profit)
    total += profit
print(total)
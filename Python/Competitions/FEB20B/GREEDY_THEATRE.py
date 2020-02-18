def Cal(data,movie,indexes,price,played):
    request = 0 
    rm_movie = ""
    rm_index = 0 
    for i in movie:
        for  j in indexes:
            if data[i][j] >  request: 
                request = data[i][j]
                rm_movie = i 
                rm_index = j 
    if rm_movie != "":
        # print(rm_movie,request,price)
        movie.remove(rm_movie)
        indexes.remove(rm_index)
        played.append(rm_movie)
    else: request = 0 
    
    return request*price,movie,indexes,played
    
total = 0 
for a in range(int(input())):
    n = int(input())
    data = {}
    data['A'] = [0,0,0,0]
    data['B'] = [0,0,0,0]
    data['C'] = [0,0,0,0]
    data['D'] = [0,0,0,0]

    index_map =  {12:0,3:1,6:2,9:3}
    
    ans = 0 
    
    check = [-1,-1,-1,-1]
    
    for i in  range(n):
        movie,time  = input().split()

        if check[ord(movie)-65] == -1: 
            check[ord(movie)-65] = 0
        
        data[movie][index_map[int(time)]] += 1
    
    movie = ['A','B','C','D']
    for i in range(4):
        if  check[i] == -1 :  
            ans -= 100
            movie.remove(chr(i+65))
    

    indexes  = [0,1,2,3]
    temp = 0 
    price = 100 
    temp_movie = len(movie)

    played = []
    for  i in range(temp_movie):

        temp,movie, indexes,played = Cal(data,movie,indexes,price,played)
        
        if temp == 0 : break 
        else: 
            price  -= 25 
            ans += temp
    
    if  temp_movie != len(played):
        ans += abs(temp_movie-  len(played))*-100
    print(ans)  
    total += ans 

print(total)
for p  in range(int(input())):
    n, a , b , c  =  map(int,input().split())
    array = list(map(int,input().split()))
    ans  = 0 ; temp = 0 
    for  i in range(n):
        if i == 0 :  
            ans = abs(array[i] - a) +  c + abs(array[i] - b) 
        else:
            temp = abs(array[i] - a) +  c + abs(array[i] - b)
            if temp < ans : 
                ans = temp 
    print(ans)
import math 
for  a  in range(int(input())):
    Finish,TigerDistance,accerlation,bolt = map(int,input().split())
    
    t1 = Finish/bolt 
    
    t2 = (2*(TigerDistance+Finish))/accerlation
    t2 =  math.sqrt(t2)
    
    if t1 < t2 : 
        print("Bolt")
    else:
        print("Tiger")
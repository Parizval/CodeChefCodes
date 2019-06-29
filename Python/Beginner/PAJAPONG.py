for a in range(int(input())):
    x,y , k = map(int,input().split())
    total =  ( x + y ) // k
    if total % 2 == 0 :print("Chef")
    else:print("Paja")
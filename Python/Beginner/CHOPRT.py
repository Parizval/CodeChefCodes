for a in range(int(input())):
    a,b = map(int,input().split())
    if a > b : 
        print(">")
    elif b > a : 
        print("<")
    else:
        print("=")
for a in range(int(input())):
    n,b = map(int,input().split())
    area = []
    for i in range(n):
        w,h,p = map(int,input().split())
        if p <= b : 
            area.append(w*h)
    if len(area) == 0 :
        print("no tablet")
    else:
        print(max(area))
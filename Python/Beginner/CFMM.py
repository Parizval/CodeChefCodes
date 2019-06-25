for _ in range(int(input())):
    v = int(input())
    a = [0,0,0,0,0,0]
    for i in range(v):
        st = input()
        a[0] += st.count('c')
        a[1] += st.count('e')
        a[2] += st.count('d')
        a[3] += st.count('o')
        a[4] += st.count('h')
        a[5] += st.count('f')
    b = min(a[0],a[1])
    c = min(a[2],a[3],a[4],a[5])
    b = b//2
    print(min(b,c))
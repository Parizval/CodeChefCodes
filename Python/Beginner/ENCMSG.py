# cook your dish here
for _ in range(int(input())):
    n = int(input())
    st = input()
    ans = ""
    for i in range(0,n-1,2):
       ans += st[i+1] + st[i]
    if n % 2 == 1 : 
        ans += st[n-1]
    mid = ""
    for j in ans:
        val = ord(j) - 97
        mid += chr(122 - val)
    print(mid)
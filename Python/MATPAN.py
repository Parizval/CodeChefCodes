for a in range(int(input())):
    val = list(map(int,input().split()))
    string = input()
    ans = 0 
    for i in range(97,123):
        if chr(i) not in string:
            ans += val[i-97]
    print(ans)
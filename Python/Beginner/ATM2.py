for a in range(int(input())):
    N,balance = map(int,input().split())
    val = list(map(int,input().split()))
    string = ""
    for i in val:
        if balance >= i :
            string +="1"
            balance += -i
        else:
            string += "0"
    print(string)
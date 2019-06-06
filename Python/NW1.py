day = {"mon":0,"tues":1,"wed":2,"thurs":3,"fri":4,"sat":5,"sun":6}
31
for a in range(int(input())):
    val = list(input().split())
    an = int(val[0])
    ans = [0,0,0,0,0,0,0]
    index = day[val[1]]
    for i in range(1,8):
        if index >= 7 : 
            index = index - 7
        n = (an - i )//7 + 1 
        ans[index] = n
        index += 1
    string = ""
    for i in ans:
        string += str(i) + " "
    print(string)
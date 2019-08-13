for a in range(int(input())):
    n = int(input())
    goal = list(map(int,input().split()))
    foul = list(map(int,input().split()))
    score = [0 for i in range(n)]
    temp = 0 ; 
    for i in range(n):
        temp = 20*goal[i] - 10*foul[i]
        if temp <=  0 : score[i] = 0 
        else : score[i] = temp 
    ans = max(score)
    print(ans)
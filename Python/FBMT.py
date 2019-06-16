for a in range(int(input())):
    n = int(input())
    if n == 0 :
        print("Draw")
    else:
        TeamA = input()
        ScoreA= 1
        ScoreB = 0
        TeamB = ""
        for i in range(n-1):
            j = input()
            if j == TeamA:
                ScoreA += 1
            else:
                TeamB = j
                ScoreB += 1
        if ScoreA > ScoreB:
            print(TeamA)
        elif ScoreB > ScoreA:
            print(TeamB)
        else:
            print("Draw")
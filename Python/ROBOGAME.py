def answer(string):
    if len(string) == 1 :
        return 'safe'
    else:
        count = 0
        position = -1
        for i in range(len(string)):
            if string[i] != '.' and position == -1 :
                count = int(string[i])
                position = i
                continue
            if string[i] != '.':
                if position+count >= i - int(string[i]):
                    return 'unsafe'
                else:
                    count = int(string[i])
                    position = i
        return 'safe'


t = int(input())
for i in range(t):
    string = ""
    string = input()
    print(answer(string))
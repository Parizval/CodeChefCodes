for a  in  range(int(input())):
    n = int(input())
    TrainData = {}
    ans = 0 
    for i in range(n):
        word,count = map(str,input().split())
        
        if word in TrainData.keys():
            TrainData[word][int(count)] += 1 
        else:
            TrainData[word] = [0,0]
            TrainData[word][int(count)] += 1
                
    for k,v in TrainData.items():
        ans += max(v)
    #print(TrainData)
    print(ans)
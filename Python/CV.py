vowel = ['a','e','i','o','u']
for a in range(int(input())):
    n = int(input())
    cv = input()
    counter = 0 
    for i in range(n-1):
        if cv[i] not in vowel and cv[i+1] in vowel:
            counter += 1 
    print(counter)
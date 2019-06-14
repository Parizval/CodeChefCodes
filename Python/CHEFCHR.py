for a in range(int(input())):
    string = input()
    n = len(string) -3 
    match = set("chef")
    counter = 0 
    for i in range(n):
        if set(string[i:i+4]) == match:
            counter += 1 
    if counter == 0 :
        print("normal")
    else:
        print("lovely",counter)
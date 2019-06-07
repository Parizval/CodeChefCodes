for a in range(int(input())):
    b = input()
    c = input()
    counter = 0 
    one = b.split()
    two = c.split()
    for i in one:
        if i in two : 
            counter += 1 
    if counter >= 2 : 
        print("similar")
    else:
        print("dissimilar")
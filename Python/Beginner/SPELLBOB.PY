for a in range(int(input())):
    one = input()
    two = input()
    first = list(one)
    second = list(two)
    b = False ; c = -1 ; counter = 0 ;
    for i in range(3):
        if first[i] == "o" or second[i] == "o":
            c = i
        if (first[i] == "o" and second[i] != "b" ) or (first[i] != "b" and second[i] == "o"):
            c = i
            break
    for j in range(3):
        if j == c :
            continue
        if first[j] == "b" or second[j] == "b":
            counter += 1
    if counter == 2 and c >= 0 :
        print("yes")
    else:
        print("no")
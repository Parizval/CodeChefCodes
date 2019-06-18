for a in range(int(input())):
    string = input()
    amber = string.count("a")
    brass = string.count("b")
    print(min(amber,brass))
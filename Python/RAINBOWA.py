for a in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))
    rainbow = [1,2,3,4,5,6,7]
    valset = set(val)
    if (val == val[::-1] and sorted(valset) == rainbow):print("yes")
    else:print("no")
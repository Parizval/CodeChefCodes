for a in range(int(input())):
    b = int(input())
    value = input()
    if 'Y' not in value and 'I' in value:
        print("INDIAN")
    elif 'I' not in value and 'Y' in value:
        print("NOT INDIAN")
    else:
        print("NOT SURE")
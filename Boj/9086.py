for _ in range(int(input())):
    l=input()
    if len(l)<2:
        print(l+l)
    else:
        print(l[0]+l[-1])
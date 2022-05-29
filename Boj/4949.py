while True:
    n = input()
    if n == ".": break
    l = []
    value= True
    for i in n:
        if i == '(' or i == ")" or i == '[' or i == ']':
            if i == '(' or i == '[':
                l.append(i)
            else:
                if len(l) == 0:
                    value = False
                    break
                if i == ')' and l[-1] == '(':
                    l.pop()
                elif i == ']' and l[-1] == '[':
                    l.pop()
                else: 
                    value = False
                    break
    if (len(l) > 0) and ((l[-1] == '(' ) or (l[-1] == '[')):
        print ("no")
    else:    
        if value: print ("yes")
        else: print ("no")
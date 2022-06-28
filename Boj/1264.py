l =["a","e","i","o","u"]

while True:
    t = input()
    if t =='#':
        break
    else:
        value=0
        for i in t:
            if i.lower() in l:
                value+=1
        print(value)
            
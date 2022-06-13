n = input()
m = input()
value=0
i = 0
while i < len(n):
    t= n[i:i+len(m)]
    if t == m :
        value+=1
        i+=len(m) -1
    i+=1
print(value)
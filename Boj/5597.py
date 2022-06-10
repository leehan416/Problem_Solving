l=[]
k=[]
for _ in range(28):
    l.append(int(input()))
for i in range(1,31):
    if not i in l:
        k.append(int(i))
k.sort()
for i in k:
    print(i)
l = []

for _ in range(10):
    l.append(list(map(int, input().split())))
x, y = 1, 1
while True:
    if (l[x][y] == 0):
        l[x][y] = 9
    elif (l[x][y] == 2):
        l[x][y] = 9
        break

    if ((l[x][y+1] == 1 and l[x+1][y] == 1)):
        break

    if (l[x][y+1] != 1):
        y = y + 1
    elif (l[x+1][y] != 1):
        x = x + 1
for i in l:
    for j in i:
        print(j, end=' ')
    print("")
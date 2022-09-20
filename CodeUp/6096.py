l = [[0 for _ in range(19)] for _ in range(19)]
for i in range (19):
    l[i] = list(map(int, input().split()))
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    x -=1
    y-=1
    for i in range(19):
        l[x][i] = 1 if l[x][i] == 0 else 0
    for i in range(19):
        l[i][y] = 1 if l[i][y] == 0 else 0
for i in range(19):
    for j in range(19):
        print(l[i][j], end=' ' )
    print('')
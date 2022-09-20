n = int(input())
l = [[0 for _ in range(19)] for _ in range(19)]
for _ in range(n):
    x, y = map(int, input().split())
    l[x-1][y-1] = 1
for i in range(19):
    for j in range(19):
        print(l[i][j], end=' ' )
    print('')
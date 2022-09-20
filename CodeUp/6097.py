h,w  = map(int, input().split())
m = [[0 for _ in range(w)] for _ in range(h)]
n  = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    x -= 1 
    y -= 1 
    for i in range(l):
        m[x][y]=1
        if d == 0: y += 1
        else: x += 1

for i in range(h):
    for j in range(w):
        print(str(m[i][j]), end=' ')
    print('')
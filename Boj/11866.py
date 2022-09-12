n, k = map(int, input().split())
l = [i for i in range(1, n + 1)]
outList = []

while l:
    for i in range(k - 1):
        l.append(l.pop(0))
    outList.append(l.pop(0))

print("<",end='')
for i in range(len(outList) - 1):
    print("%d, "%outList[i], end='')
print(outList[-1], end='')
print(">")
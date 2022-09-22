l = [0, 1, 1]
n = int(input())
for i in range(3, n + 1):
    l.append(l[i-2] + l[i-1])
print(l[n])

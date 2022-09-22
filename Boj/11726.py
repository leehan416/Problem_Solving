l = [0, 1, 2, 3]
n = int(input())
for i in range(3, n + 1):
    l.append(l[i-1] + l[i])
print(l[n] % 10007)

l = [0, 1, 3, 5]
n = int(input())
for i in range(3, n + 1):
    l.append(l[i-1] * 2 + l[i])
print(l[n] % 10007)

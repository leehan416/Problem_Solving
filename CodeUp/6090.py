a1,m, d, n = map(int, input().split())
value = a1
for _ in range(1, n): value = value * m + d
print (value)
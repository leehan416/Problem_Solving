n = int(input())
h=-1
for i in range(n+1):
  l = list(map(int, str(i)))
  if n == i+ sum(l):
    h = i
    break

if h > 0:
  print (h)
else:
  print(0)
N,M = map(int, input().split())
l = []
for i in range(N):
  l.append(int(input()))
start, end = 1, max(l)
while start <= end:
  value = 0
  mid = (start + end) // 2
  for i in l:
    value += i // mid
  if value >= M: start = mid + 1
  else: end = mid - 1
print (end)
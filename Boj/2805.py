#pypy3 로 통과함
#py로는 시간초과
N,M = map(int, input().split())
trees  = list(map(int, input().split()))
start, end = 0, max(trees)
while start <= end:
  value = 0
  mid = (start + end) // 2
  for i in trees:
    if i - mid > 0:
      value += i - mid
  if value >= M: start = mid + 1
  else: end = mid - 1
print (end)
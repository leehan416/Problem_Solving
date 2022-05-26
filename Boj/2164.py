from collections import deque
import sys
n = int(sys.stdin.readline())
l = deque([i for i in range(1 ,n + 1)])
for i in range(n-1):
  l.popleft()
  l.append(l.popleft())
print(l[0])
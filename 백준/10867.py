import sys
n = sys.stdin.readline()
l = list(map(int, str(sys.stdin.readline()).split()))
v = []
for i in l:
  if not i in v:
    v.append(i)
v.sort()
for i in v:
  print(i, end=" ")
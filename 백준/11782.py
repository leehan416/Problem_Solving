import sys
n = sys.stdin.readline()

l = list(map(int, input().split())) + list(map(int, input().split()))
l.sort()
for i in l:
  print(i, end=" ")
  
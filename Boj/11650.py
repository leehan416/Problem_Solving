num = int(input())
l=[]
for _ in range(num):
  value = input().split()
  l += [[int(value[0]), int(value[1])]]
l.sort()
for i in l:
  print(i[0], i[1])
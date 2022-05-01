num = int(input())
l=[]
for _ in range(num):
  value = input().split()
  l += [[int(value[1]), int(value[0])]]
l.sort()
for i in l:
  print(i[1], i[0])
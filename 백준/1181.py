value = int(input())
n=[]
words=[]
for _ in range(value):
  i = input()
  if not i in words:
    words += [i]
    n += [[len(i), i]]
  else:
    value-=1
n.sort()
for i in range(value-1):
  if n[i][1] == n[i+1][1]:
    if n[i][0] > n[i+1][0]:
      n[i], n[i+1] = n[i+1], n[i]
for i in n:
  print(i[1])
l =[]
for i in range(int(input())):
  i= int(input())
  if i == 0: l.pop()
  else: l.append(i)
print(sum(l))
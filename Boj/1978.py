import sys
n = sys.stdin.readline()
l = list(map(int, sys.stdin.readline().split()))
value = 0
for i in l:
  if i == 1 or (i % 2 == 0 and i != 2):
    continue 
  else:
    if i == 2:
      value +=1
      continue
    v = False
    for j in range(3, i, 2):
      if i % j == 0: 
        v = True 
        break
    if not v:   
      value += 1
print (value)
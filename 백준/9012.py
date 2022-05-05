n = int(input())
l =[]
for i in range(n):
  l +=[input()]

for i in l:
  k = 0
  for j in i:
    if j == "(":
      k += 1
    elif j == ")":
      k -=1
      if k < 0:
        break
  if k == 0:
    print("YES")
  else:
    print("NO")
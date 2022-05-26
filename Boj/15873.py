i = input()
sum = 0
if "0" in i:
  k = i.split("0")
  if len(k) > 2:
    sum += 18
  else:
    sum += 9
  for k in i:
    sum += int(k)
else:
  for j in i:
    sum += int(j)
print(sum)
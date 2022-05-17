n = int(input())
num = n
value = 0
while True:
  i = num // 10
  j = num % 10
  k = (i + j) % 10
  num =   j * 10 + k
  value+=1
  if n== num:
    break
print(value)
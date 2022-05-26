n = int(input())
value =0
while n>0:
  if n % 5 == 0 :
    value += n // 5
    n = 0
    break
  else:
    n -= 3
    value +=1
if n == 0:
  print(value)
else:
  print(-1)
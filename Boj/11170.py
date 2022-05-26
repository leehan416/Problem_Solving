num = int(input())
value = 0
for _ in range (num):
  value = 0
  m, n = map(int, input().split())
  for j in range(m, n+1): 
    for k in str(j): 
      if k =="0":
        value+=1
  print(value)